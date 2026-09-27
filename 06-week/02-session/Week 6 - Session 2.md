# Week 6 - Sesion 2

## Ambientes, estrategia de configuracion y promocion

**Proyecto:** RedFish  
**Responsable:** LUIS FERNANDO CLAROS RAMOS  
**Asignatura:** Sistemas Distribuidos  
**Semana:** 6  
**Sesion:** 2  
**Historia de usuario:** HU-012

---

## 1. Objetivo de la sesion

Definir como se ejecuta y promueve RedFish entre desarrollo, QA y produccion,
utilizando la misma imagen de la aplicacion con configuraciones externas y
secretos independientes por ambiente.

Esta historia no incorpora entidades ni endpoints. Su alcance corresponde a
la estrategia de ejecucion y promocion del MVP 2.

---

## 2. Historia de usuario

### HU-012 - Definir ambientes y estrategia de configuracion del MVP 2

**Como** responsable del desarrollo de RedFish,  
**quiero** ejecutar una misma imagen en los ambientes Develop, QA y produccion,  
**para** promover cambios sin reconstruir el artefacto ni almacenar secretos
en el repositorio.

### Criterios de aceptacion

| ID | Criterio |
|---|---|
| CA-01 | Se definen los ambientes `develop`, `qa` y `prod`. |
| CA-02 | Existe un archivo Compose base con la topologia compartida. |
| CA-03 | Desarrollo puede construir la imagen mediante un override. |
| CA-04 | QA y produccion consumen una imagen existente y no la reconstruyen. |
| CA-05 | Se documenta una matriz unica de nombres de variables. |
| CA-06 | Las credenciales reales permanecen fuera de Git. |
| CA-07 | Compose valida las variables requeridas antes de iniciar. |
| CA-08 | Se documenta la relacion entre ramas y ambientes. |
| CA-09 | Se conserva el flujo `Qa -> main` definido por RedFish. |
| CA-10 | Las tres combinaciones de Compose tienen sintaxis valida. |
| CA-11 | Las pruebas automatizadas finalizan correctamente. |

---

## 3. Ambientes definidos

| Ambiente | Rama | Caracteristicas |
|---|---|---|
| Develop | `Develop` | Rapido, reconstruible y con puertos locales de aplicacion y MySQL. |
| QA | `Qa` | Configuracion aislada, sin construir la imagen y cercana a produccion. |
| Produccion | `main` | Imagen aprobada, configuracion externa y base de datos no publicada al host. |

La arquitectura sigue siendo un monolito modular. Los ambientes no convierten
los modulos internos en microservicios.

---

## 4. Estructura de Compose

```text
RedFish/
|-- compose.yaml
|-- compose.override.yaml
|-- compose.qa.yaml
|-- compose.prod.yaml
`-- .env.example
```

Responsabilidades:

| Archivo | Responsabilidad |
|---|---|
| `compose.yaml` | Servicios, dependencias, health checks, red y volumen comunes. |
| `compose.override.yaml` | Construccion local y publicacion del puerto de MySQL. |
| `compose.qa.yaml` | Puerto y limites de recursos para QA, sin `build`. |
| `compose.prod.yaml` | Puerto, recursos y reinicio continuo, sin `build`. |

---

## 5. Construir una vez y promover

La imagen se construye en desarrollo:

```powershell
docker compose up --build -d
```

QA y produccion reciben el mismo valor de `APP_IMAGE`:

```text
redfish-app:mvp2
```

En una entrega real, este valor sera una etiqueta inmutable o un digest de un
registro. Los ambientes de QA y produccion no contienen una seccion `build` y
sus comandos no utilizan `--build`.

---

## 6. Configuracion y secretos

La matriz detallada se encuentra en:

```text
docs/configuration/environment-matrix.md
```

Los nombres de variables son iguales en todos los ambientes. Solamente cambian
sus valores. `.env.example` documenta el contrato, mientras `.env`, `.env.qa`
y `.env.prod` permanecen ignorados por Git.

Las variables obligatorias utilizan la expresion `${VARIABLE:?mensaje}` en
Compose. Si falta una de ellas, el inicio se detiene antes de crear los
contenedores.

---

## 7. Relacion entre ramas y ambientes

La guia academica se adapta al flujo definido para RedFish:

```text
hu-012-dev -> Develop
hu-012-qa  -> Qa
```

No se crea `hu-012-main`. Cada HU termina en `Qa`; `main` recibe directamente
un Pull Request de `Qa` solo despues de validar la ultima HU del MVP 2.

---

## 8. Trabajo de orquestacion para el MVP 2

| Candidato | Resultado verificable |
|---|---|
| Publicar imagen inmutable | Una imagen identificada por version o digest queda disponible en un registro. |
| Automatizar promocion a QA | QA consume la imagen construida en desarrollo sin volver a compilar. |
| Versionar el esquema | Flyway o Liquibase prepara la base antes de usar `ddl-auto=validate`. |
| Agregar observabilidad | Salud, logs y metricas permiten diagnosticar los ambientes. |
| Definir recuperacion | Se documenta rollback de imagen y respaldo de la base de datos. |

Estos candidatos se refinaran cuando las siguientes sesiones definan su
alcance y prioridad. No se incorporan como historias oficiales anticipadas.

---

## 9. Validacion esperada

Configuracion:

```powershell
docker compose --env-file .env -f compose.yaml -f compose.override.yaml config --quiet
docker compose --env-file .env.qa -f compose.yaml -f compose.qa.yaml config --quiet
docker compose --env-file .env.prod -f compose.yaml -f compose.prod.yaml config --quiet
```

Pruebas automatizadas:

```powershell
.\gradlew.bat test
```

Resultado esperado:

```text
BUILD SUCCESSFUL
```

### Resultado obtenido

| Validacion | Resultado |
|---|---|
| Configuracion Develop | PASS |
| Configuracion QA | PASS |
| Configuracion produccion | PASS |
| Desarrollo con `docker compose up --build -d` | PASS |
| Estado de `redfish-develop-app-1` | `healthy` |
| Estado de `redfish-develop-mysql-1` | `healthy` |
| Endpoints de productos y clientes en Develop | PASS |
| QA iniciado sin reconstruir la aplicacion | PASS |
| Estado de `redfish-qa-app-1` | `healthy` |
| Estado de `redfish-qa-mysql-1` | `healthy` |
| Imagen usada por Develop y QA | Mismo ID `sha256:80832abba980...` |
| Pruebas automatizadas | `BUILD SUCCESSFUL` |

La configuracion de produccion se valido de forma estatica. No se inicio un
ambiente productivo local porque `ddl-auto=validate` requiere un esquema
previamente aprovisionado y secretos suministrados por el despliegue.

---

## 10. Archivos modificados

```text
RedFish/compose.yaml
RedFish/compose.override.yaml
RedFish/compose.qa.yaml
RedFish/compose.prod.yaml
RedFish/.env.example
docs/configuration/environment-matrix.md
docs/Week-06/session-02/Week 6 - Session 2.md
docs/backlog.md
README.md
```

---

## 11. Resultado de la sesion

| Elemento | Resultado |
|---|---|
| Ambientes Develop, QA y produccion | Definidos |
| Compose base | Implementado |
| Override de desarrollo | Implementado |
| Configuracion de QA | Implementada |
| Configuracion de produccion | Implementada |
| Promocion de la misma imagen | Documentada |
| Matriz de configuracion | Documentada |
| Secretos fuera del repositorio | Implementado |
| Relacion rama-ambiente | Documentada |
| Validacion tecnica | Aprobada |
| Validacion QA | Pendiente en rama `hu-012-qa` |

---

## 12. Siguiente paso

Promover HU-012 hacia `Develop` mediante Pull Request y realizar la validacion
formal en la rama `hu-012-qa`.
