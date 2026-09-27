# Week 7 - Sesion 2

## Contratos versionados y pruebas orientadas al consumidor

**Historia de usuario:** HU-014  
**Rama de desarrollo:** `hu-014-dev`  
**Estado:** Implementada en desarrollo, pendiente de validacion QA

---

## 1. Historia de usuario

### HU-014 - Versionar y verificar los contratos de integracion

Como equipo de desarrollo de RedFish, queremos publicar contratos REST
versionados y verificarlos desde la perspectiva del consumidor, para evolucionar
la API sin romper silenciosamente las integraciones existentes.

---

## 2. Criterios de aceptacion

| ID | Criterio |
|---|---|
| CA-01 | Los endpoints soportados se publican bajo `/api/v1`. |
| CA-02 | Las rutas originales continúan temporalmente disponibles sin romper consumidores. |
| CA-03 | Las rutas antiguas anuncian su deprecacion y fecha de retiro. |
| CA-04 | Existe un contrato OpenAPI versionado y legible por herramientas. |
| CA-05 | El contrato declara metodo, ruta, solicitud, respuesta y errores. |
| CA-06 | Todas las respuestas de error usan un sobre estandar. |
| CA-07 | Se documentan reglas de compatibilidad y cambios incompatibles. |
| CA-08 | Existe al menos una prueba Pact del consumidor. |
| CA-09 | El proveedor verifica el pacto contra el controlador real. |
| CA-10 | Las pruebas de contrato se ejecutan en integracion continua. |
| CA-11 | Las pruebas existentes continúan aprobadas. |

---

## 3. API versionada

Las rutas canónicas son:

```text
POST /api/v1/products
GET  /api/v1/products
GET  /api/v1/products/{id}

POST /api/v1/customers
GET  /api/v1/customers
GET  /api/v1/customers/{id}
```

Los encabezados `Location` de las operaciones de creación también apuntan a
la ruta v1 correspondiente.

### Compatibilidad con el MVP anterior

Las siguientes rutas permanecen como aliases:

```text
/api/products
/api/customers
```

El filtro `LegacyApiDeprecationFilter` agrega:

```text
Deprecation: true
Sunset: Wed, 30 Jun 2027 23:59:59 GMT
Link: </api/v1/...>; rel="successor-version"
```

Esto permite una migracion gradual en lugar de eliminar las rutas existentes.

---

## 4. Contrato OpenAPI

La fuente de verdad se encuentra en:

```text
RedFish/src/main/resources/static/openapi-v1.yaml
```

El archivo declara:

- OpenAPI `3.1.0`;
- version funcional `1.0.0`;
- endpoints de productos y clientes;
- cuerpos de solicitud y respuesta;
- campos obligatorios y tipos;
- codigos HTTP;
- encabezados `Location` y `X-Trace-Id`;
- esquemas reutilizables;
- estructura estandar de errores.

Durante la ejecucion puede consultarse mediante:

```http
GET /openapi-v1.yaml
```

Swagger UI utiliza el mismo archivo y permanece disponible en:

```text
/swagger-ui.html
```

La prueba `OpenApiV1ContractTests` analiza el YAML y verifica la version, las
rutas principales y el esquema de errores.

---

## 5. Sobre estandar de errores

La API responde errores con la siguiente forma:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "invalid request body",
    "details": {
      "code": "must not be blank"
    },
    "trace_id": "9e289660-5f90-4c65-9f8f-939c91128295"
  }
}
```

Codigos iniciales:

| Codigo | Uso |
|---|---|
| `VALIDATION_ERROR` | El cuerpo no cumple sus restricciones. |
| `INVALID_REQUEST` | El JSON, parametro o identificador no puede interpretarse. |
| `BUSINESS_RULE_VIOLATION` | Se incumple una regla de negocio. |
| `RESOURCE_NOT_FOUND` | No se encuentra el recurso solicitado. |
| `INTERNAL_ERROR` | Ocurre un error inesperado. |

`X-Trace-Id` se devuelve como encabezado y dentro del cuerpo. Si el consumidor
envia un UUID valido, RedFish lo conserva; si falta o es invalido, genera uno.

---

## 6. Politica de compatibilidad

El documento `docs/api/versioning-policy.md` establece que agregar campos
opcionales o endpoints nuevos es compatible dentro de v1.

Los siguientes cambios requieren una nueva version:

- eliminar o renombrar un campo;
- cambiar el tipo o significado de un campo;
- convertir un campo opcional en obligatorio;
- eliminar una operacion;
- cambiar de forma incompatible un codigo HTTP o una respuesta.

Una version anterior debe permanecer activa durante un periodo de migracion y
anunciar su retiro mediante `Deprecation`, `Sunset` y `Link`.

---

## 7. Pruebas Pact

### Consumidor

`ProductApiConsumerPactTests` representa al consumidor
`redfish-web-client`. Declara que espera obtener un producto desde:

```http
GET /api/v1/products/1
Accept: application/json
```

La respuesta esperada contiene:

```text
id, code, name, unitOfMeasure, type, active
```

Pact inicia un servidor simulado, el consumidor realiza la peticion y se genera
un contrato Pact V4.

### Proveedor

El pacto versionado se almacena en:

```text
RedFish/src/test/resources/pacts/redfish-web-client-redfish-api.json
```

`ProductApiProviderPactTests` prepara el estado `product 1 exists` y reproduce
la interacción contra `ProductController` mediante
`Spring7MockMvcTestTarget`. Si el proveedor elimina, renombra o cambia un campo
esperado, la prueba falla.

---

## 8. Integracion continua

El workflow `.github/workflows/contract-tests.yml` ejecuta la suite Gradle en:

- Pull Requests hacia `Develop`, `Qa` y `main`;
- cambios enviados directamente a esas ramas.

Comando ejecutado:

```bash
./gradlew test --no-daemon
```

El workflow no publica contratos en un Pact Broker. Para el alcance actual, el
pacto se conserva versionado en el repositorio y se verifica localmente y en
GitHub Actions.

---

## 9. Archivos principales

| Archivo | Responsabilidad |
|---|---|
| `ProductController.java` | Rutas v1 y alias legado de productos. |
| `CustomerController.java` | Rutas v1 y alias legado de clientes. |
| `RestExceptionHandler.java` | Codigos y sobre estandar de errores. |
| `ApiContractController.java` | Publicacion del contrato como `application/yaml`. |
| `LegacyApiDeprecationFilter.java` | Encabezados para rutas deprecadas. |
| `openapi-v1.yaml` | Contrato REST legible por herramientas. |
| `versioning-policy.md` | Reglas de compatibilidad y deprecacion. |
| `ProductApiConsumerPactTests.java` | Expectativa del consumidor. |
| `ProductApiProviderPactTests.java` | Verificacion del proveedor. |
| `contract-tests.yml` | Ejecucion automatizada en CI. |

---

## 10. Validaciones de desarrollo

Comando:

```powershell
cd RedFish
.\gradlew.bat test
```

Resultado:

```text
BUILD SUCCESSFUL
27 tests, 0 failures, 0 errors, 1 skipped
```

La prueba omitida corresponde al contexto completo con Testcontainers que ya
se encontraba deshabilitado y documentado antes de HU-014. Las pruebas
unitarias, REST, OpenAPI y Pact fueron ejecutadas correctamente.

Validacion funcional en Develop:

| Prueba HTTP | Resultado |
|---|---|
| `GET /actuator/health` | `UP` |
| `GET /openapi-v1.yaml` | `200`, `application/yaml`, version `1.0.0` |
| `POST /api/v1/products` | `201`, `Location` versionado |
| `GET /api/products` | `200` con `Deprecation`, `Sunset` y `Link` |
| Solicitud invalida con `X-Trace-Id` | `400`, sobre estandar y trazas coincidentes |
| Identificador no numerico | `400`, codigo `INVALID_REQUEST` |

La imagen construida para Develop fue:

```text
sha256:44b434d3527eb63c782d19656931f268b43bde30835d4074eec832950caa19bd
```

QA y produccion no fueron recreados desde la rama de desarrollo; la promocion
de esta imagen corresponde a las siguientes etapas del flujo Git.

---

## 11. Flujo Git

```text
hu-014-dev -> Develop
hu-014-qa  -> Qa
```

HU-014 termina en `Qa`. La promocion `Qa -> main` se realizara una sola vez,
despues de aprobar la ultima HU del MVP 2.

---

## 12. Siguiente paso

Promover HU-014 a `Develop` mediante Pull Request y realizar la validacion
formal en `hu-014-qa`.
