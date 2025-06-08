#### ***4- Recuperación ante el desastre*** {#4--recuperación-ante-el-desastre}

```mermaid
graph TD
    A["Recuperación ante el Desastre"] --> B{Planificación de Contingencia};
    B --> C["Definición de planes para la supervivencia y operación de la empresa tras una interrupción"];
    B --> D["Incluye metodología para recuperar el grado de prestaciones"];

    A --> E{Conceptos Clave};
    E --> F["<b>Tiempo de inhabilitación:</b><br/>Tiempo hasta que los sistemas vuelven a estar disponibles"];
    E --> G["<b>Respaldo:</b><br/>Mantener funcionamiento con sistemas críticos hasta la normalidad"];
    E --> H["<b>Reinstalación:</b><br/>Actualizar sistemas con datos generados durante la inactividad"];

    A --> I{Primer Paso};
    I --> J["Clasificar sistemas y aplicaciones por necesidad de negocio (tolerancia)"];
    J --> K["Crítico (tolerancia muy baja)"];
    J --> L["Vital (tolerancia moderada)"];
    J --> M["Sensible (tolerancia flexible)"];
    J --> N["No crítico (tolerancia amplia)"];

    A --> O{Soluciones de Respaldo (Backup)};
    O --> P["<b>Instalaciones de emergencia (Hot Sites):</b><br/>Todo instalado, operatividad inmediata"];
    O --> Q["<b>Instalaciones intermedias (Warm Sites):</b><br/>Centro de datos equipado pero vacío, más lento que Hot Site"];
    O --> R["<b>Instalaciones móviles:</b><br/>Provisión desde vehículos o edificaciones prefabricadas"];

    A --> S{Niveles de Emergencia};
    S --> T["<b>Catástrofe:</b><br/>Destrucción de instalaciones, requiere instalación alternativa"];
    S --> U["<b>Desastre:</b><br/>Interrupción > 1 día, posibilidad de reanudar en sede original"];
    S --> V["<b>No desastre:</b><br/>Interrupciones breves, fallas no graves"];

    A --> W{Contenido del Plan de Contingencia};
    W --> X["Orden de prioridades de recuperación"];
    W --> Y["Mecanismos de acoplamiento manual"];
    W --> Z["Disponibilidad de hardware y telecomunicaciones de respaldo"];
    W --> AA["Sede alternativa para almacenamiento"];
    W --> BB["Metodologías de recuperación (pasos, responsables, tiempos)"];
```

**Planificación de la contingencia**, debo tener siempre uno pensado. Es la definición de una serie de planes que permita que la empresa sobreviva a una situación que le exija parar las operaciones, es decir, que pueda seguir operando. **Además debe acompañarse de la metodología para recuperar ese grado de prestaciones**. Tener en cuenta:

-   Cuánto tiempo puedo pasar sin operar.
-   El grado de respaldo o mantenimiento que tengo.
-   Situaciones que puedan ser de re-instalación de sistemas.
-   Cuál es la tolerancia del sistema a quedar paralizado.

La planificación de contingencias incluye planes para métodos de trabajo que permitan que la empresa sobreviva al desastre, y para procesos a largo plazo a fin de que la organización se recupere. La primera etapa consiste en incrementar la seguridad, minimizar los daños y facilitar el regreso al trabajo. En la segunda etapa se minimizan los efectos secundarios del desastre. Los tiempos relacionados con estas etapas son:

-   **Tiempo de inhabilitación**: cantidad de tiempo antes de que los sistemas vuelvan a estar disponibles para las operaciones.
-   **Respaldo**: mantener el funcionamiento de la empresa a través de los sistemas claves (críticos y vitales) hasta que se vuelva a la normalidad.
-   **Reinstalación**: sistemas de actualización con todos los datos generados durante el tiempo de inactividad de la sede central.

El primer paso de la planificación de contingencias consiste en clasificar los sistemas y aplicaciones **de acuerdo a la necesidad de operaciones empresariales** (grado de tolerancia). Esta clasificación permite establecer prioridades entre los elementos de los SI. El plan de recuperación debe cubrir todos los aspectos del uso y del management de los SI.

|     | Crítico | Vitales | Sensibles | No críticos |
| :---: | :---: | :---: | :---: | :---: |
| **Tolerancia a la interrupción** | Muy baja (costo de interrupción muy alto) | Moderada (costo de interrupción ligeramente menor) | Flexible (costos tolerables) | Amplia (costo escaso o costo adicional nulo) |
| **Reemplazo de funciones** | No pueden ser reemplazadas por métodos manuales | Puede ejecutarse manualmente por periodos breves | Pueden realizarse en forma manual por períodos relativamente largos.Exige mano de obra adicional | Pueden reemplazarse con poco esfuerzo (manualmente) |

Como la planificación de contingencias es parte del management estratégico de los SI, no se la puede separar de otros aspectos de gerenciamiento del uso de los SI y **debe ser considerada junto con otros temas de la selección y la implementación de estrategias.**

Existen **dos problemas importantes en la planificación ante desastres:** la dificultad de mantenerse actualizado con los tiempos de desastre, y la dificultad de mantenerse actualizado con los cronogramas de prioridades.

**Las soluciones de respaldo** (disponibilidad de hardware alternativo) pueden clasificarse en:

-   **Instalaciones de emergencia**: en las que todo lo que posibilita el funcionamiento de IS ya está instalado; permiten una operatividad inmediata, siempre y cuando los backups de datos estén disponibles.
-   **Instalaciones intermedias**: un centro de datos vacío pero equipado se encuentra disponible. Son menos costosas que el anterior pero su puesta en actividad es más lenta.
-   **Instalaciones móviles**: la provisión se realiza desde vehículos o desde edificaciones prefabricadas semi-móviles.

*Todos los enfoques de desarrollo de los SI **deben ofrecer puntos de recuperación.***

##### **Niveles de emergencia**

-   **Catástrofe**: Se trata de interrupciones en la capacidad de procesamiento provocadas por la destrucción de instalaciones de los componentes físicos que las integran. En estos casos, se requiere acudir, transitoriamente, a otra instalación alternativa de configuración similar a la destruida. Simultáneamente, debe comenzarse a equipar una nueva instalación que, a muy corto plazo, tenga capacidad de procesamiento continuo del servicio de procesamiento de datos. Este reequipamiento incluye los dispositivos de conexión a telecomunicaciones. Se pierde todo.
-   **Desastres**: Se trata de interrupciones en la capacidad de procesamiento de información durante un período superior a un día, pero con altas posibilidades de reanudar las mismas en las instalaciones originales luego de superados los inconvenientes causantes de la interrupción. Se deberá recurrir a una instalación de procesamiento alternativa utilizando copias de software y de archivos de datos conservados fuera de la sede original. La instalación alternativa deberá estar disponible todo el tiempo que dure la interrupción. Pérdida parcial.
-   **No desastre**: Se trata de interrupciones breves. Son provocadas por mal funcionamiento de algún dispositivo o por fallas en el software no detectadas anteriormente y que requieren inmediata corrección. Hubo fallas, pero no graves.

**Todo sistema tiene un lapso crítico de recuperación.** Este es el periodo o tiempo hasta dónde puede extenderse una interrupción antes de que se presente el riesgo de incurrir en pérdidas. Es la naturaleza del negocio y de los sistemas lo que condiciona este lapso crítico.

##### **Contenido de un Plan de Contingencia**

1.  Determinación del **orden de prioridades** en materia de recuperación de aplicaciones, software de base y archivos de datos según el grado de tolerancia.
2.  Detalle del **orden de procesamiento de tareas complejas**.
3.  **Mecanismos de acoplamiento manual** durante interrupciones cortas.
4.  Tener en cuenta los equipos de **todo el ambiente informático** y no solo las unidades centrales. El personal debe ser entrenado.
5.  Disponibilidad de hardware alternativo **(backup)**:
    1.  **Centro duplicado de procesamiento** de información de propiedad de la misma empresa (para aplicaciones críticas). Es costoso.
    2.  **Centros de procesamiento ubicados en otra sede** (por contratos con 3ros). En función del tiempo de activación y costos se pueden clasificar en:
        1.  **Hot Sites:** son instalaciones completas, configuradas de manera similar a la sede primaria y pueden activarse rápidamente.
        2.  **Warm Sites:** son instalaciones parcialmente configuradas en las que generalmente falta la unidad central de procesamiento. Dado que esta unidad es el dispositivo más costoso, esta alternativa es más económica.
        3.  **Cold Sites:** son lugares físicos que se encuentran en condiciones de recibir el equipamiento necesario, pero no dispone de instalaciones específicas.
6.  Disponibilidad de la **capacidad de telecomunicaciones:**
    1.  Rutas **alternativas**.
    2.  Rutas **diversificadas**. Alternativas y en distinto lugar físico.
7.  Disponibilidad de una **sede alternativa para el almacenamiento** de medios magnéticos y documentación.

**Metodologías de recuperación**: conjunto de pasos a seguir en situaciones de emergencia, los responsables y los tiempos.

-   Protección de la vida humana
-   Evaluación de daños y estimación de tiempo necesario para la recuperación.
-   Coordinación de las actividades de recuperación; recuperar datos vitales y críticos y reconstruir la base de datos; instalar y probar el software en una sede alternativa.
-   Recuperación de la red de telecomunicaciones.
-   Administración de condiciones de seguridad.
-   Gestión de aspectos legales derivados de la emergencia. 