# **Unidad 3: Subsistema de Aplicación** {#unidad-3:-subsistema-de-aplicación}

El subsistema de aplicación dispone de y utiliza los recursos (Humanos, SI/TI) de la empresa. 

Para los recursos de SI/TI, se tiene por un lado la determinación de la carga de sistemas (ya que los sistemas deben dar prestaciones a distintas actividades). Se tratarán las técnicas que ayudan a prevenir situaciones de pico donde la carga de trabajo supera a la capacidad.

Es todo lo que hay que hacer para distribuir los recursos existentes en términos de los esquemas de trabajo (modelo de explotación, planificaciones, etc.) 

![][image18]

## **Subsistema de aplicación de SI/TI** {#subsistema-de-aplicación-de-si/ti}

Brindan diferentes servicios y en diferentes niveles de los mismos. Difieren en las PRESTACIONES. El SI es el HW y el SO que lo hace funcionar ⇒ La aplicación de SI/TI es el subsistema cuya finalidad es disponer los recursos de SI/TI en función a la carga de trabajo y los niveles de servicios requeridos para satisfacer el nivel de prestaciones de la organización.  
![][image55]

**Carga** → Conjunto de demandas que realizan los usuarios al sistema durante un intervalo de tiempo. *(Ejs:  Actualización y consulta a la BD, Solicitud de acceso a pag web, Peticiones de salida)*  
**Prestaciones** →  Es el conjunto de funcionalidades/servicios que brinda un SI a sus usuarios. También se refiere a las partes componentes de un sistema  
**Rendimiento** → Es la medida de cómo un determinado SW utiliza el HW con la carga del sistema. El rendimiento de un sistema es inverso al tiempo que le tome al mismo ejecutar procesos.

*Menor tiempo de ejecución, mayor velocidad, mayor rendimiento* 

Por tanto, el subsistema de aplicación consiste en las actividades de asignar, configurar, planificar la capacidad, explotar y evaluar los recursos de SW Y HW.

Las tareas que se realizan son:

* Dimensionar la carga de trabajo → **Análisis y representación de la carga de trabajo**  
  * Definir necesidades → entrada a provisión que define cantidad de dispositivos a comprar u optimizar a partir de la carga de trabajo.

* Asignar los recursos en base a prestaciones requeridas → **Planificación de las prestaciones.**  
  * Una vez incorporado los recursos, como voy a aplicarlos de acuerdo a las prestaciones. espacio en disco, tiempo de servicio, espacio en memoria.

* Evaluar el funcionamiento de las prestaciones → **Evaluación de las prestaciones**  
  * Cómo están funcionando las prestaciones.

### Caracterización de la carga {#caracterización-de-la-carga}

Es el proceso de describir la carga real a través de esos parámetros, generando un modelo que refleje las particularidades más importantes y el comportamiento de la carga real.

**Se denomina *carga* a todas las demandas que realizan los usuarios de un sistema** (programas, datos, órdenes, etc.) **durante un intervalo de tiempo.**

El resultado de las medidas de prestaciones de un sistema es función y, por tanto, es inseparable de la carga bajo la cual fue determinado. Por ello, cuando se da un índice de prestaciones de un sistema, debe especificarse la carga bajo la que fue obtenido dicho índice (la comparación entre sistemas sólo tiene sentido cuando la carga es la misma).

En general, se ve, pues, que las relaciones entre el sistema, **la carga y las prestaciones pueden ser muy complejas**. Las principales causas de esta complejidad son:

* La carga está continuamente fluctuando.  
* La carga interacciona con su entorno

Estas consideraciones justifican la necesidad de llegar a definir cuantitativamente la carga de un sistema, es decir, llegar a establecer un modelo de la carga.

**Una carga está correctamente caracterizada** si, y sólo si, su resultado es un **conjunto de parámetros cuantitativos** seleccionados de acuerdo con los objetivos de la operación de caracterización. 

Por lo tanto, lo primero que se deben definir son los **objetivos.**

Una vez establecidos los objetivos, deben determinarse las herramientas que manipularán (modelos analíticos, simulación, el sistema real, etc.) el modelo de la carga.

⇒ Para evaluar correctamente las prestaciones de un sistema informático, la carga debe de ser seleccionada cuidadosamente. Si bien a la Carga de trabajo se la puede observar, no se la puede utilizar para poder comprender su comportamiento, y por lógica consecuencia, no se puede utilizar para poder efectuar análisis ni proyecciones. También, debe tener en cuenta cuestiones de integridad, seguridad y protección de datos y programa → ***Se debe elaborar un MODELO DE CARGA*** (o bien, carga de prueba o test).

El término **carga de prueba** se utiliza para denominar la carga usada en el estudio de prestaciones → Es la carga obtenida de caracterizar a la carga real, mediante parámetros cuantitativos, cualitativos y funciones que sean relevantes al funcionamiento del sistema. Esta carga puede ser real o sintética.

| Carga de Prueba |  |  |
| :---: | :---- | :---- |
| **Real** | Se observa en un sistema durante su funcionamiento normal. **Inconveniente:** es fluctuante y no permite repeticiones. |  |
| **Sintética** | Está constituida por un conjunto de programas extraídos, o no, de la carga real del sistema informático que *la reproduce de forma compacta*.  Puede utilizarse repetidamente y modificarse sin afectar a la operatividad del sistema. |  |
|  | **Natural** | Consta de un conjunto de programas extraídos de la carga real. Se aplican principalmente en el campo de estudios de selección y aplicación. |
|  | **Híbrida** | Se puede adoptar este tipo de solución cuando la carga a modelar no existe completamente.  Se presenta la carga conocida con un conjunto de programas extraídos de ella, y la no existente mediante algunos de los elementos artificiales. |
| **Artificial** | Consta de componentes diseñados con el propósito de cargar el sistema real o un modelo matemático de él. |  |
|  | **Ejecutable** | **Instrucción de suma** (obsoleto) **Mix:** Mezcla de instrucciones y sentencias. **Kernel:** Programa o fragmento de programa representativo de la carga. Programas cerrados que no pueden modificarse. **Programa sintético:** No realizan ningún trabajo útil, sino que se limitan a consumir recursos del sistema.Les permite simular un amplio espectro de programas reales, desde el punto de vista del consumo de recursos. **Secuencias transaccionales:** Para entornos de un conjunto de usuarios remotos. La conexión entre ambos tiene tantas líneas como el sistema que se está evaluando. **Secuencias conversacionales**: Se describe a nivel funcional el guión de trabajo de cada uno de los usuarios. **Benchmarks:** Programas estándares para simular una carga genérica. |
|  | **No Ejecutable** | **Distribuciones de estadísticas:** En una carga de test probabilística, los parámetros se consideran como variables aleatorias. También se las utiliza en los modelos de simulación gobernados por las distribuciones. **Trazas para la simulación:** Consiste en una secuencia cronológica, registrada en un soporte adecuado y representando la información referente a determinados tipos de acontecimientos. Un acontecimiento es un cambio de estado de algún componente del sistema. |

Características deseables de la carga de prueba:

* **Reproductibilidad:** para reproducir los experimentos.  
* **Compacidad**: Reducir sustancialmente la duración de cada sesión de medición con respecto a la que se requeriría para ejecutar la carga real total.  
* **Compatibilidad:** Obtener una representación de la carga consistente con su uso.  
* **Representatividad:** que indica los aspectos de la carga real retenidos en el modelo.  
* **Flexibilidad:** indica si es posible y poco costoso variar el modelo.  
* **Independencia del sistema:** importante en los problemas de selección.

Se llama *sesión de medida* al intervalo de tiempo en que se realiza un experimento. Esta no tiene por qué continuar en el tiempo.

### Sistemas de referencia (entornos informáticos) {#sistemas-de-referencia-(entornos-informáticos)}

La carga es operada (guiada) por usuarios o no, a partir de ahí puigjaner plantea sistemas de referencia.

* **Por lotes:** toma todo lo que hay que procesar, lo va haciendo y termina. Por ej. Sistemas de Backup, Sistemas de computación científica, sistema de liquidación de haberes.  
* **Interactivos**: quien decide adonde va el procesamiento es el usuario. Ej. Videojuegos.  
* **Transaccionales**: la atención la procesa de forma completa, o la logra completar de forma correcta o retrocede al estado inicial. Las operaciones son individuales. No hay intervención externa. Ej. Cajero automático.

#### ***Sistemas por lotes o batch*** {#sistemas-por-lotes-o-batch}

Estos trabajos realizan ciclos de uso de la CPU y de los discos de forma continua hasta que finalizan.

**Índices característicos:** 

* Turnaround time: Es el tiempo que transcurre desde que se lanza la ejecución de un trabajo hasta que finaliza  
* Productividad: Medida en trabajo por unidad de tiempo

#### ***Sistema transaccional*** {#sistema-transaccional}

*Transacción: Tiene un inicio y un fin y produce un resultado. Si la transacción no finaliza correctamente se vuelve toda para atrás. No conozco la cantidad de terminales operando en una transacción.* 

Es el tipo más común de sistemas, las partes interactúan entre ellas mediante la transacción de datos.

**Índices característicos:**

* Tiempo de respuesta: sumatoria de todos los siguientes tiempos:  
  * Tiempo de reacción  
  * Tiempo de ejecución  
  * Tiempo de retorno

#### ***Sistema interactivo o por demanda*** {#sistema-interactivo-o-por-demanda}

*Espera órdenes del usuario, para continuar.*

Un sistema interactivo es aquél en que los usuarios acceden a él desde terminales remotos teniendo acceso a la totalidad del sistema operativo. Un usuario desde un terminal, después de un tiempo de pensar o de reflexión, da una orden al terminal que pasa a procesarse por el conjunto CPU y discos y que después de un tiempo dado produce una respuesta en el terminal.

En estos sistemas, pues, la generación de una nueva petición depende de la recepción de la respuesta a la petición anterior.

**Índices característicos:**

* Tiempo de respuesta: Es la sumatoria de los siguientes tiempos:  
  * Tiempo de reacción  
  * Tiempo de ejecución  
  * Tiempo de retorno  
* Productividad: Medida en peticiones cumplidas por unidad de tiempo

### Evaluación del rendimiento de un sistema informático {#evaluación-del-rendimiento-de-un-sistema-informático}

La evaluación del rendimiento de un sistema informático se define como la medida de cómo un software determinado está utilizando el hardware con una determinada combinación de programas, que constituyen lo que se denomina carga del sistema.

Las dificultades de realizar la medición son:

* La carga real cambia continuamente.  
* Las variables o índices de medición varían de una instalación y configuración a otra.

Es necesario evaluar un sistema, **para comprobar que su funcionamiento es correcto,** es decir, el esperado. Otro de los objetivos que se pretende al evaluar un sistema informático es **encontrar los factores que impiden un funcionamiento adecuado**, como pueden ser los cuellos de botella. También la predicción del comportamiento del sistema con nuevas cargas. Esta evaluación va a influir en las decisiones de diseño, implantación, compra y modificación de los sistemas informáticos.

Por lo tanto, es necesario evaluar un sistema informático cuando se quiere:

* Diseñar una máquina.  
* Diseñar un sistema informático.  
* Seleccionar y configurar un sistema informático.  
* Planificar la capacidad del sistema informático.  
* Sintonizar o ajustar un sistema informático.

### Magnitudes que se deben medir {#magnitudes-que-se-deben-medir}

**Las magnitudes que se deben medir son:**

* Consumo de tiempo  
* Utilización de recursos o dispositivos  
* Trabajo realizado por el sistema o componentes de los mismos.

Se tienen variables para las magnitudes antes nombradas. Éstas pueden ser:

**Variables externas o perceptibles por el usuario**

* *Productividad:* Es la cantidad de trabajo útil ejecutado por unidad de tiempo en un entorno de carga determinado (normalmente se mide en trabajos por hora o en transacciones por segundo).  
* *Capacidad:* Es la máxima cantidad de trabajo útil que se puede realizar por unidad de tiempo.  
* *Tiempo de respuesta:* Es el tiempo transcurrido entre la entrega de un trabajo o una transacción al sistema y la recepción del resultado o la respuesta. 

**Variables Internas o del sistema** 

* *Factor de utilización de un componente:* Es el porcentaje de tiempo durante el cual un componente del sistema informático (CPU, canal, dispositivo de E/S, etc.) ha sido realmente utilizado.  
* *Solapamiento de componentes:* Es el porcentaje de tiempo durante el cual dos o más componentes del sistema han sido utilizados simultáneamente.  
* *Overhead:* Es el porcentaje de tiempo que los distintos dispositivos del sistema (CPU, discos, memoria, etc.) han sido utilizados en tareas del sistema no directamente imputables a ninguno de los trabajos en curso.  
* *Factor de carga de multiprogramación* Es la relación entre el tiempo de respuesta de un trabajo en un determinado entorno de multiprogramación y su tiempo de respuesta en monoprogramación.  
* *Factor de ganancia de multiprogramación:* Es la relación entre el tiempo total necesario para ejecutar un conjunto de programas secuencialmente en monoprogramación y en multiprogramación.  
* *Frecuencia de fallo de página:* Es el número de fallos de página que se producen por unidad de tiempo en un sistema de memoria virtual paginada*.*  
* Frecuencia de swapping

**Magnitudes referidas al comportamiento**: Tienen más que ver con aspectos funcionales del SI.

* *Fiabilidad:* es la probabilidad que el sistema trabaje correctamente a lo largo de un intervalo de tiempo dado. Se mide por la probabilidad de fallos por unidad de tiempo, o por el tiempo medio entre fallos.  
* *Disponibilidad:* probabilidad de que el sistema esté trabajando correctamente y que esté disponible para realizar sus funciones en el instante considerado *t.*  
* *Seguridad:* probabilidad de que el sistema no perturbe el funcionamiento de otros sistemas ni comprometa la seguridad de las personas relacionadas con él.  
* *Performabilidad:* probabilidad de que las prestaciones del sistema estarán por encima de un cierto nivel en un instante determinado.  
* *Mantenibilidad:* Es la medida de la facilidad con que un sistema puede ser reparado después de un fallo.

### Magnitudes que caracterizan la carga {#magnitudes-que-caracterizan-la-carga}

#### ***Niveles de caracterización de la carga***

Variables que sirven: 

**Para cada componente de la carga**

* *Tiempo de CPU por trabajo:* Es el tiempo total de CPU necesario para ejecutar un trabajo en un sistema determinado.  
* *Número de operaciones de E/S por trabajo:* Es el número total de operaciones de entrada/salida que requiere la ejecución de un trabajo. Conviene desglosarlo por dispositivo.  
* *Características de las operaciones de E/S por trabajo:* Hacen referencia al soporte (cinta, disco, etc.) y, en el caso de discos, a la posición que ocupa el archivo sobre el que se efectúan.  
* *Prioridad:* Es la que el usuario asigna a cada uno de los trabajos que somete al sistema.  
* *Memoria:* Es la que requiere ocupar, para su ejecución, un trabajo determinado (Real y/o virtual).  
* *Localidad de las referencias:* Es el tiempo en el que todas las referencias a memoria hechas por un trabajo permanecen dentro de una página (segmento) o conjunto de páginas (segmentos).

**Para el conjunto de la carga**

* *Tiempo entre llegadas:* Es el tiempo entre dos requerimientos sucesivos para un servicio.  
* *Frecuencia de llegada*: inversa del tiempo medio entre llegadas.  
* *Distribución de trabajos:* Define la proporción existente entre las ejecuciones de los distintos trabajos que constituyen la carga.

**Paro cargas conversacionales (o interactivas):** 

* *Tiempo de reflexión del usuario:* Es el tiempo que el usuario de un terminal de un sistema interactivo necesita para generar una nueva petición al sistema.  
* Número de usuarios simultáneos  
* *Intensidad del usuario: Es la* relación entre el tiempo de respuesta de una petición y el tiempo de reflexión del usuario.

Una carga está correctamente caracterizada **si y sólo si** su resultado es un conjunto de parámetros seleccionados de acuerdo con los objetivos de operaciones de caracterización.

#### ***Opciones para mejorar el comportamiento de un sistema informático***

Las modificaciones que se pueden introducir en un sistema para mejorar su comportamiento pueden hacerse en todos los niveles que influyen en el comportamiento del mismo mediante:

* **Ajuste de los parámetros del SO:** la relación no dice que en todos los SO puedan modificarse con igual facilidad los parámetros expuestos, es una lista de parámetros de un sistema operativo que pueden modificarse con facilidad y cuya variación puede influir en el comportamiento del sistema

  * **Tamaño del quantum**: Es la cantidad de tiempo de uso ininterrumpido de la CPU que un sistema de tiempo compartido asigna a los diferentes trabajos. Si tenemos un SO con varios quantums definidos por prioridades, hay que encontrar el equilibrio en el cambio. Quantum muy grande, se favorece a los procesos con mucho uso de CPU, muy pequeño y se puede producir overhead.  
  * **Prioridad interna**: Es el nivel inicial de prioridad interna que recibe un programa en función de la prioridad externa asignada.  
  * **Factor de Multiprogramación**: Es el Nº máximo de trabajos que están simultáneamente en memoria principal y tienen la opción de usar la CPU y los demás recursos activos del sistema.  
  * **Tamaño de la partición de memoria**: Es la cantidad fija de memoria principal asignada a una cola de trabajos  
  * **Tamaño de la ventana**. Es el intervalo de tiempo durante el cual el sistema toma medidas para determinar el conjunto de trabajos de un programa en un entorno de memoria virtual paginada que use esa política.  
  * **Máxima frecuencia de fallo de página**: a partir del instante en el que se alcanza, se efectúa la suspensión o swapping de algún trabajo para evitar overhead.  
  * **Índice de supervivencia de las páginas**: Es el N° de ráfagas de CPU recibidas por un programa antes de que saque de la memoria principal una página que no haya sido referenciada durante ese período.  
  * **Nº de usuarios simultáneos:** Es el Nº máximo de usuarios de terminales permitidos por un sistema de tiempo compartido.

* **Modificación de las políticas de gestión del sistema operativo:** Es posible que en determinados SO, las políticas no sean las más adecuadas en un caso concreto, por lo que puede ser conveniente y recomendable la sustitución de la rutina encargada de la gestión de un determinado recurso por otra que utilice una política más idónea. Hay que tener en cuenta que hay que adaptar el cambio a las sucesivas versiones del SO.

* **Equilibrado de la distribución de la carga:** hay que tener en claro que se tienen que utilizar todos los dispositivos del sistema informático de la manera más uniforme posible, no existe utilizarlos por igual. Cuando no se logra está uniformidad y hay un desequilibrio muy notable debemos efectuar cambios para tener a lograr el equilibrio deseado. Este tipo de corrección puede lograr mejoras espectaculares en el comportamiento del SI.

* **Sustitución o ampliación de los componentes del sistema:** modificación de la configuración del sistema, bien sea sustituyendo determinados elementos por otros de mayor capacidad o rapidez, o por el aumento del Nº de dispositivos que constituyen la configuración del sistema. Hay que hacer esto siempre **teniendo en cuenta** que se quiere **eliminar** el cuello de botella que se haya detectado.

* **Modificación de los programas:** de forma que su ejecución promedio requiera menos recursos, ya sea por recodificación de los caminos del programa recorrido con mayor asiduidad, o por un montaje que agrupe en la misma página o segmento aquellos módulos de programas que deben coexistir en memoria para la ejecución del programa, etc. Esto provoca la modificación de la carga. Hay que revisar continuamente que las hipótesis que generaron la modificación sigan siendo válidas.

### Técnicas más comunes a la hora de evaluar un sistema {#técnicas-más-comunes-a-la-hora-de-evaluar-un-sistema}

Se denominan *técnicas de evaluación* a los métodos y herramientas que permiten obtener los índices de prestaciones de un sistema que está ejecutando una carga dada y con unos valores determinados de parámetros del sistema.

**Monitorización**  
Los monitores son las herramientas de medición que permiten seguir el comportamiento de los principales elementos de un sistema informático cuando éste se halla sometido a una carga de trabajo determinada.

**Modelado**  
Ésta es la herramienta que hay que utilizar cuando se trata de evaluar el comportamiento de un sistema en el que hay algún elemento (hardware o software) que no está instalado.

**Benchmarking**  
Es un método bastante frecuente de comparar sistemas informáticos frente a una carga característica de una instalación concreta, efectuándose la comparación, básicamente, a partir del tiempo necesario para su ejecución. Generalizando se puede considerar como la medición del comportamiento sobre un prototipo.

### Representatividad de un modelo de carga {#representatividad-de-un-modelo-de-carga}

La representatividad de la carga es una medida de la similitud entre el modelo y la carga real. Una vez que el modelo de carga está disponible se pueden estudiar los efectos de cambios en la carga de una manera controlada simplemente cambiando el peso de los parámetros en el modelo.

La carga puede representarse a distintos niveles, correspondientes a aquéllos en que puede describirse un sistema informático. Esto significa que no hay un criterio único para evaluar la representatividad de un modelo.

#### ***Representatividad a nivel físico***

El modelo de la carga se basa en los consumos absolutos o unitarios de los recursos hardware y software. Este nivel de modelado, se basa en una caracterización orientada a recursos y depende fuertemente del sistema empleado

La mayoría de los parámetros usados en la modelización a este nivel están recopilados por las rutinas de contabilidad *(logging o accoutuing)* presentes en la práctica totalidad de los sistemas operativos.

*Se dice que un modelo de la carga W’ representa perfectamente la carga W si solicita los mismos recursos físicos en las mismas proporciones que W.*

**Campos de aplicación:**

* Sintonización del sistema: Modificación del consumo de recursos para un mejor funcionamiento.  
* Planificación de la capacidad residual: Porcentaje del equipo que no está siendo usado  
* Diseño

#### ***Representatividad a nivel virtual***

En este nivel se consideran los recursos del sistema a nivel lógico (ejemplo: accesos a la base de datos, número de sentencias). A causa de este tipo de parámetros, los modelos de este nivel están próximos al punto de vista del programador y son menos dependientes del sistema que los modelos a nivel físico. Tiene como desventaja, que es más difícil obtener los parámetros para la construcción del modelo.

*Se dice que un modelo de la carga W’ representa perfectamente la carga W si solicita los mismos recursos físicos con la misma frecuencia que W.*

**Campos de aplicación**

* Estudios de ampliación, en los que se quiere prever el funcionamiento del sistema después de añadir nuevas unidades.

#### ***Representatividad a nivel funcional***

En este nivel la carga viene determinada por las aplicaciones que la componen.

En el modelo deben aparecer programas que efectúen las mismas funciones que en la carga original. Así pues, las funciones que componen la carga deben describirse de forma independiente del sistema. Este nivel de carga trae aparejada una dificultad para diseñar sistemáticamente. 

*Se dice que un modelo de la carga W’ representa perfectamente la carga W si realiza las mismas funciones con las mismas proporciones que W.*

**Campos de aplicación:**

* Selección de un computador  
* Planificación de la capacidad.

#### ***Representatividad a nivel de comportamiento***

En el modelo de carga, deben aparecer las mismas variables de comportamiento que los de la carga original. Ejemplo: reproducción de esquemas de seguridad, capacidad, fiabilidad del sistema.

Un modelo *W* representa perfectamente la carga *W,* si produce los mismos valores de los índices de comportamiento que W, cuando se ejecuta en el mismo sistema.

Se considera como criterio de la precisión del modelo, la diferencia que puede existir entre los valores de los índices de comportamiento que produzca la carga y su modelo.

### Planificación de la capacidad (de las prestaciones) {#planificación-de-la-capacidad-(de-las-prestaciones)}

Es el proceso de **identificar la configuración de un sistema** para suministrar el rendimiento satisfactorio ante cargas de trabajo futuras proyectadas. Los recursos sobre los que habitualmente se fija la atención son: procesador, memoria, disco, redes de área local o de almacenamiento, y redes de comunicaciones.

Una metodología básica y sencilla en el proceso de planificación de un sistema informático se puede realizar siguiendo los pasos siguientes:

* Dotar de una instrumentación al sistema (monitores).  
* Monitorizar la utilización del sistema.  
* Caracterizar la carga  
* Predecir el rendimiento bajo diferentes alternativas.  
* Seleccionar la alternativa más eficiente o eficaz según se necesite Mediante **racionalización**.

Una buena planificación de la capacidad, revisada con la periodicidad conveniente, puede, al menos, **minimizar el ajuste de rendimiento en un sistema.** 

El **plan de capacidad** predice los dispositivos que podrían convertirse en el cuello de botella del sistema, avanzando posibles soluciones antes de que se produzca su saturación. Los estudios relacionados con la planificación de la capacidad **dependen de una caracterización correcta de la carga.**

***Pasitos a tomar, explicado:***  
*Debo dotar al sistema de monitores para analizar la carga y sus efectos. Se debe monitorizar la utilización del sistema, se debe observar en un determinado tiempo. A partir de ahí, caracterizamos la carga, es decir, vemos cuánto usa de cada recurso, como son las operaciones de IO, etc.*  
*Podemos predecir el rendimiento bajo distintas alternativas. Gerardo nos decía que la carga es más pesada luego de los feriados y ferias. Pedimos monitorear al sistema un par de fines de semanas. Además, podemos pensar en los posibles casos de picos de carga, plantear distintos escenarios de cómo se va a comportar el sistemas con esa carga particular.*   
*Finalmente, debemos seleccionar la alternativa.*

#### ***Capacidad adecuada*** {#capacidad-adecuada}

¿Qué significa aceptable? →  debe definirlo cada organización.

La capacidad adecuada es función de tres elementos:

* **Los acuerdos de nivel de servicio** *(Service Level Agreements,* SLA, ANS): Son umbrales de productividad, rendimiento y de disponibilidad exigidos y pactados entre los grupos de usuarios y la organización de soporte de los sistemas informáticos de la instalación.

Aquí se debe introducir el término **calidad de servicio** *(Quality of Service,* QoS). Una forma de cuantificar la calidad de servicio es calcular el ratio de la deficiencia de la calidad de servicio ante un nivel deseado de la misma, tal como se indica en la siguiente ecuación:

Desviación QoS=QoS conseguida-QoS deseadaQoS deseada

* **La arquitectura del sistema**: la capacidad adecuada para alcanzar un nivel de servicio acordado se puede conseguir utilizando dispositivos y subsistemas de distintos tipos. La arquitectura seleccionada puede depender de las exigencias del aplicativo que se ejecuta en el sistema, del grado de experiencia y madurez en la explotación del sistema, de la facilidad de administración o de otros motivos, que no tienen por qué estar directamente relacionados con el rendimiento.

* **Presupuesto**: Todas las organizaciones tienen presupuestos que restringen la capacidad de la que se puede disponer. Se debe evaluar el coste total de la propiedad, que es la suma del costo de implementación (compra de HW, sw, formación inicial del personal) y el costo de operación (mantenimiento de HW y sw, de personal, consumo eléctrico, etc.).

Se podría decir que un sistema informático tiene una capacidad adecuada si los niveles de servicio se cumplen continuamente para una tecnología y estándares especificados, y si los servicios se suministran dentro de los límites de coste acordados.

#### ***Niveles de gestión y planificación*** {#niveles-de-gestión-y-planificación}

* **Nivel 0** No hay un programa de gestión de la capacidad. La gestión de la capacidad se realiza ocasionalmente.  
* **Nivel** 1 Se realizan medidas de tendencia y predicción de la utilización en periodos de pico. Se planifica la capacidad de los recursos con unas revisiones periódicas.  
* **Nivel** 2 Se conoce exactamente las utilizaciones de cada uno de los recursos debidas a las cargas de trabajo significativas.  
* **Nivel 3** Existe un sistema automático de análisis y predicción de la carga de trabajo.  
* **Nivel** 4 Se predicen automáticamente los niveles de servicio a partir de las predicciones de capacidad.  
* **Nivel** 5 Se utilizan los criterios de las aplicaciones de negocio a través de un modelo que sirve para predecir los niveles de servicio.

#### ***Métodos de predicción***  {#métodos-de-predicción}

Los métodos de predicción suelen dividirse en dos tipos: cuantitativos y cualitativos.

* Los **métodos cuantitativos** se basan en la existencia de datos históricos para estimar los valores futuros de los parámetros de la carga de trabajo.   
* Los **métodos cualitativos** son un proceso subjetivo basado en el análisis y la intuición sobre un mercado considerado, así como los planes de negocio, las opiniones de expertos, las analogías históricas y cualquier otra información relevante del escenario tecnológico del sistema.

A la hora de seleccionar la técnica de predicción cuantitativa más adecuada se han de considerar los factores siguientes:

* La disponibilidad y la habilidad de los datos históricos.  
* La exactitud y el horizonte de planificación.  
* El patrón encontrado en los datos históricos.

**El modelo se elige a partir de las características del escenario, el objetivo y las variables definidas.**

Patrones de comportamiento o de datos históricos: tendencia, cíclico, estacional, estacionario.En función del patrón de comportamiento se elige la técnica cuantitativa para la predicción de la carga:

* **Regresión lineal** (para datos no estacionales que muestran una **tendencia**)  
* **Medias móviles** (se aplica a datos casi **estacionarios**)  
* **Suavizado exponencial** (para datos **no estacionales** que no muestran una tendencia sistemática, coloca más peso en las observaciones recientes)

![][image56]

#### ***Técnicas cuantitativas para la predicción de la carga*** {#técnicas-cuantitativas-para-la-predicción-de-la-carga}

* ***Regresión lineal**.* Los modelos de regresión se utilizan para estimar el valor de una variable como una función de otras variables. La variable que hay que predecir se llama variable dependiente y las variables utilizadas para predecir su valor se llaman variables independientes.

Las técnicas de regresión son apropiadas para trabajar con datos no estacionales que muestran una tendencia. En concreto, la regresión lineal simple supone que los datos históricos muestran un patrón de evolución lineal.

La ecuación general para calcular la línea de regresión viene dada por:

y=a+b×x

El método de los mínimos cuadrados determina los valores de a y b:

b=i=1nxiyi-n×xyi=1nxi2-n×x2			a=y-b×x

* ***Medias móviles:*** Esta es una técnica de predicción simple que hace que el valor predicho para el siguiente periodo sea la media de observaciones previas. Cuando se aplica a datos casi estacionarios, la exactitud alcanzada por la técnica es normalmente alta.

El valor predicho viene dado por la ecuación

ft+1=yt+yt-1+…+yt-n+1n

Donde ft+1 es el valor de la predicción, yt es el valor observado hasta el instante t*,* y n es el número de observaciones utilizadas para calcular ft+1. Se debería seleccionar un valor de *n* que minimice el error de predicción, que es definido mediante el cuadrado de la diferencia entre el valor predicho y el valor actual. El error cuadrático medio viene dado por el valor:

1nt=1nyt-ft2

Se pueden probar diferentes valores de n para encontrar el que da un menor error cuadrático medio.

* ***Suavizado exponencial:*** Esta técnica se debería utilizar para datos no estacionales que no muestran una tendencia sistemática. El suavizado exponencial realiza una media ponderada de las observaciones pasadas y la presente para predecir un valor. Este valor se puede interpretar como el valor esperado en el futuro. La diferencia con medias móviles está en que el suavizado exponencial coloca más peso en las observaciones recientes.

![][image57]

El valor que hay que predecir se calcula como:

ft+1=1-αft+αyt+1

Es decir, el valor que se obtiene en la predicción es la suma del valor de la predicción en el periodo anterior más el valor observado en la actualidad, ponderados según una probabilidad que puede ser fija o variable. Operando sobre la expresión anterior se obtiene:

ft+1=ft+αyt+1-ft

Donde ft+1 es el valor esperado del periodo t+1, yt+1 es el valor observado en el instante t+1, ft es el valor estimado en el instante t y  es el peso que se le otorga al valor observado más reciente (0 \<α \<1).

En la aproximación de Tustin, se puede tomar más de un valor estimado anterior (si se quiere dar mayor relevancia a lo estimado), o bien se puede tomar más de un valor observado (si se pretende dar mayor relevancia a varias observaciones consecutivas).

#### ***Unidades de predicción natural*** {#unidades-de-predicción-natural}

Una unidad de predicción natural *(Natural Forecast Unit.* NFU) es una variable de negocio cuyo valor está directamente relacionado con los recursos consumidos por una o varias aplicaciones.

Los componentes esenciales de la caracterización de la carga utilizando las unidades de predicción natural para los propósitos de estimación del rendimiento son los siguientes:

* Medidas del trabajo solicitado al sistema utilizando variables de negocio como métrica, que son propiamente las unidades de predicción natural.  
* Las relaciones que muestren el número de transacciones generadas para el periodo caracterizado para cada unidad de predicción natural.  
* Las relaciones que indiquen los recursos del sistema que consume cada transacción.

#### ***Capacidad bajo demanda*** {#capacidad-bajo-demanda}

Es la automatización de la asignación de la capacidad necesaria (durante la ejecución) ante una carga del sistema para cumplir con un nivel de servicio especificado. Es para un nivel de gestión 3 en adelante.

De esta forma, el sistema de análisis y predicción:

* Analiza las medidas de rendimiento que se van realizando en tiempo real.  
* Modela automáticamente sus diferentes facetas.  
* Inician acciones automáticamente para mantener los tiempos de servicio acordados y la utilización de los recursos

Los beneficios son varios:

* Ahorra el personal necesario que realizaba manualmente estas tareas antes  
* Difiere la inversión en la sustitución (reemplazo) de máquinas o contratación de nuevos servicios, consolidando aplicaciones y utilizando un gestor de recursos compartidos  
* Facturación de hardware y software bajo demanda. Esto supone el pago por los recursos que se están utilizando tal como actualmente se factura el consumo de agua o de energía eléctrica en una población: tanto se consume, tanto se paga  
* Aceleración de la implantación de la externalización de la informática de las empresas *(outsourcing).* La garantía de los acuerdos de servicio requeridos por los usuarios, mediante el uso de una planificación de la capacidad en función de la demanda, provoca una mayor aceptación de que esos servicios se realicen externamente a la organización que los demanda, es decir, que los sistemas no pertenezcan propiamente a las empresas que los necesitan.

## 

## **Subsistema de aplicación de RRHH** {#subsistema-de-aplicación-de-rrhh}

Es el subsistema cuya finalidad es la de emplear los recursos de SI/TI y designar al personal del área de acuerdo con los esquemas de trabajo y explotación de la infraestructura de información.

* **Socialización organizacional:** A las personas hay que INTEGRARLAS a la org. No es algo que se hace una sola vez, la org es un sistema dinámico, todo tiene un contexto que puede llegar a cambiar.  
* **Diseño de cargos:** Elaborar las unidades de organización (“cargos”) del área de SI/TI  
* **Evaluar el desempeño:** Evaluar el desempeño de cada miembro respecto de su cargo.

Los Procesos de aplicación de personas incluyen los primeros pasos de la integración de los nuevos miembros en la organización, el diseño del cargo que debe desempeñarse y la evaluación del desempeño en el cargo.

Las personas, después de reclutadas y seleccionadas, deben ser integradas en la organización, destinadas a sus cargos y evaluadas en cuanto a su desempeño. En consecuencia, después de los procesos de provisión siguen los procesos de aplicación de recursos humanos. 

### Socialización organizacional {#socialización-organizacional}

Se inculca en los empleados, los valores, normas y patrones de conducta, etc. Tenemos que funcionar en orden, para no entrar en entropía. Es como el individuo con sus propias costumbre, lo voy llevando al ideal de empleado que necesito; algunas cosas personales, va incorporar, no va a ser 100% ideal a lo que tenía planteado, *si una persona le gusta escuchar música clásica, capaz le va contagiando ese gusto a su equipo.* **Se trata de moldear el individuo, sin sacarle su individualidad.**

Es el proceso **permanente** de inculcar en todos los empleados las actitudes, normas, valores y patrones de conducta y las relativas al cargo que son esperados por la organización y sus departamentos.

La organización trata de inducir la adaptación del comportamiento del individuo a sus necesidades y objetivos imprimiéndole sus características con firmeza. Entre tanto, el nuevo miembro tratará de influir en la organización y el gerente para crear una situación laboral que le proporcione satisfacción y le permita alcanzar sus objetivos personales. En muchas ocasiones, este proceso de personalización está en conflicto con el proceso de socialización propuesto por la organización. 

![][image58]  
La adaptación es mutua en busca de una verdadera simbiosis entre las partes. En otros términos, además de bidireccional, la adaptación es recíproca, pues cada una de las partes influye en la otra

### Métodos para promover la socialización {#métodos-para-promover-la-socialización}

Los más utilizados son:

* **Planeación del proceso selectivo (Para tramos finales)**. Se trata de permitir que el candidato, antes de ser admitido, obtenga información y sepa cómo funciona la organización y cómo se comportan las personas que conviven en ella, así como también preguntarle que onda sus gustos/preferencias. Es decir, se piensan formas de ir socializando a un nivel mínimo en el mismo proceso de selección.

* **Contenido inicial de la tarea.** El gerente puede asignar al nuevo empleado tareas retadoras y capaces de garantizar el éxito al comienzo de la carrera en la organización, y entregarle después tareas gradualmente más complejas y cada vez más exigentes. Cuando se asignan tareas fáciles al principiante, estas no le brindan la oportunidad de lograr éxito ni obtener motivación; necesito que se adapte bien sin sentir una sobreexigencia que, seguramente, no lo va a poder cumplir.

* **Papel del gerente.**Para el empleado nuevo, el gerente representa la imagen de la organización. El gerente puede designar a un supervisor para que se encargue de ser el tutor del nuevo empleado y lo oriente y lo guíe durante el periodo inicial en la organización. Si el supervisor desempeña un buen trabajo en la ejecución de tareas clave, el empleado ve la organización de manera positiva; si, por el contrario, el supervisor es ineficiente en su labor con el nuevo empleado, este verá la organización de modo negativo. El superior debe cumplir tres funciones básicas con el nuevo empleado  
  * Entregar al nuevo empleado una descripción clara de la tarea que debe desempeñar  
  * Suministrar toda la información técnica acerca de cómo realizarla  
  * Proporcionar retroalimentación adecuada al nuevo empleado sobre la calidad de su desempeño.

* **Grupos de trabajo:** El gerente puede encomendar la integración del nuevo empleado a un grupo de trabajo. La aceptación del grupo es fuente fundamental de satisfacción de las necesidades sociales. Además, los grupos de trabajo influyen bastante en las creencias y actitudes de los individuos frente a la organización, así como la manera de comportarse. Un grupo de trabajo bien entrenado, enseña como se hacen las cosas y sirve para que el individuo se integre mejor al equipo.

* **Programas de integración.** Entrenamiento intensivo inicial dirigido a los nuevos miembros de la organización para familiarizarlos con el lenguaje habitual de la organización, los usos y costumbres internos (cultura organizacional), la estructura de la organización (áreas o departamentos existentes), los principales productos o servicios, la misión de la organización y los objetivos organizacionales, etc. El programa de integración busca que el/nuevo empleado asimile con rapidez e intensidad, en una situación de laboratorio, la cultura de la organización, y de ahí en adelante se comporte como un miembro comprometido con la organización.

| Asuntos organizacionales | a. Misión y objetivos básicos de la organización b. Políticas: medios a través de los cuales se alcanzarán los objetivos c. Cómo se organiza y estructura la empresa: qué hace cada área o departamento d. Distribución física del área que utilizará el nuevo miembro e. Principales productos y servicios de la organización f. Normas y reglamentos internos g. Procedimientos de seguridad en el trabajo |
| :---: | :---- |
| **Beneficios** | a. Horario de trabajo, de descanso y de comida (o refrigerios) b. Días de pago y anticipos salariales c. Beneficios sociales ofrecidos por la organización |
| **Presentación** | a. A los superiores y los colegas de trabajo |
| **Deberes de los cargos** | a. Responsabilidades básicas confiadas al nuevo empleado b. Tareas del cargo c. Objetivos del cargo d. Visión general del cargo |

### La empresa como sistema de roles {#la-empresa-como-sistema-de-roles}

**Rol** es el conjunto de **actividades y comportamientos que se solicitan a un individuo que ocupa determinada posición en la organización.** La empresa puede considerarse como una serie de roles o un conjunto de actividades que deben realizar los individuos, y una serie de conjuntos de roles o de grupos que se superponen, cada uno de los cuales está conformado por personas cuyas expectativas giran en torno a un individuo. En resumen, la empresa es un sistema de roles.

*¿Cómo soy yo ejecutando ese cargo? Aparecen los estilos personales y las expectativas a cómo quieren que me comporte (¿Son los que me dan problemas? ¿Son los que me ayudan en mis problemas? etc, etc)*

#### ***Desempeño del rol***

El proceso comienza cuando el jefe explica al subordinado lo que debe hacer (**expectativa del rol**); el empleado recibe las explicaciones e interpreta las expectativas que se le comunican, con algunas distorsiones provenientes del proceso de comunicación (**rol percibido**) y realiza lo que se le pidió, según su interpretación personal (**comportamiento del rol**). Cumplido este paso, el jefe evalúa el desempeño del subordinado (**comportamiento controlado**) y compara este desempeño con la expectativa del rol.

![][image59]

El desempeño del rol no siempre está de acuerdo con las expectativas, pues en este proceso pueden ocurrir cuatro discrepancias o disonancias.

* **Discrepancia de la expectativa***.* Diferencia entre la expectativa del rol transmitida por el jefe y el rol percibido por el subordinado, de acuerdo con su interpretación. No siempre aquello que explica el jefe lo entiende perfectamente el subordinado.  
* **Discrepancia con el rol***.* Diferencia entre el rol percibido por el subordinado y el comportamiento del rol que desempeña. El subordinado no siempre consigue ejecutar lo que entiende que debe hacer, o no es capaz de realizarlo de manera efectiva.  
* **Retroalimentación de la discrepancia***.* Diferencia entre el comportamiento del rol del subordinado y el comportamiento controlado por el jefe. El jefe no siempre evalúa adecuadamente todo lo que el subordinado realiza.  
* **Discrepancia en el desempeño***.* Diferencia entre el comportamiento controlado por el jefe y la expectativa del rol que él transmitió al subordinado. El subordinado no siempre realiza lo que se le dice que ejecute.

La comprensión del desempeño del rol debe tener en cuenta los cuatro aspectos mencionados con anterioridad. Para efectos de lo que se estudiará en este libro, es conveniente relacionar los conceptos de rol y de cargo, aunque sean bastante diferentes entre sí.  de aquí en adelante, en vez de hablar de roles, hablaremos de cargos.

### Evaluación de los procesos de aplicación de las personas {#evaluación-de-los-procesos-de-aplicación-de-las-personas}

| ![][image60] |  |
| ----- | ----- |
| Lado izquierdo **Modelo mecánico** **y determinista:** a cada causa corresponde un solo efecto. **Énfasis en la eficiencia:** exigir que las personas ejecuten sus actividades de acuerdo con el método de trabajo, procedimientos y rutinas establecidos por la organización. **Factores higiénicos:** se otorga mucha importancia a los salarios que se pagan, a los beneficios ofrecidos, al tipo de supervisión aplicado a las personas, a la política interna de la organización. **Permanente y definitivo:** permanencia de las actividades (no cambian). | Lado derecho Los procesos de aplicación se caracterizan por el **modelo orgánico,** el énfasis en la eficacia, la focalización en los factores motivacionales y la innovación y la creatividad, pues se considera que los cargos y las actividades organizacionales no son inmutables y están sujetos a mejoramiento continuo**.** |

### Diseño de cargos {#diseño-de-cargos}

Para la organización, el cargo es la base de la aplicación de las personas en las tareas organizacionales; para la persona, el cargo es una de las mayores fuentes de expectativa y motivación en la organización. Las personas siempre ocupan un cargo cuando ingresan en una organización.

**Puesto** → es una ocurrencia de un cargo (cargo: programador; puestos: 10 programadores)

**Cargo: funciones \+ rol**

El concepto del **cargo** se fundamenta en las nociones de tarea, atribución y función.

* **Tarea***.* Actividad individual que ejecuta el ocupante del cargo. En general, es la actividad asignada a cargos simples y rutinarios.  
* **Atribución***.* Actividad individual que ejecuta la persona que ocupa un cargo. En general, se refiere a cargos más diferenciados. Es algo sobre lo cual uno puede decidir, y la responsabilidad recae sobre él.  
* **Función***.* Conjunto de tareas (cargos por horas) o atribuciones (cargos o meses) que el ocupante del cargo ejecuta de manera sistemática y reiterada. También puede ejecutarlas un individuo que, sin ocupar un cargo, desempeña una función de manera transitoria o definitiva. Para que un conjunto de tareas o atribuciones constituya una función, se requiere que se ejecuten de modo repetido.

**⇒ Cargo**: Conjunto de funciones (tareas o atribuciones) con posición definida en la estructura organizacional, en el organigrama. Un cargo constituye una unidad de la organización y consiste en un conjunto de deberes que lo separan y distinguen de los demás cargos. La posición del cargo en el organigrama define su nivel jerárquico, la subordinación, los subordinados, y el departamento o división donde está situado.

![][image61]

#### ***Concepto de diseño del cargo*** {#concepto-de-diseño-del-cargo}

Diseñar un cargo significa establecer cuatro condiciones fundamentales:

* Conjunto de tareas o atribuciones que el ocupante deberá cumplir (contenido del cargo).  
* Como deberá cumplir esas atribuciones y tareas (métodos y procesos de trabajo)   
* A quién deberá reportar el ocupante del cargo (responsabilidad); es decir, la relación con su jefe, porque responde que cosas puedo responder.  
* A quién deberá supervisar o dirigir (autoridad); es decir, la relación con los subordinados.

El diseño de los cargos representa el modelo que los administradores emplean para proyectar los cargos individuales y combinarlos en unidades, departamentos, y organizaciones. 

**Los cargos** no son estables, estáticos, ni definitivos, sino que **están en evolución, innovación y cambio continuos** para adaptarse a las constantes transformaciones tecnológicas, económicas, sociales, culturales y legales. 

##### **Modelo clásico o tradicional de diseño de los cargos**

Apunta a eficientizar las tareas, tengo un gran detalles de las tareas.

Utilizado por los ingenieros pioneros de la teoría administrativa. Su enfoque de la *administración científica* destaca que, mediante métodos científicos, pueden proyectarse cargos y entrenar a las personas para obtener la máxima eficiencia. Se establecía una separación entre pensamiento (gerencia) y actividad (obreros): los cargos se proyectan según el modelo de hacer y no de pensar, y el entrenamiento en el cargo, estaba restringido a las habilidades específicas necesarias para la ejecución de las tareas. El punto de vista dominante era que cuanto más simples y repetitivas fueran las labores, mayor sería la eficiencia del trabajador. 

En esta lógica fría y mecanicista, el resultado esperado es la eficiencia máxima. Además, aumentarán las utilidades de la organización y, gracias a los incentivos salariales, los salarios de los trabajadores serán mayores.

La siguiente tabla muestra las ventajas esperadas con este modelo y los resultados reales que se obtienen con el mismo:

| Ventajas Esperadas | Resultados Reales |
| ----- | ----- |
| Las funciones que implican los cargos pueden aprenderse rápidamente, lo que requiere poco entrenamiento.  Los cargos pueden ser ocupados por personas no capacitadas pero que están disponibles y con bajos salarios.  Los trabajadores pueden ser cambiados de puesto, debido a las pocas habilidades que se requieren y a la facilidad de entrenamiento.  Los trabajadores no se sienten físicamente cansados debido a la mecanización.  El establecimiento de patrones permite mayor facilidad en el control de la calidad; también se minimiza la probabilidad de error.  La mecanización hace que pueda proveerse la producción.  La administración ejerce el control sobre los trabajadores en tal grado que pueden ser supervisados mediante la observación.  | Los ahorros en el costo de entrenamiento no llegan a materializarse por causa de la elevada rotación de personal.  Los altos índices de ausentismo requieren trabajadores extras. Esto eleva los costos laborales.  Debido al trabajo en línea de montaje y a su naturaleza insatisfactoria, es necesario pagar altos salarios para que las personas acepten los cargos en línea.  Debido a la falta de compromiso de los trabajadores ocurren sustanciales problemas de calidad.  Debido a la rotación del personal se elevan los costos de reclutamiento y selección de los trabajadores.  Los problemas de supervisión aumentan la distancia entre el trabajo y la administración.  |

##### **Modelo humanista de las relaciones humanas**

La única diferencia r**adica en las implicaciones humanas**, puesto que el modelo humanista se centra más en el contexto del cargo **y las condiciones sociales** en que se desempeña, que en el contenido del cargo o en su ejecución. La persona que ocupa el cargo recibe atención y consideración en lo que se refiere a sus necesidades, y no es tratado como máquina. 

Este modelo permite una mayor interacción entre las personas y sus superiores y la participación en algunas decisiones acerca de las tareas de la unidad, como medio de satisfacer las necesidades individuales y de aumentar la moral del personal. Permite el desarrollo de relaciones entre colegas y deja margen para algunas oportunidades de desarrollo individual. El superior debe organizar un grupo de trabajo cohesionado y de apoyo, promover una atmósfera amigable y cooperativa, independientemente de la condición de trabajo, y minimizar los roces entre los empleados.

##### **Modelo situacional o contingencial**

Casi no abunda, diseño el cargo pensado en la variedad que pueda tener dentro de las tareas, pensar en la autonomía de esa persona, trabajar sobre lo que significa ese puesto dentro de la cadena de valor de la org y todos los aspectos de retroalimentación.

Es el enfoque más amplio y complejo; tiene en cuenta dos variables: las diferencias individuales de las personas y las tareas involucradas. De ahí la denominación de situacional, porque depende de la adecuación del diseño del cargo a esas dos variables. **En el modelo situacional convergen tres variables**: la estructura de la organización, la tarea y la persona que la ejecutara.

No se basan en la suposición de estabilidad y permanencia de los objetivos y los procesos organizacionales, sino que, al contrario, son dinámicas y se basan en la ampliación continua del cargo mediante el enriquecimiento de tareas. 

* El modelo situacional supone la aplicación de la capacidad de autodirección y autocontrol de las personas y, sobre todo, de objetivos planeados conjuntamente por el ocupante del cargo y el gerente para que el cargo sea un verdadero factor de motivación.  
* La satisfacción de las necesidades individuales de participación y reconocimiento es un subproducto deseable, pero no el objetivo principal de las actividades gerenciales.

Las oportunidades de obtener mejores resultados del personal y del trabajo aumentan cuando se conjugan tres estados psicológicos esenciales en las personas que ejecutan el trabajo:

1. Cuando la persona cree que su trabajo es significativo y tiene valor.  
2. Cuando la persona se siente responsable por los resultados del trabajo.  
3. Cuando la persona conoce los resultados que obtiene haciendo el trabajo.

Cada cargo diseñado debe reunir cinco dimensiones esenciales:

* **Variedad***:* de habilidades exigidas por el cargo, de operaciones, uso de equipos, procedimientos. Esto es para eliminar la rutina y monotonía.  
* **Autonomía***.* Grado de independencia y criterio personal que tiene el empleado para planear y ejecutar el trabajo.  
* **Significado de la tarea***.* Volumen del impacto reconocible que el cargo produce en otras personas. Se refiere a la interdependencia del cargo con los demás cargos de la organización, y a la contribución de su trabajo en el departamento o la organización como totalidad.  
* **Identidad con la tarea***.* Grado en que el cargo requiere que la persona complete una unidad integral del trabajo. Se refiere a la posibilidad de ejecutar una porción completa o global del trabajo e identificar con claridad los resultados de sus esfuerzos.  
* **Retroalimentación***.* Grado de información de retorno que recibe el empleado para evaluar la eficiencia de su esfuerzo en la producción de resultados. Se refiere a la información de retorno que la persona recibe cuando está trabajando, la cual le indica cómo está desempeñando su tarea.

Las cinco dimensiones esenciales o profundas crean condiciones para que el empleado encuentre satisfacción intrínseca en el cumplimiento de la tarea que realiza. Estas condiciones permiten que los factores motivacionales o de satisfacción influyan profundamente en el cargo.

#### ***Enriquecimiento de los cargos*** {#enriquecimiento-de-los-cargos}

Para enriquecer un cargo hay que **redistribuir sus elementos**. Es una técnica para que una persona tenga una variación del cargo y prepara a la persona para que ascienda. Cuando quiero empezar a enriquecer el trabajo de alguien pienso en dos dimensiones: 

* **Horizontal:** empiezo a incluir trabajo previo y trabajo posterior, siempre que se pueda (adición de responsabilidades en el mismo nivel). Por ejemplo, yo soy un programador al que le empiezo a agregar tareas de definición de requerimientos.  
* **Vertical:** empiezo a hacer tareas operativas o automatizarlas y le empiezo a dar más responsabilidades y decisiones (adicción de responsabilidades de nivel gradualmente más elevado).

*Si el cargo se amplía para que el empleado cumpla una mayor variedad de tareas o un mayor número de operaciones, el cargo se enriquece horizontal o lateralmente. Por el contrario, si el empleado debe involucrarse en la planeación, organización, e inspección, además de realizar su trabajo, el cargo se enriquece verticalmente.*   
*![][image62]*  
Si bien el enriquecimiento del cardo produce efectos convenientes y positivos, también puede generar efectos colaterales inconvenientes, en especial si las organizaciones privilegian el status quo. La principal dificultad del enriquecimiento de los cargos está en la resistencia al cambio ante el incremento de las tareas y atribuciones.  
![][image63]

Hay muchos factores implícitos en el tema, pero el principal es que, si la organización no está suficientemente madura y concientizada para poner en marcha un programa sincero y auténtico de enriquecimiento de cargos, es mejor no intentarlo.

### Descripción y análisis de cargos {#descripción-y-análisis-de-cargos}

Las necesidades básicas de recursos humanos para la organización, sea en cantidad o en calidad, se establecen mediante un esquema de descripción y especificación de cargos.

**Descripción** → Pone énfasis en el contenido *(qué hace, cómo, cuándo; son aspectos intrínsecos*).

**Análisis** → Pone énfasis en los requisitos de formación y responsabilidades *(aspectos extrínsecos).*

Es necesario que se analicen y se describan los cargos para conocer su contenido y sus especificaciones, con el fin de administrar los recursos humanos empleados en ellos.

![][image64]

#### ***DESCRIPCIÓN de cargos*** {#descripción-de-cargos}

Es necesario describir un cargo, para conocer su contenido. 

Es un proceso que consiste enumerar las tareas o atribuciones que conforman un cargo y que lo diferencian de los demás cargos que existen en la empresa; es la enumeración de detallada de las atribuciones o tareas del cargo (que hace el ocupante), la periodicidad de la ejecución (cuando lo hace), los métodos aplicados para la ejecución de las atribuciones o tareas (por qué lo hace).

Un cargo puede ser descrito como una unidad de la organización, que consiste en un conjunto de deberes y responsabilidades que lo distinguen de los demás cargos. Los deberes y responsabilidades de un cargo corresponden al empleado que lo desempeña, y proporcionan los medios con que los empleados al logro de los objetivos en una empresa.

Básicamente, tareas o funciones “son los elementos que conforman un rol de trabajo y que debe cumplir el ocupante del cargo”. 

Un cargo es la reunión de todas aquellas actividades realizadas por una sola persona, que pueden unificarse en un sólo concepto y ocupa un lugar formal en el organigrama.

En resumen, la descripción de un cargo está orientada hacia el contenido de los cargos, es decir, hacia los aspectos intrínsecos de los cargos.

![][image65]

#### ***ANÁLISIS de cargos*** {#análisis-de-cargos}

La descripción de cargos y análisis de cargos están estrechamente relacionados en su finalidad y en el proceso de obtención de datos; a pesar de esto están perfectamente diferenciados entre sí: la descripción se preocupa por el contenido del cargo (qué hace el ocupante, cuándo lo hace, cómo lo hace y por qué lo hace), en tanto que el análisis pretende estudiar y determinar todos los requisitos de calificación, responsabilidades implícitas y las condiciones que el cargo exige, para poder desempeñarlo de manera adecuada. Este análisis es la base para la evaluación y la clasificación que se harán de los cargos para efectos de comparación.

**Estructura del análisis de cargos**  
Por lo general, el análisis de cargos se refiere a cuatro áreas de requisitos, aplicados casi siempre a cualquier tipo o nivel de cargo.

* **Requisitos Intelectuales:** Tienen que ver con las exigencias del cargo, en lo que hace referencia a los requisitos intelectuales que el aspirante debe poseer para poder desempeñar el cargo de manera adecuada. Los factores de especificación son los siguientes:  
* **Requisitos físicos:** Tienen que ver con la cantidad y continuidad de energía y esfuerzos físicos y mentales requeridos, y la fatiga provocada, y también con la constitución física que necesita el ocupante para desempeñar el cargo adecuadamente.  
* **Responsabilidades implícitas:** Se refiere a la responsabilidad que el ocupante del cargo tiene, además del trabajo normal y de sus funciones (atribuciones), con la supervisión del trabajo de sus subordinados, con el material, con las herramientas o equipos, con el patrimonio de la empresa, etc.   
* **Condiciones de trabajo:** Se refiere a las condiciones ambientales del lugar donde se desarrolla el trabajo y sus alrededores, que puede hacerlo desagradable, molesto o sujeto a riesgos, exigiendo al ocupante del cargo una fuerte adaptación para mantener su productividad y rendimiento. 

Cada una de estas áreas está dividida en varios factores de especificaciones. Los factores de especificaciones son puntos de referencia que permiten analizar una gran cantidad de cargos de manera objetiva.

![][image66]

#### ***Métodos de descripción y análisis de cargos*** {#métodos-de-descripción-y-análisis-de-cargos}

La descripción y análisis de cargos son responsabilidad de línea y función de *staff*, es decir, la línea responde por las informaciones ofrecidas, en tanto que la prestación de servicios de obtención y manejo de la información es responsabilidad de staff. El analista de cargos puede ser un funcionario especializado de staff, como el jefe de departamento en que está localizado el cargo, como también puede ser el propio ocupante del cargo. 

Los métodos que más se utilizan en la descripción y análisis de cargos son: 

* Observación directa.   
* Cuestionario.   
* Entrevista directa.   
* Métodos mixtos. 

##### **Método de observación directa** 

Es uno de los métodos más utilizados, tanto por ser el más antiguo como por su eficiencia. El análisis del cargo se efectúa mediante la observación directa y dinámica al ocupante del cargo, en pleno ejercicio de sus funciones, en tanto que el analista de cargos anota los puntos clave de su observación en la hoja de análisis de cargos.

Es más recomendable para aplicarlo a los trabajos que comprenden operaciones manuales o que sean sencillos y repetitivos.

Dado que no en todos los casos la observación responde todas las preguntas, ésta suele ir acompañada de entrevista y análisis con el ocupante o con su supervisor. 

**Características:** La participación del analista de cargos en la recolección de información es activa, la del ocupante es pasiva.

**Ventajas:**

* Veracidad de los datos obtenidos ya que se originan en una sola fuente y la misma es ajena a los intereses de quien ejecuta el cargo.  
* No requiere que el ocupante del cargo deje de hacer sus labores.  
* Ideal para aplicarlo en cargos simples y repetitivos.  
* Correspondencia adecuada entre los datos obtenidos y la fórmula básica del análisis de cargos (que hace, cómo lo hace y por qué lo hace).

**Desventajas**:

* Costo elevado porque el analista de cargos requiere invertir bastante tiempo para que el método sea completo.  
* La simple observación, sin el contacto directo y verbal con el ocupante del cargo no permite obtener datos importantes para el análisis.  
* No se recomienda aplicarlos a cargos que no sean sencillos y repetitivos.

Se recomienda aplicarlo en combinación con otros para que el análisis sea más completo y precioso.

##### **Cuestionario**

El análisis se realiza solicitando al personal que llene un cuestionario de análisis de cargos, y que registre todas las indicaciones posibles acerca del cargo, su contenido y sus características.

Cuando se trata de una gran cantidad de cargos semejantes, de naturaleza rutinaria y burocrática, es más rápido y económico elaborar un cuestionario que se distribuya a todos los ocupantes de esos cargos.

**Características:** La participación del analista de cargos en la recolección de datos es pasiva, la del ocupante es activa.

**Ventajas**

* Se proporciona una visión más amplia de su contenido y de sus características, además de que participan varias instancias jerárquicas.  
* Es el método más económico.  
* Es el método que más personas abarca.  
* Es el método ideal para analizar cargos de alto nivel, sin afectar el tiempo ni las actividades de los ejecutivos.

**Desventajas**

* No se recomienda su aplicación en cargos de bajo nivel.  
* Exige que se planee y elabore con cuidado.  
* Tiende a ser superficial o distorsionado en lo referente a la calidad de las respuestas escritas.

##### **Método de la entrevista** 

Es el enfoque más flexible. Si está bien estructurada puede obtenerse información acerca de todos los aspectos del cargo, de la naturaleza y la secuencia de las diversas tareas que comprende el cargo, y de los porqué y cuando. Permite comparar la información obtenida por medio de los ocupantes de otros cargos similares y verificar las incoherencias de la información. Garantiza una interacción frente a frente entre el analista y el empleado. Lo cual permite la eliminación de dudas y desconfianzas. 

**Características:** La participación del analista y del ocupante es activa.

**Ventajas**

* Los datos relativos a un cargo se obtienen de quienes lo conocen mejor.  
* Hay posibilidad de analizar y aclarar todas las dudas.  
* Este método es el de mejor calidad y el que proporciona mayor rendimiento en el análisis, debido a la manera racional de reunir los datos.  
* Se puede aplicar a cargos de cualquier tipo y nivel.

**Desventajas**

* Una entrevista mal conducida puede llevar a que el personal reaccione de modo negativo, no la comprenda ni acepte sus objetivos.  
* Puede generar confusión entre opiniones y hechos.  
* Se pierde tiempo si el analista no se prepara bien para realizarla.  
* Costo operativo elevado.

##### **Métodos mixtos** 

Para contrarrestar las desventajas y obtener el mayor provecho posible de las ventajas. Los métodos mixtos son combinaciones de dos o más métodos de análisis. Las combinaciones más comunes son:

* Cuestionario y entrevista, ambos con el ocupante del cargo   
* Cuestionario con el ocupante y entrevista con el supervisor   
* Cuestionario y entrevista, ambos con el supervisor   
* Observación directa con el ocupante y entrevista con el supervisor   
* Cuestionario y observación directa, ambos con el ocupante del cargo.  
* Cuestionario con el superior y observación directa con el ocupante del cargo, etc.

#### ***Objetivos de la descripción y el análisis de cargos*** {#objetivos-de-la-descripción-y-el-análisis-de-cargos}

La aplicación de los resultados del análisis de cargos es muy amplia: reclutamiento y selección de personal, identificación de necesidades de capacitación, definición de programas de capacitación, planeación de la fuerza de trabajo, evaluación de cargos, proyecto de equipo y métodos de trabajo, etc.

Los principales objetivos son:

* Ayudar a la elaboración de los anuncios, demarcación del mercado de mano de obra donde debe reclutarse, etc., como base para el reclutamiento del personal   
* Determinar el perfil ideal del ocupante del cargo, como base para la selección de personal   
* Suministrar el material necesario según el contenido de los programas de capacitación, como base para la capacitación de personal   
* Determinar las franjas salariales, como base para la administración de salarios   
* Estimular la motivación del personal, para facilitar la evaluación de desempeño y verificar el mérito funcional   
* Servir de guía del supervisor en el trabajo con sus subordinados, y guía del empleado para el desempeño de sus funciones   
* Suministrar datos relacionados con higiene y seguridad industrial los datos relacionados para minimizar la insalubridad y peligrosidad de ciertos cargos. 

#### ***Equipo de trabajo*** {#equipo-de-trabajo}

Un equipo de trabajo es una unidad de dos o más personas con habilidades complementarias que están comprometidas en un propósito común y con un conjunto de metas de rendimiento y de expectativas, para lo cual establecen normas colectivas de rendición de cuentas (accountability). Los premios y los fracasos son responsabilidad compartida.

*Todos los equipos son grupos formales (constituidos oficialmente), pero no todos los grupos formales son equipos.*

El concepto de equipo implica

* Sensación de **misión compartida y responsabilidad** colectiva.  
* **Metas y tareas comunes**. Al equipo le une las metas.  
* **Roles de liderazgo** compartido o rotativo.  
* **Rendición de cuentas** individual y mutua dentro del equipo.  
* **Igualdad**: no hay protagonismo de ningún miembro, cada cual suprime su ego individual para el bienestar de todos.

La tendencia de conformación de equipos estaría causada por:

* En un equipo es posible alcanzar sinergia – cooperación creativa. Los resultados que logra un equipo son mejores que los individuales.  
* Los miembros del equipo a menudo evalúan el razonamiento del otro, con lo que el equipo tiene mayores probabilidades de evitar errores mayores.  
* Los equipos contribuyen eficazmente a la innovación y al mejoramiento continuo. Aceleran la toma de decisiones y los miembros del equipo obtienen mayores satisfacciones de sus trabajos.

***Tipos de equipo***

* **Según su propósito:** de desarrollo de un producto, reingeniería, o cualquier otro.  
* **Según su estructura**: dirigida (identificación de un líder formal), auto-dirigida  
* **Según su duración**: permanente, temporal.  
* **Según su membresía** (de donde vienen los integrantes): funcional (todos los miembros vienen de una misma área de la organización), inter-funcional (personal de distintas áreas).

***Características de equipos efectivos***

* Compromiso unificado  
* Metas claras  
* Habilidades pertinentes (habilidades técnicas que se requieren según el propósito)  
* Habilidades para negociar (Consenso, convencer a usuarios)  
* Apoyo interno (de qué modo se puede ayudar mutuamente en las tareas)  
* Apoyo externo (de parte de la organización)  
* Liderazgo apropiado  
* Confianza mutua  
* Buena comunicación 

***Equipos de proyecto***   
**Proyecto:** Es un esfuerzo **temporal** orientado a la creación de un producto o servicio **único**.

**Administración de proyectos (project management):** es el conjunto de conocimientos, habilidades, herramientas y técnicas; aplicadas a las actividades a realizar, para satisfacer los requerimientos del Proyecto.

**El gerente de proyecto – responsabilidades.**

* integrar los esfuerzos de las personas provenientes de la distintas áreas de la organización para alcanzar los objetivos del proyecto  
* definir la metodología de trabajo  
* proveer recursos  
* asegurar contrataciones adecuadas  
* evaluar progresos  
* establecer medidas correctivas

**Equipo de proyecto:** Grupo de personas lideradas por el Gerente de Proyecto, pueden representar áreas funcionales u organizaciones o bien profesionales independientes, que desempeñan roles específicos, su número suele variar durante el avance del proyecto. Al final del proyecto son asignadas a un nuevo emprendimiento o retornan a sus áreas u organizaciones o se desvinculan (en el caso de profesionales independientes).

***Conformación de un equipo de proyecto.***

* **Son creados a partir de la tarea:** Los equipos de proyectos se integran por la selección de especialistas técnicos que son elegidos primordialmente por su capacidad para desarrollar una determinada función en el proyecto y si bien es conveniente tomar en cuenta su afinidad personal, éste nunca es un factor determinante.  
* **Se integran una vez** **establecido el objetivo:** La organización que requiere un producto o servicio establece primero el objetivo y posteriormente integra al grupo, los miembros del equipo deberán adherirse al fin una vez que han ingresado al equipo.  
* **No necesariamente comparten valores ni modelos mentales***:* La selección a partir de la especialidad técnica, hace que el equipo tienda a ser "multicultural".  
* **Tienen una existencia efímera:** La naturaleza única del proyecto hace que se formen grupos nuevos, que durante el proyecto se incorporen nuevos participantes y que los esfuerzos de comunicación e integración deban dar resultados en muy corto plazo, a fin de resultar de utilidad para el proyecto.  
* **Están subordinados al objetivo:** El sentido de utilidad es muy intenso en el proyecto, la integración del equipo es un medio para lograr el objetivo y nunca un fin por sí mismo. 

### Evaluación de desempeño {#evaluación-de-desempeño}

Es la apreciación sistemática del desempeño de cada persona en el cargo o del potencial de desarrollos futuros. **Es un proceso para estimular o juzgar** el valor, la excelencia, las cualidades de una persona.

Es una zona gris, porque es cierto que cuando incorporo por primera vez a las personas estoy evaluando el desempeño, pero la evaluación de alguien en su desempeño **se mide cuán integrado está**, **cuán aplicado está,** pero es una herramienta de seguimiento de RRHH (esto se retoma en Unidad 5). **Es algo puntual para ver cuánto le falta a una persona para integrarse**.

**Objetivo de la evaluación de desempeño:**

* Justificar el procedimiento salarial recomendado por el superior.  
* Detectar oportunidades de mejoramiento del desempeño del empleado (momento de verdad).  
* Objetivos intermedios, entre otros: capacitación, mejoramiento de las relaciones interpersonales entre el supervisor y el empleado, conocimiento de los estándares de la organización, autoperfeccionamiento del empleado.

⇒ No estamos interesados en el desempeño general, sino en **el desempeño del cargo**, en el comportamiento de rol del ocupante de cargo. El desempeño del cargo es situacional. El valor de las recompensas y la percepción de que las recompensas dependen del esfuerzo determinan el volumen de esfuerzo individual que la persona está dispuesta a realizar, una perfecta relación costo-beneficio. A su vez, el esfuerzo individual depende de las habilidades y capacidades de la persona, y de su percepción del papel que desempeñará. Todas estas variables condicionan el desempeño del cargo.

![][image67]

Una evaluación es un concepto dinámico, ya que los empleados **son siempre evaluado**s con cierta continuidad, sea formal o informalmente, en las organizaciones. Es un medio a través del cual es posible localizar problemas de supervisión de personal, de integración del empleado a la organización o al cargo que ocupa, etc.

#### ***Responsabilidad por la evaluación de desempeño*** {#responsabilidad-por-la-evaluación-de-desempeño}

De acuerdo con la política de recursos humanos adoptada por la organización, la responsabilidad por el desempeño humano puede atribuirse a diferentes personas u órganos.

##### **El gerente** 

Existe una rígida centralización. La mayor parte de las veces, la evaluación de desempeño es responsabilidad de línea y función de staff con la ayuda de la dependencia de administración de recursos humanos. Quién evalúa al personal es el propio jefe, el staff de la dependencia de recursos humanos proyecta, prepara, y luego acompaña y controla el sistema, en tanto que cada jefe aplica y desarrolla el plan dentro de su círculo de acción. De esta forma, el jefe mantiene su autoridad de línea, en tanto que la dependencia de administración de recursos humanos mantiene su autoridad de staff.

##### **El empleado**

Algunas organizaciones más democráticas permiten que el mismo individuo responda por su desempeño y realice su autoevaluación. En estas organizaciones cada persona autoevalúa su desempeño, eficiencia y eficacia, teniendo en cuenta parámetros establecidos por el gerente o la organización.

##### **El empleado y el gerente**

En la actualidad las organizaciones están adoptando un esquema dinámico y avanzado de administración del desempeño. Aquí resurge la vieja administración por objetivos (APO). Ahora la APO es democrática, participativa, involucrada y muy motivadora. La evaluación del desempeño recorre los siguientes caminos:

* **Formulación de objetivos por consenso:** entre el gerente y el evaluado.  
* **Compromiso del personal en la consecución de los objetivos fijados en conjunto**. Siempre es necesario que el evaluado acepte plenamente los objetivos y que se comprometa a alcanzarlos  
* **Actuación y negociación con el gerente en la asignación de los recursos y los medios necesarios para alcanzar los objetivos**. Definidos los objetivos por consenso, el paso siguiente es conseguir los recursos, si no los hay, los objetivos se tornan inalcanzables.  
* **Desempeño**: Comportamiento del evaluado en la búsqueda de los objetivos fijados. Constituye la estrategia individual para lograr los objetivos deseados.  
* **Medición** **constante** de los resultados y comparación con los objetivos fijados. Verificación de los costos y beneficios involucrados en el proceso.   
* **Retroalimentación intensiva y medición conjunta continúa**. El evaluado debe tener una percepción de cómo va marchando, para establecer una relación entre el esfuerzo y el resultado alcanzado.

En esta concepción, la evaluación del desempeño no comienza por la apreciación del pasado, sino por la preparación del futuro

##### **El equipo de trabajo**

El equipo de trabajo también puede evaluar el desempeño de cada uno de sus miembros y programar con cada uno de ellos las medidas necesarias para mejorarlo cada vez más. El equipo además define sus objetivos y metas.

##### **El órgano de gestión de personal**

Es una alternativa corriente en organizaciones más conservadoras, aunque están dejando de practicarla por su carácter centralista y burocrático en extremo.

En este caso, el órgano de gestión de personal responde por la evaluación del desempeño de todos los miembros de la organización. Cada gerente proporciona la información del desempeño de cada empleado, la cual se procesa e interpreta para enviar informes o programas de pasos coordinados por el órgano de gestión de personal. Se basa en lo genérico y no en lo particular.

##### **Comité de evaluación**

La evaluación del desempeño corresponde a un comité nombrado para este fin, y constituido por los empleados permanentes o transitorios, pertenecientes a diferentes departamentos. La evaluación es colectiva y la realiza un grupo de personas.

Los miembros permanentes o estables participan en todas las evaluaciones, y su papel es mantener el equilibrio de los juicios, el acatamiento de los estándares y la permanencia del sistema. Los miembros transitorios son el gerente de cada evaluado o su supervisor.

Esta alternativa también recibe críticas por su aspecto centralizador y por su espíritu de juzgamiento, en lugar de utilizarse en la orientación y el mejoramiento continuo del desempeño. 

##### **Evaluador de 360°**

Es una innovación reciente en la apreciación del desempeño, según la cual cada persona es evaluada por personas de su entorno; esto significa cualquier persona que mantenga cierta interacción o intercambio participa en la evaluación de su desempeño: El superior, los subordinados, colegas, proveedores internos y clientes internos, de modo que ésta refleje los puntos de vista de los diversos individuos involucrados en el trabajo de cada persona. 

#### ***Objetivos de la evaluación de desempeño*** {#objetivos-de-la-evaluación-de-desempeño}

La evaluación de desempeño no puede reducirse al simple juicio superficial y unilateral del jefe con respecto al comportamiento del subordinado; es necesario ir a un nivel de mayor profundidad, ubicar causas y establecer perspectivas de común acuerdo con el evaluado. Si debe modificarse el desempeño, del evaluado que es el mayor interesado, debe adquirir conocimientos del cambio planeado, y saber también por qué y cómo deberá implementarse este, debe recibir retroalimentación adecuada y reducir discrepancias con respecto a su actuación en la organización. 

En la mayoría de las organizaciones, el programa tradicional y amplio de evaluación de desempeño tiene dos propósitos principales: salarial recomendada por el supervisor.

* Buscar una oportunidad para que el supervisor re-examine el desempeño del subordinado, y fomentar la discusión acerca de la necesidad de superación.  

La evaluación de desempeño no es por sí misma un fin, sino una herramienta para **mejorar los resultados de los recursos humanos**. Para alcanzar este objetivo básico, la evaluación de desempeño intenta alcanzar diversos objetivos intermedios:

* Adecuación del individuo al cargo;  
* Entrenamiento;  
* Promociones;  
* Incentivo salarial por buen desempeño;  
* Mejoramiento de las relaciones humanas entre supervisor y subordinado;  
* Autoperfeccionamiento del empleado;  
* Informaciones básicas para la investigación de recursos humanos;  
* Cálculo del potencial de desarrollo de los recursos humanos;  
* Estímulo a la mayor productividad;  
* Oportunidad de reconocimiento de los patrones de desempeño de la empresa;  
* Retroalimentación de información al propio individuo evaluado;  
* Otras decisiones de personal, como transferencias, etc.

Los objetivos fundamentales de la evaluación de desempeño son:

* Permitir condiciones de medición del potencial humano   
* Convertir el tratamiento de los recursos humanos como un recurso básico de la empresa, como una importante ventaja competitiva, y cuya productividad puede desarrollarse indefinidamente  
* Dar oportunidades de crecimiento y condiciones de efectiva participación a todos los miembros de la organización, teniendo en cuenta los objetivos empresariales y los individuales.

#### ***Beneficios de la evaluación del desempeño*** {#beneficios-de-la-evaluación-del-desempeño}

Por lo general, los principales beneficiarios son el individuo, el jefe, la empresa, y la comunidad.

**1\. Beneficios para el jefe** 

* Evaluar mejor el desempeño y el comportamiento de los subordinados, contando con un sistema de medición capaz de neutralizar la subjetividad  
* Proponer medidas orientadas a mejorar el patrón de comportamiento de sus subordinados   
* Comunicarse con sus subordinados para que comprendan la mecánica de evaluación, y mediante este sistema la manera como está desarrollándose su comportamiento 

**2\. Beneficios para el subordinado** 

* Conoce los aspectos de comportamiento y de desempeño que la empresa valora más en sus funcionarios   
* Conoce cuales son las expectativas de su jefe acerca de su desempeño, y sus fortalezas y debilidades, según la evaluación del jefe   
* Sabe qué medidas está tomando su jefe con el fin de mejorar su desempeño, y las que el propio subordinado deberá tomar por su cuenta   
* Adquiere condiciones para hacer autoevaluación y autocrítica para su desarrollo y su autocontrol. 

**3\. Beneficios para la empresa** 

* Está en condiciones de evaluar su potencial humano a corto, mediano y largo plazo y definir la contribución de cada empleado   
* Puede identificar los empleados que necesitan reciclaje y/o perfeccionamiento, y seleccionar los que tienen condiciones de transferencia o promoción   
* Puede estimular la productividad y mejorar las relaciones humanas en el trabajo 

![][image68]

#### ***Métodos tradicionales de evaluación del desempeño*** {#métodos-tradicionales-de-evaluación-del-desempeño}

La evaluación de desempeño es un medio, un método, una herramienta, y no un fin en sí misma. Es un medio para obtener datos e información que puedan registrarse, procesarse y canalizarse para mejorar el desempeño humano en las organizaciones. Los principales métodos tradicionales de evaluación del desempeño son:

* Método de las escalas gráficas  
* Método de elección forzada  
* Método de investigación de campo  
* Método de los incidentes críticos  
* Métodos mixtos

##### **Método de las escalas gráficas**

Es el método de evaluación del desempeño más utilizado y divulgado. En apariencia, es el método más sencillo, pero su aplicación exige múltiples cuidados, con el fin de evitar la subjetividad y los prejuicios del evaluador.

Reduce los resultados a expresiones numéricas mediante la aplicación de procedimientos matemáticos y estadísticos para corregir las distorsiones personales introducidas por los evaluadores.

Este método evalúa el desempeño de las personas mediante factores de evaluación previamente definidos y graduados. Utiliza un formulario de doble entrada, en donde las filas (horizontales) representan los factores de evaluación del desempeño, en tanto que las columnas (verticales) representan los grados de variación de tales factores, seleccionados previamente para definir en cada empleado las cualidades que se intenta evaluar.

Entre los extremos de evaluación existen tres alternativas:

* **Escalas gráficas continuas***.* Escalas donde solo están definidos los extremos; la evaluación del desempeño puede situarse en cualquier punto de la línea que los une.  
* **Escalas gráficas semi-continuas***.* Idénticas a las escalas continuas, excepto que se incluyen puntos intermedios definidos entre los extremos (límite mínimo y límite máximo) para facilitar la evaluación.  
* **Escalas gráficas discontinuas***.* En estas, la posición de las marcaciones ya está fijada y descrita con anterioridad; el evaluador solo debe seleccionar una de ellas para evaluar el desempeño del empleado.

Algunas empresas utilizan el método de escala gráfica con atribuciones de puntos, con el fin de cuantificar los resultados para facilitar las comparaciones entre los empleados. Los factores se ponderan y ganan puntos con relación a su importancia en la evaluación.

##### **Método de elección forzada** 

El objetivo de crear este sistema de evaluación era obtener uno que neutralizara el efecto de halo, el subjetivismo y el proteccionismo propios del método de escala gráfica, y que permitiese obtener resultados de evaluación más objetivos y válidos.

Consiste en evaluar el desempeño de los individuos mediante frases descriptivas de alternativas de tipos de desempeño individual. En cada bloque o conjunto compuesto de dos, cuatro o más frases, el evaluador debe elegir por fuerza solo una o dos, las que más se apliquen al desempeño del empleado evaluado. De ahí la denominación "elección forzada".

La naturaleza de las frases varía bastante; no obstante, hay dos formas de componerlas:

* Se forman bloques de dos frases de significado positivo y dos de significado negativo: AI juzgar al empleado, el supervisor o evaluador elige la frase que más se ajusta y, luego, la que menos se ajusta al desempeño del evaluado.  
* Se forman bloques de sólo cuatro frases de significado positivo. AI juzgar al empleado, el supervisor o evaluador elige las frases que más se ajustan al desempeño del evaluado.

##### **Método de investigación de campo** 

Está desarrollado con base en entrevistas de un especialista en evaluación con un supervisor inmediato, mediante el cual se evalúa el desempeño de sus subordinados, determinando las causas, los orígenes y los motivos de tal desempeño, por medio del análisis de hechos y de situaciones. Es un método de evaluación más amplio ya que permite además de un diagnóstico del desempeño del empleado, la posibilidad de planear junto con el supervisor inmediato su desarrollo en el cargo y en la organización. También permite acompañar el desempeño del empleado de manera mucho más dinámica que otros métodos.

La evaluación de desempeño la efectúa el supervisor (jefe), pero con asesoría de un especialista (staff) en evaluación del desempeño. El especialista va a cada una de las secciones para entrevistar a los jefes sobre el desempeño de sus respectivos subordinados.

##### **Método de incidentes críticos**

Se basa en el hecho de que en el comportamiento humano existen ciertas características extremas capaces de conducir a resultados positivos (éxito) o negativos (fracaso). En consecuencia, el método no se preocupa por las características normales, sino exactamente por aquellas características muy positivas o muy negativas.

El supervisor inmediato observa y registra los hechos excepcionalmente positivos y los excepcionalmente negativos con respecto al desempeño de sus subordinados.

Las excepciones positivas deben realizarse y ponerse más en práctica, en tanto que las negativas deben corregirse y eliminarse.

##### **Método de comparación por pares**

Compara a los empleados en turnos de a dos, y se anota en la columna de la derecha aquel que se considera mejor en cuanto al desempeño. En este método también pueden utilizarse factores de evaluación. De este modo, cada hoja del formulario está ocupada por un factor de evaluación de desempeño. Resulta una clasificación final con relación al factor de desempeño.

Solo se recomienda cuando los evaluadores no estén en condiciones de utilizar otros métodos de evaluación más precisos, porque es un proceso muy sencillo y poco eficiente.

##### **Método de frases descriptivas**

Este método es ligeramente diferente del método de elección forzada porque no es obligatoria la elección de frases. El evaluador señala las frases que caracterizan el desempeño del subordinado (signo " \+ " o "S") y aquellas que demuestran el opuesto de su desempeño (signo " \- " o "N").

#### ***Nuevas tendencias en las evaluaciones de desempeño*** {#nuevas-tendencias-en-las-evaluaciones-de-desempeño}

La entrevista de evaluación de desempeño

De nada sirve la evaluación si el mayor interesado \-el propio empleado- no llega a conocer el resultado de su evaluación.

Los propósitos de la entrevista de evaluación del desempeño son:

* Dar al subordinado las condiciones necesarias para mejorar su trabajo.  
* Dar al subordinado una idea clara acerca de cómo está desempeñando su trabajo (retroalimentación), destacando sus fortalezas y sus debilidades y comparándolas con los estándares de desempeño esperados.  
* Discutir los dos \-empleado y gerente- las medidas y los planes, para desarrollar y utilizar mejor las aptitudes del subordinado  
* Estimular relaciones personales más fuertes entre el gerente y los subordinados.  
* Eliminar o reducir discrepancias, ansiedades, tensiones e incertidumbres que surgen cuando los individuos no gozan de asesoría planeada y bien orientada.

#### ***Gestión por competencias*** {#gestión-por-competencias}

**Competencia** es la característica de una persona, ya sea innata o adquirida, que está relacionada con una actuación de éxito en un puesto de trabajo. 

Los elementos que determinarían la capacidad de un individuo para el trabajo, son tres:

* Complejidad de los procesos mentales (carácter)  
* Los valores  
* Los intereses de la persona o el comportamiento con el trabajo, y los conocimientos y habilidades para ese trabajo.

Los valores, habilidades y conocimientos reunidos para el desarrollo de una tarea en particular, influyen sobre el grado de aprovechamiento del potencial de los procesos mentales de una persona.

Las competencias son una lista de comportamientos que ciertas personas poseen más que otras, y que las transforman en más eficaces para una situación dada.

***Competencias técnicas o de conocimientos***  
Son las más fáciles de detectar o evaluar, son la base para seguir adelante. Así, un proceso de selección empieza con una evaluación de conocimientos requeridos. Esta evaluación es excluyente, y los candidatos que aprueben serán luego evaluados en sus características más profundas.

***Competencias de gestión o derivadas de las conductas***  
*Ejemplos*: Iniciativa, autonomía, relaciones públicas, comunicación, trabajo en equipo, liderazgo, capacidad de síntesis, etc. 

Cinco tipos de competencias:

1. **Motivación:** Las motivaciones dirigen, conllevan y seleccionan el comportamiento hacia ciertas actitudes u objetivos, y los alejan de otros.   
2. **Características:** Características físicas y respuestas consistentes a situaciones o información. Ejemplos: Iniciativa, autocontrol, tiempo de reacción, respuesta al stress, resolución de problemas.  
3. **Concepto propio o concepto de uno mismo:** Las actitudes, valores o imagen propia de una persona  
4. **Conocimiento**: La información que una persona posea sobre áreas específicas. Es importante cómo se evalúa.  
5. **Habilidad:** La capacidad de desempeñar cierta tarea física o mental.

***Modelo de iceberg***   
El gráfico (modelo) muestra 2 grandes grupos:

* **Las más fáciles de detectar** y desarrollar: Destrezas y conocimientos (competencias superficiales)  
* **Las menos fáciles de detectar** y desarrollar: Concepto de uno mismo, actitudes, valores, personalidad, motivación (competencias centrales)

Por lo cual, puede ser más económico para las empresas contratar seleccionando según competencias centrales, y luego enseñar el conocimiento y habilidades

##### **Evolución y grados de las Competencias** 

La definición de las competencias deberá hacerlo la misma organización, y estará a cargo de la “línea”. Luego se aplican a las diferentes funciones y procesos de recursos humanos.

***¿Cómo evolucionan las competencias según los niveles jerárquicos?***  
A medida que se sube o se desciende en la escala jerárquica, las competencias pueden cambiar, o cambiar su peso específico para la posición.

##### **Implementación de un Sistema de gestión por Competencias** 

Para trabajar con un esquema por competencias es necesario “empezar por el principio”: Definir la visión de la empresa (hacia dónde vamos), los objetivos, y la misión (qué hacemos). Para luego decidir cómo lo hacemos.

Los pasos necesarios para implementar un sistema de gestión por competencias:

* Definir visión y misión  
* Definición de competencias por la máxima dirección  
* Prueba de las competencias en un grupo de ejecutivos de la organización  
* Validación de las competencias  
* Diseño de los procesos de recursos humanos por competencias  
* Criterios efectivos para definir competencias:  
* Definir criterios de desempeño  
* Identificar una muestra  
* Recoger información  
* Identificar tareas y los requerimientos en materia de competencias de cada una de ellas; esto implica la definición final de las competencias y su correspondiente apertura en grados  
* Validar el modelo de competencias  
* Aplicar el modelo a los subsistemas de recursos humanos: selección, entrenamiento y capacitación, desarrollo, evaluación de desempeño, planes de sucesión, remuneraciones.

***Definición de los niveles de competencia***  
Puede haber varios niveles (3, 4, …) para el cumplimiento de la competencia.

* **A:** Alto o desempeño superior. Aprox. unas de cada diez personas alcanzan este nivel  
* **B:** Bueno  
* **C:** Mínimo necesario para el puesto, pero dentro del perfil requerido  
* **D:** Insatisfactorio. Por lo tanto, este nivel no se aplica a la descripción del perfil, ya que, si no es necesaria esa competencia para el puesto, no será necesario indicar nivel.