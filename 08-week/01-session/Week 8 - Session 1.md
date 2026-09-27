# Week 8 - Sesion 1

## Agile y DevOps para el equipo de RedFish

**Historia de usuario:** HU-015  
**Rama de desarrollo:** `hu-015-dev`  
**Estado:** Implementada en desarrollo, pendiente de validacion QA

---

## 1. Historia de usuario

### HU-015 - Formalizar el modelo Agile y DevOps de RedFish

Como equipo responsable de RedFish, queremos establecer acuerdos Agile y
DevOps verificables, para entregar cambios pequenos con responsabilidades
claras, retroalimentacion rapida y operacion compartida..

---

## 2. Criterios de aceptacion

| ID | Criterio |
|---|---|
| CA-01 | Se documentan los roles y responsabilidades mediante una matriz RACI. |
| CA-02 | El ciclo Scrum define refinamiento, planificacion, sincronizacion, revision y retrospectiva. |
| CA-03 | Existe una plantilla de historia con criterios de aceptacion verificables. |
| CA-04 | Se define una Definition of Ready para admitir historias al ciclo. |
| CA-05 | Se define una Definition of Done alineada con `Develop`, `Qa` y `main`. |
| CA-06 | Se establecen limites explicitos de trabajo en curso. |
| CA-07 | Todo cambio se revisa mediante Pull Request con una plantilla comun. |
| CA-08 | La CI se ejecuta en Pull Requests hacia las ramas de ambiente. |
| CA-09 | Se definen WIP, lead time, cycle time, throughput y defectos escapados. |
| CA-10 | El backlog incluye HU-015 y la siguiente actividad de planificacion. |
| CA-11 | Las practicas no contradicen el flujo Git aprobado del proyecto. |

---

## 3. Modelo operativo

La fuente de verdad del proceso se encuentra en:

```text
docs/process/agile-devops.md
```

El documento concentra:

- responsabilidades por rol;
- ceremonias y resultados verificables;
- formato de historia de usuario;
- Definition of Ready y Definition of Done;
- limites WIP;
- revision por Pull Request;
- integracion continua;
- metricas de flujo;
- formato de retrospectiva.

Mantener estas reglas en un solo documento evita contradicciones entre varias
copias del mismo proceso.

La Definition of Ready y la Definition of Done iniciales de Week 1 se conservan
como evidencia historica. HU-015 las refina para incorporar WIP, CI, metricas y
el significado actual de las promociones hacia `Develop`, `Qa` y `main`.

---

## 4. Scrum aplicado a RedFish

El ciclo semanal comienza con un backlog priorizado y termina con un incremento
demostrable y una mejora de proceso.

| Ceremonia | Aplicacion |
|---|---|
| Refinamiento | Confirmar valor, criterios, dependencias, prioridad y tamano. |
| Planificacion | Comprometer solo trabajo que cumple Definition of Ready. |
| Sincronizacion | Hacer visibles avance, siguiente paso y bloqueos. |
| Revision | Demostrar el resultado contra los criterios de aceptacion. |
| Retrospectiva | Acordar una mejora medible para el siguiente ciclo. |

Las actividades se registran en Jira y las decisiones tecnicas permanecen en
el repositorio mediante documentos, contratos, ADR o Pull Requests.

---

## 5. Responsabilidad compartida

La matriz RACI diferencia Product Owner, Desarrollo, QA y DevOps. En un equipo
pequeno una persona puede ocupar varios roles, pero debe conservar las
evidencias correspondientes a cada responsabilidad.

La frase "you build it, you run it" se aplica de la siguiente manera:

- Desarrollo entrega codigo, pruebas y documentacion;
- QA valida el comportamiento y registra defectos;
- DevOps conserva CI, imagenes, configuracion y observabilidad;
- el equipo revisa los fallos sin buscar culpables y convierte el aprendizaje
  en una mejora verificable.

---

## 6. Definition of Ready

Antes de iniciar una HU se comprueba que:

- la historia expresa rol, accion y beneficio;
- los criterios pueden evaluarse como PASS o FAIL;
- la prioridad y estimacion estan registradas;
- el alcance cabe en el ciclo;
- contratos, datos y modulos afectados estan identificados;
- dependencias, riesgos y responsable son visibles.

Esto evita iniciar trabajo basado solamente en un titulo o en una expectativa
no verificable.

---

## 7. Definition of Done

Para RedFish, terminar la implementacion no equivale a terminar la historia.
La HU queda `Done` cuando cumple criterios, pruebas, documentacion, CI, revision
y evidencia QA, y fue promovida a `Qa`.

```text
hu-xxx-dev -> Develop -> hu-xxx-qa -> Qa
```

Cada HU termina en `Qa` y permanece alli mientras avanzan las siguientes
historias. Solamente despues de aprobar la ultima HU del MVP se crea el Pull
Request directo de `Qa` hacia `main`, que convierte el conjunto completo en
una version `Released`.

---

## 8. Limite WIP

El limite principal es una HU en desarrollo por responsable. QA puede mantener
como maximo dos HU activas para todo el equipo.

Si una HU se bloquea, se registra la causa y se intenta resolver antes de
iniciar otra. El trabajo parcialmente terminado no cuenta como throughput.

---

## 9. Metricas

| Metrica | Uso |
|---|---|
| WIP | Detectar exceso de trabajo iniciado. |
| Lead time | Medir tiempo desde Ready hasta Qa. |
| Cycle time | Medir tiempo desde inicio de desarrollo hasta aprobacion QA. |
| Throughput | Contar HU terminadas por ciclo. |
| Defectos escapados | Aprender de problemas encontrados despues de QA. |

Week 6 y Week 7 entregaron dos HU por semana, lo que establece una linea base
de throughput. No se declara todavia velocidad en puntos porque las historias
anteriores no fueron estimadas con planning poker. HU-016 iniciara esa medida.

---

## 10. Plantilla de Pull Request

Se incorpora:

```text
.github/pull_request_template.md
```

La plantilla solicita historia relacionada, alcance, criterios, cambios
tecnicos, pruebas, riesgos y una lista de comprobacion. GitHub la presentara al
crear nuevos Pull Requests desde las ramas HU.

---

## 11. Integracion continua

El workflow existente:

```text
.github/workflows/contract-tests.yml
```

ya se ejecuta en Pull Requests hacia `Develop`, `Qa` y `main`. Aunque su nombre
destaca los contratos, el comando `./gradlew test --no-daemon` ejecuta toda la
suite automatizada, incluidas las pruebas OpenAPI y Pact.

No se duplica el workflow porque dos pipelines con el mismo comando aumentarian
tiempo y ruido sin agregar una validacion diferente.

---

## 12. Archivos principales

| Archivo | Responsabilidad |
|---|---|
| `docs/process/agile-devops.md` | Fuente de verdad del modelo operativo. |
| `.github/pull_request_template.md` | Informacion minima de cada Pull Request. |
| `docs/backlog.md` | Trazabilidad de HU-015 y HU-016. |
| `README.md` | Acceso visible a las reglas de trabajo. |
| `contract-tests.yml` | Retroalimentacion automatizada en cada promocion. |

---

## 13. Validacion de desarrollo

Se debe comprobar:

```powershell
git diff --check
cd RedFish
.\gradlew.bat test --no-daemon
```

Resultado obtenido en `hu-015-dev`:

```text
BUILD SUCCESSFUL
27 tests, 0 failures, 0 errors, 1 skipped
```

La prueba omitida corresponde al contexto completo con Testcontainers y ya se
encontraba deshabilitada antes de HU-015. Esta historia no modifica codigo de
produccion ni agrega una nueva omision.

La validacion formal, las evidencias finales y cualquier defecto encontrado se
registraran posteriormente en `hu-015-qa`.

---

## 14. Flujo Git

```text
hu-015-dev -> Develop
hu-015-qa  -> Qa
```

El mismo ciclo se repetira para las siguientes HU. Cuando la ultima HU del MVP
2 quede aprobada en `Qa`, se ejecutara una sola liberacion:

```text
Qa -> main
```

---

## 15. Siguiente paso

Promover HU-015 hacia `Develop` y realizar su validacion en `hu-015-qa`.
Despues, HU-016 construira el story map, estimara el backlog y definira el
compromiso realista del MVP 2.
