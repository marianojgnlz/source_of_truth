# Representatividad de un modelo de carga

La representatividad de la carga es una medida de la similitud entre el modelo y la carga real. Una vez que el modelo de carga está disponible se pueden estudiar los efectos de cambios en la carga de una manera controlada simplemente cambiando el peso de los parámetros en el modelo.

La carga puede representarse a distintos niveles, correspondientes a aquéllos en que puede describirse un sistema informático. Esto significa que no hay un criterio único para evaluar la representatividad de un modelo.

## Representatividad a nivel físico

El modelo de la carga se basa en los consumos absolutos o unitarios de los recursos hardware y software. Este nivel de modelado, se basa en una caracterización orientada a recursos y depende fuertemente del sistema empleado

La mayoría de los parámetros usados en la modelización a este nivel están recopilados por las rutinas de contabilidad *(logging o accoutuing)* presentes en la práctica totalidad de los sistemas operativos.

*Se dice que un modelo de la carga W' representa perfectamente la carga W si solicita los mismos recursos físicos en las mismas proporciones que W.*

**Campos de aplicación:**

* Sintonización del sistema: Modificación del consumo de recursos para un mejor funcionamiento.
* Planificación de la capacidad residual: Porcentaje del equipo que no está siendo usado
* Diseño

## Representatividad a nivel virtual

En este nivel se consideran los recursos del sistema a nivel lógico (ejemplo: accesos a la base de datos, número de sentencias). A causa de este tipo de parámetros, los modelos de este nivel están próximos al punto de vista del programador y son menos dependientes del sistema que los modelos a nivel físico. Tiene como desventaja, que es más difícil obtener los parámetros para la construcción del modelo.

*Se dice que un modelo de la carga W' representa perfectamente la carga W si solicita los mismos recursos físicos con la misma frecuencia que W.*

**Campos de aplicación**

* Estudios de ampliación, en los que se quiere prever el funcionamiento del sistema después de añadir nuevas unidades.

## Representatividad a nivel funcional

En este nivel la carga viene determinada por las aplicaciones que la componen.

En el modelo deben aparecer programas que efectúen las mismas funciones que en la carga original. Así pues, las funciones que componen la carga deben describirse de forma independiente del sistema. Este nivel de carga trae aparejada una dificultad para diseñar sistemáticamente.

*Se dice que un modelo de la carga W' representa perfectamente la carga W si realiza las mismas funciones con las mismas proporciones que W.*

**Campos de aplicación:**

* Selección de un computador
* Planificación de la capacidad.

## Representatividad a nivel de comportamiento

En el modelo de carga, deben aparecer las mismas variables de comportamiento que los de la carga original. Ejemplo: reproducción de esquemas de seguridad, capacidad, fiabilidad del sistema.

Un modelo *W* representa perfectamente la carga *W,* si produce los mismos valores de los índices de comportamiento que W, cuando se ejecuta en el mismo sistema.

Se considera como criterio de la precisión del modelo, la diferencia que puede existir entre los valores de los índices de comportamiento que produzca la carga y su modelo. 