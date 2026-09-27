# Week 8 - Sesion 2

## Story mapping, estimacion y compromiso del MVP 2

**Historia de usuario:** HU-016  
**Rama de desarrollo:** `hu-016-dev`  
**Estado:** Implementada en desarrollo, pendiente de validacion QA

---

## 1. Historia de usuario

### HU-016 - Planificar y comprometer el alcance del MVP 2

Como equipo de RedFish, queremos organizar el recorrido del usuario, estimar el
trabajo restante y ordenar sus dependencias, para comprometer un MVP 2
realizable con comunicacion integrada y persistencia confiable.

---

## 2. Criterios de aceptacion

| ID | Criterio |
|---|---|
| CA-01 | Existe un story map organizado por recorrido y prioridad. |
| CA-02 | La linea de liberacion muestra la rebanada minima de extremo a extremo. |
| CA-03 | El trabajo se prioriza mediante MoSCoW. |
| CA-04 | Las historias comprometidas tienen criterios verificables. |
| CA-05 | Las historias se estiman con puntos relativos Fibonacci. |
| CA-06 | Ninguna historia comprometida conserva un tamano de 8 puntos o mas. |
| CA-07 | Las dependencias entre migraciones, Inventario y Pedidos son visibles. |
| CA-08 | Las dependencias tienen contrato primero y estrategia de mocks. |
| CA-09 | El compromiso utiliza throughput real sin inventar velocidad historica. |
| CA-10 | El plan conserva margen para incertidumbre y defectos. |
| CA-11 | El frontend y capacidades no esenciales quedan bajo la linea. |
| CA-12 | `Qa -> main` ocurre solamente al aprobar la ultima HU del MVP 2. |

---

## 3. Estado actual

RedFish ya dispone de:

- Productos y Clientes con REST y MySQL;
- modelos iniciales de Inventario, Pedidos, Despachos y Vehiculos;
- puertos de colaboracion entre Pedidos e Inventario;
- eventos locales con consumo idempotente;
- OpenAPI, Pact y errores estandarizados;
- Docker Compose y ambientes separados;
- CI, QA y un modelo Agile/DevOps.

Inventario y Pedidos todavia no ofrecen un flujo persistente completo. Esta
brecha define el valor principal pendiente del MVP 2.

---

## 4. Story map

La fuente visual y funcional se encuentra en:

```text
docs/planning/mvp-2-story-map.md
```

El backbone es:

```text
Preparar datos
  -> Controlar stock
    -> Registrar pedido
      -> Reservar sin duplicar
        -> Consultar resultado
          -> Validar y liberar
```

La rebanada comienza con un movimiento de entrada y termina con un pedido
consultable cuyo stock fue reservado una sola vez.

---

## 5. Alcance comprometido

| HU | Resultado | Puntos |
|---|---|---:|
| HU-017 | Migraciones versionadas | 5 |
| HU-018 | Existencias y movimientos | 5 |
| HU-019 | Pedidos y detalles persistentes | 5 |
| HU-020 | Reserva transaccional de inventario | 5 |
| HU-021 | Creacion idempotente de pedidos | 3 |
| HU-022 | Validacion y liberacion del MVP 2 | 3 |
|  | **Total restante** | **26** |

Las historias de 8 o mas puntos fueron evitadas separando persistencia,
integracion e idempotencia. Cada HU conserva un resultado demostrable propio.

---

## 6. Priorizacion MoSCoW

### Must

- migraciones versionadas;
- stock y movimientos persistentes;
- pedidos y detalles persistentes;
- reserva transaccional;
- idempotencia de creacion;
- validacion y liberacion.

### Should

- cliente web inicial;
- alertas de stock;
- cancelacion controlada;
- flujo inicial de despachos.

### Could

- reportes operativos;
- proyecciones de inventario;
- mensajeria durable.

### Won't now

- separacion en microservicios;
- gRPC;
- broker externo;
- pagos;
- aplicacion movil.

`Won't now` significa fuera del MVP 2, no descartado permanentemente.

---

## 7. Estimacion

Se utiliza la escala `1, 2, 3, 5, 8, 13`. Los puntos representan tamano,
complejidad, integracion e incertidumbre; no horas ni productividad individual.

El detalle de cada historia, sus criterios y la justificacion del compromiso se
encuentran en:

```text
docs/planning/mvp-2-commitment.md
```

Las estimaciones deben revisarse al iniciar cada HU. Un cambio se documenta, no
se oculta para conservar artificialmente una cifra.

---

## 8. Capacidad y ciclos

Week 6 y Week 7 muestran un throughput de dos HU por semana. No existen puntos
historicos completados, por lo que `8-10` puntos es una hipotesis inicial de
capacidad.

| Ciclo | HU | Puntos | Objetivo |
|---|---|---:|---|
| 1 | HU-017 y HU-018 | 10 | Base versionada e inventario funcional. |
| 2 | HU-019 y HU-020 | 10 | Pedido persistente con reserva. |
| 3 | HU-021 y HU-022 | 6 | Reintentos seguros y liberacion. |

El ultimo ciclo mantiene margen para defectos y ajustes de integracion. Las
historias `Should` no se agregan automaticamente para ocuparlo.

---

## 9. Dependencias

```text
HU-017
  |-- HU-018 --\
  |             -> HU-020 -> HU-021 -> HU-022
  |-- HU-019 --/
```

Pedidos e Inventario acuerdan primero el contrato de reserva. Los consumidores
pueden trabajar contra mocks o dobles mientras el proveedor completa su
adaptador. Esto evita que un modulo quede detenido esperando la implementacion
interna del otro.

---

## 10. Frontend

HU-023 propone un cliente web inicial de 5 puntos y prioridad `Should`. Puede
comenzar despues de estabilizar la API de Pedidos, usando OpenAPI y mocks, si no
desplaza trabajo Must ni viola el limite WIP.

El frontend no bloquea el MVP 2 porque la rebanada puede demostrarse mediante
API, pruebas automatizadas y Postman. Esta decision puede revisarse con nueva
capacidad, pero no se asume como compromiso actual.

---

## 11. Politica de liberacion

Cada historia sigue:

```text
hu-xxx-dev -> Develop
hu-xxx-qa  -> Qa
```

HU-017 a HU-021 terminan en `Qa` y no generan un PR hacia `main`. HU-022 es la
ultima historia comprometida y valida el conjunto completo. Solo despues de su
aprobacion se ejecuta:

```text
Qa -> main
```

---

## 12. Archivos principales

| Archivo | Responsabilidad |
|---|---|
| `mvp-2-story-map.md` | Recorrido, prioridades y linea de liberacion. |
| `mvp-2-commitment.md` | Historias, puntos, dependencias, ciclos y riesgos. |
| `docs/backlog.md` | Trazabilidad de HU-017 a HU-023. |
| `agile-devops.md` | Capacidad inicial y medicion posterior. |
| `README.md` | Estructura documental actualizada. |

---

## 13. Validacion de desarrollo

Se debe comprobar:

```powershell
git diff --check
cd RedFish
.\gradlew.bat test --no-daemon
```

Resultado obtenido en `hu-016-dev`:

```text
BUILD SUCCESSFUL
27 tests, 0 failures, 0 errors, 1 skipped
```

La prueba omitida corresponde al contexto completo con Testcontainers y ya se
encontraba deshabilitada antes de HU-016. Esta historia no modifica codigo de
produccion ni agrega una nueva omision.

QA validara que la suma de puntos, dependencias, linea de liberacion y politica
de ramas sean consistentes antes de aprobar HU-016.

---

## 14. Flujo Git

```text
hu-016-dev -> Develop
hu-016-qa  -> Qa
```

HU-016 no se promueve individualmente a `main`.

---

## 15. Siguiente paso

Promover HU-016 hacia `Develop`, validarla en `hu-016-qa` y comenzar HU-017 con
la estrategia de migraciones versionadas. El compromiso sera revisado con
velocidad real despues del primer ciclo estimado.
