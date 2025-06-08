# Sistemas de referencia (entornos informáticos)

La carga es operada (guiada) por usuarios o no, a partir de ahí puigjaner plantea sistemas de referencia.

* **Por lotes:** toma todo lo que hay que procesar, lo va haciendo y termina. Por ej. Sistemas de Backup, Sistemas de computación científica, sistema de liquidación de haberes.
* **Interactivos**: quien decide adonde va el procesamiento es el usuario. Ej. Videojuegos.
* **Transaccionales**: la atención la procesa de forma completa, o la logra completar de forma correcta o retrocede al estado inicial. Las operaciones son individuales. No hay intervención externa. Ej. Cajero automático.

## Sistemas por lotes o batch

Estos trabajos realizan ciclos de uso de la CPU y de los discos de forma continua hasta que finalizan.

**Índices característicos:**

* Turnaround time: Es el tiempo que transcurre desde que se lanza la ejecución de un trabajo hasta que finaliza
* Productividad: Medida en trabajo por unidad de tiempo

## Sistema transaccional

*Transacción: Tiene un inicio y un fin y produce un resultado. Si la transacción no finaliza correctamente se vuelve toda para atrás. No conozco la cantidad de terminales operando en una transacción.*

Es el tipo más común de sistemas, las partes interactúan entre ellas mediante la transacción de datos.

**Índices característicos:**

* Tiempo de respuesta: sumatoria de todos los siguientes tiempos:
  * Tiempo de reacción
  * Tiempo de ejecución
  * Tiempo de retorno

## Sistema interactivo o por demanda

*Espera órdenes del usuario, para continuar.*

Un sistema interactivo es aquél en que los usuarios acceden a él desde terminales remotos teniendo acceso a la totalidad del sistema operativo. Un usuario desde un terminal, después de un tiempo de pensar o de reflexión, da una orden al terminal que pasa a procesarse por el conjunto CPU y discos y que después de un tiempo dado produce una respuesta en el terminal.

En estos sistemas, pues, la generación de una nueva petición depende de la recepción de la respuesta a la petición anterior.

**Índices característicos:**

* Tiempo de respuesta: Es la sumatoria de los siguientes tiempos:
  * Tiempo de reacción
  * Tiempo de ejecución
  * Tiempo de retorno
* Productividad: Medida en peticiones cumplidas por unidad de tiempo 