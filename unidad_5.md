# **Unidad 5: Subsistema de Seguimiento** {#unidad-5:-subsistema-de-seguimiento}

El **subsistema de seguimiento** es el subsistema conformado por los procesos, métodos y herramientas que permiten evaluar el grado de adecuación del desempeño/rendimiento de los recursos humanos y de SW y HW a las metas de funcionamiento establecidas y determinar las acciones de mejora adecuadas.

**Seguimiento de los Recursos de HW Y SW**  Evaluación de las prestaciones

**Seguimiento de los RRHH** → Evaluación de desempeño y  Auditoría de la función de RRHH

E**s más complejo analizar el rendimiento de las personas** que de los recursos de SI/TI, por cuestiones relacionadas con la motivación, la resistencia al cambio, etc.

![][image18]

## **Seguimiento de SI/TI** {#seguimiento-de-si/ti}

El subsistema que nutre el subsistema de seguimiento es el subsistema de aplicación de RR SI/TI, a través de la carga de trabajo, la [caracterización de la carga](#caracterización-de-la-carga), y la [planificación de las prestaciones](#planificación-de-la-capacidad-\(de-las-prestaciones\)) (modelo de explotación).

El **Rendimiento** de un SI es la medida de cómo un SW determinado utiliza el HW con la carga del sistema.

**Evaluar el rendimiento** de un sistema es medir el comportamiento del sistema ante la carga de trabajo de acuerdo con una serie de requisitos de ejecución, para luego determinar el grado de prestaciones (satisfacción de las necesidades de servicio del usuario) que está brindado, y así establecer si este **rendimiento es aceptable**.

El **Subsistema de seguimiento de SI/TI** es el subsistema conformado por los procesos, métodos y herramientas que permiten evaluar el grado de adecuación del rendimiento de los recursos de SW y HW a las metas de funcionamiento establecidas y determinar las acciones de mejora adecuadas.

Puigjanier centra su análisis en el **HW y el SO** (o software de base). Estos dos componentes conforman un sistema informático.

Razones para efectuar la evaluación de las prestaciones:

* Diseñar una máquina  
* Diseñar un sistema informático (arquitectura que tiene que dar soporte a la cartera de aplicaciones)  
* Seleccionar y configurar un sistema informático  
* Planificar la capacidad de un sistema informático (Relacionado con la unidad de aplicación, desde aquí es donde se sacan los datos)  
* Sintonizar un sistema informático: ajustar los parámetros del SO para que esas prestaciones se adecuen a las prestaciones necesarias de servicio, normalmente para mejorar el comportamiento del sistema. En algunos casos si el sistema no se puede variar, hay que intentar mejorar el comportamiento del sistema modificando la carga → ajustar los parámetros del SO para que esas prestaciones se adecuen a las prestaciones necesarias de servicio. Busco como afino el cuello de botella para volver al rendimiento aceptable. En caso de no poder, se buscará la adquisición.

### Relación entre rendimientos

Consideremos dos computadores X e Y**,** los cuales tardan Tx y Ty unidades de tiempo, respectivamente, en ejecutar un programa. Si Tx=Ty diremos que el rendimiento de ambas máquinas es igual o equivalente, ya que en ambas obtenemos el mismo tiempo de ejecución. 

Por el contrario, si Tx \< Ty, el computador X tarda menos tiempo en ejecutar el programa. Esta relación nos permite afirmar que "X es más rápido que Y**".** Sin embargo, nuestro objetivo es cuantificar esta relación y decir que "X es *tantas veces más* rápido que Y**".** El valor numérico al que nos estamos refiriendo recibe el nombre de aceleración *(speedup) y* se puede calcular como la relación entre el tiempo de ejecución más grande y el más pequeño:

Aceleracion=TyTx

Por lo tanto, la aceleración representa el incremento de rendimiento de una máquina respecto de la otra.

Finalmente, hay ocasiones en que esta aceleración se expresa en términos porcentuales, esto es, "X es un n% más rápido que Y**"**, en cuyo caso la relación anterior se expresa:

Aceleracion=TyTx=1+n100

### Relación de costes

Si los costes de los computadores X e Y son Cx y  Cy***,*** respectivamente, el incremento (o también aceleración) del coste de una opción respecto de la otra se puede expresar dividiendo el coste más elevado entre el más bajo. Entonces podemos escribir

Incremento=CxCy=1+n100

En consecuencia, esta expresión nos permitirá decir que "X es tantas veces más caro que Y", o que "X es un n% más caro que Y".

### Relación entre prestaciones y coste

Las expresiones empleadas hasta ahora nos han permitido cuantificar, de manera aislada, la relación entre sus prestaciones y la relación entre sus costes. Para realizar un análisis conjunto de precio y prestaciones no queda más remedio que establecer algún tipo de conexión entre ambas. 

Por ejemplo, se puede dividir el rendimiento de cada computador entre su coste y comparar ambas cantidades:  
RendimientoXCosteX vs RendimientoYCosteY

Las cantidades anteriores nos pueden ayudar a conocer qué opción de las dos, en su conjunto, ofrece una mejor relación entre el rendimiento obtenido y el precio que se va a pagar por él.

Otro posible contexto, diferente al anterior, viene dado cuando se trata de analizar el efecto de una determinada **mejora** en un sistema informático. El valor de este incremento se puede calcular dividiendo el coste del equipo con el componente añadido entre el coste del computador original:

∆C=Nuevo CosteCoste Original

Sin embargo, cuando se trata de comparar entre sí diversas alternativas para la actualización de un sistema (con o sin reemplazo de componentes), se tiene el problema de que el incremento del coste del sistema global puede estar muy influenciado por el coste original (principalmente para aquellos componentes con mucha influencia en el rendimiento, pero con poca repercusión en el coste de todo el sistema). Si se quiere actualizar un sistema y se posee más de una alternativa, con una influencia muy baja en el coste global del sistema, entonces se analiza la mejora del rendimiento de cada alternativa, y los costes de cada una, C1 y C2 por ejemplo, sin tener en cuenta el coste global del sistema.  

### La ley de Amdahl

Esta ley acota, de una manera muy sencilla, el incremento de prestaciones obtenido en un sistema como consecuencia de la mejora de una o varias partes del mismo.

Consideremos, para simplificar nuestro planteamiento, un computador que tarda un tiempo Toriginal en ejecutar una determinada aplicación, y que nuestro objetivo es reducir este tiempo de ejecución mejorando una de las partes del computador. Supongamos que durante una fracción *f* del tiempo original el programa hace uso exclusivo de un recurso del sistema (por ejemplo, el procesador). En consecuencia, podemos expresar Toriginal como la suma de dos componentes disjuntos: uno en el que no se utiliza este componente más otro en el que sí se utiliza:

Toriginal=Toriginal1-f+Toriginal∙f

![][image122]

El nuevo tiempo de ejecución Tmejorado que se obtendrá después de mejorar k veces el recurso afectado puede calcularse teniendo en cuenta que el segundo sumando de la expresión anterior se reducirá en un factor de k***:***  
Tmejorado=Toriginal×(1-f)+Toriginal∙fk

Donde se puede notar que el incremento de prestaciones conseguido con la mejora del recurso depende de la fracción de tiempo en que se emplea. Si dividimos ahora el tiempo original entre el tiempo mejorado obtendremos la cuantificación de la mejora de prestaciones global A obtenida (aceleración).   
A=11-f+fk

La expresión anterior recibe el nombre de ley de Amdahl (que se utiliza para justificar el upgrading del sistema) donde *f* es la proporción en la que el componente está siendo utilizado por la carga y k es el factor de mejora que se introduce mejorando esa carga. De aquí se pueden tomar ciertas conclusiones:

* Si f=0, entonces A=1. Es decir, cuando la fracción de tiempo en la que se utiliza el componente es nula, no existe aceleración.  
* Si f=1, entonces A=k. Es decir, la aceleración obtenida en el sistema global será equivalente al factor de mejora del componente si éste se utiliza durante todo el tiempo.   
* Cuando k→∞, es decir que el factor de mejora se hace muy grande, se tiene: 

A \=11-f+fk \=11-f

Que deja en claro que, independientemente de la mejora llevada a cabo en un sistema, el incremento de prestaciones global está limitado intrínsecamente por las operaciones que no están afectadas por esta mejora. 

En la obtención de A podemos despejar el Tmejorado, obteniendo

Tmejorado=ToriginalA

La aceleración A esta en veces, por lo que es más cómodo calcular en tiempo (Tmejorado)

También es posible, conocidas k y A, calcular la fracción de tiempo f. La expresión que relaciona estas variables, obtenida de la anterior, es la siguiente:

f=k×(A-1)A×(k-1)

La ley de Amdahl puede generalizarse fácilmente al caso en que se lleven a cabo mejoras sobre más de un recurso. En efecto, si se mejoran n recursos del sistema en factores k1, k2, …, kn, y cada uno de ellos se utiliza de manera exclusiva durante las fracciones de tiempo f1, f2, …, fn, respectivamente, la mejora global o aceleración obtenida se puede expresar:   
A=1f0+i=1nfiki	Con 	f0=1-i=1nfi

Las ecuaciones anteriores muestran de manera directa que una mejora es más efectiva cuanto mayor es la fracción de tiempo en que se aplica. 

### REPASO de carga

Una [carga está completamente caracterizada](#caracterización-de-la-carga) sí y sólo sí su resultado es un conjunto de parámetros cuantitativos seleccionados de acuerdo con los objetivos de operación de caracterización.

**Cualidades:** reproductibilidad, compacidad, compatibilidad, representatividad, flexibilidad, independencia del sistema

Se caracteriza la carga para obtener un modelo que represente la carga real y de allí poder hacerle pruebas.

* **Carga de prueba o test**: Carga que se puede utilizar cuando se está realizando un experimento de medición dado.  
* **Sesión de medida:** Intervalo de tiempo durante el que se observa el experimento (segundos, minutos, horas, etc.)

**En función del modelo que se tenga se deberá caracterizar la carga puede ser:**

* **Físico:** se basa en los consumos absolutos o unitarios de los recursos de hw y sw. (tiempo de CPU, tiempo total de E/S consumido, espacio en memoria p-s). Depende fuertemente del sistema empleado. Los parámetros usados están recopilados en logging o accounting del S.O.  
* **Virtual**: Se basa en el uso de recursos del sistema a nivel lógico (número de sentencias de cada tipo de lenguaje de alto nivel, acceso lógico a BD) Programador. Son parámetros difíciles de obtener.  
* **Funcional**: En el modelo de carga deben aparecer las aplicaciones (programas) que efectúen las mismas funciones que en la carga original con las mismas proporciones.  
* **Comportamiento**: tiempo medio de respuesta, productividad

### 

**Técnicas de implementación de los modelos de carga**

Las operaciones para implantar modelos de la carga p**ueden agruparse en tres fases:**

* **Formulación o especificación →** Secuencia de decisiones que se pretenden tomar, influenciadas por los objetivos de estudio. La definición de los componentes básicos de la carga, es decir, la identificación del menor nivel de detalle que debe modelarse y del conjunto de parámetros que debe usarse. El componente básico de la carga es la menor unidad de trabajo que se considerará (cuánto más alto es el nivel de componente básico, menor es el detalle que describe la carga), y por consiguiente, influirá en la selección de los parámetros que deben utilizarse para la descripción cuantitativa. 

Otro factor que influye en la selección de parámetros es su disponibilidad. Así pues, los parámetros que debe utilizarse para caracterizar la carga se seleccionan basándose:

* Nivel de detalle del modelo, después de estudiar sus objetivos.  
  * Verificar la disponibilidad.

* **Construcción**  
  * Análisis de parámetros: Se comienza realizando la operación de medida sobre el sistema y da como resultado un conjunto de datos considerablemente grande, por eso se agrupa en conjuntos de componentes que tienen características similares.  
  * Extracción de valores representativos: se utilizan técnicas estadísticas. Cuyo resultado es la determinación de las características de las clases componentes del modelo.  
  * Asignación de valores a los componentes del modelo: Trata de la transformación de los valores representativos en componentes ejecutables. El número de componentes que constituirán el modelo influye directamente en su representatividad e indirectamente en su capacidad.  
  * Reconstrucción de mezclas de componentes significativos: El objetivo consiste en reproducir en el modelo situaciones similares a las que se producirían en el modelo real.

* **Validación →** La evaluación del criterio de representatividad del modelo, basado en los objetivos del estudio definidos en la fase de formulación, debe efectuarse en la fase de validación para establecer la validez del modelo implementado. En esta fase no sólo se evaluará la representatividad del modelo con el conjunto de parámetros determinado que se considera, sino que se deberán realizar experimentos para determinar el dominio de validez del modelo. La validación del modelo deberá efectuarse comparando su comportamiento con el de la carga real en aquellos puntos en que se conozca por haberse efectuado algún tipo de medición.

### Teoria de colas

**Una estación de servicio está compuesta por un servidor y una cola de espera**. El servidor representa al recurso físico del computador, mientras que la cola de espera modela la cola de trabajos que aguardan a utilizar el recurso físico. **Los parámetros temporales más importantes** de una estación de servicio desde el punto de vista del rendimiento son dos: 

* El **tiempo de servicio** es el tiempo que transcurre desde que un trabajo empieza a utilizar el recurso hasta que lo deja libre.  
* El **tiempo de respuesta** es el tiempo de servicio más el tiempo que el trabajo pasa aguardando en la cola de espera.

Cuando se puede atender a más de un trabajo en paralelo, las estaciones de servicio incluyen más de un servidor. Se pueden describir tres tipos de estaciones de servicio:  
![][image123]  
Formalmente podemos definir una red de colas como un grafo dirigido cuyos nodos son las estaciones de servicio. Los arcos entre estos nodos indican las transiciones posibles entre las estaciones. 

Las redes también pueden ser clasificadas según la topología del grafo subyacente.

* **Las redes abiertas** se caracterizan por la existencia de, al menos, una fuente de trabajos y uno o más sumideros que absorben los trabajos que salen del sistema y, así mismo, la posibilidad de encontrar al menos un camino que, a partir de cada nodo, lleve a un sumidero. **Las redes abiertas se emplean para modelar el comportamiento de sistemas que soportan cargas transaccionales**. La productividad de una red abierta es igual a la tasa de entrada al sistema. Los índices son el tiempo de respuesta y el número de trabajos dentro del sistema. En la Figura 4.2 se muestra una red de colas abierta que comprende tres estaciones de servicio, la fuente de trabajos y el sumidero de la red.

![][image124]

* **Las redes cerradas** son redes en las cuales los trabajos ni entran ni salen y, por tanto, su número permanece constante. El flujo de trabajos a través del enlace entre la salida y la entrada define la productividad de la red. En estas redes resulta de gran interés conocer el tiempo de respuesta y la productividad. **Los sistemas con carga de tipo interactivo y con carga por lotes (batch) se modelan mediante redes cerradas.** La Figura 4.3 muestra un ejemplo en donde la estación con infinitos servidores se suele utilizar para representar el tiempo transcurrido entre la finalización de una petición al sistema y el comienzo de una nueva. En caso de que la carga fuera por lotes la estación con infinitos servidores desaparecería del modelo y se uniría la salida con la entrada de esta estación.

![][image125]

⇒ Una estación de servicio puede tener más de un servidor y más de una cola.

Sistema real                                                                 	Modelo

Recurso del sistema (HW)		 →	 servidor

Trabajos (SW) asociados al recurso 	→	 cola

**El análisis intenta deducir los simples índices de prestaciones a partir de parámetros cuantificables del sistema y las relaciones entre esos parámetros.** Las relaciones entre ellos se establecen a través de las Leyes Operacionales / verificables mediante mediciones

### Análisis operacional (Técnicas analíticas)

El análisis operacional forma parte de una serie de técnicas, denominadas analíticas, empleadas en la estimación del rendimiento de los sistemas informáticos. Estas técnicas hacen uso de un modelo de comportamiento del computador y su carga, y calculan los índices de prestaciones a partir de este modelo.

Es la modelización de un sistema mediante un conjunto de variables y ecuaciones, cuya resolución permite obtener índices de prestaciones a partir de un modelo de colas.

En este contexto, la palabra ***operacional*** equivale a ''directamente medible". Así una hipótesis operacionalmente comprobable es una hipótesis que puede ser verificada por medidas.

#### ***Leyes Operacionales***

##### **Variables operacionales básicas**

Las variables operacionales son cantidades directamente medibles durante un periodo de observación finito. 

Sobre un dispositivo cualquiera i de un sistema informático definimos:

* T: periodo de observación  
* Ai: número de arribos durante T  
* Ci: número de trabajos completados durante T  
* Bi: tiempo en el que el dispositivo i está ocupado.

De estas magnitudes operacionales podemos derivar las siguientes:

| Nombre | Ecuación | Unidad | Detalle |
| :---: | :---: | :---: | ----- |
| **Tasa de llegada** | i=Ai/T  | Trabajos por unidad de tiempo | Indica cuántos trabajos llegan por unidad de tiempo. |
| **Tasa de Productividad** | Xi=Ci/T  | Trabajos por unidad de tiempo | Productividad se refiere a la cantidad de trabajos completados por unidad de tiempo. |
| **Factor de utilización** | Ui=Bi/T | Adimensional | Es el tiempo en el que el dispositivo fue usado sobre el tiempo total.  |
| **Tiempo de servicio** | Si=Bi/Ci | Unidades de tiempo por trabajo | Refiere a cuánto tiempo presta ese dispositivo a los trabajos (cuanto tiempo lo usó) |
| **Tiempo entre llegadas** | 1/i=T/Ai | Tiempo | Refiere al intervalo de tiempo que llegan los trabajos. |
| **Tasa de servicio** | µi= Ci/Bi=1/Si | Adimensional | Trabajos completados sobre su utilización  (tiempo de uso del dispositivo) |

Las variables operacionales pueden cambiar de valor de un periodo de observación a otro. Sin embargo, hay relaciones que se mantienen para cualquier periodo de observación.

Estas relaciones se denominan leyes operacionales, y no dependen de hipótesis sobre la distribución estadística que siga los tiempos de servicio y los tiempos entre llegadas. 

Como punto de partida supondremos que durante el periodo de observación T el sistema se encuentra operando en un estado estable o de equilibrio, lo que recibe el nombre de **hipótesis del flujo equilibrado de trabajos**. En este estado se cumple que el número de trabajos que entra es igual al número de trabajos que sale. Esto se obtiene tomando un tiempo T lo suficientemente grande. 

Nótese que Ai \= Ci implica λ=Xi***.*** Esta hipótesis operacional, comprobable por medida, nos será muy útil de ahora en adelante.

*NOTA: las leyes no hace falta saberlas de memoria.*

##### **Ley de la utilización**

La utilización de un dispositivo se puede expresar en función del número de terminaciones mediante la siguiente fórmula:

Ui=BiT=CiTBiCi=XiSi

Si además se cumple la hipótesis del flujo equilibrado de trabajos obtendremos una expresión equivalente a la anterior en función de la tasa de llegada

Ui=iSi

##### **Ley del flujo forzado**

Esta ley es de gran importancia y relaciona la productividad del sistema X0 con la productividad de un dispositivo individual Xi***.*** En un **modelo abierto** (existencia, de, al menos, una fuente de trabajos y uno o más sumideros y, así mismo, la posibilidad de encontrar al menos un camino que a partir de cada nodo lleve a un sumidero. Sistemas transaccionales) la productividad está definida por el número de trabajos que abandona el sistema por unidad de tiempo. En cambio, en un **modelo cerrado** (los trabajos ni entran ni salen y, por tanto, su número permanece constante. Sistemas batch), ningún trabajo abandona el sistema. Aun así, los trabajos que atraviesan el enlace que une la salida con la entrada se comportan como si abandonaran el sistema e inmediatamente re-entraran en él. La productividad del sistema en este último caso viene dada por el número de trabajos que atraviesan este enlace por unidad de tiempo.

Supongamos que cada trabajo realiza Vi peticiones o visitas al dispositivo i***.*** Si el flujo de trabajos está equilibrado, el número de trabajos que sale del sistema C0 (O atraviesa el enlace exterior) y el número de trabajos que atraviesa el dispositivo i están relacionados por la expresión:

Ci=C0Vi	Y, por tanto,	Vi=Ci/C0

La variable Vi recibe el nombre de razón de visitas al dispositivo i***.*** La productividad total del sistema X0 durante el periodo de observación es:  
X0=C0T

Mientras que la productividad del dispositivo i es:

Xi=CiT=CiC0C0T

En consecuencia, podemos obtener una expresión de Xi, en función de las variables Vi y X0:  
Xi=X0Vi

Que représente la expresión de la ley del flujo forzado. Esta ley establece que el flujo a través de un determinado dispositivo de la red determina el flujo en cualquier otro dispositivo. La ley del flujo forzado es válida si lo es la hipótesis del flujo equilibrado de trabajos.

Combinando los resultados de la ley del flujo forzado y de la ley de la utilización podemos obtener la siguiente expresión para el valor de la utilización del dispositivo:

Ui=XiSi=X0ViSi=X0Di

Donde Di \= ViSi recibe el nombre de **demanda de servicio** sobre el dispositivo i en todas las visitas que un trabajo realiza al mismo. La relación anterior establece que la utilización de cada dispositivo del sistema es proporcional a su demanda de servicio.

Otra descripción equivalente se puede realizar mediante la proporción de trabajos, también denominada probabilidad de encaminamiento o de transición. Así las probabilidades de encaminamiento, pij***,*** indican la proporción de trabajos que cuando salen de la estación i se dirigen a la estación j***,*** o de forma equivalente, indican la probabilidad de que un trabajo pase a la estación j después de terminar su servicio en la estación i***.*** En este sentido se tendrá que pij \= Cij/Ci y en particular, p0j \= A0j/A0 y pi0 \= Ci0/C0***.***

Razones de visita y probabilidades de encaminamiento son equivalentes en el sentido de que a partir de una se obtienen las otras. En un sistema con K estaciones de servicio en que se cumple la hipótesis del flujo equilibrado de trabajos se tiene:  
Cj=i=0KCipij

Donde el subíndice 0 representa el exterior del sistema y pi0 es la proporción de trabajos que, después de recibir servicio en la estación i*,* abandonen la red. Dividiendo ambos lados de la igualdad por C0 obtenemos:  
Vj=i=0KVipij

Que representan las denominadas ecuaciones de las razones de visita. Como cada visita al mundo exterior corresponde a una terminación de un trabajo, tendremos que siempre se cumplirá V0=1.

##### **Ley de Little**

La única hipótesis requerida para su aplicación es la del flujo equilibrado de trabajos. Si llamamos Ni al número de trabajos y Ri al tiempo de respuesta de la estación de servicio i*,* la ley de Little establece que:  
Ni=iRi

Y como hemos exigido que se cumpla la hipótesis del flujo equilibrado de trabajos podemos sustituir i por Xi.  
Ni=XiRi

**La ley de Little se puede utilizar en sistemas interactivos**. 

##### **Ley general del tiempo de respuesta** 

El número de trabajos en una red de colas formada por K estaciones se puede expresar como N \= N1 \+ N2 \+ … \+ NK**.** Si sustituimos los valores de Ni, de acuerdo con la ley de Little tendremos:   
X0×R=X1R1+X2R2+…+XKRK=i=1KXiRi

Dividiendo ambos miembros de la igualdad por X0 y aplicando la ley del flujo forzado quedará la expresión:  
R=V1R1+V2R2+…+VKRK=i=1KViRi

Esta expresión recibe el nombre de ley general del tiempo de respuesta, y permite ver claramente que el tiempo de permanencia de un trabajo en un sistema depende del número de visitas que realiza a cada dispositivo y del tiempo de respuesta que experimenta en él por cada una de las visitas.

##### **Ley del tiempo de respuesta interactivo**

Todos los modelos de sistemas con carga interactiva pueden dividirse conceptualmente en dos partes: una que modela el tiempo de reflexión (subsistema de terminales) y otra que contiene los dispositivos físicos del computador contemplados por el modelo (subsistema central). El tiempo de reflexión ***(think time),*** identificado habitualmente mediante la variable Z*,* es el tiempo que transcurre desde que un trabajo abandona el subsistema central hasta que entra de nuevo en él.   
El tiempo de respuesta del sistema, R, corresponderá al tiempo que un trabajo pasa en el subsistema central.  
El funcionamiento del sistema es el que sigue: los usuarios generan peticiones desde los terminales que se sirven en el subsistema central, y vuelven posteriormente a los terminales. Estos terminales están modelados por una estación con infinitos servidores (no hay tiempo de espera en cola). Transcurrido el tiempo de reflexión los usuarios generan la siguiente petición.  
![][image126]  
Podemos aplicar la ley de Little al conjunto de los dos subsistemas. Este conjunto incluye el subsistema central y el subsistema de terminales. El número de trabajos en el conjunto es N***.*** El tiempo medio que permanece un trabajo en el conjunto es igual al tiempo que permanece en los terminales, Z***,*** más el tiempo que permanece en el subsistema central, R***.*** Por tanto, aplicando la ley de Little, se puede escribir:  
N=Z+RX0

Y despejando la variable R obtenemos la expresión para la ley del tiempo de respuesta interactivo:  
R=NX0-Z

Nótese que el número de trabajos en los terminales viene dado, empleando la ley de Little, por Z×X0 y el número de trabajos dentro del sistema que compiten por los recursos es R×X0

### Técnicas de evaluación de sistemas

Se denominan técnicas de evaluación a los métodos y herramientas que permiten **obtener los índices de prestaciones** de un sistema que está ejecutando una carga dada y con unos valores determinados de parámetros del sistema.

Las técnicas pueden ser de tres tipos: 

* Monitorización  
* Modelado  
* Benchmarking

#### ***Monitorización***

La **monitorización** es una técnica de uso generalizado para supervisar, analizar y evaluar el comportamiento, y el rendimiento de los sistemas informáticos, que están en funcionamiento. **Es decir, es la técnica que permite observar la actividad de un sistema mientras es utilizado por los usuarios.** 

Los **monitores** son las herramientas de medición que permiten seguir el comportamiento de los principales elementos de un sistema informático cuando éste se halla sometido a una carga de trabajo determinada. Aunque su objetivo es la medición de las prestaciones, se les denomina monitores ya que, debido a la imposibilidad de reproducir situaciones con la carga real, estos instrumentos hacen un seguimiento de lo que sucede en el sistema, es decir, lo monitorizan.

* Hace un seguimiento (NO una medición, captura datos de la actividad del sistema)  
* Tienen como objetivo cuantificar los resultados de una observación.  
* Al administrador la información aportada por el monitoreo le es útil para:  
  * Conocer la utilización de los recursos del sistema y los cuellos de botella  
  * Ajustar los parámetros del sistema y mejorar sus prestaciones

Aparte de su utilización directa para tomar medidas de un sistema existente, permiten determinar la aproximación de una carga de *benchmark* a la carga real, obtener datos para la construcción de modelos y su validación posterior, etc.

Estas herramientas son imprescindibles para evaluar el comportamiento de un sistema existente, a pesar de las **perturbaciones** que pueden introducir en el sistema cuyo comportamiento se va a evaluar.

#### ***Modelado***

Es la técnica que se debe utilizar cuando se trata de **evaluar el comportamiento de un sistema en el que hay algún elemento (hardware o software) que no está instalado.** 

En general, *se fundamentan en la teoría de colas,* pudiéndose considerar las colas o bien de forma individual o bien unidas formando redes abiertas o cerradas. Su tratamiento se puede realizar mediante los métodos analíticos que proporcionan las teorías de colas y de redes de colas, o por medio de la simulación

Las técnicas de simulación consisten en la construcción de un programa que reproduce el comportamiento temporal del sistema, basándose en sus estados y sus transiciones. **Los resultados se obtienen por extracción de estadísticas del comportamiento simulado del sistema**. Las técnicas analíticas se basan en la resolución mediante fórmulas cerradas o algoritmos aproximados de las ecuaciones matemáticas que representan el equilibrio que existe entre los eventos o transiciones de estado discontinuas que se producen en el sistema.

**La limitación de los métodos analíticos es su incapacidad para tratar determinadas estructuras y comportamientos** de las colas que existen en los sistemas informáticos. **Los métodos de simulación** **no tienen estas limitaciones, pero, en general, son mucho más caros** que los analíticos tanto en tiempo de cálculo como en esfuerzo de puesta a punto.

No obstante, la principal dificultad de esta herramienta reside en la obtención de datos lo suficientemente precisos para ejecutar el modelo y obtener resultados con el grado de aproximación que se exige.

#### ***Benchmarking***

Es un método de **comparar sistemas informáticos frente a una carga característica de una instalación concreta**, efectuándose la comparación, básicamente, a partir del tiempo necesario para su ejecución. Generalizando se puede considerar como la medición del comportamiento sobre un prototipo. Variantes de este método se usan para evaluar la potencia relativa de un sistema a lo largo de su ciclo de vida, para contrastar monitores y para validar modelos. 

BENCHMARKING  MEDICIÓN

La finalidad es analizar el rendimiento del sistema poniendo énfasis en la carga de trabajo, hay una **comparación,** en la medición solo se recolectan los datos.

Las **principales dificultades** que se plantean son:

* Cómo determinar esa carga característica, de forma que sea suficientemente reducida para ser manejable y suficientemente extensa para ser representativa.  
* Cómo valorar el aprovechamiento que hacen los programas de las peculiaridades de los distintos sistemas.

**Resultado de un benchmarking**

* Es un número o conjunto de números, que representa el grado de ajuste del equipo a las exigencias de la carga. Es decir, en cuanto se acerca al rendimiento aceptable.  
* Las unidades dependen totalmente del objetivo del estudio y de qué nivel del sistema informático interese medir.  
* Por ejemplo: número de programas o usuarios concurrentes que le SO es capaz de soportar.  
* Así el equipo que corriendo la carga testigo obtenga la mejor performance (menor tiempo de respuesta, menor porcentaje de utilización de recursos) será el más conveniente.

**Utilidad de benchmarking**

* Nutre al proceso de provisión para evaluar equipos  
* El mismo seguimiento se puede utilizar para hacer la sintonización  
* Sirve al subsistema de aplicación para analizar las prestaciones 

### Herramientas de medida

#### ***Monitores***

La herramienta del monitoreo es el **monitor**, que observa el sistema, recolecta los datos estadísticos de la ejecución de los programas, analiza los datos obtenidos y presenta resultados. Sus características de calidad son las mismas que las de los instrumentos de medición.

Una característica de una medida debe ser su **repetibilidad,** esto es, la posibilidad de realizar una medición diferentes veces, y que el resultado de este proceso (la medida) sea siempre el mismo.  

Ahora bien, en informática, el resultado de una medición será distinto unas veces de otras, ya que, normalmente, no es posible repetir las mismas condiciones de carga y en los mismos instantes. Por ello, se habla de monitorización y no de medición ya que lo que estrictamente se efectúa es un **seguimiento** de la actividad realizada **(seguimiento, no medición)**.

**Tienen como objetivo cuantificar los resultados de una observación.**

Pueden ser utilizados para:

* Conocer la utilización de los recursos del sistema y los cuellos de botella  
* Para el programador, puede encontrar los segmentos de código más utilizados y mejorarlos.  
* Ajustar los parámetros del sistema en vistas de mejorar las prestaciones  
* Un analista de sistemas puede caracterizar la carga y crear cargas de prueba, cuyos resultados se pueden utilizar para planificar la carga del sistema.

##### **Características del monitor**

Los monitores definen sus características en función de las mismas que los instrumentos de medición, que son, a saber:

* **Sobrecarga o interferencia**: Como sustraen energía al sistema observado, esta debe ser tan poca que no altere los resultados de la observación. En los monitores HW se da en los puntos de conexión, y en los de SW se da por el aumento que producen en la carga del sistema.  
* **Precisión**: Se expresa por el error que puede afectar el valor de los datos obtenidos, por interferencia del propio monitor, incorrecta instalación o utilización, dígitos para representar la medición.  
* **Resolución**: Máxima frecuencia a la que puede detectarse y registrar correctamente los datos. Capacidad de separar dos eventos consecutivos en el tiempo.  
* **Ámbito o dominio de la medida**: Tipo de acontecimientos que puede registrar y características que es capaz de observar y medir.  
* **Anchura de entrada**: Máximo de bits de información de entrada que puede extraer y procesar en paralelo cuando sucede un acontecimiento.  
* **Capacidad de reducción de datos**: Capacidad de analizar, procesar y empaquetar datos para mejor comprensión y reducción de espacio de almacenamiento.  
* **Compatibilidad**: El HW y el SW de monitorización deben ser fácilmente adaptables a cualquier requerimiento de aplicación.  
* **Coste**: Considerar el coste de adquisición, los de instalación, mantenimiento, formación y operación.  
* **Facilidad de instalación**: Del monitor, así como también la facilidad de retirarlo del sistema.  
* **Facilidad de utilización**: Deben ofrecer al usuario una interfaz que pueda ser utilizada por cualquier programador.

##### **Estructura del monitor**

| Sistema a medir | La conexión entre el monitor y el sistema se realiza a través de la interfaz de instrumentación. |
| :---: | :---- |
| **Interfaz de instrumentación** | Contiene todos los elementos que permiten acceder a los puntos del sistema que contiene información relevante para el monitor. |
| **Selector de filtro** | Permite una captura selectiva de las actividades sondeadas. También genera aquellas variables que no son directamente observadas por el sistema a partir de las variables observadas. |
| **Procesador** | Comprueba los elementos del sistema a ser analizados |
| **Registrador** | El resultado se graba en un medio de almacenamiento para poder ser analizados e interpretados y así obtener los resultados deseados. |
| **Analizador** | Algunas veces se analiza con la detección y captura de eventos (tiempo real), otra se hace después de la recogida de toda la información (análisis diferido) |

##### **Tipos de monitores**

**Según su mecanismo de activación**

Hay diversas técnicas para medir (observar) un sistema informático; su elección depende del tipo de análisis que deba efectuarse y del nivel al que deba realizarse.

* ***Detección de acontecimientos (Eventos):*** Se define un acontecimiento como un cambio de estado del sistema. El principio de detección de acontecimientos software es el de insertar un código suplementario *(**traps**,* es decir, interrupciones controladas por el programa) en lugares determinados del sistema operativo. Cuando se produce un acontecimiento que debe detectarse, este código transferirá el control a la rutina de tratamiento, que almacenará sus datos significativos, junto con el instante de aparición. Esta técnica se deberá utilizar sólo cuando sea necesario conocer la secuencia de estos acontecimientos o el número de veces que se han producido en un intervalo determinado.  
* ***Periodos de tiempo (Muestreo):*** es una técnica estadística que se puede usar siempre que el conocimiento de todos los componentes, objetos o acontecimientos de una población sea imposible, poco práctica o demasiado cara. Entonces, en vez de examinar todos los elementos de la población completa, este método **analiza solamente una parte de ellos, denominada una muestra**. Estos monitores se activan a intervalos de tiempo fijos o aleatorios mediante interrupciones de reloj. El muestreo puede usarse con dos objetivos distintos:   
  * Evaluar las fracciones de un intervalo de tiempo dado que cada componente del sistema ha permanecido en distintos estados.   
  * Seguir la evolución de un sistema y predecir su comportamiento futuro de forma que puedan tomarse las decisiones que tendrán una influencia positiva en su comportamiento.

**Según su implantación**

* ***Monitores software**,* que son **programas o ampliaciones del sistema operativo** que acceden al estado del sistema, informando al usuario (ya sea de forma continua, o cuando éste lo requiere) sobre dicho estado. Son, sobre todo, adecuados para monitorizar los sistemas operativos, las redes y las bases de datos, así como las aplicaciones que las utilizan.  
* ***Monitores hardware**,* que son dispositivos electrónicos que se conectan a determinados puntos del sistema, donde se encargan de detectar determinados niveles o señales eléctricas que caracterizan la evolución del sistema.  
* ***Monitores híbridos**,* que son una combinación de las dos técnicas anteriores, intentando combinar las ventajas de una y otra

![][image127]

| Característica | Monitor Hardware | Monitor software | Monitores híbridos |
| :---- | :---: | :---: | :---: |
| **Dominio de medición** | Bajo nivel (fijo) | Alto nivel | Todos |
| **Resolución** | Alta (fija) | Baja (variable) | Alta |
| **Anchura** | Finita | Infinita | Infinita |
| **Interferencia** | Baja | Alta | Media |
| **Coste** | Alto | Bajo | Alto |
| **Reducción** | No | Si | No/Sí |
| **Portabilidad** | Sí | No | No |

|  DETALLE | Monitores |  |
| :---: | ----- | ----- |
|  | **Software** | **Hardware** |
| **Dominio de medición** | \-Acceso controlado mediante alguna instrucción de máquina. \-Puede elegir qué datos deben ser accedidos o controlados | \-Tiene acceso a la información solo cuando entra o sale de la memoria. \-Es un observador pasivo. |
| **Resolución** | \-Frecuencias elevadas, determinada por la velocidad de las sondas y lógica del monitor. | \-Condicionado a la ejecución de la instrucción, se debe tener en consideración las instrucciones necesarias del monitor. \-Puede parar el sistema y analizar los acontecimientos, pero puede provocar una distorsión en el funcionamiento del sistema. |
| **Interferencia** | \-No produce interferencia, si las sondas han sido elegidas correctamente | \-Provoca perturbación en el sistema observado, ya que utiliza los propios recursos del sistema. |
| **Anchura de entrada** | \-Puede detectar los acontecimientos sólo secuencialmente. \-Anchura, teóricamente, ilimitada, con la perturbación del Overhead introducido | \-Permite la detección de acontecimientos en paralelo. \-Anchura limitada por el número de sondas disponibles |
| **Facilidad de uso** | \-Al ser una extensión de SO, es más fácil utilizarlo | \-Requiere un mayor grado de especialización y conocimiento |
| **Costo** | \-Accesible (instalación y funcionamiento) | \-Costoso (instalación y funcionamiento) |

**Según su forma de mostrar los resultados**

* ***Monitores en tiempo real,*** que constan de un módulo analizador que procesa los datos recogidos a medida que los recibe. En consecuencia, el módulo de proceso debe ejecutarse de forma continua, o con gran frecuencia, para poder presentar resultados parciales al analizador que informará de la evolución del sistema.   
* ***Monitores batch**,* que difieren de los anteriores en que primero se recoge la totalidad de la información y, una vez terminado el período de recolección, se procesa dicha información.

##### **Monitores de redes LAN**

La monitorización de una red es esencial para administrarse bien ya que proporciona todos los datos necesarios para caracterizar o estudiar prestaciones.

*Los dominios de administración de LAN que define la OSI son:*

* **Manejo de fallos**: esfuerzo para minimizar el tiempo medio requerido para detectar y reparar un problema en la red.  
* **Administración de cuentas**: se lleva a cabo mediante un tipo de monitor conocido como monitor de contabilidad, que informa de los recursos utilizados por los usuarios del sistema con el fine, entre otras cosas, de proceder a la facturación de recursos.  
* **Manejo de configuraciones:** esfuerzo para definir y monitorizar las configuraciones física y lógica de la red.  
* **Manejo de las prestaciones:** esfuerzo para mejorar las prestaciones de la red y detectar prestaciones degradadas por colección y análisis de estadísticas de la red, y modificación de parámetros apropiados de la red.  
* **Manejo del control de acceso**

 *Características de los monitores LAN:*

* **Interferencia:** Corresponde a la interferencia producida en el sistema por la introducción de un dispositivo monitor.  
* **Generación de tráfico artificial:**  pueden ser usados para emular condiciones de altas cargas, producir patrones de tráfico variable y repetitivo, y extraer información temporal.  
* **Análisis en tiempo real:** losa datos recogidos por el monitor pueden ser analizados inmediatamente o almacenados para un análisis posterior.  
* **Parámetros de interés:** la elección del tipo de monitorización puede ser muy dependiente de los parámetros que interese conocer de la red.

#### ***Benchmarking***

Se denomina Benchmark a los programas (kernels, programas sintéticos y de nivel aplicación) utilizados en el benchmarking (objeto estacionario). 

**El resultado del benchmarking es un número o conjunto de números, que representa el grado de ajuste que requiere ese equipo a las exigencias de la carga**. Las unidades dependen totalmente del objetivo del estudio y de qué nivel del sistema informático interese medir. *Por ejemplo: número de programas o usuarios concurrentes que un sistema operativo es capaz de soportar.*

Así, el equipo que corriendo la carga testigo obtenga la mejor performance (menor tiempo respuesta, menor porcentaje de utilización de recursos) será el más conveniente.

##### **Factores que influyen en benchmarking**

* **El rendimiento puede depender del tipo y versión del sistema operativo que tenga instalado el sistema estudiado:** una forma idónea de realizar las pruebas de medida consiste en usar en los distintos sistemas que se van a comparar la misma copia de sistema operativo; se aconseja que las características y parámetros de los sistemas operativos sean los más parecidos posible.  
* **El compilador** usado en la prueba es realmente un elemento determinante del rendimiento obtenido en el sistema, ya que según la facilidad que tenga el compilador en generar el código eficiente, el modelo de carga se ejecutará más o menos rápidamente. Además del nivel de optimización que se esté usando.  
* **Los lenguajes de programación** influyen sobre los tests realizados con benchmarks, ya que tienen facilidades diferentes en secuencias de llamadas, punteros, manejo de tiras de caracteres, etc., que repercuten directamente sobre los tiempos de ejecución, aunque los algoritmos parezcan similares.  
* **El sistema de librerías de ejecución**, ya que, según sean éstas, las funciones que implantan serán más eficientes, disminuyendo el tiempo de ejecución. Esto debe tenerse en cuenta sobre todo cuando el usuario necesita una buena precisión y, por lo tanto, es necesario saber qué tipo de librería se ha usado en la prueba.  
* **El tamaño de la memoria caché** es un factor importante porque los tiempos de ejecución varían notablemente dependiendo de si el programa cabe entero en la cache o si no cabe y debe acceder a la memoria principales.  
* **Es conveniente que programas usados como modelo de carga realicen una verificación de resultados obtenidos,** para que el usuario sepa que el benchmark se ha ejecutado correctamente.

##### **Errores comunes en el benchmarking**

* **Representar en la carga de test sólo los comportamientos medios:** las cargas de test o de prueba se diseñan para que sean representativas de la carga real. Los diseñadores de carga se aseguran de que la demanda relativa de recursos sea similar a la observada en el entorno real. Estos valores constantes no son deseables ya que pueden causar sincronizaciones llevando a conclusiones erróneas. En estas ocasiones, es necesario ir a una representación más detallada de recursos.  
* **Controlar de manera inadecuada el nivel de carga.** La carga de test dispone de varios parámetros que se pueden modificar para incrementar el nivel de carga en el sistema.  
* **Ignorar los efectos de la caché.** Las memorias caches son muy sensibles al orden de las peticiones. En los sistemas modernos se emplean las caches en los accesos de memoria, a los discos, a las redes, por tal motivo, cada vez es más necesario modelar de manera precisa el orden de las llegadas.  
* **Ignorar el overhead del monitor.** Los mecanismos de recolección de datos o los monitores software que se utilizan en las medidas presentan un overhead que introduce error en los valores medidos.  
* **No validar las medidas.** Es un error bastante común, cualquier error cometido en el experimento de medida puede pasar totalmente desapercibido.  
* **No asegurar las mismas condiciones iniciales.** Cada ejecución del benchmark altera el estado del sistema.  
* **No medir las prestaciones del transitorio**. Durante las medidas, se permite al sistema alcanzar el estado estable antes de tomar las medidas. Al sistema le cuesta un largo período de tiempo alcanzar el estado estable puede ocurrir que el sistema esté más tiempo en estado transitorio que en estado estable. Sería más realista estudiar las prestaciones en el transitorio.  
* **Usar las utilizaciones de los dispositivos para comparar las prestaciones.** Las utilizaciones de los dispositivos son índices de prestaciones en el sentido que, dada la misma carga, es preferible la utilización menor, emplearlas para comparar dos sistemas puede ser no adecuado. Utilizaciones menores para el mismo número de usuarios no deberían interpretarse como mejores prestaciones. El índice adecuado para comparar dos sistemas en este caso sería la productividad expresada en peticiones por segundo.  
* **Recoger muchos datos para realizar poco análisis**. El análisis de datos no suele recibir la atención adecuada por varias razones, puede suceder porque la persona que realiza las medidas no suele tener demasiada práctica en la utilización de técnicas estadísticas. O porque la toma de datos suele ocupar tanto tiempo del proyecto que ya no queda para el análisis.

##### **Pasos para conseguir un buen paquete de programas benchmark**

* Determinar que se quiere estudiar y porqué (objetivo).  
* Seleccionar en benchmark sobre la base del objetivo definido (características: representatividad, reproducibilidad, compacidad, escalabilidad).  
* Se deben **comprobar** los **aspectos** del sistema bajo estudio **que influyen en el rendimiento**, como pueden ser el sistema operativo, los compiladores y su nivel de optimización, el uso de memorias caché, etc.  Además, se debe comprobar que los programas, versiones y datos usados como *benchmark* sean los mismos en todas las pruebas. Todo esto es fundamental para que las comparaciones tengan significado.  
* Finalmente, obtenidos los resultados y entendiendo perfectamente qué hace cada programa *benchmark,* se debe intentar **estudiar la causa que produce variaciones en los resultados de los distintos sistemas.**

##### **Tipos y necesidad de los benchmarks**

* **Benchmark general (carga artificial)** La primera definición nos dice que los *benchmarks* son una forma de evaluar las prestaciones de un sistema informático, en conjunto o sobre partes determinadas. Además, si el *benchmark* está estandarizado, los resultados se podrán comparar con los obtenidos en distintos sistemas.  
* **Benchmark natural, (carga de prueba teniendo en cuenta la carga real).** La segunda definición de *benchmark* se obtiene particularizando y creando una clasificación en la que se reparten los distintos programas usados para evaluar sistemas informáticos; en este caso los *benchmarks* se pueden definir como conjuntos de programas completos escritos en lenguaje de alto nivel extraídos de la carga real y que se consideran representativos de esta carga real.

##### **Razones para utilizar Benchmarks**

* Nutre al proceso de provisión para poder evaluar equipos (Seguimiento → provisión)  
* Sirve para saber qué ajustar para sintonizar los equipoS (Como retroalimentación a sí mismo)  
* Para poder analizar las prestaciones (Seguimiento → aplicación)

### Sintonización de un sistema

El primer paso para **mejorar las prestaciones y la eficiencia de un sistema informático** es analizar su funcionamiento. Es decir, llevar a cabo un estudio de evaluación de las prestaciones del sistema. Las operaciones que se llevarán a cabo se pueden agrupar en las siguientes **fases**: 

![][image128]

#### ***Definición de objetivos***

Hay que determinar los objetivos del estudio y el tipo de datos que se desea obtener. Se determinará el método que se utilizará para analizar las prestaciones del sistema, la cantidad de recursos que es preciso emplear y la forma de justificar la inversión necesaria.  
![][image129]

#### ***Caracterización de la carga***

Caracterizamos la carga para obtener una carga modelo (carga de prueba o test) y así realizar pruebas. Una carga está correctamente caracterizada si y sólo si, su resultado es un conjunto de parámetros cuantitativos seleccionados de acuerdo con los objetivos de operación de caracterización.

Cualidades: reproducibilidad, compacidad, compatibilidad, representatividad, flexibilidad, independencia del sistema.

#### ***Selección de la instrumentación***

Una vez definidos los objetivos del estudio, el siguiente paso será medir todo aquello que pueda tener influencia sobre los mismos. Medir implica recoger datos acerca de la actividad del sistema empleando para ello las técnicas y la instrumentación adecuada.  
![][image130]

El estudio se centra en las siguientes áreas: 

* Los componentes hardware del sistema.   
* El software del sistema (sistema operativo y los programas de sistema y de usuario)  
* La carga, es decir, el conjunto de programas que el sistema tiene que procesar durante un período dado.

#### ***Diseño y planificación de la sesión de medida***

Para poder planificar una sesión de medida debe conocerse, al menos someramente, la carga y su evolución en el tiempo. Las medidas deben llevarse a cabo en un entorno controlado con carga conocida y no se deben hacer modificaciones en el hardware ni cambios en los procedimientos habituales de operación durante su realización. 

Se deberá saber, al menos de manera aproximada, cuándo se producen los mayores incrementos de carga (picos de carga) para poder tenerlo en cuenta a la hora de planificar la sesión. Las sesiones suelen incluir medidas correspondientes a, precisamente, esos períodos de incremento de carga.

Si se utiliza un **monitor de software** se debe tener en cuenta que este también utiliza recursos.  Por tanto, habrá que seleccionar la longitud de la sesión de medida (y, por tanto, la frecuencia de muestreo) de manera que, dado un nivel de confianza, la interferencia con el sistema sea la mínima posible.

Si se utiliza un **monitor de hardware** se debe tener en cuenta la correcta conexión de sensores, la longitud de los cables, la correcta selección de las señales, etc.

#### ***Validación***

El esquema global de las operaciones implicadas en esta fase aparece en la figura. (El libro solo tiene esto).  
![][image131]

### Estudios de sintonización

**Se siguen los siguientes pasos:**

* Planteamiento del problema: Se plantean los síntomas externos de ineficiencia que han motivado el estudio, así como los objetivos que se pretenden alcanzar.   
* Medidas e interpretaciones.   
* Acciones emprendidas y verificación de sus efectos.

### Evaluación de las prestaciones del sistema informático

De acuerdo con parámetros de rendimientos aceptables según el entorno particular…

| Técnica | Herramientas | Finalidad |
| :---: | :---: | :---: |
| **Modelado-Técnicas analíticas** | Análisis Operacional | Evaluar índices. Detectar cuellos de botellas potenciales |
| **Monitorización (uso de recurso por lo general)** | Monitores | Observación y medición del sistema. Caracterización de la carga |
| **Benchmarking (uso de recurso y comportamiento)** | Benchmark Sintéticos/ artificiales | Comparación Selección, configuración |
| **Sintonización Experimentación** | HW, SO, Carga | Mejora las prestaciones del sistema actual |

## 

## **Seguimiento de RRHH** {#seguimiento-de-rrhh}

**Sistema de evaluación de cómo el personal está rindiendo**, de cómo se está acercando a tener lo más alto del perfil pedido y como está contribuyendo a los objetivos y metas.

Por un lado tengo el **control de desempeño** para ver como esta el personal, pero también **debo hacer una auditoría**, necesito saber como estoy llevando adelante la gestión de los RRHH (esta auditoría se hace en un área FUERA del área de la gerencia, una auditoría interna la hace el staff de RRHH, en caso de necesitar más hago una auditoría externa).

⇒ Es el subsistema conformado por los procesos, métodos y herramientas que permiten **evaluar el grado de adecuación del desempeño/rendimiento de los RRHH a las metas de funcionamiento establecidas y determinar las acciones de mejora adecuadas.**

* [**Evaluación de desempeño**](#evaluación-de-desempeño)**:** es el proceso de calificar la actuación (pasada o presente) del personal (un empleado, un equipo de trabajo) en base a normas de desempeño establecidas. Su finalidad es verificar y asegurar el desempeño de las tareas. Todo, según lo que la organización se ha fijado como metas y formas de desempeño deseables.  
* El **control** trata de asegurar que las diversas unidades de la organización marchen de acuerdo con lo previsto. Es la **acción** que ajusta las operaciones a los estándares predeterminados; su base de acción es la información de retorno. El control trata de garantizar que todo ocurre de acuerdo con la planeación adoptada y los objetivos preestablecidos, señalando las fallas y los errores para corregirlos y evitar reincidir en ellos.

Hay diferentes **momentos en los que controlar,** derivando asi en **tipos de control**:

* Cuando es previo a que ocurra un hecho, que se intenta evitar, entonces el **control es preventivo**  
* Cuando los controles preventivos han fallados, primero se debe identificar el hecho antes de poder solucionarlo, allí hablamos de **control detectivo**  
* Por último se intenta restablecer el funcionamiento normal del sistema, que fue alterado por la falla detectada, esto es el **control correctivo**, realizamos acciones correctivas para restablecer el estado deseable del sistema.

### Administración por excepción

*“Me tengo que preocupar cuando hay incidentes o situaciones imprevistas, o alejadas de la norma (superan un cierto rango de desvío).*”

Toda operación se caracteriza por experimentar variaciones; cuando estas son pequeñas y no causan distorsiones, pueden aceptarse como normales, pero cuando son muy grandes y causan tropiezos, constituyen **excepciones** que deben tratarse con cuidado y corregirse de manera adecuada.

### Etapas del proceso de control

**El proceso de control es cíclico y repetitivo**, y sirve para ajustar las operaciones a los estándares preestablecidos.

![][image132]*Chiavennato*

*![][image133]Robbins y Coulter*

#### ***Establecimiento de los estándares deseados***

Los estándares representan el desempeño deseado. Un estándar es una norma, define el nivel normal de trabajo, es decir, es un valor de referencia que indica cómo se debería trabajar **→** valor que determina el rendimiento normal, lo que es esperable y alcanzable por todos.

*estándar \<\> umbral: el umbral tiene que ser más alto.*

Los estándares representan desempeños que son significativos para cada organización en particular,  y pueden expresarse en:

* **Cantidad:** Número de empleados, Volúmenes de producción o ventas, Índice de accidentes, Índice de rotación.  
* **Calidad:** Calidad de los productos, Calidad de los servicios, Asistencia técnica, Mantenimiento de equipos.  
* **Tiempo:** tiempo estándar, tiempo medio desde el hogar, horas hombre trabajadas, ciclo de producción.  
* **Costos:** de cada orden de servicio, costo medio de selección, costo medio de entrenamiento, costo de salario indirecto.

#### ***Medición del desempeño real (Seguimiento o monitoreo del desempeño)***

![][image134]![][image135]

**Nota**: En este momento entra la evaluación de desempeño.

#### ***Comparación del desempeño con los estándares deseados***

Luego de evaluar se hace la comparación entre el **desempeño real** y el **estándar.** Toda actividad experimenta alguna variación, error o desviación. Por tanto, es importante determinar los límites en que esa variación podrá aceptarse como normal o deseable: la llamada **tolerancia**.

La comparación no sólo busca localizar errores o variaciones, sino también predecir resultados y localizar las dificultades para alcanzar mejores resultados en operaciones futuras. Sirve para saber cuánto se está alejando del desempeño real.

**Umbral de desempeño**: aquello que yo fijo que está sobre el estándar y que se lo firma en forma consciente, mediante el cual todos que cumplan, acceden a la remuneración variable que pudo haber sido establecido. Es distinto al LÍMITE SUPERIOR

![][image136]  
Se pueden observar tres casos:

* etapa 1 \> etapa 2 → tengo un \- aceptable  
* etapa 1 \< etapa 2 → tengo un \+ aceptable  
* etapa 1 \= etapa 2 

⇒ Si estoy permanentemente por debajo, tengo que replantear los estándares, ya que estoy poniendo metas que requieren mucho esfuerzo y que eso me lleva a ciertos desequilibrio. Si pongo estándares muy bajitos me puede llegar a desmotivar a la gente. **El estándar refleja el rendimiento normal.**

#### ***Acción correctiva, si es necesaria***

Las variaciones, errores o desviaciones deben corregirse para que las operaciones se normalicen. La **acción correctiva** incide sólo sobre los casos excepcionales.

Con la acciones correctivas puedo notar:

* estándares poco exigentes o muy exigentes ⇒ debo revisar el estándar  
* trabajar sobre el desempeño  
* trabajar sobre la evaluación o el evaluador.

**Nota:** en esas etapas, **¿qué coincidencias tengo con la evaluación de desempeño?** Las técnicas de evaluación de desempeño las puedo aplicar en esas etapas ⇒ el control de desempeño incluye la evaluación de desempeño.  
![][image137]

### Criterios de control

Para que el proceso de control sea eficaz, **debe atender los siguientes criterios:**

* **Controlar por excepción:** investigar situaciones que se alejan de la norma, bastante alejado de lo común.

Toda operación se caracteriza por experimentar variaciones; cuando estas son pequeñas y no causan distorsiones, pueden aceptarse como normales, pero cuando son muy grandes y causan tropiezos, constituyen excepciones que deben tratarse con cuidado y corregirse de manera adecuada → *“Me tengo que preocupar cuando hay incidentes o situaciones imprevistas, o alejadas de la norma (superan un cierto rango de desvío).”*  
![][image138]![][image139]

* **Controlar las actividades apropiadas**: actividades que deben y requieren ser controladas (no puedo controlar todo, me enfoco en lo principal)  
* **Oportunidad**: debe efectuarse en el momento adecuado para señalar las desviaciones necesarias en tiempo real y permitir emprender las acciones correctivas. Por ejemplo: Si es un trabajo largo, no se va a controlar al comienzo.   
* **Economía**: El control no puede costar más que el elemento controlado. Las medidas, herramientas y el elemento de control no pueden salir más caras que el beneficio que se obtiene.   
* **Precisión**: Los procesos de control son indicadores de progreso y son la base para las acciones correctivas, por lo tanto, debe ser objetivo claro y preciso. El grado de precisión dependerá de cuánto necesito saber de eso que estoy controlando.   
* **Aceptación de control**: Es importante que las personas acepten el control y comprendan los objetivos del proceso. Esto tiene que ver con una cuestión cultural, evaluar debe ser un proceso visto como positivo, para que todos logren mejorar. El control es lo único que me permite saber de como estoy yendo; no Marta, no te vamos sacar la remuneración variable en tu primer control.

#### ***Medios de control***

* **Jerarquía de autoridad:** es la manera más común de controlar a las personas. La jerarquía representa un tipo de control personal de los subordinados.  
* **Reglas y procedimientos:** son controles impersonales que gobiernan el comportamiento de las personas en la organización.  Es un mapeo (llegar temprano o llegar tarde, por ejemplo)  
* **Establecimiento de objetivos:** sirven de guía a la acción de las personas.  
* **SI verticales:** La información en SI verticales, puede ir en sentido ascendente (de eventos, resultados, aclaraciones y retroalimentación) y descendente (mandatos, decisiones, aclaraciones y orientaciones). En ambos sentidos, los sistemas de información vertical constituyen medios de control, aunque esta no sea su finalidad principal. (Puedo ver el avance del proyecto, por ejemplo)  
* **Relaciones laterales:** son un medio de tipo referencial comunicaciones entre pares, es decir, entre personas y cargos que ocupan el mismo nivel jerárquico en la organización.  
* **Organizaciones Matriciales:** aunque esta doble subordinación origina conflictos, su estructura matricial permite innovación, cambio y, sobre todo, adaptación rápida a las exigencias ambientales.

### Evaluación de los procesos de monitoreo de personas

El control debe evolucionar desde la primera situación hacia la segunda:

| *Empleados que deben ser constantemente controlados* | *Evaluación gradual Control externo y rígido  Autocontrol y flexibilidad Restricciones  Autonomía Centralización  Descentralización* | *Empleados que se autocontrolan* |
| :---: | :---: | :---: |

### Auditoria de RRHH

Es el análisis de las políticas y prácticas de personal de una empresa y la evaluación de su funcionamiento actual acompañados de sugerencias para mejorar. **Su finalidad es verificar el desempeño de la gestión de los RRHH.**

#### ***¿Qué evalúa la auditoría de RRHH?***

* Inspección y verificación de las funciones de personal llevadas a cabo por el área de RRHH de la organización.  
* Inspección y verificación de las funciones de personal llevadas a cabo por los gerentes de línea. Es determinar la forma en que los gerentes de línea llevan a cabo sus funciones de personal y en qué medida cumplen con las políticas y los procedimientos.  
* Auditoría del nivel de satisfacción de los empleados.

#### ***Técnicas para obtener información sobre las actividades de RRHH***

* Entrevistas – entrevistas de salida  
* Encuestas/sondeos de opinión  
* Análisis de los registros de RRHH  
* Análisis de las políticas y procedimientos de RRHH  
* Análisis de los cargos y sus habilidades

#### ***Patrones de evaluación de control en RRHH***

El sistema de ARH necesita estándares que permitan una evaluación continua y un control sistemático de su funcionamiento.

En general, los estándares permiten la evaluación y el control mediante la comparación con:

* ***Resultados:*** Cuando la comparación entre el estándar y la variable se hace **después** de realizada la operación.  
* ***Desempeño**:* Cuando la comparación entre el estándar y la variable es **simultánea** con la operación.

La **comparación** es la función de verificar el grado de concordancia entre una variable y su estándar. La ARH se encarga de planear, organizar y controlar las actividades relacionadas con la vida del personal en la empresa.

**La función de la auditoría no es sólo señalar las fallas y los problemas, sino también presentar sugerencias y soluciones**.

#### ***Amplitud y profundidad de la función de auditoría***

La cobertura de la auditoría de recursos humanos es tan amplia como las mismas funciones de ARH y presenta una división semejante a las divisiones seccionales de los organismos de ARH.

Generalmente requiere de un SI gerencial, basado en los registros de personal y estadísticas provistas por los otros subsistemas

La auditoría de RH puede enfocarse en uno o en todos los siguientes niveles de productividad:

* **Resultados***.* Incluyen las realizaciones concretas y la solución de problemas en la administración actual.  
* **Programas***.* Comprenden prácticas y procedimientos de RH.  
* **Políticas***.* Incluyen la explícita, formalizada por la empresa, y la implícita.  
* **Filosofía de la administración***.* Sus prioridades, valores, metas y objetivos.  
* **Teoría***.* Relaciones y explicaciones que detallan y relacionan la filosofía, la política y las prácticas del personal.

**La auditoría permite verificar:**

* Hasta qué punto es aceptable la teoría que fundamenta la política de recursos humanos.  
* Hasta qué punto se adecuan la práctica y los procedimientos a la política y teoría adoptadas.

En últimas, se trata de evaluar y medir los resultados de la ARH en sus actividades de mayor o menor prioridad tales como:

* Indicadores de eficiencia y eficacia, entrenamientos, remuneración, etc.  
* Claridad de objetivos de la ARH en términos de calidad, cantidad, tiempo y costos.  
* Distribución de recursos y resultados obtenidos.  
* Contribución de la ARH al logro de los objetivos de la organización  
* Clima organizacional