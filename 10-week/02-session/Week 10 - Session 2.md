# Semana 10 — Sesión 2
## Lanzamiento: envío del MVP 2 (sistema integrado)

## 1. Objetivo de la versión

MVP 1 demostró un servicio en ejecución. MVP 2 debe demostrar el sistema integrado: servicios colaborando mediante contratos, consistencia entre los pasos de negocio y configuración/secrets administrados por entorno.

El lanzamiento corresponde al cierre del Corte 2. La versión no se considera lista solo porque la aplicación arranque.

## 2. Promoción y etiquetado

El flujo de trabajo definido para RedFish utiliza ramas de historia por ambiente y promoción controlada. Cada HU debe pasar por desarrollo y QA. La promoción final a producción y la etiqueta `v2.0.0` solo deben realizarse cuando todas las historias comprometidas hayan superado las verificaciones.

Antes de etiquetar:
- confirmar el commit o artefacto que se validó;
- comprobar que la configuración corresponde al entorno;
- no incluir secretos en Git ni en las imágenes;
- registrar los cambios y decisiones arquitectónicas (ADR);
- conservar evidencia reproducible de la versión.

No crear una etiqueta de liberación como si el MVP estuviera aprobado si faltan criterios obligatorios o pruebas.

## 3. Lista de verificación de la versión (Definition of Done)

- [ ] Se cumplen los criterios de aceptación de todas las historias comprometidas.
- [ ] Las pruebas unitarias, de integración y de contrato terminan correctamente; la cobertura se reporta con una medición real.
- [ ] El sistema completo inicia con Docker Compose y sus controles de salud permiten comprobar el estado de los componentes.
- [ ] El flujo de negocio funciona de principio a fin (por ejemplo, crear pedido y reservar existencias).
- [ ] Se demuestra una ruta de fallo y su compensación o manejo idempotente.
- [ ] Los eventos se publican de forma fiable mediante el mecanismo implementado; los consumidores toleran reenvíos.
- [ ] La configuración es específica por entorno y no hay secretos versionados ni incorporados a las imágenes.
- [ ] Los contratos, el registro de cambios y los ADR están actualizados.
- [ ] Las evidencias individuales de cada integrante están completas.
- [ ] La versión aprobada se identifica mediante la etiqueta acordada, `v2.0.0`.

Cada casilla debe marcarse únicamente después de comprobarla. Si algo no aplica, documentar la razón; si está pendiente, mantenerlo visible como bloqueo.

## 4. Demostración de extremo a extremo

Guion recomendado:
1. Iniciar el sistema por el punto de entrada previsto (por ejemplo, la puerta de enlace, si forma parte de la arquitectura desplegada).
2. Mostrar el flujo normal del negocio.
3. Consultar los datos persistidos en las bases de datos propiedad de los servicios implicados.
4. Inyectar un fallo controlado o enviar un evento duplicado.
5. Mostrar la compensación de la Saga o que el consumidor idempotente evita aplicar el efecto por segunda vez.
6. Verificar que no queda una combinación inconsistente de pedido e inventario.
7. Referenciar los contratos y ADR que explican el comportamiento.

La demostración debe usar un entorno de prueba controlado. No provocar fallos en un entorno productivo real.

## 5. Retrospectiva — Corte 3

Registrar problemas observados durante la integración, por ejemplo:
- arranque inestable;
- discrepancias entre contratos;
- errores de consistencia;
- recuperación incompleta ante fallos;
- evidencias o automatizaciones ausentes.

Por cada hallazgo, anotar evidencia, impacto, causa conocida o hipótesis, acción concreta, responsable y prioridad. Convertir los hallazgos en elementos del backlog. La siguiente etapa se orienta a operación del sistema: observabilidad, despliegue, seguridad, CI/CD y versión final.

## 6. Errores comunes

- Mostrar solo el camino feliz.
- Etiquetar una versión sin completar la lista de verificación.
- No demostrar la ruta de fallo ni la compensación.
- Afirmar consistencia sin inspeccionar los datos y el resultado del escenario.
- Dejar configuración o secretos acoplados al entorno equivocado.
- Omitir la retrospectiva y repetir los mismos problemas de integración.

## 7. Evidencias que deben conservarse

- PRs y commits de las historias comprometidas.
- Resultado de CI y comandos de pruebas ejecutados.
- Configuración de despliegue sin secretos.
- Evidencia de flujo normal y de fallo controlado.
- Verificación de persistencia y consistencia.
- Registro de cambios, ADR y etiqueta de versión, una vez aprobada.
- Retrospectiva con acciones asignadas.

> Estado inicial: checklist pendiente de ejecución. Esta guía no certifica que el MVP 2 ya haya sido desplegado, validado o liberado.
