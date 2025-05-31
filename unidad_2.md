# **Unidad 2: Subsistema de provisión** {#unidad-2:-subsistema-de-provisión}

*PLANIFICACIÓN ESTRATÉGICA ⇒ ESTRATEGIAS, PLANES , UBICACIONES, ROL Y ORG*

Toda estrategia organizacional se factoriza en estrategias funcionales *(porque es una estrategia para cada área, para alguna función de la organización)*. Entre otras cosas que debemos hacer, son las decisiones de la estructura organizativa del área ⇒ tiene que ser una definición estratégica de con qué estructura voy a acompañar a esos planes de sistemas que resultan de mi estrategia org (debo pensar cómo me organizo para poder funcionar).

**Subsistema de provisión (en general) →** Es el subsistema conformado por procesos y técnicas  que suministran de los recursos de SI/TI que requiere la  org (sw, hw y personas), de acuerdo con las necesidades específicas (las cuales surgen de los roles y ubicaciones que definí, desde la planificación estratégica, etc)

*|NOTA| RECURSOS HUMANOS → Conjunto de proceso y técnicas que se destina a como obtengo las personas que se INTEGRARÁN a la org, a mi cultura, la tecnocracia, etc. Su finalidad es abastecer a los talentos que tiene que estar en mi org y que son los que requiero para el funcionamiento que yo planifiqué.*   
![][image18]

## **Provisión de SI/TI** {#provisión-de-si/ti}

Es el conjunto de **procedimientos técnicos de calificación y pautas** que tienen como fin la selección de soluciones de sw y/o hw más conveniente para la organización. Su finalidad es **abastecer a la organización de los SI/TI** adecuado para la arquitectura planeada (tengo en cuenta la ubicación ej: centralizado marco las pautas, si son delegados tendré que seguir las pautas de los delegados).

El *sistema de seguridad y auditoría*, le da la corrección y grado de cumplimiento de los PP de los diseños y desarrollos (grado de cumplimeinto en ls proceos, en los diseños, en las metodologías de desarrollo que supe que mi org ha decidido seguir para desarrollar ⇒ cuando voy a una provisión debo tener en cuenta todo); como devolución le da, las políticas de provisión, los contratos, las verificaciones de prestaciones, los objetivos de las aps, etc.

*La Provisión de SITI → recursos adecuados para la arquitectura que se diseñó.*

*![][image19]![][image20]*

**Conceptos claves**

* El proceso de provisión consiste en determinar **la mejor alternativa técnica-operativa-económica para proveer del SW y/o HW** que requiere la organización, de acuerdo a las diferentes circunstancias que se puedan presentar, **apelando al principio de RACIONALIDAD.** 

* Los recursos de SW y HW deben **ser seleccionados en base a técnicas de calificación y priorización**, siguiendo pautas de provisión formales y las establecidas por criterio profesional. Por más chica e informal que sea la organización, se debe cumplir esto *(cada componente tiene una prioridad, criterio profesional a medida que voy adquiriendo experiencia).*

* El proceso de **determinar las fuentes**, no es un proceso técnico, **es un proceso de toma de decisiones.**

* ***¿De que me voy a nutrir?*** La carga de trabajo, esta refleja mi entorno informático (usuarios simultáneos, aplicaciones y de qué tipo, cuales se están ejecutando, cuanto es el uso de las aps, cuanto espacio ocupan, etc) ⇒ necesito conocer esta carga para poder dimensionar, por ejemplo, el performance que necesito para un posible servidor que voy a adquirir. **Aparte de la cartera, tengo que ver mi carga de trabajo, todo eso nutre a mi proceso de provisión.**

### Objetivos {#objetivos}

* Identificar e investigar las alternativas de obtención de SW y HW concretos, susceptibles de servir de soporte a la solución recomendada para el sistema de información objeto. *(Investigación de alternativas de solución posibles en el mercado)*  
* Desarrollar, evaluar y clasificar las fuentes de obtención posibles. *(ó desarrollo, ó adquiero, dos extremos de decisión)*  
* Determinar y recomendar las mejores propuestas de los posibles proveedores. *(Parte del proceso de provisión)*  
* Establecer los requisitos de integración de los desarrollos y/o productos elegidos. *(Cómo y de qué forma se van a integrar a los sistemas existentes)*

### Enfoques de conversión {#enfoques-de-conversión}

Se consideran cuatro enfoques básicos de conversión en donde, de manera aproximada, el “riesgo” sigue un orden ascendente y la generación de costos adecuados un orden descendente. Este enfoque debe determinarse antes de hacer la adquisición y en el inicio del proceso de selección, pues la opción de la estrategia de conversión influirá a su vez en otras opciones. 

![][image21]  
Explica cómo voy a convertirme de un sistema nuevo a uno viejo. 

* **Abrupto**: dejo de usar el viejo de un día para el otro.   
* **En fases:** voy pasando por funciones o por etapas, y voy supliendo de a poco hasta que hago que el nuevo reemplaza del todo al otro. Incorporo la funcionalidad del sistema nuevo, y esa misma similar dejo del sistema existente.se incorpora el modulo dejando el viejo  
* **Paralelo:** uso los dos a la vez y en un día específico me deshago del viejo.   
* **Piloto**:tengo parte del sistema nuevo (como islitas del sistema anterior), pero esto lo puedo ver en el distribuido como sucursales con el sistema nuevo y algunas otras con el sistema viejo, en este caso pueden llegar a convivir el sistema viejo con el sistema nuevo (ocurre, por ejemplo, cuando el sistema viejo tiene funcionalidades que pueden seguir siendo usadas), y las “islitas” (en estas islas solo se usa el sistema nuevo, se saca el viejo en esa parte)son funcionalidades que se aplican del nuevo sistema porque antes no existían o porque se reemplazan. Voy eligiendo determinadas áreas y le doy una parte de la aplicación nueva que le corresponde 

**La decisión del enfoque de conversión depende de las características de la organización**, por ejemplo: Si continuidad del servicio es vital, es muy probable que el enfoque paralelo sea un mejor método de conversión que el del cambio abrupto; cuando el elemento del sistema dado depende de otros, es más adecuado el enfoque en fases, pues reduce el riesgo

**La resistencia al cambio de los usuarios no puede influir en la decisión de alguno de estos enfoques, nosotros tenemos el deber de convencer.**

No hay que cambiar sin razón; cuando es preciso cambiar, es mejor hacerlo de manera simple y buscar la flexibilidad. Sobre todo, hay que partir desde el problema empresarial y tratar de solucionarlo mediante el software y el hardware, y no buscar la solución más elegante sin considerar el problema real

### Características y Parámetros {#características-y-parámetros}

La selección requiere identificar determinadas necesidades en un orden de prioridades. Éstas pueden establecerse sobre la base de dos elementos:

* **Características obligatorias:** El incumplimiento de alguna de ellas implica la impugnación de la oferta en su totalidad. Cualquier alternativa que carezca de las características obligatorias no tiene curso en el proceso de selección  
* **Características Deseables y Altamente Deseables:** Sirven para flexibilizar la oferta de los oferentes, ya que sobre ellas se efectúa el proceso de calificación de características de las ofertas presentadas.

Los **parámetros cuantitativos** son medidas, o proyecciones de éstas, de alguna capacidad o cantidad que determina una característica o sub-característica de un elemento de HW o de una facilidad de SW. **Su determinación se basa en el empleo de fórmulas matemáticas determinísticas o métodos probabilísticos**, que arrojan una apreciación altamente objetiva sobre una característica. *Ej.: tps, tasa de transferencia, capacidad de almacenamiento.*

Los **parámetros cualitativos** son similares a los anteriormente nombrados, con el agregado de que su cumplimiento no solo permitirá definir al mejor equipo que se adapte a la organización, sino también aquel que posea la mejor performance aplicada a las capacidades manejadas por la misma. Es decir, los parámetros cualitativos **son determinados por la experiencia, la observación, convenciones, restricciones, políticas, etc. Poseen cierta subjetividad** y por lo general se deben transformar en cuantitativas, o controlar que no superen el 20% del total de parámetros. *Ej.: tecnología de disco, dimensiones de pantalla, variables de consumo de electricidad (como frecuencia y voltaje), estética, etc.*

### Esquema del proceso de selección {#esquema-del-proceso-de-selección}

![][image22]![][image23]

***|Nota|Especificación del problema:** hablamos de la estrategia de ti (ya sé la solución), ahora tengo que ver cómo la adquiero.*

La compra de servicios de SI debe implicar un determinado proceso de selección, que generalmente involucra **cierta técnica de puntaje y calificación** (la economía de la información es una de ellas). Sin importar el grado de formalidad o informalidad del método de selección, los principios básicos de la técnica son:

1\. Seleccionar los criterios para hacer la elección.  
2\. Asignar a cada criterio un valor de importancia.  
3\. Dar un puntaje a las alternativas de adquisición (cómo satisfacen cada criterio).  
4\. Calcular la calificación de cada propuesta, multiplicando los puntajes por el valor de importancia; los resultados se suman en un total.  
5\. Seleccionar la alternativa que tenga el puntaje más alto.

**→ Para el SW**  
Ya tengo mis necesidades, la cosa es ver la fuente que voy a necesitar ⇒

**1- Especificar las fuentes posibles:** requiere investigación, es casi lo mismo cómo investigar el mercado de RRHH para ver donde encuentro lo que busco. Voy a tener info de las decisiones del comité SI/TI, algún lineamiento que me bajen de las posibles fuentes, opiniones tencias, investigación del mercado de sw, políticas de org y SI/TI ⇒ me enmarcar a donde va mi investigación y mi carpeta de apps que me guia.

**2- Viabilidad de las posibles fuentes:** evaluación, se determina cuales de las fuentes son viables PARA MI. Los criterios con los que voy a evaluar las opciones  es seguir las restricciones de la org. 

**3- Concreción de la solución mediante la fuente seleccionada:**  tengo parámetros cuantitativos y cualitativos; cualquiera sea la fuente, a quien me la vaya a dar la app le tengo que decir mis requerimientos, los cuales reflejan esos parámetros; es como un gran pliego de condiciones técnicas

* Adquirir paquete  
  * Desarrollo paquete  
  * Outsourcing. Si tengo todo en la nube, estoy en uno de los esquemas de acá (agencia de servicios)

**→ Para el HW**  
Se centra en dos cuestiones:

1- Las fuentes de adquisición (externo)  
2- Indole de la plataforma.

## 

## **Proceso de obtención de software** {#proceso-de-obtención-de-software}

### ![][image24]

### Canales de provisión {#canales-de-provisión}

Las opciones de provisión de SW comprenden un continuo de posibilidades que se muestran en la figura, dónde se observa que no existe una división fija entre los desarrollos externos e internos, y que solo las opciones 1a, 1b, 4 y 5 pueden definirse claramente. 

![][image25]

Independientemente de que el desarrollo definitivo sea interno o no, es necesaria la participación de personal experto interno para establecer los requerimientos. Lo que determina que rutas de adquisición son las más apropiadas es la índole de esos requerimientos, que capturan los principios comprendidos en la estrategia de SI. Los requerimientos deben incluir limitaciones en el proceso de selección.

#### ***Desarrollo interno***

Cuando se considera el software de aplicaciones muchas empresas eligen desarrollar sus propios sistemas. Cuanto mayor es la sección de IS, y cuanto más centralizada está, mayores son las probabilidades de que se desarrolle internamente.

Los proyectos de desarrollo de software actuales contienen incertidumbres inherentes debido a la necesidad de retener la flexibilidad en un entorno que cambia con rapidez.

Para evitar ese problema, el trabajo de desarrollo interno requiere:

* Control efectivo del proyecto por medio de enfoques actuales de management de proyecto.  
* Predisposición y herramientas para la producción de software.

* La necesidad de un control eficaz de proyecto es obvia, pero puede ser difícil lograrlo a menos que el software se realice mediante ingeniería de producción en lugar de ser creado individualmente.

Ha habido una tendencia estable a prescindir de los equipos de desarrollo a gran escala formados por personal interno. Los factores que motivaron esa tendencia están dados por todo un historial de poca fiabilidad, falta de un management de proyectos capacitado y dificultad de retener los equipos de personal con aptitudes en un entorno de cambios veloces.

**En general los paquetes estándar presentan menores costos.**

Como resultado de la tendencia hacia el desarrollo de aplicaciones por usuarios y de los paquetes adquiridos, gran parte del trabajo interno consiste en el mantenimiento y mejora de los sistemas existentes, por lo general en la reingeniería de dichos sistemas, y muy pocas actividades se dedican a los nuevos desarrollos.  
**![][image26]**

#### ***Uso de paquetes estándar***

Los paquetes están presentes en **todas** las arquitecturas de hardware (no solo pc).

Para la mayoría de las empresas aportan ventajas, sobre todo en las áreas de aplicación de baja importancia estratégica. Para las pequeñas empresas que se han informatizado, es impensable considerar otra cosa que no sean las soluciones en paquete.

Algunas de **las ventajas** son: 

| Rápida disponibilidad Procedimientos comerciales sólidos Calidad conocida y comprobable Menores costos iniciales y generales | Documentación verificable Mantenimiento disponible Investigación y actualización continuas Soporte y capacitación variados |
| :---- | :---- |

El costo de la compra o de la licencia del paquete, si bien puede ser alto, ofrece **certidumbre***,* a diferencia del costo de un desarrollo interno de software.

Cuando se adquiere un paquete, todo el aprendizaje de desarrollo queda retenido por el fabricante. Existen tres situaciones ideales de uso que **recomiendan la opción de paquetes de soluciones:**

* Un conjunto de aplicaciones bien integradas para una empresa relativamente pequeña que desea adoptar un paquete sin realizar cambios.  
* Una aplicación no fundamental para la actividad principal de la empresa, que tenga una interfaz bien definida y relativamente simple.  
* Una aplicación compleja que necesite de especialización técnica en un área donde la empresa no considere que puede obtener una ventaja competitiva importante.

**En la adquisición de paquetes, el esfuerzo y las aptitudes dejan de centrarse en el desarrollo del SW y pasan a enfocarse en la selección del paquete,** que lleva un ciclo de desarrollo bastante diferente que el del SW a medida. Además, como la mayoría de los paquetes se pueden adecuar, existen diferentes caminos a seguir, que también es preciso seleccionar. La identificación y la priorización de los requerimientos puede compararse con algo ya existente y el comprador tiene que localizar dónde están los desfasajes y decidir sobre un proceso para manejar la disparidad de capacidades. A continuación, se ilustran **estrategias para manejar la disparidad entre las necesidades de la empresa y las capacidades del paquete.**   
![][image27]

* **ADECUACIÓN DEL PAQUETE:** Genera conflictos primero legales, ya que perdemos las licencias y a su vez quien se hará cargo de implementar la modificación.(No es viable).  
* **MODIFICAR EL PROCESO EMPRESARIAL:** Tienen definido un mapa de proceso (Haciendo referencia a la práctica). Es una alternativa a evaluar.  
* **TOLERAR EL DESAJUSTE:** Dependiendo del nivel de desajuste, si son tolerables o no.  
* **COMPLEMENTAR EL PAQUETE CON FUNCIONALIDAD ADICIONAL**: del fabricante o de terceros

Existen cuatro enfoques diferentes para definir el **grado de libertad** que pueden tener las áreas empresariales al seleccionar los paquetes:

1\. ***Libertad total:*** este enfoque permite que todas las áreas empresariales elijan su paquete preferido y puede provocar el caos, donde nadie sabe qué comprar, cuáles son los costos de instalación, capacitación y soporte, ni tampoco los costos futuros, posiblemente enormes, que surgen de las oportunidades perdidas de integración. Sin embargo, cada área puede optar por un paquete que se adecue bien a sus requerimientos sin compromiso.

2\. ***Intercambio de datos**:* este enfoque permite que los sectores individuales adquieran el paquete que desean siempre que soporte el intercambio de datos con otros paquetes y sistemas, según sea necesario.

3\. ***Lista***: en este enfoque, algún área de la empresa dedicada a la definición de normas confecciona una lista breve de los paquetes aceptables; los sectores individuales sólo pueden optar sobre la base de esa lista.

4\. ***Normas fijas***. El área dedicada a la definición de normas establece el paquete permitido, y de ese modo los sectores individuales pueden optar por “cualquier color que deseen, siempre que sea negro”.

*Los dos primeros enfoques se refieren a un área de sistemas descentralizada, mientras que los últimos a áreas de sistemas centralizadas*

### Determinación del canal de provisión {#determinación-del-canal-de-provisión}

#### ***1\. Criterios para seleccionar canales de provisión de SW***

Los criterios listados deben considerarse en el proceso de decisión del canal de obtención de SW, esta consideración consiste en, determinar, para cada alternativa, en qué grado los criterios listados se cumplen, afectan, benefician, constituyen una ventaja o desventaja según la situación de la organización y la estrategia (según el impacto estratégico que representan). 

1. Costo  
2. Disponibilidad  
3. Mantenimiento  
4. Especificidad de la aplicación  
5. Modificaciones  
6. Documentación  
7. Utilización de recursos

#### ***2\. Análisis de alternativas de obtención de SW***

Una vez que se han determinado todas las alternativas (canales): 

1. Determinar un subconjunto de los criterios que serán la base de la evaluación  
2. Asignar pesos según la importancia relativa de cada criterio base  
3. Asignar puntajes para cada combinación alternativa/criterio sobre la base de la escala definida  
4. Multiplicar los puntajes por los pesos y se suman los resultados para cada alternativa  
5. La alternativa con el puntaje más alto satisfará mejor los requerimientos de usuario. Si se impone un mayor análisis (por ej. las dos alternativas poseen un puntaje muy próximo) **se puede recurrir a una segunda técnica**, análisis de las probabilidades de éxito y riesgo. 

#### ***3\. Análisis de probabilidad de éxito y riesgo***

Descartar aquellas opciones que tengan alta probabilidad de ocurrencia de un factor de alto impacto estratégico. El procedimiento es el siguiente:

1. Se determinan los factores de riesgo.  
2. A cada riesgo se le da una probabilidad de ocurrencia (alta/mediana/baja) y un puntaje similar por el impacto que tendrá en la organización  
3. Se obtienen los totales  
4. Se selecciona la alternativa de menor impacto o riesgo  
5. Se deben descartar aquellas opciones que tengan alta probabilidad de ocurrencia de un factor de riesgo con alto impacto. 

| Riesgos | Alternativas |  |  |  |
| ----- | :---: | :---: | :---: | :---: |
|  | Desarrollo interno |  | Desarrollo personal contratado |  |
|  | Probabilidad | Impacto | Probabilidad | Impacto |
| **Sobreutilización de recursos** | A | M | B | A |
| **Escaso apoyo para mantenimiento** | M | M | A | M |

### Concreción de la solución mediante la fuente seleccionada {#concreción-de-la-solución-mediante-la-fuente-seleccionada}

Se tienen en cuenta parámetros cuantitativos (se pueden medir) y cualitativos (responden a criterios profesionales sobre algo). Hay tres posibilidades:

* Adquisición  
* Desarrollo  
* Outsourcing

#### ***Adquisición*** {#adquisición}

* Rápida disponibilidad.  
* Procedimientos comerciales sólidos.  
* Calidad conocida y comparable.  
* Menores costos iníciales y generales.  
* Documentación verificable.  
* Actualización continua.  
* Soporte y capacitación variados.


Estos esfuerzos se centran en la adecuación de las funcionalidades y modos de operación del mismo a las de la organización (Costos adicionales al precio de compra) y eventualmente la conversión de datos. **El proceso principal será la selección del paquete**. Se analiza el plano de discrepancias.

**Etapas del proceso**

1. **Definición de la solución y elaboración del RDP** (también llamado pliego técnico), es un documento usado para solicitar ofertas competitivas para adquisiciones especiales.  
2. **Convocatoria de oferentes.**  
3. **Selección de la oferta** → Herramienta MEM, esta da un resultado que es numérico y representa el grado de adecuación de la propuesta a mis necesidades (RDP). Luego de esto se presenta generalmente a otras áreas (financieras).  
   1. Si no cumple las características obligatorias → afuera.  
   2. Luego analizo las deseables → ver cuánto mejor me lo ofrece.

Estoy tratando de buscar una aplicación que mejor cumpla con la intersección de requerimientos empresariales y funcionalidades del paquete.

4. **Instalación y prueba de aceptación** de la solución seleccionada.  
5. **Ejecución de los aspectos contractuale**s consecuentes de la etapa 4 (financieros, administrativos, legales).

#### ***Desarrollo*** {#desarrollo}

* **Control efectivo del proyecto** de desarrollo mediante una gestión del proyecto apropiada.  
* **Considerar al desarrollo de SW como un proceso de producción,** por lo tanto hay que definir criterios que hagan a la medición de productividad.  
* **El mayor costo** va a estar en el proceso de codificación.  
* **El análisis de ahorro de costos:** desarrollo interno presenta costos y tiempos importantes en el análisis, diseño, desarrollo y prueba. Sin embargo, es mejor con respecto a la especificidad, documentación y el mantenimiento.  
* Apropiado para cuando la necesidad empresarial consiste en **obtener ventaja competitiva**. → APLICACIONES ESTRATÉGICAS Y DE ALTO POTENCIAL DE LA CARTERA.  
* LA GRAN VENTAJA ES EL GRADO DE ADECUACIÓN POSIBLE  
* El mayor riesgo: debo tener un control efectivo del proyecto  
* Otro requisito importante, mi equipo de desarrollo interno \-debe tener las capacidades y habilidades necesarias.

#### ***Outsourcing***  {#outsourcing}

Consiste en transferir a terceros la responsabilidad de proporcionar un servicio adaptado a las necesidades de una organización.

**Se entiende por outsourcing la cesión, a una empresa externa, de la gestión de los SI de una organización.** Aglutina una combinación dinámica de actividades de gestión de SI y que puede ir desde la asistencia técnica en labores de operación de centro de proceso de datos, mantenimiento de equipos, etc. hasta el desarrollo y mantenimiento de aplicaciones, diseño de redes de comunicaciones, consultoría, etc.

⇒ Le transfiero a un tercero la responsabilidad que debería tener el área de sistemas, y el área de sistemas de la organización debe controlar ese servicio (con pautas contractuales y pautas de servicio bien detalladas). LO QUE NUNCA ES DEL TERCERO SON LOS DATOS Y LA INFORMACIÓN.

⇒ ***¿Qué servicios pueden estar incluidos en estos contratos de tercerización?***

* Transferencia de operaciones de management a gran escala    
* Transacciones rutinarias  
* Procesamiento de datos  
* Proyectos de desarrollo  
* Apoyo al usuario  
* Redes  
* Almacenamiento  
* Cualquier aspecto relacionado con la operación o management de los SI 

**Tipos:**  
Representan el grado de transferencia de la responsabilidad del MANAGEMENT DE LOS SI, van de menor a mayor responsabilidad respectivamente:

* **Proveedor de tiempo compartido**: proveen acceso en línea a una capacidad de procesamiento externa que generalmente se cobra según el tiempo utilizado. El espacio de almacenamiento requerido puede ser compartido o privado. Cloud storage, alquiler de capacidad de procesamiento para cálculos complejos, etc.

* **Agencia de servicios**: se cede una tarea completa a una empresa. Por ejemplo, soporte técnico, desarrollo y mantenimiento de aplicación, liquidación de haberes.

* **Management completo de servicios**: Todos los elementos de los SI permanecen dentro de la casa del cliente, pero el management (por ende la toma de decisiones) y la operación de dichos elementos es lo que se terceriza, es decir que el cumplimiento de esas funciones de management son responsabilidad del tercero contratado. Por ejemplo: Sistema de gestión tributaria de la Municipalidad de Resistencia. 

  * De los tres enfoques de contratos de servicios, es el que presenta más riesgo y quien exige mayor demanda sobre el contratado (es más probable que el proveedor experimente problemas, sobre todo porque los insumos siguen siendo propiedad del cliente o contratante). En este caso la empresa, el contratante, sólo retiene el management del contrato, y tal vez el management estratégico (define plan estratégico si/ti, define cartera de apps)

![][image28]

**Decidir la tercerización de los sistemas informáticos exige una profunda evaluación del qué, cómo, cuándo y con quien tercerizar.** Para esto la empresa debe tener en claro las aptitudes esenciales, la naturaleza de la empresa y la importancia empresarial del elemento de los SI. 

Una organización que apuesta a la innovación tecnológica debe disponer de recursos flexibles, procesos organizacionales orgánicos y fluidos y capacidades experimentales, atributos todos que la tercerización no garantiza.

![][image29]

Algunos **motivos** para tercerizar:

* Concentrarse en el negocio de la compañía  
* Los recursos libres para otros propósitos.  
* Disponer de tics actualizadas.  
* Acelera los beneficios de la reingeniería.  
* Riesgos compartidos.  
* Hace fondos a capitales disponibles.  
* La infusión constante.  
* Reduce y controla los costos operacionales.  
* La difícil tarea de administrar los SI/TI (fuera de control)

**Riesgos** de tercerizar:

* Mantener los niveles de servicio: controlar los servicios que se contrató.  
* Plazo contractual inadecuado. Dificultad para separar funciones de servicios.  
* Dificultad para proteger los derechos de SW.  
* Pérdidas del copyright del SW propio ejecutado por el proveedor.  
* Pérdidas del copyright del SW desarrollado por el proveedor para la contratista.  
* Habilidades tecnológicas obsoletas (capacidades del personal interno original pérdidas)  
* Dificultad para cambiar el proveedor.  
* Costos ocultos

La salida de esta etapa es la solución definitiva.

***Relacionando con la cartera de aplicaciones*** → las aplicaciones de tipo estratégico y alto potencial de la cartera deberían ser las que más usen el desarrollo interno, mientras que las clave para las operaciones y las de apoyo son las más propensas a beneficiarse del outsourcing o adquisición.

**¿Qué factores deben tenerse en cuenta para el outsourcing?.** 

* **Capacidad del management:** las distintas rutas de adquisición requieren diferentes aptitudes de management. Los estilos, la cultura y la idoneidad del management de la empresa forman la base para la adecuación de cualquier ruta.  
* **Capacidad del personal:** es probable que la escasez de aptitudes técnicas, de visión comercial, de management de proyectos o de negociación de contratos limite significativamente las alternativas, al igual que el grado de compromiso del personal.  
* **Posición a largo plazo:** deben considerarse las posibles consecuencias de la transferencia a largo plazo del management, del personal y de los recursos, que al otorgar valor agregado de especialización, favorece a la empresa externa.  
* **Costos convenientes**: compartir los costos para beneficio de ambas partes puede compensar el conflicto inherente de intereses en la relación cliente/proveedor.  
* **Generalidades:** el grado de generalidad de los requerimientos debe afectar significativamente la decisión.

**Los costos de los SI relacionados con la provisión externa son menores que los generados por los desarrollos internos?** 

Normalmente, los contratantes descubren que l**os costos de tercerización son más elevados de lo que esperaban** *(Fuente: estudio de 1994 dice que solo el 57% de contratos con terceros perciben un ahorro real).* Los costos iniciales que se definen, a lo largo de la prestación del servicio pueden ir cambiando, y el contratante termina pagando más. También, si la tercerización incluye trabajo de desarrollo, esta incluye los [costes de personal,](https://docs.google.com/document/d/1WYvXYmw1cM3d8N8IJ9fMtDY1Txxq5-6mkgo2Pufqv8w/edit#heading=h.h1svywz1gln1) que pueden ir fluctuando (por ejemplo aumento en índices de rotación dispara costos no esperados) ⇒ Debo reestructurar los contratos de tercerización, incluir costos a largo plazo.

**¿Qué otros riesgos o costos ocultos se presentan?** Muchos contratos pueden ser poco flexibles, tener cláusulas punitivas, donde en el caso de que el servicio no  brinde los beneficios esperados, el contratante deberá pagar por rescindir el contrato. Donde no solo se percibe el costo punitorio, sino también el desaprovechamiento de las ventajas, y por ende de la inversión, de los SI/TI al no ser implementados de la manera esperada y no poder cambiarlo fácilmente (también mencionado en riesgos de tercerizar).

### Método de evaluación de paquetes estándar {#método-de-evaluación-de-paquetes-estándar}

Si del proceso de decisión sobre el canal de provisión de SW, se define que la alternativa es la adquisición de un paquete estándar, el proceso tiene una segunda etapa que es la decisión sobre cuál de las ofertas de paquetes disponibles en mercado se adecue mejor a las necesidades de la organización. 

#### ***Criterios de selección de paquetes estándares de SW*** {#criterios-de-selección-de-paquetes-estándares-de-sw}

Se establece un conjunto de criterios que permitan ser ajustados en función a las expectativas deseadas de los paquetes a evaluar, que pudieran reflejar potenciales particulares, y que sirvan al mismo tiempo de elementos de evaluación. 

1. **Funcionalidad**: Aspectos operativos. Si el paquete cubre todos los procesos que debería realizar. 

2. **Capacidad**: Si el paquete cubre aspectos de administración de datos, en cuanto a tamaño y cantidades, transacciones.

3. **Flexibilidad**: ¿Se pueden cambiar fácilmente el formato de las transacciones y de los informes? ¿La disposición de las pantallas pueden cambiarse fácilmente? ¿Es difícil agregar nuevos cálculos o pasos de procesamiento? ¿Pueden adaptarse los programas a nuevas aplicaciones?

4. **Uso**: Se refiere a aspectos de facilidad de uso, interfaz amigable, nivel de conocimientos, etc.)

5. **Confiabilidad**: Que el paquete falle lo menos posible (MTBF) y que se pueda recuperar rápidamente de caídas.

6. **Seguridad**: Se refiere a aspectos de restricciones de acceso y resguardo de la información

7. **Performance**: Se refiere al nivel de respuesta del paquete, dependiendo de una carga de trabajo representativa. Siempre está en conflicto con el criterio de capacidad.

8. **Mantenimiento**

9. **Propiedad**: Se refiere a los tipos de licencia y derechos que tendrá sobre el producto (licencia de uso, licencia de propiedad, copyright del producto y/o documentación, etc.). 

10. **Minimización de costos operativos y de mantenimiento**

11. **Minimización de costos de compra e instalación**

#### ***Técnica de evaluación*** {#técnica-de-evaluación}

Una vez establecidos los criterios, se puede efectuar una comparación de los paquetes de SW propuestos. Debido a que no todos los criterios pueden ser representativos, es importante establecer solamente **un mínimo de criterios que respondan a necesidades reales,** a través de una “pre ponderación” de los mismos en función al nivel de necesidad de la empresa, permitiendo eliminar criterios que carecen de representatividad para el escenario en particular, y disminuyendo la complejidad del proceso de evaluación *(dejar de lado aquellos que estén debajo de un nivel de corte preestablecido con anterioridad)*. 

![][image30]

Finalizada esta primera selección, es posible pasar a un segundo proceso llamado **evaluación técnica**, solo en **el caso en que los valores obtenidos por oferentes se encuentren muy cercanos entre sí** (se establece una lista de componentes, elementos, características y subcaracterísticas referidos a aspectos técnicos del paquete a seleccionar). Se pasa ahora a un nuevo análisis **para detectar cuál de ellos es el más óptimo**, tomando como referencias sus capacidades técnicas.  Se puede proceder a una técnica para evaluar ofertas denominada **Método de Evaluación Manual (MEM)**

## **Proceso de adquisición de Hardware** {#proceso-de-adquisición-de-hardware}

Al analizar la adquisición de hardware, se presentan básicamente dos temas principales: la fuente de suministro y la índole de las *plataformas.* En la figura siguiente se describen someramente las diferentes fuentes de adquisición de HW.

| Mainframe | Computadoras de alto rendimiento con grandes cantidades de memoria y procesadores que procesan miles de millones de cálculos y transacciones simples en tiempo real.  Más orientado al upsizing (centralizado) | \- Fabricante \- Terceros especializados | Se pueden adquirir HW de cualquier tipo en el mercado de segunda mano |
| :---- | :---- | :---- | :---: |
| **Minicomputadora** | Tipo de computadora multiusuario que está comprendida en un rango medio de tamaño (no es una computadora muy pequeña, como sugiere el nombre.) Sistema informático económico en comparación con el mainframe y la baja necesidad de mantenimiento | \- Fabricante \- Revendedores de valor agregado (VARs) |  |
| **Microcomputadoras** | Es una computadora pequeña con un microprocesador.  Más orientado al downsizing | \- Equipos de ventas “tradicionales” del fabricante \- Revendedores de valor agregado \- Comercios minoristas \- Supermercados de computadoras \- Compra por correo \- Ensamblaje de componentes realizado en la empresa |  |

### Canales de adquisición {#canales-de-adquisición}

Con la pequeña excepción del ensamblaje de microcomputadoras, **todo el HW se adquiere de forma externa;** el **tamaño** de la plataforma define principalmente el alcance y la índole de los canales de adquisición de HW.

* **Consignatarios de fabricantes:** si el cliente es muy importante, es posible que se presente la opción de comprar directamente al fabricante. El equipo de ventas, gracias a sus conocimientos técnicos, diseña a medida soluciones muy específicas además de ofrecer un mantenimiento intensivo y la seguridad de contar con piezas de repuesto. La desventaja es que suelen tener un gasto mayor y una orientación más restringida la falta de soporte de integración con otros vendedores.  
* **Revendedores de valor agregado** (VARs): generalmente están preparados para vender y apoyar una amplia gama de productos. Los VARs agregan un margen al costo básico del software para cubrir su provisión de “servicios” (por ejemplo: instalación y mantenimiento).  
* **Comercios minoristas:** dado que las microcomputadoras ya son un artículo de uso cotidiano, se venden de la misma forma que otros bienes de consumo. Si bien los comercios minoristas brindan asesoramiento muy limitado, normalmente ofrecen poca variedad, y siempre dentro de la línea de uso generalizado.  
* **Supermercados de computadoras:** como ocurre con los comercios minoristas, no suelen estar orientados a las grandes empresas, pero buscan ofrecer el rango de opciones del canal directo junto con un servicio personal, además de permitir ver los productos antes de comprar. Sólo las empresas más grandes excluyen las compras mediante este canal.  
* **Compra por correo:** tiene como competidores a los supermercados de computadoras y a los comercios minoristas. Las agencias y los VARs de los fabricantes ofrecen un tipo de servicio tan diferente que pueden considerarse como canales complementarios.  
* **Ensamble de componentes por parte del personal:** algunas compañías compran componentes tales como motherboards, monitores, disqueteras, etc., que luego ensambla el personal de la empresa. La brusca reducción en los precios de hardware hace que este canal de adquisición no sea muy usado, excepto cuando se requieren configuraciones muy específicas o especiales.

### Índole de la plataforma {#índole-de-la-plataforma}

El segundo aspecto clave en la selección de hardware es la escala de la plataforma del hardware. **Durante la provisión de HW queremos alcanzar el rightsizing**

* **Rightsizing:** elección de la plataforma más adecuada  
* **Downsizing.** Tendencia hacia el uso de plataformas de procesamiento más pequeñas (mejor para sistemas distribuidos).  
* **Upsizing:** integración de aplicaciones. y ordenadores aislados en entornos de red, de forma que se permita el compartimiento de datos (mejor para sistemas centralizados, justificado desde el punto de vista de integridad, complejidad y accesibilidad de los datos).

**Cuestiones a tener en cuenta:**

* Aspectos financieros.  
* Grado de adecuación entre la estructura empresarial y la ubicación.  
* Gestión de la seguridad.  
* Confiabilidad y disponibilidad de los datos.  
* Volumen de los datos a procesar y almacenar, y la escala de procesamiento.  
* Políticas del SW: sistemas abiertos.  
* Estabilidad del procesamiento de la información (ritmo de implementación de las migraciones).

#### ***Downsizing*** {#downsizing}

El **downsizing** es la etapa actual de una tendencia a muy largo plazo que consiste en desarrollar bases de hardware para sistemas de software más pequeños y por lo tanto más distribuibles. Es muy probable que la opción de distribuir el poder de procesamiento representado por el downsizing esté motivada por una autonomía mayor del usuario causada por la computación controlada por el usuario (U-CC), y a su vez, la mayor flexibilidad ofrecida por las aplicaciones de PCS en red sobre los sistemas mainframe estimule el crecimiento de la computación de usuario final. Esta tendencia llega hasta tal punto que los nuevos desarrollos tienen tanta posibilidad de estar basados en plataformas desktop como de hacerlo en arquitecturas de mainframe o de mediano rango.

La expresión downsizing implica la migración de un sistema o de un conjunto de sistemas desde un mainframe o minicomputadora a una red de PC o minicomputadoras. Sin embargo, a las aplicaciones nuevas y basadas en plataformas pequeñas también se les da este nombre (es decir que vocablo incluye un grado importante de distribución y procesamiento de red). 

El downsizing se puede aplicar en todas las áreas empresariales y de sistemas. Lo que motiva el downsizing es el aumento en el valor percibido de los entornos más pequeños. El downsizing requiere de equipos del mercado masivo y no de grandes máquinas. Sin embargo, el costo no siempre es la mayor motivación, se considera que el downsizing permite que el personal tenga más espacio para manejarse, lo que resulta ventajoso para la empresa.

Usualmente se considera que sus ventajas más importantes son el potencial ahorro de costos y el incremento en los controles del usuario. Por lo general, cuanto mayor es la escala de hardware, mayormente son los costos asociados, en especial los gastos operativos. De la misma forma, una de las mayores críticas que ha recibido el downsizing han sido en base a la realidad de ese ahorro de costos, ya que existen muchos costos ocultos que no se suelen tener en consideración. Estos costos subestimados presentan dos aspectos: el costo operativo real y el costo de migración. En realidad, se pudo determinar que a pesar de los costos ocultos y subestimados del downsizing, aún habrá un rendimiento que supera de dos a cinco veces la inversión total.  

| Posibles ventajas | Posibles desventajas |
| :---- | :---- |
| Mayor control y autonomía del usuario Mayor flexibilidad Costos descentralizados Menores costos Mayor capacidad de respuesta Incentivo de los sistemas adquiridos Reducción del volumen de trabajo de los SI Incentivo de la innovación Facilidad y rapidez de integración Capacidad de respuesta empresarial Orientación hacia los sistemas abiertos Desarrollo más rápido de los sistemas | Control central más débil Costos ocultos Mayor demanda de idoneidad del usuario Incremento en el volumen de trabajo de usuario Mayor inversión de capital inicial Resistencia del personal Falta de aptitudes Desintegración de la base de datos Desalienta una mentalidad más amplia Fragmentación de la dirección estratégica Ruptura con la empresa Complejidad técnica |

#### ***Rightsizing*** {#rightsizing}

El **rightsizing** es el proceso de elegir la arquitectura de SI más adecuada. Aun dada la resolución del debate sobre el ahorro de costos potenciales del downsizing, todavía existen casos en los que la decisión que se toma consiste en seguir con la plataforma de hardware existente e incluso extenderla. Actualmente existe una gama de alternativas de hardware de procesamiento, y las ventajas y desventajas de cada una para cada caso particular constituyen una forma de tomar la decisión de rightsizing motivada por la empresa. 

La controversia entre el procesamiento centralizado y el procesamiento distribuido está ligada a la **ubicación** de los recursos de SI. Este debate debe ser resuelto antes del downsizing, pues junto con una mayor distribución del **procesamiento** se produce una mayor distribución de los **datos**.

Cabe recordar que el desarrollo de nuevas aplicaciones en hardware de pequeña escala no necesariamente hace que las aplicaciones existentes sean obsoletas, y que el rightsizing **no es** solo decidir si es adecuado migrar de un mainframe a una red de PC. 

### Layout del HW {#layout-del-hw}

Un layout es un esquema de distribución de los elementos, utilizado como boceto de diseño.

En el caso de los recursos de SI/TI, **se utiliza para tener “un plano”** de la disposición de las estaciones de trabajo, impresoras, servidores, routers, medios de comunicación, etc. y sus cantidades de acuerdo con:

* **La índole de la plataforma elegida**: downsizing, upsizing.  
* **La extensión geográfica de la red**: LAN, MAN, WAN.  
* **La topología de red elegida:** Bus, Anillo, Estrella.

### Determinación del Volumen de Datos a Procesar y Almacenar {#determinación-del-volumen-de-datos-a-procesar-y-almacenar}

En la adquisición de hardware HW es necesario analizar la *fuente de suministro* y *la índole de las plataformas.* Se debe definir previamente el volumen de datos a procesar y almacenar; y las operaciones de entrada/salida que el HW a adquirir deberá soportar.

**1\. Consideraciones previas**  
Para poder realizar las estimaciones requeridas, primero es necesario diseñar la estructura de datos que el sistema necesitaría manejar (tablas; campos por tabla, tipo y tamaño de cada uno; cantidad de registros y tamaño aproximado de c/u; frecuencia de uso y/o actualización)

Esto ayudaría a tener una primera idea del volumen de datos actual, o sea que se necesitan manejar hoy. Por lo tanto, luego se deberá estimar cuál sería el volumen futuro de datos.

Pautas y convenciones para considerar:

* Tener bien definidas las dimensiones operativas de la organización: cantidad de transacciones, frecuencia de cada operación, etc.  
* En base a los antecedentes históricos, estimar el crecimiento que tendrá la organización, en término de sus dimensiones operativas.  
* De acuerdo al crecimiento estimado para una tabla, también deberán crecer en forma proporcional las tablas con datos relacionados.

Estos cálculos permiten determinar volúmenes o cantidades “potenciales”, para casos de máxima exigencia.

**2\. Cálculo de Espacio en Disco**  
Para realizar el cálculo de espacio en disco, otras de las cuestiones a definir previamente es el crecimiento que tendrá el volumen de información a almacenar.

Analizando la operatoria de la organización y sus antecedentes históricos (en cuanto a volumen de transacciones) se podrá determinar cuál es el índice (porcentaje) de crecimiento anual que tiene cada uno de los datos con los que trabaja.

Luego de determinar el índice de crecimiento para cada archivo/tabla de datos, se deben determinar los **criterios de almacenamiento** a utilizar para cada uno, los que incluyen:

* **Crecimiento Acumulativo**: Se refiere a aquel que se calcula teniendo en cuenta que, si bien el índice de crecimiento anual es igual para cada año, el mismo debe ser aplicado al volumen de datos que se tendría cada año, ya que éste se va incrementando año a año según el índice definido.

La forma de calcular el volumen de transacciones para un período de N años, con un índice de crecimiento acumulativo de X %, sería la siguiente:  
**Transacciones en N años** \= Transacciones Actuales x (1 \+ X/100)N 

* **Resguardo de información del año anterior**: Este criterio hace referencia a determinar la necesidad de ir armando un “histórico” de transacciones, lo cual generalmente resulta muy conveniente para los archivos de datos que crecen periódicamente y de manera constante, y cuyos registros por lo general no serán eliminados, ya que es importante poder disponer siempre de cada uno de los registros de esta información, como lo son los archivos de registro de cuotas y facturaciones, por ejemplo. Por lo tanto, al calcular su crecimiento se deberá tener presente que se requiere un tratamiento especial, diferente al simple crecimiento acumulativo.

La forma de calcular el volumen de transacciones para un período de N años, con un índice de crecimiento anual acumulativo de X %, con resguardo de la información anterior, sería la siguiente:

**Transacciones en N años \=** S \[Transacciones Actuales x (1 \+ X/100)N\] \=Transacciones Actuales x S (1 \+ X/100)N .

* Otra cuestión a considerar es que los índices de crecimiento se deben estimar y justificar adecuadamente, basándose en la recolección de diferentes datos.

* Finalmente, como los datos son sólo uno de los elementos que se deben almacenar, para calcular el espacio total de almacenamiento, al espacio requerido por los datos se le debe sumar el espacio requerido para almacenar los otros elementos (índices, software de aplicaciones, sw de sistema, necesidades no previstas).

### Cálculo de Cantidad de Terminales {#cálculo-de-cantidad-de-terminales}

Para poder determinar cuántas terminales se requieren para procesar la información, se deben tener en cuenta las siguientes convenciones y supuestos:

* **Velocidad de tipeo de un Operador:** Existe un estándar de 3 caracteres/segundo x terminal

* **Cantidad de Caracteres a tipear por Jornada**: Según estudios realizados por expertos, se ha llegado a la conclusión de que sólo el 75% del tiempo de una jornada laboral son de tipeo neto.

Entonces, considerando una jornada laboral de 6 hs. diarias, sólo 4 hs. serán de tipeo neto. Luego:  
1 h. 3.600 seg.  
4 hs. 14.400 seg. de tipeo neto por jornada.  
1 seg. 3 car.  
14.400 seg. 43.200 car. Se pueden tipear en 1 jornada laboral x terminal.

* **Cantidad de Jornadas Laborales en 5 años**: Considerando una semana laboral de 5 días, y que el año tiene 52 semanas, tenemos que en 1 año podemos tener 260 días hábiles. Luego, en 5 años hay 1.300 días hábiles,

* **Cantidad de Transacciones por día**: Se obtiene dividiendo las “Transacciones a 5 años” calculadas **anteriormente**, por la cantidad de jornadas laborales en 5 años.

* Otro aspecto a considerar es que el cálculo de terminales debe hacerse por cada área o sector de la Organización, a fin de poder determinar la cantidad de terminales que cada una requiere.

Una vez definidas las áreas que requerirán de terminales, para cada una deberá determinarse con qué datos (archivos o tablas) necesita trabajar, cuál es el volumen de transacciones sobre cada uno, y cuántos caracteres deberá tipear por cada uno de esos archivos.

Finalmente, luego de haber calculado la cantidad de terminales que cada área requerirá para el procesamiento de la información, es importante tener en cuenta además aquellas terminales que se podrían asignar por razones de política administrativa de la empresa (por ejemplo: para los niveles jerárquicos, para un sistema especial, turnos de trabajo y cantidad de personal en cada turno, seguridad en el acceso a usuarios, relación entre la cantidad de usuarios/puesto de trabajo, etc.).

Por lo tanto, luego de realizar estos cálculos por cada área, se podrá obtener el **total de terminales que se necesitan en toda la Organización**.

### Cálculo de Cantidad de Impresoras y Picos de Impresión {#cálculo-de-cantidad-de-impresoras-y-picos-de-impresión}

Para poder determinar cuántas impresoras se requieren en una Organización, es necesario que previamente se realice una descripción detallada de las salidas impresas que se requieren, como informes, boletas de pago, etc. (mejor aún si se acompaña con un diseño), clasificadas según el sector que las debe generar, su periodicidad, calidad y cantidad de copias.

Una vez detallada cada salida impresa se debe realizar el conteo de caracteres, a fin de determinar la cantidad máxima de caracteres que incluiría cada impresión de la misma.

Luego, considerando que cada página impresa en tamaño A4 puede tener 80 columnas y 66 líneas (como máximo), se tendría que: **1 página \= 80 x 66 \= 5280 car. (Como máximo)**. Entonces, en base a esto se debe calcular cuántas páginas tendría cada copia.

Luego, en función a los requerimientos de impresión de la organización, en cuanto a calidad, volumen y velocidad de impresión –definidos como parámetros cuantitativos y cualitativos–, y a lo que el mercado ofrece, se deberá determinar la tecnología de impresión a utilizar para cada salida impresa.

Luego, partiendo de la convención de que **cada impresora tiene una capacidad neta de impresión (**nos referimos a que se descuentan los tiempos “muertos” que se pierden en: tomar y sacar cada hoja, comunicación entre ordenador e impresora, solucionar problemas de atascamiento de papel, cargar más papel cuando la impresora se queda sin él, etc.)  **de 60 minutos por jornada laboral (6 hs.),** se debe calcular cuántas impresoras se necesitarán para soportar los requerimientos de impresión de cada sector.

Finalmente, por cada tipo de impresora se debe planificar su carga de trabajo para todo el mes (siempre que sea posible) y luego analizar los picos de impresión que tendría cada una en cada sector.

Luego de analizar todos los aspectos indicados, para calcular la cantidad definitiva de impresoras para un sector hay que tener en cuenta también las impresoras que la organización asigna por cuestiones de política administrativa.

## 

## **Método de Evaluación Manual (MEM)** {#método-de-evaluación-manual-(mem)}

El **M**étodo de **E**valuación **M**anual (MEM) se aplica en forma común para evaluar **técnicamente** ofertas de HW y de paquetes de SW.

Los elementos que se deben generar a fin de poder llegar a materializar el sistema de la aplicación del método de evaluación manual son 7:

1. Lista de requerimientos  
2. Tabla de ponderación  
3. Cuestionario  
4. Planilla comparativa  
5. Planilla de evaluación  
6. Planilla de resultados  
7. Informe final

**1- Lista de Requerimientos**  
Una vez realizada la detección de las necesidades, y la determinación de los requerimientos específicos **(parámetros cualitativos y cuantitativos)** se hace necesario formalizar en cuanto a la elaboración de una lista que refleje el conjunto de dispositivos de hardware y software necesarios para la implementación. 

Si el canal de obtención de SW es la adquisición de un paquete estándar, debido a la gran cantidad y diversidad de ofertas que pueden llegar a presentarse en el proceso de adquisición, se hace necesario establecer una estructura que permita agrupar los requisitos del SW en distintos niveles de la siguiente manera:

1 – Componente 1 – SW....  
1.1 – Facilidad 1  
1.2 – Facilidad 2  
1.2.1 – Característica 1  
1.2.2 – Característica 2  
1.2.2.1 – Sub-característica 1  
1.2.2.2 – Sub-característica 2  
1.2.2.3 – Sub-característica 3

2 – Componente 2 – HW  
2.1 – Elemento 1  
2.2.1 – Característica 1  
2.2.1.1 – Sub-característica 1  
2.2.1.2 – Sub-característica 2  
2.2.1.3 – Sub-característica 3  
2.2.2 – Característica 2  
2.2 – Elemento 2

**2- Tabla de Ponderación**  
Una vez determinados los parámetros se debe efectuar la respectiva ponderación de los mismos. Sobre la base de la lista de requerimientos, se debe determinar la importancia relativa que tiene cada requerimiento con respecto a los demás, y en función de esta diferencia se los pondera. La ponderación entonces deberá ser establecida sólo al último nivel de la lista de requerimiento, sea esta una característica o sub-característica.

El envío de la tabla de ponderación al proveedor, le permite esmerarse en la definición del paquete a ofertar teniendo en cuenta las facilidades de software que tengan mayor peso.

**3- Cuestionario**  
Consiste en una planilla que contiene en su primera columna la descripción de cada requisito de SW solicitado en la lista de requerimientos. En esta, se procede a asentar a cada característica y sub-característica de la lista de requerimientos indicando las unidades y/o valores posibles para cada característica y sub-característica. Por ej.: “Mbps” o “Sí/No” o “GHz”, etc. 

En una segunda columna el nivel de obligatoriedad de cada característica y sub-característica. Los posibles niveles de obligatoriedad son:

1. Sistema de prioridades Obligatorio (O), Altamente Deseable (AD), Deseables (D)  
2. Sistema de prioridades Imprescindibles (I), Recomendables (R), Convenientes (C)

Cada una de ellas con una connotación distinta dentro del proceso de evaluación.

La confección de Cuestionarios obliga a que el proveedor plantee su oferta lo más objetiva y acotada posible, en función a las necesidades planteadas.

![][image31]

**4- Planilla Comparativa**  
Sobre la base del cuestionario, y luego de haber recibido las respuestas de los oferentes (ofertas), se elabora una planilla comparativa por cada oferta y para cada facilidad. Es decir, la primera columna es la lista de requerimientos, la segunda el cuestionario, y cada una de las columnas siguientes representan a las ofertas. 

Esta planilla se completa volcando lo que cada oferta propone para cada característica y sub- característica. La utilidad de esta planilla es sumamente importante pues se usa para descartar aquellas ofertas que no cumplen con los requisitos fundamentales, y evitar que prosigan en la etapa de evaluación.

![][image32]

**5- Planilla de evaluación**  
Se debe confeccionar una planilla de evaluación por cada facilidad de SW que se identifique en la lista de requerimientos que se confecciona. Es necesario confeccionar estas Planillas de Evaluación tratando de lograr **OBJETIVIDAD en las calificaciones.**

Cada componente o facilidad no puede ser calificado en forma directa. Para que la calificación que reciban tenga cierta objetividad, se deben dividir a estos en partes que sí se puedan calificar en forma directa y con objetividad.

**Valor Ponderado:** Es el valor obtenido de multiplicar el peso de una sub-característica por el peso de la característica respectiva. Si no hay sub-características, el valor ponderado es igual al cuadrado del peso de la característica.

**Calificación:** Nota asignada a una característica /sub-característica, en función al análisis de las ofertas del Cuestionario.

**Calificación Ponderada:** Valor que surge de multiplicar la nota de una sub-característica por su correspondiente valor ponderado.

La calificación ponderada a nivel de característica será:

* La suma de las calificaciones ponderadas de las subcaracterísticas, o bien  
* El producto del valor ponderado de la característica por la nota respectiva (si no está desagregada en sub-características)

**6- Planilla de resultados**  
La planilla de resultados deberá reflejar la integración de todas las planillas de evaluación, al nivel de facilidad. El que tenga mejor puntaje, será la oferta más viable.

Sumando en la planilla de evaluación el puntaje de cada facilidad, se obtiene un subtotal. Estos subtotales se suman en otra planilla obteniéndose el resultado final. Cuando se agotan todas las facilidades de SW se hace un subtotal para ese componente. Es decir, se tendrá una planilla de resultado que integre los resultados parciales de las facilidades del componente SW.

**7- Informe Final**  
Permite reflejar la recomendación técnica final que surja del análisis de todo el proceso de evaluación y sus correspondientes resultados, ordenándolos por Puntaje final obtenido y el nombre del proveedor. A esto último se le conoce como **Orden de Mérito.**

Es importante su confección ya que seguramente estos resultados serán tomados por otros equipos que continuarán aplicando evaluaciones orientadas a otros aspectos, como por ejemplo el Económico.

Algunos equipos de evaluación técnica, suelen establecer antes del proceso un valor denominado nivel de corte, que permita excluir a aquellos proveedores que hubieran obtenido puntuaciones finales por debajo de esta franja.

## **Alternativas para el pago de las adquisiciones** {#alternativas-para-el-pago-de-las-adquisiciones}

Una vez elegida una alternativa determinada, y suponiendo que se adquiera fuera de la empresa, debe establecerse el método de financiación adecuado.

### Compra definitiva  {#compra-definitiva}

Es conveniente cuando se adquiere un elemento particular de los IS para utilizarlo en forma permanente. Los costosos gastos iniciales se compensan con la libertad de disponer de la propiedad. La compra definitiva también transfiere todos los costos y riesgos de la propiedad: junto con el elemento de SI se "compra" la responsabilidad del mantenimiento y el seguro, y todos los riesgos de que se torne obsoleto.

A pesar de los problemas contables y de capital, éste es el método más simple de pago cuando los elementos de IS están relacionados con un alto grado de seguridad de que se van a cumplir todos los criterios de selección.

### Compra “temporaria” {#compra-“temporaria”}

Los costos relacionados con las compras temporarias por lo general son más flexibles que los de la compra definitiva, pues la empresa sólo tiene que hacer un desembolso inicial pequeño, y los pagos de alquiler o de concesión son totalmente deducibles de impuestos. Sin embargo, la mayoría de las compras temporarias son de duración fija, y existen altas multas por rescindir el contrato antes de tiempo.

El vendedor, que sigue siendo el propietario, retiene casi todo el riesgo de propiedad, pero el alcance real de lo que se retiene o se transfiere depende de la variedad de la compra temporaria.

Existen tres variedades de compra temporaria: *leasing* simple u operativo, *leasing* con derecho a compra, y alquiler, cada una con distintas ventajas.

#### ***Leasing simple u operativo***

El elemento de IS se financia en base a un contrato que dura tres, cuatro o cinco años, con o sin pagos importantes por adelantado. En el *leasing* simple u operativo el vendedor conserva la propiedad del elemento de IS, sea hardware o software, después de finalizado el contrato, y en este sentido es muy similar al alquiler, con excepción de la duración del contrato.

**Motivaciones claras para el *leasing:***

* Es barato y requiere menos habilidades internas que la compra para recuperar los valores residuales.  
* Es flexible y, por lo tanto, responde al cambio y a la necesidad de actualizaciones.  
* Es conveniente en relación al IVA, y, por consiguiente, para las compañías del sector financiero.  
* Libera fondos de capital para utilización en otras áreas.

El *leasing* principalmente se aplica a los elementos de hardware, y por lo general el costo justifica el esfuerzo de gestionarlo. Sin embargo, el *leasing* de software crece en dos direcciones: el *leasing* de software en sí y los permisos de acuerdos de licencia para cubrir el software del hardware en *leasing* o en alquiler.

#### ***Leasing con derecho a compra***

Este tipo de concesión también se denomina concesión financiada, dado que es una forma de financiar en cuotas la eventual compra de un elemento de IS. Mediante este tipo de financiación, el que recibe el *leasing* tiene *derecho* de propiedad al finalizar el contrato.

El monto de la cuota generalmente se compone del precio de concesión simple, más un interés establecido, más un margen de ganancia, de modo que el *leasing* financiado es algo más caro que el simple; no obstante, permite que la empresa cuente con el valor residual del equipo, lo que compensa el mayor costo. Pero lo que puede ser de mayor importancia para las empresas es que este tipo de concesión puede otorgar el *derecho* de propiedad al finalizar el contrato; ese derecho hace posible que se pueda modificar el equipo de IS.

El *leasing* se aplica principalmente a los elementos de hardware. Sin embargo, como el software se está convirtiendo en un elemento de IS de alto costo, está incrementándose cada vez más el *leasing* de software, sobre todo en dos áreas: el *leasing* del software en sí y los permisos de acuerdos de licencia para cubrir el software instalado en el hardware en *leasing* o alquiler. La dificultad con el software es que prácticamente carece de valor residual en el momento de finalización del contrato.

#### ***Alquiler***

Alquilar elementos de IS implica hacer acuerdos de adquisición temporal a corto plazo. Esta opción generalmente es la más cara de todas las alternativas de financiación; los plazos de alquiler pueden ser tan breves como un mes, si bien la duración más común del contrato es de tres meses. Cuanto más corto es el período de alquiler, más caro resulta con respecto a su precio de compra, pues los *pagos* se calculan en base a la *flexibilidad* permitida.

Los acuerdos de alquiler ofrecen las mismas ventajas impositivas que el *leasing,* pues son completamente deducibles de impuestos.

El alquiler es una opción útil para cubrir los picos de demanda y para probar las posibles configuraciones antes de encarar una concesión simple o con derecho a compra.

La principal desventaja de los contratos de alquiler son los altos costos generales y las limitaciones específicas de uso. Otro inconveniente relacionado con el alquiler del hardware es la licencia del software: cuando el contrato es a corto plazo, de unos tres meses**,** el costo *real* del alquiler se incrementa exageradamente si se compra software, debido a las obligaciones que exige la ley con respecto a la licencia.

Al optar entre las alternativas de adquisición, es preciso considerar los riesgos inherentes vinculados a tres factores:

* Flexibilidad: respuesta al cambio empresarial  
* Obsolescencia: respuesta al cambio tecnológico  
* Costos: costos de la disponibilidad del capital

Cuando hablamos de flexibilidad nos referimos a flexibilidad de:

* Almacenamiento  
* Procesamiento  
* Formatos de datos

Es muy importante además el riesgo de que el elemento se torne obsoleto. Esto hace que el *leasing* y el alquiler sean opciones convenientes debido al alto riesgo de que la tecnología que se adquiere en forma definitiva se vuelva obsoleta.

## **Requerimiento de propuestas (RPD)** {#requerimiento-de-propuestas-(rpd)}

**Consideraciones previas**  
Dentro de la primera etapa de un proceso de compra de SW y HW (Estudio de solución y determinación de los criterios) se deben efectuar el estudio de factibilidad de la solución y definir las necesidades de tecnología de SI. Así se debe:

* **Eliminar sistemas inconvenientes:** eliminar sistemas inadecuados, concentrando el esfuerzo en aquellos que se consideren aceptables.  
* **Estimar los costos de procesamiento de datos:** un cálculo de capital y de costos de ejecución de procesamiento de datos.   
* **Justificar el sistema:** Debe realizarse el análisis de la cartera de aplicaciones y las estrategias genéricas. Así también se deben indicar las razones económicas para las soluciones. Análisis de costos/beneficios). Es decir, deben estar justificadas y factibles  
* **Desarrollar el sistema en forma realista:** El RDP debe ser realista en el sentido de que se tendrá en cuenta el potencial real tanto del equipo como de la tecnología disponible.  
* **Advertir a los proveedores potenciales:** es conveniente dar aviso previo a los posibles oferentes, a fin de que cuenten con tiempo para preparar ofertas serias. Esto suele implementarse a través de la denominada “Carta de Invitación”.

**Encuesta de mercado informal**  
Se realizará luego de ser conocida la necesidad de un nuevo sistema.

Tal encuesta ayudará también a refinar las consideraciones cualitativas y cuantitativas inherentes a la obtención del nuevo sistema. Sólo después de efectuada esta encuesta pueden armonizarse eficiente e inteligentemente las necesidades del comprador con los sistemas disponibles. La encuesta ahorrará tiempo futuro, y debe comprender las siguientes actividades:

* Obtención de copias de otros RDP's: De organizaciones similares  
* Visita a otros gerentes de procesamiento de datos (PD)  
* Uso de organizaciones profesionales: Asociarse a las organizaciones profesionales permite compartir conocimientos técnicos y profesionales, así como contactarse con los fabricantes.  
* Investigación de publicaciones técnicas especializadas: Las publicaciones pueden ofrecer información detallada y comparativa acerca de los sistemas actuales de PD, y de los problemas de administración asociados a ellos.  
* Uso de los oferentes de computadoras como fuente de información: Los oferentes brindan mucha información sin costo alguno, y pueden ofrecer demostraciones de casi todos los temas que se deseen.

**Planificación**  
Es necesario planificar las etapas del proceso de adquisición y elaborar el cronograma respectivo.

La mejor planificación ocurre cuando se detecta la necesidad del reemplazo aproximadamente 2 años antes de que se efectúe el reemplazo real. El plazo de dos años es para grandes sistemas. No obstante, los plazos dependerán de las prioridades empresariales, tiempos de cada organización, de la dimensión de los cambios y plataformas y del tiempo de vida útil que el administrador de los recursos \- a través del monitoreo y evaluación del sistema actual- considere que reste antes del reemplazo.

**Encuesta**  
Debe establecerse el interés del usuario por, o su necesidad de, la nueva aplicación. El administrador de las SI/TI debe tener una clara comprensión de los objetivos de la organización, así como de los objetivos y necesidades del usuario.

Una vez realizado esto, el administrador de las SI/TI debe identificar sus propios objetivos y requerimientos y asegurarse de que no existe en la organización un sistema similar.

Seleccionar todos los oferentes disponibles que ofrecen paquetes de SW y/o HW que satisfagan los requerimientos.

Obtener informes que analicen los paquetes/equipos que se están considerando. Es caro evaluar un gran número de sistemas. Consecuentemente, es importante eliminar candidatos lo más rápidamente posible, de manera que la evaluación total se aplique a un pequeño número de sistemas.

**Informe de Evaluación Preliminar**  
Como resultado de la encuesta preliminar, el responsable técnico debe preparar un informe preliminar que incluya:

* Definición de los requerimientos del paquete/equipo.  
* Razones por las cuales se recomienda un paquete de SW, en vez de su desarrollo interno.  
* Resumen de cada paquete de SW que incluya costos, especificaciones y características. (Ídem para el HW).

**Consideraciones particulares de la Adquisición de SW**  
En el proceso de adquisición de SW, es importante determinar si el SW propuesto cumple con los requisitos obligatorios. La esencia de un requisito obligatorio es que excluye totalmente a aquellos sistemas de SW que no lo contengan. La selección de los sistemas a considerar es la primera parte del proceso de evaluación.

Además de evaluar las características y capacidades funcionales de los sistemas a considerar, deben tomarse en cuenta otros factores, tales como entrenamiento, mantenimiento, apoyo en la instalación, documentación, flexibilidad, implementación y operación del sistema de SW dentro de la organización. Para hacer posible la consideración de estos factores, es necesario evaluar tanto a los oferentes como a los paquetes.

También es beneficioso obtener información de usuarios que han instalado los sistemas que se consideran, lo cual se puede hacer desarrollando un cuestionario del usuario y un cuestionario del vendedor de paquetes de SW.

En la evaluación de usuario se deben hacer preguntas respecto a: Operación, confiabilidad, mantenimiento, performance, flexibilidad, instalación, costos, seguridad, documentación, etc.

En la evaluación de vendedor se deben hacer preguntas respecto a: Uso de paquete de aplicación (nombre, fecha de creación, cantidad de organizaciones que lo usa, etc.), documentación, modificación del paquete (si hay planeadas, si se pueden hacer), costos, operaciones, instalación y mantenimiento, seguridad, descripción de la empresa vendedora, otras garantías, tipos de contrato.

### Descripción de cada sección del RDP {#descripción-de-cada-sección-del-rdp}

**1\. RESUMEN EJECUTIVO**  
Aunque esta es la primera sección que se presenta, debe ser la última redactada. Es un resumen del contenido del RDP, y no se lo puede hacer con propiedad hasta que se lo ha redactado. Debe contener una breve descripción de la empresa, sus operaciones y requerimientos de sistema. El resumen debe afirmar explícitamente que es un panorama general del RDP, y que el oferente no debe considerarse como sustituto del RDP (o de **cualquiera de sus subsecciones).**

**2\. PROPÓSITO**  
Esta sección debe considerar 3 tópicos esenciales. Primero, debe discutir la estructura básica y objetivos generales del RDP. Debe incluir ítems tales como los elementos principales del RDP, las expectativas explícitas referentes a la respuesta del oferente, y los objetivos principales de la adquisición propuesta.

Segundo, debe identificar el departamento/oficina/división de la empresa que emitió el RDP, incluyendo el nombre y dirección al cual se deben dirigir todas las propuestas y preguntas relacionadas. Debe también identificar el departamento/persona(s) responsables de decidir respecto de los méritos y aceptación de las propuestas.

Finalmente, debe establecer el alcance del RDP. En otras palabras, debe definir exactamente lo que el RDP pretende ser, y las limitaciones implícitas en su estructura o contenido.

**3\. INTRODUCCIÓN Y REQUERIMIENTOS GENERALES**  
Esta sección debe comenzar con una breve descripción general del negocio en que opera su compañía, y la extensión de sus operaciones.

En segundo lugar, esta sección debe discutir las funciones que se van a realizar por medio de o de las operaciones a ser soportadas por el sistema propuesto.

Finalmente, se deben identificar y definir los requerimientos generales del sistema propuesto. Además de las funciones y/o capacidades requeridas, esta sección debe especificar los elementos (HW-SW-Servicio) del sistema propuesto, que la gerencia espera que el proveedor suministre.

Deben identificarse todos los requerimientos mayores, pese a que la descripción puede (y posiblemente debe), indicar al oferente a las sub secciones apropiadas del RDP para los detalles.

**4\. ORGANIZACIONES INCLUIDAS**  
Aquí se deben identificar los departamentos o divisiones de la compañía que utilizarán el sistema propuesto, incluyendo las funciones generales y responsabilidades de los departamentos identificados y su interrelación.

Implícitamente se identificarán las demandas que cada departamento hará sobre el sistema propuesto. El objetivo de esta sección es brindar al proveedor toda la información referente a las operaciones de la empresa, lo cual le ayudará al oferente a proveer un sistema con la máxima eficiencia operativa, al menor costo.

Cuanta más información se ofrezca al oferente, mayor es la garantía de recibir un sistema que satisfaga todas las expectativas.

**5\. DESCRIPCIÓN DE LA APLICACIÓN**  
Esta es una de las secciones más importantes del RDP. Es esencial que exista el mayor nivel de detalle. Deben incluirse todos los detalles que puedan ayudar al oferente a comprender las operaciones y requerimientos.

Se debe presentar en primer lugar una descripción del flujo general de información en la empresa; es recomendable mostrar un diagrama de flujo con puntos descriptivos.

Debe seguir una descripción detallada de cada subsistema de aplicación. 

Las descripciones deben ser acompañadas por diagramas, diagramas de flujo, explicaciones y ejemplos de entradas y salidas. Además, deben detallarse totalmente las metodologías de cálculo, y las presunciones usadas en la metodología.

Esta sección debe describir también el/los sistemas/s a ser utilizado hasta que el sistema propuesto sea operativo, su limitación, sus similitudes y diferencias con el sistema propuesto, y la manera en que va a ocurrir la transición a éste.

Finalmente, deben tratarse a fondo todos los aspectos particulares (por ejemplo: integridad y seguridad de los datos y del sistema, etc.).

**6\. REQUERIMIENTOS DE INFORMACIÓN**  
En esta sección debe detallarse todos los elementos de información del sistema (archivos, tablas, bases de datos, objetos), así como las operaciones de entrada/salida.

**Archivos del sistema:** para cada uno debe especificarse:

* Nombre y Propósito (por ejemplo: de oferentes, de clientes, etc.)  
* Tipificación de los Elementos de datos que va a contener cada   
* Tamaño/ cantidad de registros  
* Restricciones de acceso   
* Requerimientos y restricciones para la actualización  
* Frecuencia de uso/ actualización

**Entrada/salida del sistema:** Legibles por la máquina. Deben identificarse todas las entradas y salidas que deben estar en forma legible para la máquina, y debe especificarse esa forma. Por ejemplo, puede desearse pasar las transacciones contables diarias a archivos de cinta.

**7\. RESTRICCIONES DE DISEÑO DEL SISTEMA**  
Aquí se establece el tamaño actual y el crecimiento esperado de las operaciones de la empresa.

El propósito es cuantificar y/o calificar las expectativas de manejo del sistema propuesto en términos de crecimiento y flexibilidad. Esta información es vital para el oferente, a fin de determinar los requerimientos de SW, el tamaño del HW y los servicios correspondientes (es decir, mantenimiento y entrenamiento).

La discusión de estas expectativas y restricciones debe estar dividida en categorías individuales, tales como performance general, hardware (computador y periféricos), software del sistema y de aplicación, comunicaciones, etc. Dentro de cada categoría se debe distinguir entre capacidades obligatorias, altamente deseables y deseables (o bien entre imprescindibles, recomendables y convenientes). Deben definirse claramente los parámetros usados (especialmente las restricciones cualitativas como confiabilidad, facilidad de operación y calidad de servicio) para evitar posibles confusiones y ambigüedades.

Otras cuestiones a incluir en esta sección, relacionadas con restricciones de diseño y expectativas, son: entrenamiento, mantenimiento (tiempos y disponibilidad), finanzas y técnicas de evaluación.

**8\. RÉGIMEN DE TRABAJO**  
El propósito de esta sección es identificar y describir los servicios que deseamos comprar al oferente más allá del sistema básico.

Es decir, en esta sección se debe identificar, especificar y definir claramente el alcance y límites de las responsabilidades del oferente, para evitar confusiones, ambigüedades y posteriores discusiones y debe incluir todas las tareas obligatorias a ser cumplidas por el vendedor.

a) El vendedor debe proveer un plan detallado del proyecto de todo el trabajo a realizar

b) El vendedor debe desarrollar y entregar para su revisión el diseño lógico detallado para el sistema propuesto. El diseño y la correspondiente documentación incluirán descripción de las entradas, procesamiento, salidas, elementos de datos, relaciones entre programas y relaciones entre todos los elementos de datos y todos los programas. El vendedor debe proveer también una capacidad de backUp manual que permita que las operaciones sean sólo mínimamente alteradas en caso de mal funcionamiento del sistema. También se proveerán las medidas que aseguren la seguridad e integridad de los datos.

c) El vendedor debe desarrollar y entregar para su revisión los diseños físicos detallados para el sistema propuesto. El diseño y la correspondiente documentación describirán la relación del diseño lógico con el HW y el SW de sistema del sistema.

d) El vendedor debe desarrollar e instalar SW y documentación para el sistema propuesto. El sistema operará en la computadora del usuario y será compatible con los sistemas relacionados existentes. La documentación incluirá por lo menos:

* Programa fuente y otra información requerida y la documentación de programas necesaria para permitir el mantenimiento y modificaciones por parte del personal del usuario.  
* Procedimientos de uso y operación del sistema. La documentación debe ser fácil de usar y comprender y fácil de actualizar. Los procedimientos deben contener todos los procedimientos manuales necesarios para la operación del sistema, así como controles de seguridad.  
* Materiales de entrenamiento para asistir al personal del usuario en el entrenamiento para el uso, operación y mantenimiento del sistema.

h) El vendedor debe desarrollar un programa de entrenamiento incluyendo por lo menos lo siguiente:

i) El vendedor debe brindar apoyo técnico para el uso operativo del sistema propuesto durante los primeros 3 meses de operación. El apoyo técnico incluirá ayuda en el uso, operación y mantenimiento del sistema. El vendedor solucionará cualquier problema que ocurra durante este período, debido a los materiales por él provistos.

j) El vendedor debe brindar apoyo de mantenimiento para todo el SW de aplicación. (O HW provisto)

**9\. INFORMACIÓN REQUERIDA DEL OFERENTE**  
Este es un resumen ejecutivo de esta sección particular del RDP. Se usa para describir la información y el formato general de la presentación que queremos que el oferente brinde en sus respuestas.

* General: Esta sección específica el contenido de la respuesta general  
* Software del sistema: Aquí se requiere la respuesta  
* Software de aplicación: Generalmente, esta sección específica requerimientos de respuesta similares a aquellos que se listaron en "Software del sistema". 	  
* Preparación del terreno: A menudo se incluye esta sección en la de HW (Características del HW).  
* Apoyo del oferente: capacitación, mantenimiento, etc.  
* Datos financieros  
* Instalación  
* Tabla de evaluación: Generalmente, esto se refiere exclusivamente al HW y SW del sistema. Usualmente se especifica una tabla de evaluación completa (cuyo contenido y formato deben especificarse en la sección Restricciones de Diseño del RDP) para cada sistema propuesto por el oferente.  
* Visita de demostración en el lugar: Los requerimientos recomendados incluyen una descripción de la demostración propuesta y una lista de lugares posibles para la demostración.  
* Cronograma del Proyecto: Los requerimientos recomendados incluyen fechas estimadas para entrega, instalación, prueba e implementación de cada elemento del HW, SW del sistema y SW de aplicación, con la fecha de otorgamiento del contrato considerada como día cero.

**10\. CRITERIOS DE SELECCIÓN**

* **General**: Esta subsección enuncia explícitamente que el objetivo del proceso de evaluación es asegurar la selección de un sistema que mejor se adecue a las necesidades (presentes y futuras) de la empresa y que satisfaga todos los requerimientos especificados en el RDP.  
* **Métodos de evaluación a usarse**: El propósito de esta subsección es identificar las 2 áreas de evaluación (técnica y financiera) y sus pesos relativos en la decisión final (generalmente se le asignan pesos relativos iguales).  
* **Criterios para la Evaluación Técnica**: Se describe el procedimiento de evaluación técnica.  
* **Criterios para la Evaluación Financiera**: Esta subsección debe especificar los métodos usados para evaluar las implicaciones financieras de la propuesta del oferente. Los métodos usuales empleados son una combinación del análisis del valor actual, del impacto del presupuesto de capital en el comprador, y de la medida en la cual la propuesta es compatible con las restricciones presupuestarias del comprador.

**11\. INFORMACIÓN ADMINISTRATIVA Y CONTRACTUAL**  
El propósito de esta sección es establecer explícitamente las implicaciones legales y contractuales del RDP (y/o de la respuesta del oferente) y todos los descargos del emisor del RDP. Esta sección debe contener los siguientes tópicos:

Propuestas del oferente, Rechazo de propuestas, Costos incurridos, Agregados al RDP, Fecha de la respuesta, Propuestas múltiples, Aceptación del Contenido de la Propuesta, Economía en la Preparación, Presentación Oral, Responsabilidad primaria del contratista, Difusión de Noticias, Programa de actividades, Acuerdos Estándar Negociados, Propuesta de Cotización de Precio de Alquiler/Compra, Visitas a Usuarios, Confidencialidad de la Información, Registros Públicos, Provisiones Contractuales, Revisiones subsiguientes.

**12\. APÉNDICE**  
El apéndice debe incluir la especificación de contenido y formato del resumen de costo(s). Para cada alternativa financiera se debe solicitar un resumen por separado (para alquiler; alquiler/compra; compra directa, etc.). Cada resumen debe dividirse en:

* **Plan financiero:** El plan financiero debe incluir la duración del período de renta, período de cancelación y precio de compra.  
* Costos de HW  
* Costos de SW del Sistema y de Aplicación  
* Costos de Capacitación y Entrenamiento

Luego de la elaboración del RDP, se debe efectuar la invitación formal a los oferentes.

Recibidas las respuestas, se inicia el proceso de evaluación propiamente dicho.

## 

## **Provisión de RRHH (Chiavenato)** {#provisión-de-rrhh-(chiavenato)}

Conjunto de procesos y técnicas que suministran las personas que se integrarán a la organización. Su finalidad es abastecer a la organización con los talentos humanos necesarios para su funcionamiento.

***|Nota| RECURSOS HUMANOS** → Conjunto de proceso y técnicas que se destina a como obtengo las personas que se INTEGRARÁN a la org, a mi cultura, la tecnocracia, etc. Su finalidad es abastecer a los talentos que tiene que estar en mi org y que son los que requiero **para el funcionamiento que yo planifiqué.*** 

***![][image33]***

***![][image34]***

Los dos grandes procesos de la provisión van a ser EL RECLUTAMIENTO Y LA SELECCIÓN, después tengo una zona media borrosa que me daría las confirmaciones a aspectos de salud, etc para que la admisión sea definitiva.

Nos interesa el hecho de que los recursos humanos ingresan en el sistema y salen de él, generando una dinámica especial. Los RRHH, entran y salen de las organizaciones. No son recursos estables, incluso se pueden ir moviendo de áreas.

![][image35]

*EL PROCESO DE PROVISIÓN SE ALIMENTA DE APLICACIÓN DE RR A TRAVÉS DE LA FICHA DE CARGO, a su vez el de provisión le da a aplicación le da las personas.*

*Provisión le da las personas a evaluar (las que ingresan) al de Seguimiento (evaluación de desempeño, para ver cómo se integran) y el de Seguimiento le da el resultado de evaluacion, me dice que tan bien seleccione*

*DESARROLLO Y MANTENIMIENTO LE DA VACANTES Y LAS políticas salariales, posibilidades de carrera, etc a Provisión. La provisión le da las necesidades inmediatas de condición y desarrollo (capacitación) al desarrollo y mantenimiento.*

### Mercado de recursos humanos y mercado laboral {#mercado-de-recursos-humanos-y-mercado-laboral}

El concepto de **mercado** presenta tres aspectos importantes:

* **Dimensión espacial***.* Todo mercado se caracteriza por un área física, geográfica o territorial. (Los mercados varían de lugar en lugar).  
* **Dimensión temporal***.* Todo mercado depende de la época. En épocas diferentes, un mismo mercado puede presentar características distintas.  
* **Dimensión de oferta y demanda***.* Todo mercado se caracteriza por la oferta y la disponibilidad de algo y, al mismo tiempo, por la demanda y la búsqueda de algo. Si la oferta es mayor que la demanda, el producto o servicio es fácil de obtener y se presenta competencia entre los vendedores o entre quienes ofrecen ese producto o servicio. Si la demanda es mayor que la oferta, entonces la situación se invierte, y el producto o servicio se constituye en algo de difícil adquirir; en este caso, se presenta competencia entre los compradores o entre quienes necesitan ese producto o servicio.

En términos de suministro de recursos humanos, existen dos tipos de mercados diferentes, aunque estrechamente entrelazados e interrelacionados: **el mercado laboral (OFERTA de puestos) y el mercado de recursos humanos (OFERTA de talentos).**

.![][image36]![][image37]

![][image38]

#### ***Mercado laboral***

Está conformado por las ofertas de trabajo o de empleo hechas por las organizaciones en determinado lugar y época. En esencia, lo definen las organizaciones y sus oportunidades de empleo.

El mercado laboral se comporta en términos de oferta y demanda, es decir, disponibilidad de empleos y demanda de empleos, respectivamente. Como puntos de referencia, se presentan a continuación las tres posibles situaciones del mercado laboral:

**Oferta mayor que la demanda**: las ofertas de empleo de las organizaciones exceden al número de candidatos para satisfacerlas. 

*Consecuencias para las organizaciones:*

* Elevadas inversiones en reclutamiento   
* Criterios de selección más flexibles y menos rigurosos   
* Elevadas inversiones en capacitaciones del personal   
* Ofertas salariales más seductoras, lo que ocasiona distorsiones en la política salarial de la organización   
* Elevadas inversiones en beneficios sociales, tanto para atraer candidatos como para conservar el personal existente   
* Énfasis en el reclutamiento interno   
* Fuerte competencia entre las organizaciones que disputan el mismo mercado de recursos humanos   
* Los recursos humanos se convierten en un recurso difícil y escaso 


  *Consecuencias para los candidatos:*

* Exceso de oportunidades de empleo   
* Los candidatos seleccionan las organizaciones que les ofrezcan los mejores cargos, salarios, etc.   
* Aumenta la rotación ya que las personas se predisponen a salir de sus organizaciones para probar oportunidades mejores   
* Las personas se sienten dueñas de la situación y comienzan a pedir aumentos salariales, mejores beneficios sociales, se vuelven indisciplinadas, hay ausentismo, etc. 

**Oferta igual a la demanda***.* Situación de relativo equilibrio entre el volumen de ofertas de empleo y el volumen de candidatos para satisfacerlas

**Oferta menor que la demanda***.* Situación en que las ofertas de empleo hechas por las organizaciones son pocas; hay escasez de ofertas de empleo y exceso de candidatos para satisfacerlas.

*Consecuencias para las organizaciones*

* Bajas inversiones en reclutamiento   
* Criterios de selección más rígidos y rigurosos   
* Bajas inversiones en capacitación, ya que la organización puede aprovechar candidatos ya capacitados   
* Pueden hacer ofertas salariales más bajas   
* Bajas inversiones en beneficios sociales   
* Énfasis en el reclutamiento externo como medio para mejorar el potencial humano   
* No hay competencia entre las organizaciones en cuanto al mercado de recursos humanos   
* Los recursos humanos se convierten en un recurso fácil y abundante que no requiere atención especial 

  *Consecuencias para los candidatos* 

* Escasez de vacantes   
* Compiten entre sí por las pocas vacantes que surgen   
* Buscan afianzarse en las organizaciones   
* Se vuelven más disciplinados y procuran no faltar al trabajo ni atrasarse 

#### ***Mercado de recursos humanos***

Lo define el sector de población que está en condiciones de trabajar o está trabajando, es decir, el conjunto de personas empleadas (mercado de RH aplicado) o desempleadas (mercado de RH disponible) y aptas para trabajar. Se trata de **candidatos reales** cuando están buscando alguna oportunidad, estén empleados o no, y son **candidatos potenciales** cuando \-aunque no estén buscando empleo- están en condiciones de desempeñarlo a satisfacción.

En teoría, **el mercado de recursos humanos actúa como un espejo del mercado laboral:** cuando uno está en oferta, el otro está en demanda, y viceversa. La oferta de un mercado corresponde a la demanda de otro, y viceversa. Es decir, los dos son sistemas en constante interrelación: la salida *{output)* de uno es la entrada *(input)* del otro, y viceversa.

### Rotación de personal {#rotación-de-personal}

El término rotación de recursos humanos se utiliza para definir la fluctuación de personal entre una organización y su ambiente.  
![][image39]

En general, la rotación de personal se expresa mediante la relación porcentual entre las admisiones y los retiros, y el promedio de trabajadores que pertenecen a la organización en cierto periodo.

Si en niveles vegetativos la rotación es provocada por la organización para hacer sustituciones orientadas a mejorar el potencial humano existente, a reemplazar una parte de sus recursos humanos por otros recursos de mejor calidad existentes en el mercado, entonces la rotación se halla bajo el control de la organización. Sin embargo, cuando las pérdidas de recursos no son provocadas por la organización, es decir, cuando se presentan independientemente de los objetivos de esta, resulta esencial establecer los motivos que provocan la desasimilación (desincorporación) de los recursos humanos, para que la organización pueda actuar sobre aquellos y disminuir el volumen de retiros inconvenientes.

![][image40]![][image41]

#### ***Diagnóstico de las causas de rotación de personal***

La rotación del personal no es una causa sino un efecto, consecuencia de ciertos fenómenos localizados en el interior o el exterior de la organización que condicionan la actitud y el comportamiento del personal. **Es una variable dependiente de los fenómenos internos y/o externos**. 

Como **fenómenos externos** pueden citarse la situación de oferta y demanda de recursos humanos, la situación económica, las oportunidades de empleo, etc. Entre los **fenómenos internos** pueden mencionarse la política salarial y de beneficios sociales de la organización, el tipo de supervisión, etc.

La información correspondiente a estos fenómenos internos y externos se obtiene mediante entrevistas de retiro.

La entrevista de retiro abarca el motivo de retiro y opiniones acerca de los siguientes puntos: la empresa, el cargo que ocupaba, su jefe directo, horarios, condiciones físicas, beneficios sociales, salario, relaciones humanas, oportunidades de progreso, moral y actitud de compañeros, mercado laboral.

#### ***Determinación del costo de la rotación de personal***

![][image42]  
**Costos primarios de la rotación de personal.** Se relacionan directamente con el retiro de cada empleado y su reemplazo por otro. Incluye:  
**Gastos secundarios de la rotación de personal.** Abarcan aspectos intangibles difíciles de evaluar en forma numérica porque sus características son cualitativas en su mayor parte  
**Costos terciarios de la rotación de personal.** Se relacionan con los efectos colaterales mediatos de la rotación, que se manifiestan a mediano y a largo plazos. En tanto los costos primarios son cuantificables y los costos secundarios son cualitativos, los costos terciarios son solo estimables. Entre dichos costos se cuentan:

1. **Costo de inversión extra**: Aumento proporcional de las tasas de seguros, depreciación de equipo, mantenimiento y reparaciones con respecto al volumen de producción. Aumento del volumen de salarios pagados a los nuevos empleados y, por tanto, incremento de reajustes a los demás empleados cuando la situación del mercado laboral es de oferta, lo que intensifica la competencia y la oferta de salarios iníciales más elevados en el mercado de recursos humanos.  
2. **Pérdidas en los negocios:** Se reflejan en la imagen y en los negocios de la empresa, ocasionadas por la falta de calidad de los productos o servicios prestados por empleados inexpertos en periodo de ambientación.

#### ***Ausentismo***

Es la suma de los períodos en que, por cualquier motivo, los empleados se retardan o no asisten al trabajo en la organización. Entre las principales causas están: 

* Enfermedad comprobada; o no comprobada   
* Diversas razones de carácter familiar   
* Tardanzas involuntarias por motivos de fuerza mayor   
* Faltas voluntarias por motivos personales   
* Dificultades y problemas financieros   
* Problemas de transportes   
* Baja motivación para trabajar   
* Escasa supervisión de la jefatura   
* Políticas inadecuadas de la organización 

Una vez diagnosticadas las causas del ausentismo, debe efectuarse una acción coordinada de supervisión con el debido apoyo de políticas de la organización y apoyo de la dirección para *tratar de reducir los niveles de ausencia y tardanzas del personal.*

Puedo tener: 

* **Ausentismo parcial** (faltas, retrasos)  
* **Ausentismo general** (vacaciones, licencias, es un periodo más prolongado). Esta puede ser una necesidad de aprovisionarse de personas, osea puedo tener una rotación de personal por ausencia si es que su puesto no puede quedarse vacío. 

### Evaluación de los procesos de provisión de personas {#evaluación-de-los-procesos-de-provisión-de-personas}

| ![][image43] |  |
| ----- | ----- |
| Lado izquierdo **Micro orientado:** pues se halla dirigido hacia el cargo que se quiere ocupar y nada más. **Vegetativo:** porque se orienta al mantenimiento del status quo, con el simple cubrimiento de vacantes.  **Desintegrado:** porque cada demanda de una vacante es una tarea particular y aislada de las demás. | Lado derecho **Estratégicos:** porque la planeación organizacional se lleva a cabo con miras al presente y al futuro y se orienta a largo plazo y al destino de la organización y de las personas que la conforman.  **Macro orientado:** porque cada demanda forma parte de una visión organizacional amplia y global. De ahí también se deriva su carácter integral y amplio. |
| El desafío está en el desplazamiento gradual y definitivo del extremo izquierdo hacia el extremo derecho del *continuum.* |  |

### Reclutamiento de personas {#reclutamiento-de-personas}

**PROCESO DE PROVISIÓN** *\[las etapas son secuenciales\]*

* Investigación Interna y Externa *\[Chiavennato lo explica dentro de reclutamiento, en clase lo vimos como etapa\].*  
* Reclutamiento.  
* Selección.  
* Evaluación → exámenes médicos, antecedentes penales, etc.  
* Admisión.

***¿Qué sentido tiene la “obligatoriedad” del requisito?** Limitar la cantidad de candidatos y gente que va a pasar a la selección. Porque las etapas posteriores son más minuciosas y caras.*

***¿Cuando un proceso de reclutamiento es eficaz?** Cuando atrae suficientes candidatos para abastecer adecuadamente al proceso de selección*

**El Reclutamiento funciona como un embudo (contra los requisitos excluyentes/obligatorios).** Es el proceso que comunica la necesidades de perfiles a un segmento del  mercado laboral para atraer a los candidatos potencialmente calificados. Comunica que cargos están disponibles, que vacantes tengo en mi org.  
![][image44]   
Consiste en:

**Una investigación interna:** verificación continua de que necesidad que voy a tener en el corto-mediano-largo plazo.  
**Una investigación externa:** analizar el mercado laboral para entroncar los perfiles que busco ⇒ segmentación del mercado y determinar las fuentes de reclutamiento  
*¿Por qué fuentes?* Es en que lugar tengo esos posibles candidatos.  
Puedo tenerlos dentro de mi org (**reclutamiento interno**)  
O fuera de mí org (**reclutamiento externo**)  
![][image45]  
A partir de ahi recien puedo hablar de las técnicas de reclutamiento (convocatorias de pasantías, anuncio en mi página web que se aceptas cv, etc)

![][image46]

⇒ A través del reclutamiento la org divulga y ofrece al mercado de RRHH los empleos que pretende llenar. **Se comunican las necesidades de la organización.** 

***|Nota| El insumo principal del proceso de provisión es la Planificación estratégica**  estrategias de SI/TI, Planes, Ubicación, Rol y Organización.*

#### ***Investigación interna*** {#investigación-interna}

Verificación de las necesidades de la organización respecto a sus necesidades de recursos humanos a corto, mediano y largo plazos para saber que requiere de inmediato y cuáles son sus planes futuros de crecimiento y desarrollo, que significarán nuevos aportes de recursos humanos. En muchas organizaciones, esta investigación interna se sustituye por un proceso más amplio denominado planeación de personal.

##### **Planeación del personal**

La planeación de personal es un proceso de decisión respecto de los recursos humanos necesarios para conseguir los objetivos organizacionales en un periodo determinado. Se trata de prever cuales serán la fuerza laboral y los talentos humanos necesarios para la realización de la acción organizacional futura.

Existen varios modelos de planeación; algunos son genéricos y abarcan toda la organización, otros son específicos para determinados sectores. Casi todos exigen la participación del órgano encargado de personal.

**Modelo basado en la demanda estimada del producto o servicio**

Las necesidades de personal son una variable dependiente de la demanda estimada del producto (en el caso de la industria) o del servicio (en el caso de una organización de servicios). La relación entre las dos variables \- número de personas y demanda del producto o servicio- está influida por variaciones en la productividad, la tecnología, la disponibilidad de recursos financieros internos o externos y la disponibilidad de personas en la organización.

**Modelo basado en segmentos de cargos**

Este modelo también se centra en el nivel operacional de la organización. Es una técnica de planeación de RH utilizada en muchas empresas de gran tamaño. Por ejemplo: 

* Seleccionar un factor estratégico (nivel de ventas, capacidad de producción, planes de expansión, etc.) en cada área de la empresa  
* Determinar los niveles históricos (pasado y futuro) de cada factor estratégico.  
* Establecer los niveles históricos de fuerza laboral por área funcional.  
* Proyectar los niveles futuros de fuerza laboral en cada área funcional, correlacionándolos con la proyección de los niveles (históricos y futuros) del factor estratégico correspondiente.

**Modelo de sustitución de puestos clave**

Se utiliza un modelo denominado mapas de sustitución u organigramas de carrera, que son una representación visual de quien sustituye a quien, en la organización, ante la eventualidad de que exista alguna vacante en el futuro.

Este estatus de los candidatos depende de dos variables: desempeño actual y posibilidad de ascenso.

**Modelo basado en el flujo de personal**

Intenta caracterizar el flujo de las personas hacia adentro de la organización, a través de ella y hacia fuera. Esto permite hacer una predicción a corto plazo de las necesidades de recursos humanos de la organización. Este modelo puede utilizarse también para predecir las consecuencias que podrían causar otras contingencias, como la política de promociones, rotación de personal, etc. Resulta muy útil para el análisis del planeamiento de carrera. 

**Modelo de planeación integrada**

Es el modelo más amplio. Desde el punto de vista de insumos, la planeación de personal debe tener en cuenta cuatro factores o variables intervinientes:

1. Volumen de producción planeado  
2. Cambios tecnológicos que alteran la productividad del personal  
3. Condiciones de oferta y de demanda, y comportamiento de la clientela  
4. Planeación de carreras en la organización

Desde el punto de vista del flujo interno, la planeación de personal debe considerar la composición cambiante de la fuerza laboral de la organización, haciendo un seguimiento o evaluando las entradas y las salidas de personal y su movimiento en la organización.

#### ***Investigación externa*** {#investigación-externa}

Es una investigación del mercado de RRHH orientada a segmentar y diferenciarlo para facilitar su análisis y su consiguiente estudio. Aquí sobresale la segmentación del mercado y la localización de fuentes de reclutamiento.

La ubicación correcta de fuentes de reclutamiento permite a la organización elevar el rendimiento del proceso de reclutamiento, disminuir su tiempo y reducir sus costos.

#### ***El proceso de reclutamiento*** {#el-proceso-de-reclutamiento}

El reclutamiento implica un proceso que varía según la organización. El comienzo del proceso depende de la decisión de línea. **Dado que el reclutamiento es una función de *staff,* sus actos dependen de una decisión de la línea**, que se oficializa mediante una especie de orden de servicio, generalmente denominada solicitud de empleado o solicitud de personal.

![][image47]

Cuando el órgano de reclutamiento la recibe verifica en los archivos si está disponible algún candidato adecuado, sino debe reclutar a través de las técnicas de reclutamiento más indicadas para el caso.

El mercado de recursos humanos presenta diversas fuentes que la empresa debe identificar y localizar con el propósito de atraer candidatos que suplan con sus necesidades. El mercado de los RRHH está compuesto por candidatos que pueden estar empleados o disponibles. Los dos tipos de candidatos pueden ser reales (están buscando trabajo o cambiar el que tienen) o potenciales (los que no están interesados).

##### **Reclutamiento interno**

Al presentarse determinada vacante, la empresa intenta llenarla mediante la reubicación de sus empleados, los cuales pueden ser ascendidos (movimiento vertical), transferidos (movimiento horizontal) o transferidos como promoción (movimiento diagonal).

El reclutamiento interno se basa en datos e informaciones relacionados con otros subsistemas:

* Resultados del candidato en pruebas de selección. (PROVISIÓN)  
* Resultados de evaluaciones de desempeño. (SEGUIMIENTO)  
* Resultados en programas de entrenamiento y perfeccionamiento. (DESARROLLO)  
* Análisis del cargo que ocupa y que puede llegar a ocupar, para ver las diferencias. (APLICACIÓN)  
* Planes de carreras del candidato. (APLICACIÓN)  
* Condiciones de ascenso y de reemplazo (si ya hay alguien que ocupe el lugar que va a dejar) (APLICACIÓN)

| Ventajas | Desventajas |
| ----- | ----- |
| Es más económico y rápido  Presenta mayor índice de validez y seguridad . Les conozco las mañas y virtudes → mayor seguridad del potencial del candidato Poderosa fuente de motivación para los empleados  Aprovecha las inversiones de la empresa en entrenamiento de personal  Desarrolla un sano espíritu de competencia entre el personal | Exige que los empleados nuevos tengan condiciones de potencial de desarrollo para poder ascender y motivación suficiente para llegar allí.  Puede generar un conflicto de intereses ya que tienden a crear una actitud negativa en los empleados que no demuestran condiciones.  Cuando se maneja de manera incorrecta puede conducir al “principio de Peter”: las empresas, al promover innecesariamente a sus empleados, los llevan siempre a la posición donde demuestran el máximo de su incompetencia.  Cuando se efectúa continuamente puede llevar a los empleados a una progresiva limitación de las políticas, ya que éstos, al convivir sólo con la situación de la organización, se adaptan a ellas y pierden creatividad e innovación.  No puede hacerse en términos globales dentro de la organización. Para no perjudicar el patrimonio humano el reclutamiento interno se debe realizar cuando los candidatos internos igualen en condiciones a los candidatos externos. *Si hice bien los deberes el empleado estará capacitado y preparado para ascender* No es posible en cualquier cargo → Si añado muchos puestos del nivel más bajo (operativo)  tengo que traer gente nueva, nadie va a querer bajar de su cargo, no? |

**POLÍTICA (guía para tomar decisiones) GENERAL DE PROVISIÓN DE RRHH** → priorizar reclutamiento interno sobre externo  
*¿Por qué priorizo el interno?*   
Recupero inversión (amortizo dice soria tmb),   
Mayor seguridad  
Motiva al personal, más rápido y económico  
si por x razones no se puede → voy al externo

##### **Reclutamiento externo**

Opera con candidatos que no pertenecen a la organización. Incide sobre los candidatos reales o potenciales, disponibles o empleados en otras organizaciones.

Hay dos tipos de enfoques de las fuentes de reclutamiento: enfoque directo (la empresa tiene contacto directo con el mercado: otras empresas, escuelas y universidades, etc.) y enfoque indirecto (la agencia recluta a través de: agencias de reclutamiento, asociaciones gremiales, sindicatos).

Las principales técnicas **(Medios según cátedra)** de reclutamiento externos son las siguientes:

* **Consultas de los archivos de los candidatos**: Los candidatos que se presentan de manera espontánea o que no se consideraron en reclutamientos anteriores deben tener un currículo debidamente archivado. Este es el sistema de menor costo, y que, cuando funciona es uno de los más breves.   
* **Candidatos presentados por empleados de la empresa:** es de bajo costo, alto rendimiento y bajo índice de tiempo. Refuerza la organización informal y brinda a los funcionarios colaboración con la organización formal.   
* **Carteles o anuncios en la puerta de la empresa:** es de bajo costo, aunque su rendimiento y rapidez dependen de varios factores, como la localización de la empresa. A menudo es utilizado para cargos de bajo nivel.   
* **Carteles con sindicatos y asociaciones gremiales:** no tiene tanto rendimiento como la anterior, pero tiene la ventaja de involucrar a otras organizaciones sin que haya elevados costos. Sirve como estrategia de apoyo a otra principal (enfoque indirecto).   
* **Contactos con universidades y escuelas, agremiaciones estudiantiles, directores académicos, centros de integración empresa-escuela**: estos están orientados a divulgar las oportunidades ofrecidas por la empresa (enfoque indirecto).   
* **Conferencias y charlas en universidades y escuelas:** destinadas a promover la empresa y crear una actitud favorable, describiendo la organización, sus objetivos, estructuras, etc.   
* **Contactos con otras empresas que actúan en el mismo mercado:** una cooperación mutua (enfoque directo).   
* **Viajes de reclutamiento a otras localidades:** cuando el mercado local de recursos humanos está ya bastante explotado. Después de un periodo de prueba los empleados se transfieren a la ciudad donde está situada la empresa.  
* **Avisos en diarios y revistas:** es una de las más eficaces para atraer candidatos. Es más cuantitativo que cualitativo.   
* **Agencias de reclutamiento:** es una de las más costosas, pero está compensado por factores relacionados con el tiempo y el rendimiento. 

La mayor parte de las veces, estas técnicas se utilizan en conjunto. Los factores costo y tiempo son importantes a la hora de seleccionar la técnica. Cuanto mayor sea la limitación de tiempo, mayor será el costo de la técnica que se aplique.

| Ventajas | Desventajas |
| ----- | ----- |
| Trae “sangre nueva” y nuevas experiencias a la organización. La entrada de recursos humanos ocasiona una importación de ideas nuevas y enfoques diferentes, y casi siempre, una revisión de la manera como se conducen los asuntos dentro de la empresa  Renueva y enriquece los recursos humanos de la organización Aprovecha las inversiones en preparación y el desarrollo de personal efectuadas por otras empresas o por los propios candidatos | Generalmente tarda más que el reclutamiento interno Es más costoso y exige costos y gastos inmediatos Es menos seguro que el reclutamiento interno Cuando monopoliza las vacantes dentro de la empresa puede frustrar al personal. Los empleados pueden percibir el monopolio de reclutamiento externo como deslealtad de la empresa al personal Afecta la política salarial cuando la oferta y la demanda en el mercado de RRHH no están en equilibrio |

##### **Reclutamiento mixto**

Las empresas nunca hacen solo reclutamiento interno ni solo reclutamiento externo, uno siempre debe complementar al otro. 

Cuando se hace reclutamiento interno, en algún punto de la organización siempre surge una posición que debe llenarse mediante reclutamiento externo, a menos que ésta se cancele. Por otra parte, siempre que se hace reclutamiento externo, debe plantearse algún desafío, oportunidad u horizonte al nuevo empleado.

El reclutamiento mixto enfoca tanto fuentes internas como externas de recursos humanos.

Puede ser adoptado de tres maneras:

* **Inicialmente reclutamiento externo seguido de reclutamiento interno**, en caso de que aquel no presente resultados deseables: la empresa está más interesada en la entrada de RRHH que en la transformación.  
* **Inicialmente reclutamiento interno seguido de reclutamiento externo**, en caso de que no presente resultados deseables: La empresa da prioridad a sus empleados en la disputa o en la competencia por las oportunidades existentes.  
* **Reclutamiento externo e interno simultáneo**: Caso en que la empresa está más preocupada por llenar la vacante existente, sea a través de entrada *(input)* o a través de la transformación de sus recursos humanos. Una buena política de personal debe preferir a los candidatos internos frente a los externos, en caso de que presenten igualdad de condiciones.

### Selección de personal {#selección-de-personal}

Escoger entre los candidatos reclutados a los más adecuados para ocupar los cargos existentes en la empresa, tratando de mantener o aumentar la eficiencia y el rendimiento del personal.

Busca solucionar dos problemas: 

* Adecuación del hombre al cargo   
* Eficiencia del hombre en el cargo 

**Es un proceso que termina en una toma de decisión**, tengo que elegir entre los candidatos que se filtraron en el reclutamiento. Entra en juego **la racionalidad** para aumentar la eficiencia en el desempeño del personal o la eficacia organizacional. 

Es con la selección con la cual garantizo que la persona que se va a incorporar es la que tiene las habilidades que se acercan al perfil que busco ⇒ **Al ser un proceso,** me va dando un pronóstico y un diagnóstico de la persona que evaluo. **Siempre tengo que partir de los datos del cargo**, porque ahí está el perfil, eso me permite tener todas las **especificaciones absolutamente objetivas**, me describe el cargo y en que aporta al área. 

**Es una comparación porque siempre estoy comprando una persona con las especificaciones del cargo.** SIEMPRE COMPARO CON EL CARGO, no entre postulantes.

**Base para la selección:** recolección de la información acerca del cargo (clave), y luego elegir las técnicas de selección. Debo ver también la cantidad de etapas que va a tener mi proceso de decisiones, y de ahí veo en cada etapa qué técnica de selección ocupo.

***¿Qué rol juega el gerente de SITI?*** Pide el personal, sabe los requisitos del puesto, conoce las necesidades. En la selección diseña las pruebas de selección, puede o no participar en las entrevistas y es el que decide al final **(ES UN PROCESO DE DECISIÓN)**

***¿Qué rol juega el área de RRHH?*** Sigue las indicaciones, ve a donde buscar, dueña la convocatoria, me dicen quienes pasan del reclutamiento a la selección.

#### ***La selección como proceso de comparación***

La selección debe mirarse como un proceso de comparación entre dos variables: las exigencias del cargo y las características de los candidatos. La primera variable la suministra el análisis y descripción del cargo y la segunda se obtiene mediante la aplicación de técnicas de selección.  
![][image48]  
Puede darse que el candidato no cumpla las condiciones ideales para ocupar el cargo, que las cumpla justo, o que las sobrepase (superdotado para el cargo). Esta comparación se centra en una franja de aceptación que admite cierta flexibilidad más o menos cercana al punto ideal.

A través de la comparación, el organismo de selección (staff) presenta ante el organismo solicitante los candidatos aprobados en la selección. La decisión de escoger, aceptar o rechazar es facultad del organismo solicitante o de su inmediato superior.

#### ***La selección como un proceso de decisión***

El organismo de selección *(staff)* no puede imponer al organismo solicitante que acepte los candidatos aprobados durante el proceso de Comparación, sino que debe limitarse a prestar un servicio especializado, aplicar técnicas de selección y recomendar a aquellos candidatos que juzgue más idóneos para el cargo. La decisión final de aceptar o rechazar los candidatos es siempre responsabilidad del organismo solicitante.

Como proceso de decisión, la selección de personal implica **tres modelos de comportamiento:**

* **Modelo de colocación**: hay solo un candidato para una vacante que debe ser cubierta por él. El candidato presentado debe ser admitido sin objeción alguna 

![][image49]

* **Modelo de selección**: hay varios candidatos para cubrir una vacante. Pueden ocurrir dos alternativas: aceptación o rechazo. Si se rechaza sale del proceso 

![][image50]

* **Modelo de clasificación**: hay varios candidatos para cada vacante y varias vacantes para cada candidato. Las características de cada candidato se comparan con los requisitos que el cargo exige. Ocurren dos alternativas: el candidato puede ser aceptado o rechazado. Si es rechazado entra a concursar en los otros cargos vacantes hasta que estos se agoten. La empresa considera que el candidato puede ser colocado en el cargo más adecuado a las características del candidato. 

![][image51]  
Consecuencia, estos **dos requisito**s aparecen en la base de cualquier programa de clasificación:

* Técnicas de selección capaces de proporcionar información respecto de las vacantes disponibles, y de permitir comparaciones de los candidatos en relación con los cargos.  
* Existencia de modelos de selección que permitan máxima ganancia en las decisiones sobre candidatos, o simplemente estándares cuantitativos de resultados.

![][image52]

#### ***Base para la selección de personas***

Recolección de información acerca del cargo. Puede hacerse a través de: 

* **Análisis del cargo**: inventario de los aspectos intrínsecos (contenidos del cargo) y extrínsecos (requisitos que debe cumplir el aspirante al cargo) del cargo. Cualquiera que sea el método de análisis empleado, lo importante para la selección es la información con respecto a los requisitos y las características que debe poseer el aspirante al cargo para que el proceso de selección se centre en ellos.  
* **Aplicación de la técnica de los incidentes críticos**: los jefes directos anotan todos los hechos y comportamientos de los ocupantes del cargo considerado, que han producido un mejor o peor desempeño en el trabajo. Esta técnica busca identificar las características deseables y las no deseables en los nuevos candidatos. Presenta el inconveniente de fundamentarse en la opinión del jefe inmediato.  
* **Requerimiento de personal:** consiste en la verificación de los datos consignados en el requerimiento, a cargo del jefe inmediato, especificando los requisitos y características que el aspirante al cargo debe poseer.   
* **Análisis del cargo en el mercado**: Cuando se trata de un cargo nuevo, sobre el que la empresa no tiene una definición a *priori,* ni el mismo jefe directo, existe la opción de verificar en empresas semejantes los cargos comparables, su contenido, los requisitos y las características de sus ocupantes.  
* **Hipótesis de trabajo**: una predicción aproximada del contenido del cargo y su exigibilidad con relación al ocupante, en caso de que ninguna de las alternativas anteriores pueda aplicarse. 

La información que el organismo recibe respecto de los cargos y de sus ocupantes se transforma en una **ficha de especificaciones o ficha profesiográfica,** que debe contener las características psicológicas y físicas necesarias para que el aspirante pueda desempeñarse satisfactoriamente en el cargo considerado. Con base en esta ficha, el organismo de selección puede establecer las técnicas de selección más adecuadas al cargo.

#### ***Elección de las técnicas de selección***

Una vez obtenida la información acerca del cargo del aspirante, y elaborada la ficha profesiográfica, el paso que sigue es la elección de las técnicas de selección más adecuadas al caso. **Las técnicas de selección pueden clasificarse en:**  
![][image53]

**Cada una de las técnicas auxilia a las demás** proporcionando un amplio conjunto de información sobre el candidato. Se denomina predictor a la característica que debe tener una técnica de selección para predecir el comportamiento del candidato.

##### **Entrevista de selección**

La entrevista personal es el factor que más influye en la decisión final respecto de la aceptación o rechazo de un candidato al empleo. Debe ser conducida con gran habilidad y tacto para que pueda producir los resultados esperados.

En el enfoque sistémico el entrevistado es visto como una caja negra al que se le aplican determinados estímulos (inputs) para verificar sus reacciones (outputs).

Como todo proceso de comunicación, la entrevista adolece de todos los males (ruido, omisión/distorsión, sobrecarga y \-sobre todo- barreras) que enumeramos al estudiar la comunicación humana.

Entrenamiento de los entrevistadores: se intenta la eliminación de barreras personales y prejuicios para permitir la autocorrección y transformar la entrevista en un instrumento objetivo de evaluación. Para alcanzar esta meta todo entrevistador debe evitar sus prejuicios personales, no formular preguntas capciosas, escuchar y demostrar interés, hacer preguntas que conduzcan a respuestas narrativas, no emitir opiniones personales, evitar tomar notas durante la entrevista, entre otras cosas.

Construcción del proceso de la entrevista: Dependiendo de la habilidad del entrevistador puede tener mayor o menor libertad de conducción. Las entrevistas se clasifican según el formato de las preguntas y las respuestas requeridas.

* **Entrevista estandarizada por completo:** Entrevista estructurada, cerrada o dirigida, con un rumbo preestablecido, en que se invita al candidato a responder preguntas estandarizadas y elaboradas con anticipación.  
* **Entrevista estandarizada solo en cuanto a preguntas**: las preguntas se elaboran con anticipación, pero permiten respuesta abierta o libre.  
* **Entrevista dirigida (estandarizada en cuanto a respuestas):** no especifica las preguntas sino el tipo de respuesta deseada. El entrevistador debe saber formular las preguntas, de acuerdo con el desarrollo de la entrevista, para obtener el tipo de información requerida.  
* **Entrevista no dirigida:** no especifica las preguntas ni las respuestas requeridas. Se denominan entrevistas no dirigidas, no estructuradas, exploratorias, informales, etc.

**Etapas de la entrevista de selección** 

Su desarrollo comprende:  
**Preparación:** la entrevista no puede ser improvisada. Tendrá un tiempo definido y debe ser planeada para determinar: 

* Los objetivos específicos de la entrevista  
* El tipo de entrevista.  
* Lectura preliminar del curriculum vitae del candidato a entrevistar.  
* La mayor cantidad de información del candidato.  
* La mayor cantidad de información acerca del cargo a ocupar. 

Esta preparación es necesaria para que el entrevistador se informe respecto de los requisitos para ocupar el cargo, para que pueda comprobar la adecuación de las características personales del aspirante

**Ambiente (de la entrevista):** Puede ser de dos tipos.

* **Físico**: el local de la entrevista debe ser confortable y sólo para ese fin, sin ruidos ni interrupciones.  
* **Psicológico**: el clima de la entrevista debe ser ameno y cordial. 

En una entrevista, la espera es inevitable. En consecuencia, debe haber sillas suficientes en la sala de espera y periódicos, revistas y textos, en especial periódicos internos o información sobre la organización.

**Desarrollo de la entrevista:** Constituye la entrevista propiamente dicha. Implica dos personas que inician un proceso de relación interpersonal, cuyo nivel de interacción debe ser bastante elevado. El entrevistador envía estímulos (preguntas) al candidato, con el fin de estudiar las respuestas y reacciones en el comportamiento (retroalimentación), para poder elaborar nuevas preguntas (estímulos), y así sucesivamente.   
Así como el entrevistador obtiene la información que desea, debe proporcionar la que el aspirante requiere para tomar sus decisiones. 

Una parte importante de la entrevista consiste en darle información de la empresa y de la vacante existente. 

**Hay dos aspectos significativos**, el material y el formal:

* **Contenido de la entrevista:** constituye el aspecto material. El conjunto de información que el candidato suministra de sí mismo. Toda esa información reposa sobre el currículum vitae y/o en la solicitud de empleo.  
* **Comportamiento del candidato:** constituye el aspecto formal. Es la manera cómo reacciona. Lo que pretende este aspecto es tener un cuadro de las características del candidato, independientemente de sus calificaciones profesionales.  
* **Terminación de la entrevista:** la terminación de la entrevista debe ser cortés. El entrevistador debe hacer una señal clara para indicar que la entrevista terminó y debe proporcionarle al candidato información sobre la acción futura y cómo será contactado para saber el resultado.  
* **Evaluación del candidato:** A partir del momento en que el entrevistado se marcha, el entrevistador debe iniciar la tarea de evaluación del candidato. Al final deben tomarse ciertas decisiones: aceptado o rechazado y cuál es su posición respecto de los otros aspirantes al mismo cargo. Los datos que el candidato aporta y la manera como se comporta ayudan a proyectar una imagen de él. 

##### **Pruebas de conocimiento o de capacidad**

Son instrumentos para evaluar con **objetividad** el grado de **nociones, conocimientos y habilidades** adquiridos mediante el estudio, la práctica o el ejercicio.

Clasificación en cuanto a manera de aplicarlas

* Orales   
* Escritas   
* De realización

Clasificación en cuanto al área de conocimientos abarcados

* Generales: cuando tienen que ver con nociones de cultura o conocimientos generales   
* Específicas: cuando indagan conocimientos técnicos directamente relacionados con el cargo. 

Clasificación en cuanto a la manera como se elaboran las pruebas

* Pruebas tradicionales: de tipo discursivo o expositivo.  
* Pruebas objetivas: también denominadas test. Estructuradas en forma de exámenes objetivos, cuya aplicación y corrección son rápidas y fáciles. Podemos nombrar Verdadero – Faso, Si – No, espacios para completar, de selección múltiple, ordenamiento o apareamiento, etc.  
* Pruebas mixtas: Utilizan preguntas discursivas e ítems en forma de test.

##### **Pruebas psicométricas**

Designa un conjunto de pruebas que se aplica a las personas para apreciar su desarrollo mental, sus aptitudes, habilidades, conocimientos, etc. Es una medida **objetiva** y estandarizada de una muestra de **comportamiento**. Su función es analizar dichas muestras, examinarlas en condiciones estandarizadas y compararlas con patrones estadísticos.

En tanto las pruebas de conocimiento o capacidad miden la capacidad de realización de una persona, las pruebas psicométricas hacen énfasis en las aptitudes individuales.

La **aptitud** es innata y representa la predisposición o potencialidad de una persona para aprender determinada habilidad o comportamiento. Es decir, la aptitud es una habilidad latente o potencial en la persona, la cual puede ser desarrollada mediante ejercicio o práctica.

Por consiguiente, una prueba de conocimiento o de capacidad ofrece un diagnóstico real de las habilidades del candidato, en tanto que una prueba de aptitud proporciona un pronóstico futuro de su potencial de desarrollo. Las pruebas psicométricas presentan importantes características que las entrevistas no consiguen alcanzar: validez y precisión.

##### **Pruebas de personalidad**

Analizan los diversos rasgos determinados por el carácter (rasgos adquiridos) y por el temperamento (rasgos innatos). Un rasgo de personalidad es una característica marcada que distingue a una persona de las demás.

Se denominan genéricas o psicodiagnósticas cuando revelan los rasgos generales de personalidad en una síntesis global, y específica cuando investigan determinados rasgos o aspectos de la personalidad como equilibrio emocional, interés, frustraciones, etc.

##### **Técnicas de simulación**

Las técnicas de simulación tratan de pasar del tratamiento individual y aislado al tratamiento en grupo, y del método exclusivamente verbal o de ejecución a la acción social.

El aspirante es sometido a una situación de dramatización de algún acontecimiento generalmente relacionado con el futuro papel que desempeñará en la empresa, suministrando una expectativa más realista acerca de su comportamiento futuro en el cargo.

La simulación fomenta la retroalimentación y favorece el autoconocimiento y la autoevaluación. Las técnicas de simulación deben ser dirigidas por psicólogos y no por legos.

#### ***El proceso de selección***

La selección de personal funciona como un proceso compuesto de varias etapas secuenciales que atraviesan los candidatos. En las primeras etapas se encuentran las pruebas más sencillas y económicas y al final se hallan las pruebas más complejas y costosas.

Entre las principales alternativas de procesos de selección se encuentran:

* **Selección de una sola etapa:** las decisiones se basan en los resultados de una técnica de selección. Es el tipo más sencillo e imperfecto de selección.  
* **Selección secuencial en dos etapas:** se emplea cuando la información estudiada en el primer paso se juzga insuficiente para aceptar o rechazar el candidato. Se exige una decisión definitiva después de la segunda etapa.   
* **Selección secuencial en tres etapas:** incluye una secuencia de tres decisiones tomadas con base en tres técnicas de selección.  
* **Selección secuencial en cuatro o más etapas:** Emplea mayor cantidad de técnicas de selección. La principal ventaja de los planes secuenciales radica en la disminución del costo de la obtención de la información, que se efectúa por etapas, según la necesidad del caso. Los métodos secuenciales se recomiendan cuando las pruebas son muy costosas, como en el caso de las pruebas que exigen exámenes y evaluaciones individualizados

En las organizaciones saludables las entrevistas prevalecen sobre las pruebas (de aptitud o de personalidad) en la selección de las personas. Las pruebas no pierden su importancia y significado, sino que, por el contrario, sirven de apoyo a la conducción de las entrevistas y la toma de decisiones respecto de los candidatos.

##### **Evaluación y control de resultados**

El proceso selectivo debe ser eficiente y eficaz. La eficiencia consiste en hacer las cosas de manera correcta: saber entrevistar bien, aplicar pruebas de conocimientos que sean válidas y precisas, agilizar la selección, contar con un mínimo de costos operacionales, involucrar las gerencias y sus equipos en el proceso de selección de candidatos, etc. La eficacia consiste en lograr resultados y conseguir los objetivos: atraer los mejores talentos hacia la empresa y, sobre todo, mejorar la empresa cada vez más con las nuevas adquisiciones de personal.

Para medir la eficiencia del proceso, deberá establecerse la siguiente estructura de costos, la cual permite un análisis adecuado:

* **Costos de personal***.* Incluyen el personal que administra los procesos de provisión de personal.  
* **Costos de operación***.* Incluyen llamadas telefónicas, telegramas, correspondencia, honorarios de profesionales y de servicios involucrados, etc.  
* **Costos adicionales***.* Otros costos como equipos, software, mobiliario, instalaciones, etc.

Pueden sugerirse otras mediciones de rendimiento del proceso de provisión de personal:

* Costo de las operaciones de reclutamiento y selección   
* Costo por admisión   
* Costo por admisión por fuente de reclutamiento   
* Total de admisiones   
* Total de admisiones por fuente de reclutamiento   
* Calidad por fuente   
* Beneficios por fuente y eficiencia de la fuente, entre otros.

No obstante, el elevado costo operacional, la selección de personal trae importantes y enormes beneficios a la organización

* Acoplamiento del hombre al cargo y satisfacción con el empleo   
* Rapidez del nuevo empleado para integrarse y adaptarse a sus funciones   
* Mejoramiento del potencial humano   
* Reducción de la rotación del personal   
* Mayor rendimiento y productividad   
* Mejoramiento en las relaciones humanas   
* Menor inversión y esfuerzo en capacitación, debido a la mayor facilidad para aprender. 

La selección de personal también deja importantes beneficios para las personas:

* Aprovecha al máximo las habilidades y características de cada persona en el trabajo.  
* Lo anterior favorece el éxito potencial en el cargo.  
* Eleva la satisfacción de las personas porque encuentra la actividad más indicada para cada individuo.  
* Evita pérdidas futuras en la reubicación o la sustitución de personas, debido al fracaso probable en el cargo.

---

En resumen…  
![][image54]