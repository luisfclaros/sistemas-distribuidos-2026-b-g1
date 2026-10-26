# Semana 10 — Sesión 1
## Persistencia en sistemas distribuidos: Saga, Outbox y CQRS

## 1. Base de datos por servicio

Cada servicio es responsable de sus propios datos. Otros servicios colaboran mediante contratos públicos y no deben modificar directamente las tablas internas de un servicio ajeno.

La separación evita una base de datos compartida como mecanismo de integración y permite definir responsabilidades y límites de consistencia.

## 2. Sin transacción global: Saga

Una operación de negocio que atraviesa varios servicios no debe asumir que existe una única transacción ACID global. Una Saga coordina pasos locales y define acciones compensatorias para recuperar la consistencia cuando un paso falla.

Ejemplo conceptual:
1. Registrar el pedido.
2. Solicitar la reserva de inventario.
3. Si un paso posterior falla, ejecutar las compensaciones que correspondan.
4. Dejar un estado de negocio explícito y consultable.

La compensación no es un rollback global automático: es una acción de negocio diseñada para cada paso.

## 3. Publicación fiable de eventos: Outbox

### Problema de doble escritura

Si una aplicación guarda un cambio en la base de datos y después publica un evento por separado, puede fallar entre ambas operaciones. El dato queda persistido, pero el evento nunca se publica.

### Solución Outbox

- Escribir el cambio de negocio y el evento pendiente en la misma transacción local.
- Un proceso relé lee la bandeja de salida y publica el evento.
- Considerar que la entrega puede ocurrir más de una vez.
- Hacer idempotentes a los consumidores para que un reenvío no duplique efectos.

Outbox ofrece una escritura atómica del estado y del evento pendiente; no significa que el intermediario y la base de datos compartan una transacción global.

## 4. Lecturas rápidas: CQRS y consistencia eventual

CQRS separa el modelo de escritura (comandos y agregados) del modelo de lectura (consultas y vistas orientadas a la consulta). La vista de lectura puede actualizarse a partir de eventos y, por ello, no necesariamente refleja el cambio de inmediato.

La interfaz o API debe representar ese retraso con estados claros, por ejemplo, “procesando”, en vez de mostrar información como si ya estuviera sincronizada.

## 5. Escenario de fallo para RedFish

Escenario: se persiste un pedido, pero la aplicación falla antes de publicar el evento que necesita Inventario.

Riesgo: el pedido queda registrado, pero la reserva no ocurre.

Control que debe demostrarse según la arquitectura elegida:
- Outbox para no perder el evento entre la escritura del pedido y la publicación.
- Entrega fiable y consumidores idempotentes.
- Saga y compensación para los pasos de negocio que necesiten recuperación.

La estrategia concreta debe corresponder al diseño implementado; no se debe afirmar que Outbox o Saga funcionan sin pruebas y evidencias.

## 6. Errores comunes

- Intentar forzar una transacción ACID global entre todos los servicios.
- Escribir en la base de datos y publicar después sin una estrategia Outbox.
- Implementar consumidores que aplican dos veces el mismo evento.
- Suponer que las vistas CQRS se actualizan instantáneamente.
- Mostrar solo el camino exitoso y no demostrar qué ocurre ante un fallo.

## 7. Criterios de comprensión

- Explicar qué datos pertenecen a cada servicio.
- Describir los pasos de la Saga y las compensaciones relevantes.
- Explicar cómo Outbox evita la pérdida de eventos por doble escritura.
- Demostrar cómo se manejan duplicados.
- Identificar dónde puede ocurrir consistencia eventual y cómo se comunica al usuario.
