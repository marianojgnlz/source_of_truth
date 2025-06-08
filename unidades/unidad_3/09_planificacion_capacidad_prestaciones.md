# Planificación de la capacidad (de las prestaciones)

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

## Capacidad adecuada

¿Qué significa aceptable? → debe definirlo cada organización.

La capacidad adecuada es función de tres elementos:

* **Los acuerdos de nivel de servicio** *(Service Level Agreements,* SLA, ANS): Son umbrales de productividad, rendimiento y de disponibilidad exigidos y pactados entre los grupos de usuarios y la organización de soporte de los sistemas informáticos de la instalación.

Aquí se debe introducir el término **calidad de servicio** *(Quality of Service,* QoS). Una forma de cuantificar la calidad de servicio es calcular el ratio de la deficiencia de la calidad de servicio ante un nivel deseado de la misma, tal como se indica en la siguiente ecuación:

Desviación QoS=QoS conseguida-QoS deseadaQoS deseada

* **La arquitectura del sistema**: la capacidad adecuada para alcanzar un nivel de servicio acordado se puede conseguir utilizando dispositivos y subsistemas de distintos tipos. La arquitectura seleccionada puede depender de las exigencias del aplicativo que se ejecuta en el sistema, del grado de experiencia y madurez en la explotación del sistema, de la facilidad de administración o de otros motivos, que no tienen por qué estar directamente relacionados con el rendimiento.

* **Presupuesto**: Todas las organizaciones tienen presupuestos que restringen la capacidad de la que se puede disponer. Se debe evaluar el coste total de la propiedad, que es la suma del costo de implementación (compra de HW, sw, formación inicial del personal) y el costo de operación (mantenimiento de HW y sw, de personal, consumo eléctrico, etc.).

Se podría decir que un sistema informático tiene una capacidad adecuada si los niveles de servicio se cumplen continuamente para una tecnología y estándares especificados, y si los servicios se suministran dentro de los límites de coste acordados.

## Niveles de gestión y planificación

* **Nivel 0** No hay un programa de gestión de la capacidad. La gestión de la capacidad se realiza ocasionalmente.
* **Nivel** 1 Se realizan medidas de tendencia y predicción de la utilización en periodos de pico. Se planifica la capacidad de los recursos con unas revisiones periódicas.
* **Nivel** 2 Se conoce exactamente las utilizaciones de cada uno de los recursos debidas a las cargas de trabajo significativas.
* **Nivel 3** Existe un sistema automático de análisis y predicción de la carga de trabajo.
* **Nivel** 4 Se predicen automáticamente los niveles de servicio a partir de las predicciones de capacidad.
* **Nivel** 5 Se utilizan los criterios de las aplicaciones de negocio a través de un modelo que sirve para predecir los niveles de servicio.

## Métodos de predicción

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

## Técnicas cuantitativas para la predicción de la carga

* ***Regresión lineal***. Los modelos de regresión se utilizan para estimar el valor de una variable como una función de otras variables. La variable que hay que predecir se llama variable dependiente y las variables utilizadas para predecir su valor se llaman variables independientes.

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

Donde ft+1 es el valor esperado del periodo t+1, yt+1 es el valor observado en el instante t+1, ft es el valor estimado en el instante t y  es el peso que se le otorga al valor observado más reciente (0 <α <1).

En la aproximación de Tustin, se puede tomar más de un valor estimado anterior (si se quiere dar mayor relevancia a lo estimado), o bien se puede tomar más de un valor observado (si se pretende dar mayor relevancia a varias observaciones consecutivas).

## Unidades de predicción natural

Una unidad de predicción natural *(Natural Forecast Unit.* NFU) es una variable de negocio cuyo valor está directamente relacionado con los recursos consumidos por una o varias aplicaciones.

Los componentes esenciales de la caracterización de la carga utilizando las unidades de predicción natural para los propósitos de estimación del rendimiento son los siguientes:

* Medidas del trabajo solicitado al sistema utilizando variables de negocio como métrica, que son propiamente las unidades de predicción natural.
* Las relaciones que muestren el número de transacciones generadas para el periodo caracterizado para cada unidad de predicción natural.
* Las relaciones que indiquen los recursos del sistema que consume cada transacción.

## Capacidad bajo demanda

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