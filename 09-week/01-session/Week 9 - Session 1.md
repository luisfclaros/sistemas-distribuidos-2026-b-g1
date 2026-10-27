# Week 9 - Session 1

## Información general

**Proyecto:** RedFish  
**Tema:** Configuración segura y gestión de secretos  
**Semana:** 9  
**Estado:** Documentación de diseño y recomendaciones

---

## 1. Objetivo

Definir criterios para administrar la configuración de RedFish por entorno y proteger información sensible, reduciendo el riesgo de exponer credenciales o utilizar configuraciones incorrectas durante el desarrollo, las pruebas y la operación.

## 2. Configuración por entorno

Los entornos de desarrollo, pruebas y producción pueden requerir valores diferentes, por ejemplo, direcciones de servicios, nombres de bases de datos y niveles de registro. Estos valores deben configurarse por entorno sin duplicar ni modificar innecesariamente el código de la aplicación.

Criterios propuestos:

- Mantener separados los valores de desarrollo, pruebas y producción.
- No incluir contraseñas ni tokens reales en archivos versionados.
- Usar nombres de variables consistentes y documentar qué variables requiere la aplicación.
- Validar la configuración al iniciar la aplicación y mostrar mensajes de error claros cuando falte un valor obligatorio.
- No publicar información sensible en logs.

Para el proyecto, las variables concretas deben definirse de acuerdo con la configuración real de RedFish. Esta documentación no presupone que ya estén creadas o conectadas.

## 3. Gestión de secretos

Se consideran secretos las contraseñas, tokens de acceso, claves privadas y credenciales de servicios. No deben incluirse en el código fuente, capturas públicas, documentación de ejemplo ni commits.

Buenas prácticas:

1. Leer los secretos desde variables de entorno o desde un gestor de secretos aprobado.
2. Mantener los archivos locales que contienen valores reales fuera del control de versiones y proporcionar, cuando sea útil, un archivo de ejemplo con valores ficticios.
3. Conceder a cada servicio únicamente los permisos que necesita.
4. Rotar una credencial si se expone o se sospecha que fue comprometida.
5. Evitar registrar secretos completos en mensajes de error o logs.
6. Revisar el historial del repositorio si se detecta una exposición; borrar el archivo en un commit posterior no invalida por sí solo el secreto expuesto.

## 4. Criterios de aceptación

| ID | Criterio |
|---|---|
| CA-01 | La documentación identifica los entornos que necesitan configuración independiente. |
| CA-02 | Los ejemplos de configuración usan valores ficticios y no contienen credenciales reales. |
| CA-03 | Se documentan los nombres y propósitos de las variables requeridas, sin publicar sus valores secretos. |
| CA-04 | Se define un procedimiento para rotar credenciales cuando exista una exposición o compromiso. |
| CA-05 | La verificación de implementación se registra con evidencia real antes de declarar estos controles como completados. |

## 5. Riesgos y mitigaciones

| Riesgo | Mitigación propuesta |
|---|---|
| Credenciales guardadas en Git | Usar variables de entorno o un gestor de secretos; revisar cambios antes del commit. |
| Uso de configuración de producción en desarrollo | Separar valores por entorno y validar la configuración al iniciar. |
| Secretos expuestos en logs | Evitar imprimir valores sensibles y revisar los mensajes de error. |
| Credencial comprometida | Revocar o rotar el secreto y revisar los accesos relacionados. |

## 6. Verificación

Cuando se implemente esta propuesta, verificar como mínimo que:

- La aplicación puede arrancar con una configuración de desarrollo válida.
- La aplicación detecta las variables obligatorias ausentes y reporta el problema sin mostrar secretos.
- Los archivos versionados no contienen credenciales reales.
- Las pruebas realizadas y sus resultados quedan registrados en el Pull Request o en la documentación de la tarea.

**Estado de implementación:** pendiente de confirmar mediante cambios y pruebas. Este documento, por sí solo, no demuestra que los controles estén implementados.

## 7. Referencia de clase

[OVA — Semana 9, Sesión 1](https://code-corhuila.github.io/ova-web/2026-B/distribuidos/09-week/01-session/)
