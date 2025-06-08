# Caracterización de la carga

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
| **Sintética** | Está constituida por un conjunto de programas extraídos, o no, de la carga real del sistema informático que *la reproduce de forma compacta*. Puede utilizarse repetidamente y modificarse sin afectar a la operatividad del sistema. |  |
|  | **Natural** | Consta de un conjunto de programas extraídos de la carga real. Se aplican principalmente en el campo de estudios de selección y aplicación. |
|  | **Híbrida** | Se puede adoptar este tipo de solución cuando la carga a modelar no existe completamente. Se presenta la carga conocida con un conjunto de programas extraídos de ella, y la no existente mediante algunos de los elementos artificiales. |
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