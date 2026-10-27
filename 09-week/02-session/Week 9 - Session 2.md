# Week 9 - Session 2

## Información general

**Proyecto:** RedFish  
**Tema:** Feature flags, despliegue y entrega progresiva  
**Semana:** 9  
**Estado:** Documentación de diseño y recomendaciones

---

## 1. Objetivo

Documentar prácticas para separar el despliegue técnico de la habilitación de funcionalidades y para reducir el impacto de los cambios mediante verificaciones, activación controlada y procedimientos de recuperación.

## 2. Despliegue y lanzamiento

El despliegue consiste en instalar o publicar una versión de la aplicación en un entorno. El lanzamiento consiste en habilitar una funcionalidad para sus usuarios. En algunos casos ocurren al mismo tiempo, pero no son necesariamente el mismo evento.

Separar ambos conceptos permite preparar y verificar una versión antes de habilitar una función para todos los usuarios.

## 3. Feature flags

Una feature flag es una condición de configuración que permite activar o desactivar una funcionalidad sin tener que volver a desplegar toda la aplicación, siempre que la función se haya diseñado para admitir ese control.

Usos posibles en RedFish:

- Habilitar gradualmente una nueva pantalla o flujo.
- Probar una funcionalidad con un grupo limitado de usuarios.
- Desactivar temporalmente una función problemática mientras se investiga.
- Separar la publicación del código de la decisión de habilitar la funcionalidad.

Criterios propuestos:

1. Cada bandera debe tener un propósito y un responsable identificables.
2. El valor por defecto debe ser seguro y adecuado para el entorno.
3. Las banderas no deben utilizarse como sustituto de autorización ni de controles de seguridad.
4. Debe definirse cómo se monitorea la funcionalidad y cómo se revierte su activación.
5. Las banderas temporales deben revisarse y retirarse cuando ya no sean necesarias.

Estos son usos propuestos; no se afirma que RedFish ya tenga un sistema de feature flags.

## 4. Entrega progresiva y recuperación

La entrega progresiva consiste en habilitar cambios de forma controlada y observar su comportamiento antes de ampliar su uso. Según las capacidades reales de la infraestructura, puede realizarse mediante grupos de usuarios, entornos de prueba o activación gradual.

Flujo recomendado:

1. Preparar el cambio en una rama de trabajo.
2. Ejecutar las verificaciones automatizadas y las pruebas pertinentes.
3. Solicitar revisión mediante Pull Request.
4. Integrar el cambio según las reglas del repositorio.
5. Desplegar primero en un entorno no productivo cuando esté disponible.
6. Verificar logs, errores y comportamiento funcional.
7. Habilitar la función gradualmente si la infraestructura lo permite.
8. Si se detecta un problema, desactivar la bandera o aplicar el procedimiento de rollback adecuado.
9. Registrar el resultado y las acciones correctivas.

La opción de recuperación debe elegirse según la causa: desactivar una bandera no revierte necesariamente cambios en la base de datos ni corrige una versión defectuosa del servicio.

## 5. Criterios de aceptación

| ID | Criterio |
|---|---|
| CA-01 | Se explica la diferencia entre desplegar una versión y lanzar una funcionalidad. |
| CA-02 | Cada feature flag propuesta tiene un propósito claro y un comportamiento por defecto definido antes de implementarse. |
| CA-03 | El flujo de entrega incluye pruebas y revisión antes de integrar cambios. |
| CA-04 | Se identifica un procedimiento de recuperación acorde con el tipo de cambio y la infraestructura disponible. |
| CA-05 | La habilitación, verificación y recuperación se documentan con evidencia cuando se realicen. |

## 6. Riesgos y mitigaciones

| Riesgo | Mitigación propuesta |
|---|---|
| Habilitar una función con errores | Probar antes del lanzamiento y habilitar gradualmente cuando sea posible. |
| Dejar banderas obsoletas | Revisar periódicamente su propósito y eliminarlas cuando ya no se necesiten. |
| Confundir una bandera con autorización | Mantener los controles de autenticación y autorización independientes. |
| Rollback incompleto | Definir el procedimiento según el cambio, incluyendo posibles efectos en datos. |
| Falta de evidencia de pruebas | Registrar resultados verificables en el Pull Request o en la tarea. |

## 7. Verificación

Antes de declarar implementadas estas prácticas, comprobar qué mecanismos existen realmente en el proyecto, ejecutar las pruebas disponibles y registrar los resultados. Si no hay infraestructura para una activación gradual, documentar esa limitación en vez de afirmar que el despliegue progresivo está habilitado.

**Estado de implementación:** pendiente de confirmar mediante cambios y pruebas. Este documento registra recomendaciones y no demuestra por sí solo que exista un sistema de feature flags o rollback automatizado.

## 8. Referencia de clase

[OVA — Semana 9, Sesión 2](https://code-corhuila.github.io/ova-web/2026-B/distribuidos/09-week/02-session/)
