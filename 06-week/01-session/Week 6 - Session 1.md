# Week 6 - Sesion 1

## Orquestacion con Docker Compose

**Proyecto:** RedFish  
**Responsable:** LUIS FERNANDO CLAROS RAMOS  
**Asignatura:** Sistemas Distribuidos  
**Semana:** 6  
**Sesion:** 1  
**Historia de usuario:** HU-011

---

## 1. Objetivo de la sesion

Orquestar el backend RedFish y la base de datos MySQL como un sistema
reproducible que pueda iniciarse con un solo comando de Docker Compose.

La solucion conserva la arquitectura de monolito modular. Los modulos de
inventario, pedidos y demas capacidades permanecen dentro de una sola
aplicacion Spring Boot; Docker Compose coordina la aplicacion y su base de
datos, no convierte los modulos en microservicios.

---

## 2. Historia de usuario

### HU-011 - Orquestar RedFish y MySQL con Docker Compose

**Como** responsable del desarrollo de RedFish,  
**quiero** iniciar la aplicacion y MySQL mediante un unico comando,  
**para** disponer de un entorno reproducible con dependencias saludables,
configuracion externa y datos persistentes.

### Criterios de aceptacion

| ID | Criterio |
|---|---|
| CA-01 | `docker compose up --build` inicia la aplicacion y MySQL. |
| CA-02 | Ambos servicios comparten una red declarada y se comunican por nombre de servicio. |
| CA-03 | MySQL debe estar saludable antes de iniciar la aplicacion. |
| CA-04 | La aplicacion publica un estado de salud mediante Spring Boot Actuator. |
| CA-05 | Los datos de MySQL se almacenan en un volumen nombrado. |
| CA-06 | La configuracion se inyecta mediante variables de entorno. |
| CA-07 | Las credenciales reales no se almacenan en Git. |
| CA-08 | El repositorio contiene `.env.example` con las variables requeridas. |
| CA-09 | Los endpoints existentes de productos y clientes siguen funcionando. |
| CA-10 | Las pruebas automatizadas finalizan correctamente. |

---

## 3. Servicios orquestados

| Servicio | Responsabilidad | Puerto |
|---|---|---|
| `app` | Ejecutar el monolito modular Spring Boot. | `8080` |
| `mysql` | Persistir productos y clientes. | `3307` en el host, `3306` en Docker |

Los servicios se conectan a la red `redfish-network`. La aplicacion usa
`mysql` como nombre de host interno:

```text
jdbc:mysql://mysql:3306/redfish
```

No se utilizan direcciones IP fijas.

---

## 4. Orden y estado de inicio

El servicio `mysql` ejecuta `mysqladmin ping` como comprobacion de salud. El
servicio `app` declara la siguiente dependencia:

```text
depends_on -> mysql -> condition: service_healthy
```

Esto evita iniciar Spring Boot mientras MySQL todavia esta inicializando. La
aplicacion tambien dispone de reintento de conexion durante el arranque y
publica su estado en:

```text
GET /actuator/health
```

---

## 5. Configuracion y secretos

`compose.yaml` no contiene contrasenas fijas. Las variables requeridas se
obtienen de un archivo local `.env`, ignorado por Git.

El repositorio conserva unicamente `.env.example`, con valores de ejemplo que
deben reemplazarse en cada ambiente.

Preparacion local:

```powershell
cd D:\descargas\pago\RedFish\RedFish
Copy-Item .env.example .env
```

Variables principales:

| Variable | Proposito |
|---|---|
| `APP_IMAGE` | Nombre y etiqueta de la imagen de RedFish. |
| `APP_PORT` | Puerto HTTP publicado en el host. |
| `MYSQL_PORT` | Puerto de MySQL publicado en el host. |
| `MYSQL_DATABASE` | Base de datos utilizada por RedFish. |
| `MYSQL_USER` | Usuario de la aplicacion. |
| `MYSQL_PASSWORD` | Contrasena del usuario de la aplicacion. |
| `MYSQL_ROOT_PASSWORD` | Contrasena administrativa de MySQL. |
| `SPRING_JPA_HIBERNATE_DDL_AUTO` | Estrategia temporal de esquema JPA. |
| `LOG_LEVEL` | Nivel general de registros. |

---

## 6. Persistencia

MySQL utiliza el volumen nombrado:

```text
redfish-mysql-data
```

El volumen conserva las tablas `productos` y `clientes` cuando los
contenedores se detienen o se vuelven a crear. Eliminar el volumen de forma
explicita tambien elimina los datos y no forma parte del inicio normal.

---

## 7. Ejecucion

Una vez creado el archivo `.env`, el sistema completo se inicia con:

```powershell
cd D:\descargas\pago\RedFish\RedFish
docker compose up --build
```

Para ejecutarlo en segundo plano:

```powershell
docker compose up --build -d
```

Estado de los servicios:

```powershell
docker compose ps
```

Detener los contenedores sin eliminar los datos:

```powershell
docker compose down
```

---

## 8. Validacion esperada

Estado de salud:

```text
GET http://localhost:8080/actuator/health
```

Recursos del MVP:

```text
GET http://localhost:8080/api/products
GET http://localhost:8080/api/customers
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
| Sintaxis de `compose.yaml` | Aprobada con `docker compose config --quiet`. |
| Construccion de la imagen | Aprobada. |
| Estado de MySQL | `healthy`. |
| Estado de la aplicacion | `healthy`. |
| `GET /actuator/health` | Respuesta `UP`. |
| `GET /api/products` | Respuesta correcta. |
| `GET /api/customers` | Respuesta correcta. |
| Persistencia despues de recrear contenedores | Aprobada con el producto de prueba `HU011-TEST`. |
| Pruebas automatizadas | `BUILD SUCCESSFUL`. |

---

## 9. Archivos modificados

```text
RedFish/compose.yaml
RedFish/Dockerfile
RedFish/.env.example
RedFish/build.gradle
RedFish/src/main/resources/application.yaml
docs/backlog.md
docs/Week-06/session-01/Week 6 - Session 1.md
```

---

## 10. Resultado de la sesion

| Elemento | Resultado |
|---|---|
| Inicio de aplicacion y MySQL con un comando | Implementado |
| Red compartida declarada | Implementada |
| Espera por salud de MySQL | Implementada |
| Salud HTTP de la aplicacion | Implementada con Actuator |
| Volumen persistente de MySQL | Implementado |
| Configuracion mediante entorno | Implementada |
| Archivo `.env.example` | Implementado |
| Credenciales fijas en archivos versionados | Eliminadas |
| Pruebas automatizadas | Aprobadas |
| Persistencia despues de recrear contenedores | Aprobada |
| Validacion QA | Pendiente en rama `hu-011-qa` |

---

## 11. Siguiente paso

Validar el sistema completo, documentar la evidencia en la rama
`hu-011-qa` y continuar con la definicion de ambientes y estrategia de
configuracion de HU-012.
