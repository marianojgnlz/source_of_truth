<div id="interactive-exam-wrapper">
        <div class="container mx-auto max-w-5xl">
            <header class="text-center mb-8">
                <h1 class="text-4xl md:text-5xl font-extrabold text-slate-800">Guía de Estudio Interactiva</h1>
                <p class="text-xl text-slate-600 mt-2">Unidad 3: Subsistema de Aplicación</p>
            </header>

            <nav class="flex flex-wrap justify-center gap-2 md:gap-4 mb-8" id="section-nav">
                <button data-target="section-a" class="nav-button active w-full sm:w-auto text-sm md:text-base bg-white shadow-md hover:bg-cyan-600 hover:text-white py-2 px-4 rounded-full font-semibold">Sección SI/TI: Fundamentos</button>
                <button data-target="section-b" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-md hover:bg-cyan-600 hover:text-white py-2 px-4 rounded-full font-semibold">Sección SI/TI: Evaluación</button>
                <button data-target="section-c" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-md hover:bg-cyan-600 hover:text-white py-2 px-4 rounded-full font-semibold">Sección SI/TI: Planificación</button>
                <button data-target="section-d" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-md hover:bg-cyan-600 hover:text-white py-2 px-4 rounded-full font-semibold">Sección RRHH: Integración</button>
                <button data-target="section-e" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-md hover:bg-cyan-600 hover:text-white py-2 px-4 rounded-full font-semibold">Sección RRHH: Equipos y Evaluación</button>
            </nav>

            <main id="questions-container">
                <!-- Sections will be populated by JS -->
                <div id="section-a" class="question-set space-y-4"></div>
                <div id="section-b" class="question-set space-y-4 hidden"></div>
                <div id="section-c" class="question-set space-y-4 hidden"></div>
                <div id="section-d" class="question-set space-y-4 hidden"></div>
                <div id="section-e" class="question-set space-y-4 hidden"></div>
            </main>
        </div>
    </div>

<style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f9ff; /* Light blue background */
        }
        .nav-button {
            transition: all 0.3s ease-in-out;
            border: 1px solid transparent;
        }
        .nav-button.active {
            background-color: #0891b2; /* Cyan-700 */
            color: white;
            font-weight: 700;
            box-shadow: 0 4px 14px 0 rgba(8, 145, 178, 0.3);
            border-color: #0e7490;
        }
        .question-answer {
            display: none;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s ease-in-out, padding 0.5s ease-in-out;
        }
        .question-answer.visible {
            display: block;
            max-height: 1000px; /* Large enough for content */
            padding-top: 1rem;
        }
        .toggle-answer-btn {
            white-space: nowrap;
        }
        .question-card {
            border-left: 4px solid #0891b2;
        }
    </style>

<script>
        document.addEventListener('DOMContentLoaded', () => {
            const navContainer = document.getElementById('section-nav');
            const questionsContainer = document.getElementById('questions-container');
            
            const fullContent = {
                'section-a': [
                    { q: '1. Defina la interrelación fundamental entre "Carga", "Prestaciones" y "Rendimiento".', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Carga:</strong> Conjunto de demandas de los usuarios en un intervalo de tiempo.</li><li><strong>Prestaciones:</strong> Funcionalidades/servicios que brinda un SI.</li><li><strong>Rendimiento:</strong> Medida de cómo el SW utiliza el HW con una carga dada.</li></ul><p class="mt-2">El <strong>rendimiento</strong> solo puede medirse en el contexto de las <strong>prestaciones</strong> que ofrece bajo una <strong>carga</strong> específica. Un cambio en la carga afecta directamente el rendimiento medido.</p>' },
                    { q: '2. ¿Cuál es la finalidad esencial del subsistema de aplicación de SI/TI?', a: 'Su finalidad es <strong>disponer y administrar estratégicamente los recursos de SI/TI</strong> (HW y SW) en función de la carga de trabajo y los niveles de servicio requeridos para satisfacer el nivel de prestaciones de la organización.' },
                    { q: '3. ¿Por qué es inseparable el resultado de una medida de prestaciones de la carga?', a: 'Porque el rendimiento no es un valor absoluto, sino una respuesta del sistema a una demanda. Un sistema puede ser muy rápido con baja carga y muy lento con alta carga. Por tanto, cualquier índice de rendimiento carece de sentido si no se especifica la carga bajo la cual se obtuvo.' },
                    { q: '4. Proporcione un ejemplo de la interacción de la carga con su entorno.', a: 'Un sistema de e-commerce que sufre una sobrecarga masiva de peticiones (cambio en la carga) debido a una campaña de marketing viral en redes sociales (interacción con el entorno externo), lo que degrada el tiempo de respuesta para todos los usuarios.' },
                    { q: '5. ¿Qué significa que una carga está "correctamente caracterizada" y cuál es el primer paso?', a: 'Significa que ha sido descrita mediante un <strong>conjunto de parámetros cuantitativos</strong> relevantes. El primer paso indispensable es <strong>definir los objetivos</strong> del estudio, pues estos determinarán qué parámetros medir.' },
                    { q: '6. ¿Por qué elaborar un "Modelo de Carga" en lugar de usar la carga real?', a: 'Porque la carga real es <strong>fluctuante y no repetible</strong>, impidiendo experimentos controlados. Además, su uso comprometería la <strong>integridad y seguridad</strong> de los sistemas productivos. Un modelo permite replicar y controlar la carga de forma segura.' },
                    { q: '7. Diferencie entre carga de prueba Real y Sintética.', a: '<strong>Real:</strong> Se observa en un sistema en funcionamiento normal. Su principal inconveniente es que es fluctuante y no permite repeticiones.<br><strong>Sintética:</strong> Es un conjunto de programas que reproduce la carga real de forma compacta y controlable, permitiendo repeticiones y modificaciones.' },
                    { q: '8. ¿En qué se diferencian las cargas sintéticas Naturales de las Híbridas?', a: '<strong>Natural:</strong> Consta de programas extraídos de la carga real.<br><strong>Híbrida:</strong> Combina programas de una carga natural (para la parte conocida del sistema) con elementos artificiales (para modelar una carga que aún no existe). Un escenario viable es planificar la capacidad para una nueva app, usando la carga actual del sistema existente y simulando la nueva carga con programas artificiales.' },
                    { q: '9. Describa tres tipos de cargas de prueba Artificiales Ejecutables.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Mix:</strong> Mezcla de instrucciones para evaluar el rendimiento puro de la CPU.</li><li><strong>Kernel:</strong> Fragmento de programa real representativo de un tipo de trabajo específico.</li><li><strong>Programa sintético:</strong> Programa que no realiza trabajo útil, sino que consume recursos (CPU, E/S) para simular una carga real de forma flexible.</li></ul>' },
                    { q: '10. ¿Qué son las "Trazas para la simulación"?', a: 'Son una secuencia cronológica de <strong>eventos</strong> (cambios de estado en el sistema) registrada. Se clasifican como <strong>No Ejecutables</strong> porque no son programas, sino datos de entrada para un modelo de simulación.' },
                    { q: '11. Enumere cuatro características deseables de una carga de prueba.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Reproductibilidad:</strong> Poder repetir los experimentos obteniendo los mismos resultados.</li><li><strong>Compacidad:</strong> Reducir la duración del experimento en comparación con la carga real.</li><li><strong>Representatividad:</strong> Retener los aspectos importantes de la carga real.</li><li><strong>Flexibilidad:</strong> Poder variar los parámetros del modelo fácilmente.</li></ul>' },
                    { q: '12. Compare los sistemas de referencia: Por lotes, Transaccionales e Interactivos.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Por Lotes:</strong> Procesa trabajos de principio a fin sin intervención del usuario.</li><li><strong>Transaccionales:</strong> Procesa operaciones individuales (transacciones) de forma completa y atómica.</li><li><strong>Interactivos:</strong> El flujo es guiado por el usuario. El factor diferenciador es que <strong>la generación de una nueva petición depende de la recepción de la respuesta a la anterior</strong>.</li></ul>' },
                    { q: '13. ¿Cuáles son los dos índices característicos de un sistema por lotes?', a: '1) <strong>Turnaround Time (Tiempo de Retorno):</strong> Tiempo total desde que se lanza un trabajo hasta que finaliza.<br>2) <strong>Productividad:</strong> Cantidad de trabajo completado por unidad de tiempo.' },
                    { q: '14. Describa los tres componentes del "Tiempo de respuesta".', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Tiempo de Reacción:</strong> Desde que la petición llega hasta que empieza a procesarse.</li><li><strong>Tiempo de Ejecución:</strong> Tiempo efectivo de procesamiento.</li><li><strong>Tiempo de Retorno:</strong> Desde que se genera el resultado hasta que llega al usuario.</li></ul>' },
                ],
                'section-b': [
                    { q: '15. ¿Cuáles son los tres objetivos principales para evaluar el rendimiento?', a: '<ul class="list-disc list-inside space-y-2"><li>Verificar que el funcionamiento es el esperado.</li><li>Encontrar factores limitantes (cuellos de botella).</li><li>Predecir el comportamiento ante nuevas cargas.</li></ul>' },
                    { q: '16. Diferencie entre variables externas e internas.', a: '<strong>Externas:</strong> Perceptibles por el usuario (ej. Tiempo de respuesta, Productividad).<br><strong>Internas:</strong> Propias del sistema (ej. Utilización de CPU, Frecuencia de fallo de página).' },
                    { q: '17. Defina "Productividad" y "Capacidad". ¿Son sinónimos?', a: '<strong>Productividad:</strong> Cantidad de trabajo útil por unidad de tiempo bajo una carga dada.<br><strong>Capacidad:</strong> <strong>Máxima</strong> cantidad de trabajo útil por unidad de tiempo. No son sinónimos; la productividad es una medida puntual, la capacidad es el límite teórico del sistema.' },
                    { q: '18. ¿Qué mide el "Factor de utilización" y el "Solapamiento de componentes"?', a: '<strong>Factor de Utilización:</strong> Porcentaje de tiempo que un componente ha estado ocupado.<br><strong>Solapamiento:</strong> Porcentaje de tiempo que dos o más componentes han trabajado simultáneamente. Un alto solapamiento es bueno, indica paralelismo eficiente.' },
                    { q: '19. ¿Qué es el "Overhead" en el contexto de variables internas?', a: 'Es el porcentaje de tiempo que los recursos del sistema se utilizan en tareas propias del sistema operativo (gestión de memoria, planificación) que no son directamente atribuibles al trabajo útil de los programas de usuario. Es un costo de operación.' },
                    { q: '20. Defina "Fiabilidad", "Disponibilidad" y "Performabilidad".', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Fiabilidad:</strong> Probabilidad de que el sistema trabaje correctamente durante un intervalo.</li><li><strong>Disponibilidad:</strong> Probabilidad de que el sistema esté disponible en un instante.</li><li><strong>Performabilidad:</strong> Probabilidad de que las prestaciones estén por encima de un nivel deseado. Esta es la que incorpora una noción de nivel de prestación.</li></ul>' },
                    { q: '21. Enumere tres parámetros para caracterizar cada componente de la carga.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Tiempo de CPU por trabajo:</strong> Total de CPU que necesita un trabajo.</li><li><strong>Número de operaciones de E/S por trabajo:</strong> Cantidad de lecturas/escrituras a disco.</li><li><strong>Memoria:</strong> Cantidad de memoria (real y/o virtual) requerida.</li></ul>' },
                    { q: '22. Para el conjunto de la carga, ¿qué significan "Tiempo entre llegadas" y "Frecuencia de llegada"?', a: '<strong>Tiempo entre Llegadas:</strong> Intervalo entre dos peticiones sucesivas.<br><strong>Frecuencia de Llegada:</strong> Inversa del tiempo entre llegadas; mide cuántas peticiones llegan por unidad de tiempo (ej. peticiones/segundo).' },
                    { q: '23. En cargas conversacionales, explique la relación entre "Tiempo de reflexión" e "Intensidad del usuario".', a: 'El <strong>Tiempo de reflexión</strong> es lo que el usuario tarda en pensar su siguiente acción. La <strong>Intensidad del usuario</strong> es la relación entre el tiempo de respuesta y el tiempo de reflexión. Una alta intensidad implica un usuario que impone una mayor carga al sistema.' },
                ],
                'section-c': [
                    { q: '24. ¿Cómo impacta el ajuste del "Tamaño del quantum"?', a: '<strong>Quantum muy grande:</strong> Favorece a procesos largos (CPU-bound) pero perjudica a los interactivos.<br><strong>Quantum muy pequeño:</strong> Mejora la respuesta para procesos interactivos pero puede generar un <strong>overhead</strong> excesivo por el constante cambio de contexto.' },
                    { q: '25. Explique el concepto de "Factor de Multiprogramación".', a: 'Es el número máximo de trabajos que residen simultáneamente en memoria principal. Es clave porque si es muy bajo, se desaprovechan recursos, y si es muy alto, puede causar sobrecarga de memoria (thrashing).' },
                    { q: '26. ¿En qué consiste el "Equilibrado de la distribución de la carga"?', a: 'Consiste en distribuir el uso de los recursos del sistema de la manera más uniforme posible para evitar cuellos de botella. Puede lograr mejoras "espectaculares" porque al eliminar un cuello de botella se libera la capacidad de todo el sistema.' },
                    { q: '27. Al sustituir o ampliar componentes, ¿cuál es la consideración fundamental?', a: 'La consideración fundamental es <strong>eliminar el cuello de botella que se haya detectado</strong>. La inversión debe dirigirse al recurso que está limitando el rendimiento global.' },
                    { q: '28. Compare las técnicas de evaluación: Monitorización, Modelado y Benchmarking.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Monitorización:</strong> Para analizar un sistema real en producción.</li><li><strong>Modelado:</strong> Para evaluar un sistema que no existe o para predecir el efecto de cambios.</li><li><strong>Benchmarking:</strong> Para comparar diferentes sistemas de forma objetiva usando una carga estándar.</li></ul>' },
                    { q: '29. Explique la diferencia entre representatividad a nivel físico y funcional.', a: '<strong>Nivel Físico:</strong> El modelo consume recursos de hardware (CPU, disco) en las <strong>mismas proporciones</strong> que la carga real.<br><strong>Nivel Funcional:</strong> El modelo realiza las <strong>mismas funciones de negocio</strong> que la carga real, independientemente de los recursos físicos.' },
                    { q: '30. ¿Para qué campo es más adecuada la representatividad virtual? ¿Y la funcional?', a: '<strong>Virtual:</strong> Para estudios de <strong>ampliación</strong> de sistemas existentes.<br><strong>Funcional:</strong> Para la <strong>selección de un computador</strong> nuevo o planificación de capacidad a largo plazo.' },
                    { q: '31. Defina "Planificación de la capacidad" y el objetivo de un "plan de capacidad".', a: '<strong>Planificación de la capacidad:</strong> Proceso para identificar la configuración del sistema que dará un rendimiento satisfactorio a futuro.<br><strong>Objetivo del plan:</strong> Predecir cuellos de botella y proponer soluciones <strong>antes</strong> de que ocurra la saturación.' },
                    { q: '32. ¿Cuáles son los tres elementos que determinan una "capacidad adecuada"?', a: '1) <strong>Acuerdos de Nivel de Servicio (SLA):</strong> Los umbrales pactados.<br>2) <strong>La arquitectura del sistema:</strong> La tecnología específica.<br>3) <strong>El presupuesto:</strong> Las restricciones de coste.' },
                    { q: '33. Explique qué es un SLA y cómo se relaciona con la QoS.', a: 'Un <strong>SLA</strong> es un contrato que define umbrales medibles de servicio. La <strong>QoS</strong> (Calidad de Servicio) es la calidad percibida por el usuario. El SLA es la herramienta que se usa para <strong>cuantificar y formalizar</strong> la QoS.' },
                    { q: '34. Describa brevemente los niveles de gestión de la capacidad (0 al 5).', a: 'Van desde el <strong>Nivel 0 (ninguna gestión)</strong>, pasando por la medición y predicción manual (Nivel 1-2), hasta la <strong>predicción y ajuste automático</strong> basado en la carga (Nivel 3), los niveles de servicio (Nivel 4) y los criterios de negocio (Nivel 5).' },
                    { q: '35. Compare los métodos de predicción cuantitativos y cualitativos.', a: '<strong>Cuantitativos:</strong> Se basan en el análisis de <strong>datos históricos</strong> con modelos matemáticos.<br><strong>Cualitativos:</strong> Son un proceso <strong>subjetivo</strong> basado en la intuición y opiniones de expertos.' },
                    { q: '36. ¿Para qué patrón de datos es más adecuada la Regresión lineal? ¿Y las Medias móviles?', a: '<strong>Regresión Lineal:</strong> Para datos que muestran una <strong>tendencia</strong> clara (creciente o decreciente).<br><strong>Medias Móviles:</strong> Para datos que son casi <strong>estacionarios</strong> (fluctúan alrededor de una media constante).' },
                    { q: '37. Explique la diferencia de ponderación entre Suavizado exponencial y Medias móviles.', a: '<strong>Medias Móviles:</strong> Asigna un peso <strong>igual</strong> a todas las observaciones del periodo.<br><strong>Suavizado Exponencial:</strong> Asigna un peso <strong>mayor a las observaciones más recientes</strong>, asumiendo que el pasado cercano es mejor predictor.' },
                    { q: '38. ¿Qué es una "Unidad de Predicción Natural" (NFU)?', a: 'Es una <strong>variable de negocio</strong> (ej. "número de pólizas emitidas") cuyo valor está directamente relacionado con el consumo de recursos de SI/TI. Permite predecir la carga informática a partir de las previsiones de negocio.' },
                    { q: '39. Defina el concepto de "Capacidad bajo demanda".', a: 'Es la <strong>automatización de la asignación de la capacidad</strong> de recursos en tiempo de ejecución para cumplir con un SLA. Requiere un nivel de madurez <strong>3 o superior</strong>.' },
                    { q: '40. Mencione tres beneficios clave de la "Capacidad bajo demanda".', a: '<ul class="list-disc list-inside space-y-2"><li>Ahorro de personal en tareas manuales.</li><li>Diferimiento de la inversión en hardware.</li><li>Facilita la facturación por uso (pago por consumo).</li></ul>' },
                ],
                'section-d': [
                     { q: '41. Defina "Socialización organizacional". ¿Por qué es permanente?', a: 'Es el proceso de inculcar en los empleados los valores, normas y patrones de conducta de la organización. Es <strong>permanente</strong> porque la organización es un sistema dinámico y la adaptación es continua, no solo al ingresar.' },
                    { q: '42. Explique la dinámica de adaptación mutua en la socialización.', a: 'Es bidireccional: la <strong>organización</strong> intenta adaptar al individuo (socialización) y el <strong>individuo</strong> intenta adaptar su entorno para su satisfacción (personalización). El conflicto surge cuando estas dos fuerzas son divergentes.' },
                    { q: '43. Describa dos métodos para promover la socialización.', a: '1) <strong>Contenido inicial de la tarea:</strong> Asignar tareas retadoras pero alcanzables para generar éxito temprano y motivación.<br>2) <strong>Papel del gerente:</strong> El gerente actúa como la imagen de la organización, proporcionando guía y retroalimentación para facilitar la adaptación.' },
                    { q: '44. ¿Cuál es el objetivo principal de un "Programa de integración"?', a: 'Que el nuevo empleado <strong>asimile de manera rápida e intensiva la cultura organizacional</strong> en un entorno controlado para que se comporte como un miembro comprometido.' },
                    { q: '45. Defina el concepto de "Rol".', a: 'Es el conjunto de <strong>actividades y comportamientos que se solicitan a un individuo</strong> que ocupa una determinada posición en la organización. La empresa es un sistema de roles.' },
                    { q: '46. Describa el proceso de "Desempeño del rol".', a: '<ol class="list-decimal list-inside space-y-1"><li><strong>Expectativa del Rol:</strong> El jefe comunica lo que espera.</li><li><strong>Rol Percibido:</strong> El empleado interpreta esas expectativas.</li><li><strong>Comportamiento del Rol:</strong> El empleado ejecuta las tareas según su interpretación.</li><li><strong>Comportamiento Controlado:</strong> El jefe evalúa el desempeño y lo compara con la expectativa.</li></ol>' },
                    { q: '47. Explique dos discrepancias en el desempeño del rol.', a: '1) <strong>Discrepancia de la Expectativa:</strong> Falla de comunicación entre lo que el jefe transmitió y lo que el subordinado entendió.<br>2) <strong>Discrepancia con el Rol:</strong> Falla en la capacidad del empleado para ejecutar lo que entendió que debía hacer.' },
                    { q: '48. Compare el modelo mecánico y el modelo orgánico en la aplicación de personas.', a: '<strong>Mecánico:</strong> Énfasis en la <strong>eficiencia</strong>, rutinas fijas y factores higiénicos (salario).<br><strong>Orgánico:</strong> Énfasis en la <strong>eficacia</strong>, innovación, creatividad y factores motivacionales (desarrollo).' },
                    { q: '49. Defina "Tarea", "Atribución", "Función" y "Cargo".', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Tarea:</strong> Actividad individual y simple.</li><li><strong>Atribución:</strong> Actividad individual que implica decisión y responsabilidad.</li><li><strong>Función:</strong> Conjunto de tareas o atribuciones ejecutadas de forma sistemática.</li><li><strong>Cargo:</strong> Conjunto de funciones con una <strong>posición definida en la estructura organizacional</strong>.</li></ul>' },
                    { q: '50. ¿Cuáles son las cuatro condiciones fundamentales al diseñar un cargo?', a: '1) <strong>Contenido</strong> (qué hacer), 2) <strong>Métodos</strong> (cómo hacerlo), 3) <strong>Responsabilidad</strong> (a quién reportar), 4) <strong>Autoridad</strong> (a quién supervisar).' },
                    { q: '51. Describa la filosofía del Modelo clásico o tradicional.', a: 'Su filosofía era la <strong>máxima eficiencia</strong> a través de la simplificación y especialización. El resultado esperado era la eficiencia, pero el resultado real frecuente fue alta rotación, ausentismo y baja calidad.' },
                    { q: '52. ¿Cuál es la principal diferencia entre el Modelo clásico y el humanista?', a: 'El modelo <strong>humanista</strong> se centra en el <strong>contexto social del cargo y las necesidades humanas</strong> del empleado, buscando un ambiente amigable y participativo para aumentar la moral, a diferencia del enfoque mecanicista del modelo clásico.' },
                    { q: '53. ¿Qué tres variables convergen en el Modelo situacional?', a: '1) La estructura de la organización, 2) La tarea, y 3) La persona que la ejecutará.' },
                    { q: '54. Nombre tres de las cinco "dimensiones esenciales" de un cargo en el modelo situacional.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Variedad:</strong> Grado de diferentes habilidades y actividades para evitar la monotonía.</li><li><strong>Autonomía:</strong> Grado de independencia y criterio personal del empleado.</li><li><strong>Significado de la Tarea:</strong> Impacto reconocible del trabajo sobre otras personas.</li></ul>' },
                    { q: '55. ¿Qué tres estados psicológicos buscan generar estas dimensiones?', a: '1) Que el trabajo sea percibido como <strong>significativo</strong>.<br>2) Que la persona se sienta <strong>responsable</strong> por los resultados.<br>3) Que la persona <strong>conozca los resultados</strong> de su trabajo.' },
                    { q: '56. Diferencie enriquecimiento horizontal y vertical con un ejemplo.', a: '<strong>Horizontal:</strong> Añadir responsabilidades del mismo nivel. Ej: Un programador también realiza casos de prueba.<br><strong>Vertical:</strong> Añadir responsabilidades de nivel superior (planificación, control). Ej: Un programador decide la arquitectura de un módulo y supervisa a un junior.' },
                    { q: '57. ¿Cuál es la principal dificultad del enriquecimiento de cargos?', a: 'La <strong>resistencia al cambio</strong>, tanto de los empleados como de la propia organización si esta tiene una cultura que privilegia el status quo y el control estricto.' },
                    { q: '58. Diferencie entre Descripción y Análisis de cargos.', a: '<strong>Descripción:</strong> Pone énfasis en el <strong>contenido del cargo</strong> (qué hace, cómo, cuándo).<br><strong>Análisis:</strong> Pone énfasis en los <strong>requisitos que el cargo exige de su ocupante</strong> (formación, habilidades, responsabilidades).' },
                    { q: '59. ¿Cuáles son las cuatro áreas de requisitos en el Análisis de cargos?', a: '1) Requisitos Intelectuales, 2) Requisitos Físicos, 3) Responsabilidades Implícitas, y 4) Condiciones de Trabajo.' },
                    { q: '60. Compare los métodos de Observación directa y Cuestionario.', a: '<strong>Observación:</strong> Ventaja en veracidad, desventaja en costo y aplicabilidad a cargos complejos.<br><strong>Cuestionario:</strong> Ventaja en economía y alcance, desventaja en la calidad potencialmente superficial de las respuestas.' },
                    { q: '61. ¿Por qué el método de la entrevista puede ser el de mayor calidad? ¿Su desventaja?', a: 'Porque permite una <strong>interacción directa</strong> que facilita aclarar dudas y obtener datos ricos y detallados. Su principal desventaja es su <strong>elevado costo operativo</strong> en tiempo.' },
                ],
                'section-e': [
                    { q: '62. Defina "Equipo de trabajo". ¿Qué lo diferencia de un grupo formal?', a: 'Un equipo es un grupo de personas con habilidades complementarias, comprometidas con un propósito común y con <strong>responsabilidad mutua</strong>. Lo diferencia la sinergia y la responsabilidad colectiva: el resultado es mayor que la suma de las partes.' },
                    { q: '63. Mencione tres características de los equipos efectivos.', a: '1) <strong>Compromiso Unificado:</strong> Misión y metas compartidas.<br>2) <strong>Confianza Mutua:</strong> Confianza en la integridad y capacidad de los demás.<br>3) <strong>Buena Comunicación:</strong> Flujo de información abierto y honesto.' },
                    { q: '64. Describa tres características de un equipo de proyecto.', a: '1) Son creados <strong>a partir de la tarea</strong> (especialistas técnicos).<br>2) Tienen una <strong>existencia efímera</strong> (se disuelven al final).<br>3) Están <strong>subordinados al objetivo</strong> (la integración es un medio, no un fin).' },
                    { q: '65. Defina "Evaluación de desempeño". ¿Por qué es una "zona gris"?', a: 'Es la apreciación sistemática del desempeño de una persona. Es una "zona gris" porque sirve tanto para medir la <strong>integración</strong> de una persona (proceso de aplicación) como para el <strong>seguimiento y control</strong> continuo de los RRHH.' },
                    { q: '66. ¿Cuál es la diferencia de responsabilidad en la evaluación (Gerente vs. Empleado y Gerente)?', a: 'En el modelo <strong>"El Gerente"</strong>, la responsabilidad es unilateral del jefe. En el modelo <strong>"El Empleado y el Gerente" (APO)</strong>, la responsabilidad es compartida, se formulan objetivos por consenso y la evaluación se enfoca en el futuro.' },
                    { q: '67. Describa el concepto de "Evaluación de 360°".', a: 'Es un método donde la persona es evaluada por <strong>todo su entorno laboral</strong> (jefe, colegas, subordinados, etc.). Su característica distintiva es la multiplicidad de fuentes, que ofrece una visión más completa y balanceada.' },
                    { q: '68. Enumere los tres objetivos fundamentales de la evaluación de desempeño.', a: '1) Medir el <strong>potencial humano</strong>.<br>2) Tratar a los RRHH como una <strong>ventaja competitiva</strong>.<br>3) Dar <strong>oportunidades de crecimiento y participación</strong>.' },
                    { q: '69. Mencione dos beneficios para el jefe y dos para el subordinado.', a: '<strong>Para el Jefe:</strong> 1) Evaluar de forma más objetiva. 2) Proponer medidas de mejora.<br><strong>Para el Subordinado:</strong> 1) Conocer las expectativas y su desempeño. 2) Adquirir condiciones para la autoevaluación.' },
                    { q: '70. Compare el Método de las escalas gráficas con el de elección forzada.', a: 'El método de <strong>elección forzada</strong> intenta solucionar el problema de la <strong>subjetividad y el efecto de halo</strong> del método de escalas gráficas, al forzar al evaluador a elegir entre frases cuyo valor desconoce, impidiendo un sesgo consciente.' },
                    { q: '71. Explique cómo funciona el Método de investigación de campo.', a: 'Funciona a través de una <strong>entrevista de un especialista (staff) con el supervisor (línea)</strong>. El especialista asesora y guía, mientras que el supervisor aporta la información y participa en la planificación de mejoras.' },
                    { q: '72. ¿En qué consiste el Método de los incidentes críticos?', a: 'Consiste en registrar hechos o comportamientos <strong>excepcionalmente positivos (éxito) o negativos (fracaso)</strong>. Se enfoca en los extremos para identificar qué conductas reforzar y cuáles corregir.' },
                    { q: '73. Defina "Competencia".', a: 'Es una <strong>característica de una persona</strong> (innata o adquirida) que está relacionada con una <strong>actuación de éxito</strong> en un puesto de trabajo.' },
                    { q: '74. Explique el "Modelo de iceberg" de las competencias.', a: 'Representa las competencias en dos niveles: <strong>Visibles</strong> (destrezas, conocimientos), que son <strong>fáciles de detectar y desarrollar</strong>; y <strong>Sumergidas</strong> (motivación, valores, personalidad), que son <strong>difíciles de detectar y desarrollar</strong> pero impulsan el comportamiento a largo plazo.' },
                    { q: '75. ¿Cuál es el primer paso para implementar un sistema de gestión por competencias?', a: 'El primer paso indispensable es <strong>definir la visión y la misión de la empresa</strong>, para saber "hacia dónde vamos" y "qué hacemos" y así poder definir las competencias clave para lograrlo.' },
                ]
            };
            
            function createQuestionCard(item, index, sectionId) {
                const globalIndex = Object.values(fullContent).slice(0, Object.keys(fullContent).indexOf(sectionId)).flat().length + index + 1;
                return `
                    <div class="bg-white rounded-lg shadow-md p-4 sm:p-6 question-card">
                        <div class="flex justify-between items-start gap-4">
                            <h3 class="text-md sm:text-lg font-semibold text-slate-800">${item.q}</h3>
                            <button class="toggle-answer-btn text-sm bg-cyan-600 text-white py-2 px-4 rounded-full hover:bg-cyan-700 transition-colors duration-300 flex-shrink-0">Mostrar</button>
                        </div>
                        <div class="question-answer mt-4 border-t border-slate-200 text-slate-700 text-sm sm:text-base">${item.a}</div>
                    </div>`;
            }
            
            function renderQuestions() {
                for (const sectionId in fullContent) {
                    const sectionDiv = document.getElementById(sectionId);
                    if (sectionDiv) {
                        const content = fullContent[sectionId].map((item, index) => createQuestionCard(item, index, sectionId)).join('');
                        sectionDiv.innerHTML = content;
                    }
                }
            }

            function handleNavClick(event) {
                const targetButton = event.target.closest('.nav-button');
                if (!targetButton) return;

                const targetId = targetButton.dataset.target;
                
                questionsContainer.querySelectorAll('.question-set').forEach(set => {
                    set.classList.add('hidden');
                });

                navContainer.querySelectorAll('.nav-button').forEach(btn => {
                    btn.classList.remove('active');
                });

                const targetSet = document.getElementById(targetId);
                if (targetSet) {
                    targetSet.classList.remove('hidden');
                }
                targetButton.classList.add('active');
            }

            function handleToggleAnswer(event) {
                const targetButton = event.target.closest('.toggle-answer-btn');
                if (!targetButton) return;

                const card = targetButton.closest('.question-card');
                const answerDiv = card.querySelector('.question-answer');

                answerDiv.classList.toggle('visible');
                
                if (answerDiv.classList.contains('visible')) {
                    targetButton.textContent = 'Ocultar';
                } else {
                    targetButton.textContent = 'Mostrar';
                }
            }

            renderQuestions();
            navContainer.addEventListener('click', handleNavClick);
            questionsContainer.addEventListener('click', handleToggleAnswer);
        });
    </script>