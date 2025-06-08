# Magnitudes que caracterizan la carga

## Niveles de caracterización de la carga

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

## Opciones para mejorar el comportamiento de un sistema informático

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