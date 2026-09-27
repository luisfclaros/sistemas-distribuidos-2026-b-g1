# Week 7 - Sesion 1

## Comunicacion entre modulos: REST, eventos e idempotencia

**Historia de usuario:** HU-013  
**Rama de desarrollo:** `hu-013-dev`  
**Estado:** Implementada en desarrollo, pendiente de validacion QA

---

## 1. Historia de usuario

### HU-013 - Definir e implementar la comunicacion interna de RedFish

Como equipo de desarrollo de RedFish, queremos seleccionar el modo de
comunicacion apropiado para cada interaccion e implementar un consumidor
idempotente, para reducir el acoplamiento entre modulos y tolerar la entrega
duplicada de eventos.

---

## 2. Criterios de aceptacion

| ID | Criterio |
|---|---|
| CA-01 | Se documentan las interacciones sincronas y asincronas de RedFish. |
| CA-02 | REST queda reservado para clientes externos y los puertos Java para colaboracion sincrona entre modulos. |
| CA-03 | Inventario publica un evento luego de crear un producto. |
| CA-04 | Reportes consume el evento sin depender del repositorio interno de Inventario. |
| CA-05 | El evento incluye una clave de idempotencia unica. |
| CA-06 | El consumidor evita registrar dos veces el mismo evento. |
| CA-07 | Existen pruebas automatizadas para publicacion e idempotencia. |
| CA-08 | Develop, QA y produccion local publican MySQL en puertos distintos. |
| CA-09 | La configuracion y sus restricciones de seguridad quedan documentadas. |

---

## 3. Seleccion tecnologica

RedFish conserva su arquitectura de monolito modular. No se agregan llamadas
HTTP entre modulos ni un broker sin una necesidad operativa real.

| Necesidad | Eleccion |
|---|---|
| API para Postman o frontend | REST/JSON |
| Respuesta inmediata entre modulos | Puerto Java |
| Notificacion desacoplada | Evento de aplicacion Spring |
| Alto rendimiento entre servicios futuros | Evaluar gRPC |
| Mensajeria durable futura | Evaluar RabbitMQ o Kafka con Outbox |

La decision completa se encuentra en
`docs/architecture/communication-strategy.md`.

---

## 4. Implementacion

Cuando `CreateProductService` guarda correctamente un producto, publica
`ProductCreatedEvent` mediante `ProductCreatedEventPublisher`. La
infraestructura adapta ese puerto a `ApplicationEventPublisher` de Spring.

El modulo Reportes escucha el contrato publico del evento y registra su
procesamiento en MySQL. No consulta ni modifica directamente la tabla
`productos`.

La creacion del producto y el consumo sincrono del evento participan en una
transaccion local. Si el registro del evento falla, la creacion del producto
tambien se revierte.

### Contrato del evento

```text
ProductCreatedEvent
- eventId: UUID
- productId: Long
- productCode: String
- occurredAt: Instant
```

### Idempotencia

La tabla `eventos_producto_procesados` utiliza `event_id` como llave primaria.
La primera entrega crea el registro y las siguientes entregas con el mismo
identificador se reconocen como duplicadas.

---

## 5. Puertos locales por ambiente

| Ambiente | API | MySQL publicado | MySQL interno |
|---|---:|---:|---:|
| Develop | `8080` | `3307` | `3306` |
| QA | `8081` | `3308` | `3306` |
| main/Produccion local | `8082` | `3309` | `3306` |

Los tres contenedores pueden usar internamente `3306` porque pertenecen a
redes Docker distintas. Los puertos publicados son diferentes para permitir
la conexion simultanea desde MySQL Workbench.

La publicacion de `3309` corresponde exclusivamente a la validacion local. En
produccion real, MySQL debe permanecer en una red privada sin puerto publicado.

---

## 6. Archivos principales

| Archivo o paquete | Responsabilidad |
|---|---|
| `inventory/application/event` | Contrato del evento de producto creado. |
| `inventory/application/port/ProductCreatedEventPublisher.java` | Puerto de publicacion. |
| `inventory/infrastructure/messaging` | Adaptador de eventos de Spring. |
| `reporting/application/service/ProductCreatedEventConsumer.java` | Consumidor idempotente. |
| `reporting/infrastructure/persistence/jpa` | Registro persistente de eventos procesados. |
| `compose.qa.yaml` | Publica MySQL de QA en `3308`. |
| `compose.prod.yaml` | Publica MySQL local de produccion en `3309`. |

---

## 7. Validaciones ejecutadas

```powershell
cd RedFish
.\gradlew.bat test

docker compose --env-file .env -f compose.yaml -f compose.override.yaml config --quiet
docker compose --env-file .env.qa -f compose.yaml -f compose.qa.yaml config --quiet
docker compose --env-file .env.prod -f compose.yaml -f compose.prod.yaml config --quiet
```

Resultados obtenidos:

| Validacion | Resultado |
|---|---|
| Suite Gradle | `BUILD SUCCESSFUL` |
| Publicacion del evento al crear un producto | PASS |
| Entrega duplicada del mismo `eventId` | PASS, un unico registro logico |
| Contrato Compose de Develop | PASS |
| Contrato Compose de QA | PASS |
| Contrato Compose de produccion local | PASS |
| Health API `8080`, `8081` y `8082` | `UP` |
| MySQL publicado en `3307`, `3308` y `3309` | PASS |
| Misma imagen promovida a los tres ambientes | PASS |

La prueba funcional creo un producto mediante `POST /api/products` y verifico
su `eventId`, `productId` y `productCode` en
`eventos_producto_procesados`. Los tres contenedores de aplicacion ejecutaron
la misma imagen:

```text
sha256:81846e8d0dcded7882b4216318d8ec76c89dbda1c675c16e8b26012580774598
```

---

## 8. Flujo Git

```text
hu-013-dev -> Develop
hu-013-qa  -> Qa
```

HU-013 termina en `Qa`. La promocion `Qa -> main` se realizara una sola vez,
despues de aprobar la ultima HU del MVP 2.

---

## 9. Siguiente historia

HU-014 formalizara los contratos versionados mediante OpenAPI, reglas de
compatibilidad, un sobre estandar de errores y al menos una prueba de contrato
orientada al consumidor.
