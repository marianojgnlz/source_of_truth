<div id="interactive-exam-5-wrapper">
<style>
    .question-answer {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.5s ease-out;
    }
    .question-answer.visible {
        max-height: 2000px;
        transition: max-height 0.7s ease-in;
    }
    .nav-button.active {
        background-color: #0d6efd;
        color: #ffffff;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .nav-button {
         border: 1px solid #dee2e6;
    }
    #ai-modal-backdrop {
        transition: opacity 0.3s ease-in-out;
    }
    #ai-modal-panel {
        transition: all 0.3s ease-in-out;
    }
    .loader {
        border: 4px solid #f3f3f3;
        border-radius: 50%;
        border-top: 4px solid #3498db;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>
<div class="container mx-auto p-4 md:p-8">
    <header class="text-center mb-8">
        <h1 class="text-4xl md:text-5xl font-bold text-blue-800">Guía de Estudio Interactiva con IA</h1>
        <p class="text-xl text-slate-600 mt-2">Unidad 5: Subsistema de Seguimiento</p>
    </header>

    <nav class="flex flex-wrap justify-center gap-2 md:gap-4 mb-8" id="section-nav">
        <button data-target="section-a" class="nav-button active w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección A: Ley de Amdahl</button>
        <button data-target="section-b" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección B: Análisis Operacional</button>
        <button data-target="section-c" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección C: Carga y Evaluación</button>
        <button data-target="section-d" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección D: RRHH</button>
        <button data-target="section-e" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección E: Escenarios</button>
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

<!-- Modal para la IA -->
<div id="ai-modal" class="relative z-10 hidden" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <div id="ai-modal-backdrop" class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
  <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
      <div id="ai-modal-panel" class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
        <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
          <div class="sm:flex sm:items-start">
            <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
              <svg class="h-6 w-6 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 01-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 013.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 013.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 01-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.898 20.553L16.5 21.75l-.398-1.197a3.375 3.375 0 00-2.456-2.456L12.75 18l1.197-.398a3.375 3.375 0 002.456-2.456L16.5 14.25l.398 1.197a3.375 3.375 0 002.456 2.456L20.25 18l-1.197.398a3.375 3.375 0 00-2.456 2.456z" /></svg>
            </div>
            <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left w-full">
              <h3 class="text-base font-semibold leading-6 text-gray-900" id="ai-modal-title">Asistente de IA</h3>
              <div class="mt-2" id="ai-modal-content-wrapper">
                 <div id="ai-modal-loader" class="flex justify-center items-center py-8">
                    <div class="loader"></div>
                 </div>
                 <div class="text-sm text-gray-700 prose prose-sm max-w-none" id="ai-modal-content"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
          <button id="ai-modal-close-btn" type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cerrar</button>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const navContainer = document.getElementById('section-nav');
        const questionsContainer = document.getElementById('questions-container');
        const modal = document.getElementById('ai-modal');
        const modalTitle = document.getElementById('ai-modal-title');
        const modalContent = document.getElementById('ai-modal-content');
        const modalLoader = document.getElementById('ai-modal-loader');
        const closeModalBtn = document.getElementById('ai-modal-close-btn');

        // --- DATA SOURCE (Corrected and Complete) ---
        const fullContent = {
            'section-a': [
                { q: '1. Con tus propias palabras, diferencia entre <strong>Rendimiento</strong> y <strong>Prestaciones</strong> de un SI. ¿Cuál de los dos es más importante desde el punto de vista del negocio?', a: '<strong>Rendimiento:</strong> Es una medida técnica y objetiva de cómo un sistema utiliza sus recursos (HW/SW) ante una carga. Ej: MIPS, IOPS, MB/s.<br><strong>Prestaciones:</strong> Es la medida del grado de satisfacción de las necesidades de servicio del usuario. Es subjetiva y orientada a la experiencia. Ej: tiempo de respuesta bajo, sistema "rápido".<br><strong>Más importante:</strong> Las <strong>prestaciones</strong> son más importantes para el negocio, ya que impactan directamente en la productividad del empleado y la satisfacción del cliente.' },
                { q: '2. Nombra y describe brevemente <strong>tres razones</strong> fundamentales para evaluar las prestaciones de un sistema informático.', a: '1. <strong>Diseñar un sistema:</strong> Para crear una nueva arquitectura que cumpla con los objetivos de servicio.<br>2. <strong>Seleccionar y configurar:</strong> Para elegir la opción más adecuada de entre varias alternativas del mercado.<br>3. <strong>Planificar la capacidad:</strong> Para prever necesidades futuras y evitar la degradación del servicio a medida que la carga crece.<br>4. <strong>Sintonizar un sistema:</strong> Para optimizar un sistema existente y encontrar cuellos de botella.' },
                { q: '3. ¿Qué es la <strong>sintonización</strong> (tuning) de un sistema y cuál es su objetivo principal?', a: 'Es el proceso de ajustar los parámetros de configuración del hardware, sistema operativo o software de base para mejorar las prestaciones del sistema ante una carga de trabajo específica, adecuándolas a las necesidades de servicio. Su objetivo es eliminar cuellos de botella y optimizar el uso de los recursos existentes.' },
                { q: '4. Define el concepto de <strong>aceleración (speedup)</strong> en el contexto de la comparación de dos sistemas.', a: 'Es una medida cuantitativa que indica cuántas veces un sistema (o una versión mejorada) es más rápido que otro. Se calcula como `A = Tiempo_lento / Tiempo_rápido`.' },
                { q: '5. Explica la <strong>Ley de Amdahl</strong>. ¿Cuál es su propósito principal y qué limitación fundamental del rendimiento nos enseña?', a: 'Es una fórmula que permite predecir la máxima mejora de velocidad (aceleración) que se puede obtener en un sistema al mejorar solo una parte de él. Su propósito es ayudar a decidir dónde invertir los esfuerzos de optimización. Nos enseña que la mejora global está intrínsecamente limitada por la porción de la tarea que no se mejora.' },
                { q: '6. En la Ley de Amdahl, `A = 1 / ((1 - f) + (f / k))`, ¿qué representan `f` y `k`?', a: '<strong>f (fracción):</strong> Es la proporción del tiempo de ejecución original que se ve afectada por la mejora. Es un valor entre 0 y 1.<br><strong>k (factor de mejora):</strong> Indica cuántas veces más rápido es el componente mejorado. Es un valor mayor que 1.' },
                { q: '7. Según la Ley de Amdahl, si `f = 0`, ¿cuál es la aceleración? ¿Qué significa esto en la práctica?', a: 'Si `f = 0`, entonces `A = 1 / ((1-0) + (0/k)) = 1 / 1 = 1`. La aceleración es 1, lo que significa que no hay ninguna mejora. En la práctica, esto quiere decir que si mejoras un componente que nunca se usa, el rendimiento del sistema no cambia.' },
                { q: '8. Según la Ley de Amdahl, cuando el factor de mejora `k` tiende a infinito, ¿a qué valor tiende la aceleración `A`? ¿Qué nos dice esto sobre la importancia de la fracción no mejorada?', a: 'Cuando `k -> ∞`, el término `(f/k)` tiende a 0. La fórmula se convierte en `A = 1 / (1 - f)`. Esto demuestra que la aceleración máxima posible está limitada por la fracción del programa que no se optimiza (`1 - f`).' },
                { q: '9. ¿Cómo se generaliza la Ley de Amdahl para el caso en que se realizan mejoras en <strong>múltiples componentes</strong> del sistema simultáneamente?', a: 'La fórmula es: `A = 1 / ( (1 - Σfi) + Σ(fi / ki) )`. Donde `fi` es la fracción de tiempo del componente `i` y `ki` es su factor de mejora. Se suman los tiempos relativos de las partes mejoradas y no mejoradas.' },
                { q: '10. Un sistema tarda 10 segundos en ejecutar una tarea. El 60% de ese tiempo se dedica a cálculos de CPU. Si reemplazamos la CPU por una que es 3 veces más rápida, ¿cuál será la aceleración global del sistema?', a: 'f = 0.60, k = 3<br>A = 1 / ((1 - 0.60) + (0.60 / 3)) = 1 / (0.40 + 0.20) = 1 / 0.60 = <strong>1.67</strong><br>La aceleración global es de 1.67 veces.' },
                { q: '11. Siguiendo con la pregunta anterior, ¿cuál será el nuevo tiempo de ejecución de la tarea?', a: 'T_mejorado = T_original / A = 10s / 1.67 ≈ <strong>6 segundos</strong>.' },
                { q: '12. Si una mejora en el disco duro (k=4) produce una aceleración global en el sistema de A=2, ¿qué fracción de tiempo (`f`) se utilizaba el disco duro originalmente?', a: 'Usando la fórmula despejada: `f = k * (A - 1) / (A * (k - 1))`<br>`f = 4 * (2 - 1) / (2 * (4 - 1)) = 4 * 1 / (2 * 3) = 4 / 6 = 0.667`.<br>El disco se utilizaba el <strong>66.7%</strong> del tiempo.' },
                { q: '13. ¿Es posible que una mejora con un factor `k` pequeño produzca una mayor aceleración global que una mejora con un factor `k` mucho más grande? Justifica tu respuesta.', a: 'Sí. La Ley de Amdahl demuestra que la aceleración depende mucho más de la fracción `f` que del factor `k`. Mejorar 2 veces (`k=2`) un componente que se usa el 90% del tiempo (`f=0.9`) da una aceleración mucho mayor que mejorar 100 veces (`k=100`) un componente que se usa el 1% del tiempo (`f=0.01`).' },
                { q: '14. Al analizar una posible actualización, ¿por qué es útil calcular la relación <strong>prestaciones/coste</strong>?', a: 'Es útil para tomar decisiones de inversión informadas. Permite comparar alternativas no solo por su mejora técnica, sino por el "valor" que se obtiene por cada dólar invertido, ayudando a maximizar el retorno de la inversión.' },
                { q: '15. Si la Opción A cuesta $1000 y ofrece una aceleración de 2, y la Opción B cuesta $3000 y ofrece una aceleración de 4, ¿cuál ofrece una mejor relación prestaciones/coste?', a: 'Opción A: 2 / $1000 = 0.002 aceleración por dólar.<br>Opción B: 4 / $3000 ≈ 0.00133 aceleración por dólar.<br>La <strong>Opción A</strong> ofrece una mejor relación prestaciones/coste.' },
            ],
            'section-b': [
                { q: '16. ¿A qué se refiere el término <strong>"operacional"</strong> en "análisis operacional"?', a: 'Se refiere a que las variables y leyes utilizadas se basan en cantidades directamente medibles u observables durante un período de observación finito, sin hacer suposiciones sobre distribuciones estadísticas subyacentes.' },
                { q: '17. Define las cuatro variables operacionales básicas: `T`, `Ai`, `Ci`, `Bi`.', a: '`T`: Período de tiempo de la observación.<br>`Ai`: Número de arribos (llegadas) al dispositivo `i` durante `T`.<br>`Ci`: Número de trabajos completados (salidas) por el dispositivo `i` durante `T`.<br>`Bi`: Tiempo que el dispositivo `i` estuvo ocupado (busy time) durante `T`.' },
                { q: '18. A partir de las variables básicas, define: <strong>Tasa de Productividad (Xi)</strong>, <strong>Factor de Utilización (Ui)</strong> y <strong>Tiempo de Servicio (Si)</strong>.', a: '<strong>Productividad (Xi):</strong> `Ci / T` (Trabajos/tiempo).<br><strong>Utilización (Ui):</strong> `Bi / T` (Adimensional, %).<br><strong>Tiempo de Servicio (Si):</strong> `Bi / Ci` (Tiempo/trabajo).' },
                { q: '19. ¿Qué establece la <strong>hipótesis del flujo equilibrado de trabajos</strong> y por qué es importante para las leyes operacionales?', a: 'Establece que, para un período de observación largo, el número de trabajos que entran al sistema es igual al que sale (`Ai = Ci`). Es importante porque permite que el sistema se considere en un estado estable (`λi = Xi`), validando la aplicación de las leyes operacionales.' },
                { q: '20. Enuncia la <strong>Ley de la Utilización</strong>. ¿Qué relación establece?', a: '`Ui = Xi * Si`. Establece que la utilización de un dispositivo es igual a su productividad multiplicada por su tiempo de servicio.' },
                { q: '21. ¿Qué es la <strong>razón de visitas (Vi)</strong> a un dispositivo `i`?', a: 'Es el número promedio de veces que cada trabajo que pasa por el sistema visita el dispositivo `i`. Se calcula como `Vi = Ci / C0`.' },
                { q: '22. Enuncia la <strong>Ley del Flujo Forzado</strong>. ¿Qué nos dice sobre la relación entre la productividad de un componente y la productividad del sistema?', a: '`Xi = X0 * Vi`. Establece que la productividad (flujo) de un componente individual es directamente proporcional a la productividad (flujo) total del sistema, forzada por el número de visitas que cada trabajo hace a ese componente.' },
                { q: '23. Define la <strong>Demanda de Servicio (Di)</strong>. ¿Qué dispositivo se considera el cuello de botella en función de la demanda de servicio?', a: 'Es el tiempo total de servicio que un trabajo requiere de un dispositivo. `Di = Vi * Si`. El dispositivo con la mayor demanda de servicio (`D_max`) es el cuello de botella del sistema.' },
                { q: '24. Enuncia la <strong>Ley de Little</strong>. ¿Qué tres variables relaciona?', a: '`Ni = Xi * Ri`. Relaciona el número promedio de trabajos en un dispositivo (`Ni`), la productividad (`Xi`) y el tiempo de respuesta (`Ri`).' },
                { q: '25. ¿Para qué tipo de sistemas es especialmente útil la <strong>Ley del Tiempo de Respuesta Interactivo</strong>?', a: 'Es útil para sistemas interactivos con un número fijo de usuarios (`N`) y un tiempo de reflexión (`Z`), para calcular el tiempo de respuesta `R` que experimentan. La fórmula es `R = (N / X0) - Z`.' },
                { q: '26. Define los componentes de una <strong>estación de servicio</strong> en teoría de colas.', a: 'Está compuesta por una <strong>cola de espera</strong> (donde los trabajos aguardan) y uno o más <strong>servidores</strong> (que representan el recurso que procesa los trabajos).' },
                { q: '27. Diferencia entre <strong>tiempo de servicio</strong> y <strong>tiempo de respuesta</strong> en una estación de servicio.', a: '<strong>Tiempo de Servicio (S):</strong> El tiempo que el servidor tarda en procesar un trabajo, sin contar la espera.<br><strong>Tiempo de Respuesta (R):</strong> El tiempo total que un trabajo pasa en la estación, es decir, `R = Tiempo en Cola + Tiempo de Servicio`.' },
                { q: '28. Describe las características de una <strong>red de colas abierta</strong> y para qué se usa.', a: '<strong>Características:</strong> Los trabajos entran desde una fuente externa, se procesan y salen (desaparecen). El número de trabajos es variable.<br><strong>Uso:</strong> Sistemas transaccionales (servidor web, cajero automático).<br><strong>Índice Clave:</strong> El <strong>Tiempo de Respuesta (R)</strong>.' },
                { q: '29. Describe las características de una <strong>red de colas cerrada</strong> y para qué se usa.', a: '<strong>Características:</strong> Un número fijo de trabajos (`N`) circula constantemente por la red. <br><strong>Uso:</strong> Sistemas por lotes (batch) o interactivos.<br><strong>Índice Clave:</strong> La <strong>Productividad (X)</strong>.' },
                { q: '30. En un modelo de red cerrada para un sistema interactivo, ¿por qué la estación que representa el <strong>tiempo de reflexión (think time)</strong> se modela con infinitos servidores?', a: 'Porque conceptualmente un usuario no tiene que "hacer cola" para empezar a pensar. Cada usuario tiene su propio "servidor de pensamiento" paralelo e independiente, garantizando que no hay tiempo de espera.' },
                { q: '31. Si la utilización de la CPU es del 90% y la del disco es del 30%, ¿podemos afirmar categóricamente que la CPU es el único cuello de botella que importa? Argumenta.', a: 'No. Una alta utilización (U_cpu=90%) identifica a la CPU como el recurso más ocupado, pero el verdadero cuello de botella lo determina la <strong>Demanda de Servicio Total (D)</strong>. El disco, aunque menos utilizado, podría tener un tiempo de servicio (S_disco) muy alto o ser visitado muchísimas veces (V_disco alto), haciendo que su demanda (D_disco) sea el factor limitante.' },
                { q: '32. La productividad de un sistema (X0) es de 10 trabajos/seg. Cada trabajo visita la CPU 5 veces (V_cpu=5) y el Disco 20 veces (V_disco=20). Calcula la productividad de cada componente.', a: 'Usando la Ley del Flujo Forzado (`Xi = X0 * Vi`):<br>X_cpu = 10 * 5 = <strong>50 solicitudes/seg</strong>.<br>X_disco = 10 * 20 = <strong>200 E/S por segundo</strong>.' },
            ],
            'section-c': [
                { q: '33. ¿Por qué es necesario <strong>caracterizar la carga</strong> de un sistema? ¿Qué se busca obtener?', a: 'Es necesario para crear un <strong>modelo de carga</strong> (carga de prueba) que sea <strong>representativo</strong> de la carga real. Este modelo permite realizar experimentos controlados (benchmarks, simulaciones) para evaluar, comparar o sintonizar sistemas de forma fiable.' },
                { q: '34. Nombra y explica <strong>cuatro cualidades deseables</strong> de un modelo de carga. ¿Cuál es la más importante?', a: '1. <strong>Representatividad:</strong> El modelo debe comportarse como la carga real. <strong>Es la más importante.</strong><br>2. <strong>Reproductibilidad:</strong> Debe ser posible repetir el experimento y obtener los mismos resultados.<br>3. <strong>Compacidad:</strong> Debe ser manejable y no excesivamente grande.<br>4. <strong>Flexibilidad:</strong> Debe ser fácil modificar sus parámetros.' },
                { q: '35. Diferencia entre un modelo de carga <strong>físico</strong> y uno <strong>funcional</strong>.', a: '<strong>Físico:</strong> Se basa en el consumo de recursos de bajo nivel (tiempo de CPU, E/S de disco). Depende fuertemente del sistema.<br><strong>Funcional:</strong> Se basa en replicar las funciones de negocio que los usuarios realizan (ej. "guardar factura"). Es más independiente del sistema.' },
                { q: '36. Describe las <strong>tres fases</strong> para la implementación de un modelo de carga. ¿En qué fase es más probable que se cometan errores estratégicos?', a: '1. <strong>Formulación:</strong> Se definen los objetivos. Es la fase más crítica donde se pueden cometer errores estratégicos.<br>2. <strong>Construcción:</strong> Se miden los parámetros y se construye el modelo.<br>3. <strong>Validación:</strong> Se compara el modelo con la carga real para asegurar que es representativo.' },
                { q: '37. ¿Qué es un <strong>benchmark</strong>? Diferencia entre <strong>natural</strong> y <strong>artificial</strong>.', a: 'Un benchmark es un programa o conjunto de programas usados como carga de prueba estandarizada para medir y comparar prestaciones.<br><strong>Natural:</strong> Programas reales extraídos de la carga de trabajo de una empresa.<br><strong>Artificial/Sintético:</strong> Programas diseñados para medir un aspecto concreto del sistema.' },
                { q: '38. Menciona <strong>tres factores</strong> que pueden influir drásticamente en el resultado de un benchmarking.', a: '1. <strong>El Compilador</strong> y su nivel de optimización.<br>2. <strong>El Sistema Operativo</strong>, su versión y configuración.<br>3. <strong>El tamaño de la memoria Caché</strong> del procesador.' },
                { q: '39. ¿Cuál es uno de los errores más comunes en el benchmarking relacionado con la <strong>caché</strong>?', a: 'Ignorar sus efectos. Un benchmark que se ejecuta repetidamente puede beneficiarse de la caché, mostrando un rendimiento irreal que no se sostendrá con una carga real y variada.' },
                { q: '40. ¿Qué es la <strong>monitorización</strong> y cuál es su principal objetivo?', a: 'Es la técnica de observar, supervisar y registrar la actividad de un sistema informático mientras está en funcionamiento. Su objetivo es recoger datos para analizar el comportamiento e identificar cuellos de botella.' },
                { q: '41. ¿Qué es la <strong>interferencia o sobrecarga</strong> de un monitor? ¿En cuál suele ser mayor?', a: 'Es la perturbación que el propio monitor introduce en el sistema que está midiendo, al consumir recursos. Suele ser significativamente mayor en los <strong>monitores de software</strong>.' },
                { q: '42. Diferencia entre un monitor por <strong>detección de acontecimientos</strong> y por <strong>muestreo</strong>.', a: '<strong>Detección de Eventos:</strong> Se activa cada vez que ocurre un suceso específico. Es preciso pero puede generar alta sobrecarga.<br><strong>Muestreo (Sampling):</strong> Se activa a intervalos de tiempo fijos y registra el estado del sistema. Introduce menos sobrecarga pero puede perder eventos cortos.' },
                { q: '43. ¿Cuál es la principal ventaja y desventaja de un monitor <strong>hardware</strong> sobre uno <strong>software</strong>?', a: '<strong>Ventaja del HW:</strong> Interferencia casi nula.<br><strong>Desventaja del HW:</strong> Costoso, menos flexible y solo mide señales de bajo nivel.' },
                { q: '44. ¿Qué es el <strong>modelado</strong> como técnica de evaluación? ¿Cuándo es imprescindible su uso?', a: 'Es una técnica que utiliza un modelo matemático o lógico para estimar las prestaciones. Es imprescindible cuando se quiere evaluar un sistema que <strong>no existe o no está disponible</strong>.' },
                { q: '45. Compara las técnicas de modelado <strong>analíticas</strong> con las de <strong>simulación</strong>.', a: '<strong>Analítico:</strong><br><em>Ventaja:</em> Rápido y barato de resolver.<br><em>Desventaja:</em> Menos detallado, no modela comportamientos complejos.<br><strong>Simulación:</strong><br><em>Ventaja:</em> Puede modelar cualquier nivel de detalle.<br><em>Desventaja:</em> Costoso en tiempo de desarrollo y ejecución.' },
                { q: '46. ¿Qué técnica usarías para: a) seleccionar un servidor, b) diagnosticar lentitud, c) predecir el futuro?', a: 'a) <strong>Benchmarking:</strong> Para comparar sistemas existentes.<br>b) <strong>Monitorización:</strong> Para observar el sistema real en producción.<br>c) <strong>Modelado:</strong> Para predecir el comportamiento futuro con una carga que aún no existe.' },
                { q: '47. ¿Qué es un <strong>cuello de botella</strong> (bottleneck) en un sistema informático?', a: 'Es el recurso del sistema que tiene la mayor demanda de servicio y que, por lo tanto, limita la productividad o el tiempo de respuesta global del sistema.' },
                { q: '48. Describe brevemente el proceso de <strong>sintonización</strong> de un sistema. ¿Cuál es el primer paso?', a: 'Es un ciclo iterativo de mejora. El primer paso indispensable es la <strong>monitorización y análisis</strong> del sistema actual para <strong>identificar el cuello de botella</strong> principal.' },
            ],
            'section-d': [
                { q: '49. ¿Por qué se considera más complejo analizar el rendimiento de las personas que el de los recursos de SI/TI?', a: 'Por factores humanos subjetivos como la motivación, la moral, la resistencia al cambio, las relaciones interpersonales y la cultura organizacional, que no existen al analizar componentes predecibles de HW/SW.' },
                { q: '50. Define <strong>evaluación de desempeño</strong>. ¿Cuál es su finalidad principal?', a: 'Es el proceso sistemático de calificar la actuación de un empleado en su trabajo en relación con unos estándares preestablecidos. Su finalidad es identificar fortalezas y debilidades para tomar decisiones de mejora, formación, promoción o remuneración.' },
                { q: '51. Describe las <strong>cuatro etapas</strong> del proceso de control de Chiavenato.', a: '1. <strong>Establecimiento de estándares.</strong><br>2. <strong>Evaluación (medición) del desempeño.</strong><br>3. <strong>Comparación del desempeño con el estándar.</strong><br>4. <strong>Acción correctiva.</strong>' },
                { q: '52. ¿Qué es un <strong>estándar</strong> en el contexto del control de desempeño? Da un ejemplo de cada tipo.', a: 'Es una norma o un valor de referencia que representa el desempeño esperado.<br><strong>Cantidad:</strong> Producir 50 unidades/hora.<br><strong>Calidad:</strong> < 1% de defectos.<br><strong>Tiempo:</strong> Responder emails en < 24hs.<br><strong>Costo:</strong> Costo por adquisición < $50.' },
                { q: '53. Explica el principio de <strong>administración por excepción</strong>.', a: 'Postula que los gerentes deben enfocar su atención únicamente en las desviaciones significativas que se salen de la norma (excepciones), ignorando las variaciones menores.' },
                { q: '54. Si el desempeño real de un empleado está constantemente muy por encima del estándar, ¿qué podría indicar y qué acción se podría tomar?', a: 'Podría indicar que el <strong>estándar es demasiado bajo o poco exigente</strong>. La acción correctiva sería <strong>revisar y ajustar el estándar</strong> para que sea más desafiante pero alcanzable. También podría indicar un desempeño excepcional que merezca un reconocimiento.' },
                { q: '55. Para que el control sea eficaz, debe ser <strong>económico</strong>. ¿Qué significa esto?', a: 'Significa que el costo de implementar el control (medir, analizar, corregir) no debe superar el beneficio que se obtiene de él o el costo de la falla que se intenta evitar.' },
                { q: '56. ¿Por qué es crucial que los empleados <strong>acepten</strong> el proceso de control?', a: 'Porque si los empleados ven el control como algo punitivo o injusto, generarán resistencia y el proceso fracasará. Si lo aceptan como una herramienta de mejora, colaborarán y el control será efectivo.' },
                { q: '57. Define <strong>Auditoría de RRHH</strong>. ¿En qué se diferencia de la evaluación de desempeño individual?', a: 'Es el análisis sistemático de las políticas y prácticas de RRHH de toda la organización. Se diferencia en que su foco es el <strong>proceso de gestión (el sistema)</strong>, no el rendimiento de un individuo.' },
                { q: '58. Menciona <strong>tres áreas</strong> que evalúa una auditoría de RRHH.', a: '1. Eficacia de los procesos de reclutamiento y selección.<br>2. Cumplimiento de las normativas legales y laborales.<br>3. Nivel de satisfacción y clima laboral.' },
                { q: '59. Nombra <strong>tres técnicas</strong> para obtener información durante una auditoría de RRHH.', a: '1. Entrevistas (incluyendo entrevistas de salida).<br>2. Encuestas de clima u opinión.<br>3. Análisis de registros y estadísticas de personal (rotación, ausentismo).' },
                { q: '60. ¿Cuál es la función principal de una auditoría de RRHH respecto a las políticas y procedimientos?', a: 'Verificar si las políticas y procedimientos de RRHH existentes se están aplicando correctamente y si siguen siendo adecuados y efectivos para alcanzar los objetivos de la organización.' },
                { q: '61. ¿Qué es el <strong>control preventivo</strong>, <strong>detectivo</strong> y <strong>correctivo</strong>? Da un ejemplo de cada uno en RRHH.', a: '<strong>Preventivo:</strong> Una política clara de acoso laboral para evitar que ocurra.<br><strong>Detectivo:</strong> Una encuesta anónima que revela un problema de liderazgo.<br><strong>Correctivo:</strong> Implementar coaching para ese líder y medir la mejora.' },
                { q: '62. ¿Por qué podría ser útil auditar la "Filosofía de la administración" de la empresa?', a: 'Porque la filosofía (valores, metas) es la base de todas las políticas y prácticas. Si la filosofía es errónea o no está alineada con la estrategia, todos los procesos de RRHH que se deriven de ella serán ineficaces.' },
            ],
            'section-e': [
                {
                    isScenario: true,
                    title: '63. Escenario: Justificando una Inversión con la Ley de Amdahl',
                    scenario: 'El sistema de una financiera es lento. 80% del tiempo se consume en la BD, 20% en la lógica de negocio. Se proponen dos mejoras: A) Nueva BD 5 veces más rápida (costo $50k). B) Nuevo servidor de aplicaciones 10 veces más rápido (costo $20k). ¿Qué inversión es más rentable?',
                    answer: `
                        <div class="space-y-3">
                            <p><strong>a) Cálculo de Aceleración (A):</strong><br>
                            - <strong>Opción A (BD):</strong> f=0.8, k=5 &rarr; A = 1 / ((1-0.8) + (0.8/5)) = 1 / 0.36 &approx; <strong>2.78</strong><br>
                            - <strong>Opción B (Lógica):</strong> f=0.2, k=10 &rarr; A = 1 / ((1-0.2) + (0.2/10)) = 1 / 0.82 &approx; <strong>1.22</strong></p>
                            <p><strong>b) Cálculo Nuevo Tiempo (T_original = 2s):</strong><br>
                            - <strong>Opción A:</strong> T = 2s / 2.78 &approx; <strong>0.72s</strong><br>
                            - <strong>Opción B:</strong> T = 2s / 1.22 &approx; <strong>1.64s</strong></p>
                            <p><strong>c) Relación Prestaciones/Coste y Recomendación:</strong><br>
                            - <strong>Opción A:</strong> 2.78 / 50000 = 0.0000556<br>
                            - <strong>Opción B:</strong> 1.22 / 20000 = 0.0000610<br>
                            <strong>Recomendación:</strong> Aunque la Opción B es marginalmente más eficiente por dólar, no resuelve el problema de rendimiento. La <strong>Opción A</strong> es la única que ofrece una mejora drástica y tangible. La Ley de Amdahl nos enseña a atacar siempre la fracción más grande del problema (f=0.8). La recomendación debe ser la Opción A.</p>
                        </div>`
                },
                {
                    isScenario: true,
                    title: '64. Escenario: El Dilema del Cuello de Botella Oculto',
                    scenario: 'En un servidor web (T=100s), la CPU está ocupada 80s y completa 500 solicitudes (V_cpu=1). El Disco está ocupado 40s y completa 2000 E/S (V_disco=4). ¿Cuál es el verdadero cuello de botella?',
                    answer: `
                        <div class="space-y-3">
                           <p><strong>a) Cálculos Básicos:</strong><br>
                           - <strong>CPU:</strong> U=80%, X=5 req/s, S=0.16s/req<br>
                           - <strong>Disco:</strong> U=40%, X=20 E/S/s, S=0.02s/E-S</p>
                           <p><strong>b) Ley del Flujo Forzado (X0=5):</strong><br>
                           - <strong>CPU:</strong> 5 * 1 = 5. Se cumple.<br>
                           - <strong>Disco:</strong> 5 * 4 = 20. Se cumple.</p>
                           <p><strong>c) Análisis del Cuello de Botella (Demanda Total D = V * S):</strong><br>
                           - <strong>D_cpu:</strong> 1 * 0.16s = <strong>0.16s</strong><br>
                           - <strong>D_disco:</strong> 4 * 0.02s = <strong>0.08s</strong><br>
                           <strong>Conclusión:</strong> El recurso con la mayor demanda total es la <strong>CPU</strong> (0.16s > 0.08s). Por lo tanto, la CPU es el verdadero cuello de botella del sistema, a pesar de que la utilización del disco es menor.</p>
                        </div>`
                },
                 {
                    isScenario: true,
                    title: '65. Escenario: Modelando con Teoría de Colas',
                    scenario: 'Se diseñan dos sistemas: 1) Un Help Desk con tickets de soporte de toda la empresa. 2) Un clúster con un número fijo de 10 simulaciones científicas que se relanzan al terminar.',
                    answer: `<div class="space-y-3">
                           <p><strong>a) Elección del Modelo:</strong><br>
                           - <strong>Sistema 1 (Help Desk):</strong> Red de colas <strong>abierta</strong>. Los trabajos (tickets) llegan de una fuente externa y salen del sistema. El número de trabajos es variable.<br>
                           - <strong>Sistema 2 (Simulación):</strong> Red de colas <strong>cerrada</strong>. El número de trabajos (simulaciones) es constante y fijo (N=10) y recirculan continuamente.</p>
                           <p><strong>b) Índices de Prestaciones Clave:</strong><br>
                           - <strong>Red Abierta:</strong> El <strong>Tiempo de Respuesta (R)</strong>. Se busca resolver los tickets rápido.<br>
                           - <strong>Red Cerrada:</strong> La <strong>Productividad (X)</strong>. Se busca completar el mayor número de simulaciones posible.</p>
                           <p><strong>c) Estación con Infinitos Servidores:</strong><br>
                           Representa el <strong>tiempo de reflexión (Z)</strong>. Se usa porque la "preparación de la siguiente simulación" es un proceso que no requiere hacer cola; cada simulación tiene su propio "servidor de preparación" conceptual.</p>
                        </div>`
                },
                {
                    isScenario: true,
                    title: '66. Escenario: El Peligro de un Modelo de Carga No Representativo',
                    scenario: 'Un equipo técnico usa un modelo de carga físico ("tiempo total de E/S") para probar un nuevo almacenamiento, con excelentes resultados. En producción, el rendimiento es terrible porque los usuarios generan E/S aleatoria y pequeña, mientras la prueba usó E/S secuencial y grande.',
                    answer: `<div class="space-y-3">
                            <p><strong>a) Análisis del Fallo:</strong> El modelo fue <strong>no representativo</strong> porque ignoró el <strong>patrón de acceso</strong>. Un modelo <strong>funcional</strong> (simulando operaciones reales de usuario) o de <strong>comportamiento</strong> (enfocándose en el tiempo de respuesta) habría sido más adecuado.</p>
                            <p><strong>b) Proceso Correcto:</strong> En la fase de <strong>Formulación</strong>, las preguntas clave debieron ser: <em>¿Qué operaciones realizan nuestros usuarios? ¿Qué patrón de E/S generan? ¿El éxito se mide en IOPS o en tiempo de respuesta de la función "buscar cliente"?</em></p>
                            <p><strong>c) Rendimiento vs. Prestaciones:</strong> El sistema tenía un excelente <strong>rendimiento</strong> (medida técnica en MB/s) pero pésimas <strong>prestaciones</strong> (medida de satisfacción del usuario). El objetivo del seguimiento es mejorar las prestaciones.</p>
                        </div>`
                },
                {
                    isScenario: true,
                    title: '67. Escenario: Generalizando la Ley de Amdahl',
                    scenario: 'En el sistema del ejercicio 63 (f_bd=0.8, f_app=0.2), se decide implementar ambas mejoras simultáneamente: la nueva BD (k_bd=5) y el nuevo servidor de aplicaciones (k_app=10).',
                    answer: `<div class="space-y-3">
                            <p><strong>a) Cálculo con Ley Generalizada:</strong><br>
                            ` + "`A = 1 / ( Σ(fi / ki) ) = 1 / ( (0.8 / 5) + (0.2 / 10) )`" + `<br>
                            ` + "`A = 1 / ( 0.16 + 0.02 ) = 1 / 0.18 ≈ 5.56`" + `<br>
                            La aceleración global es de <strong>5.56 veces</strong>.</p>
                            <p><strong>b) Comparación:</strong> El resultado (5.56x) es significativamente mejor que las mejoras individuales (2.78x y 1.22x), demostrando un efecto sinérgico.</p>
                            <p><strong>c) El Nuevo Límite:</strong> Aunque se mejoró el 100% de la tarea, la aceleración está limitada por la <strong>distribución desigual del trabajo restante</strong>. El tiempo del componente de BD mejorado (0.16) sigue siendo 8 veces mayor que el de la lógica mejorada (0.02). La BD, aunque más rápida, sigue siendo el factor limitante relativo.</p>
                        </div>`
                }
            ]
        };
        
        // --- DYNAMIC RENDERING ---
        // This function creates the HTML for a single question card, now with AI buttons.
        function createQuestionCard(item, index) {
            const aiButtons = `
                <div class="flex items-center gap-2 mt-4 pt-4 border-t border-gray-200">
                    <span class="text-xs font-semibold text-gray-500">Asistente IA:</span>
                    <button title="Explicar Mejor" class="ai-explain-btn p-1.5 text-gray-500 hover:bg-blue-100 hover:text-blue-600 rounded-full transition-colors" data-index="${index}">💡</button>
                    <button title="Generar Pregunta Similar" class="ai-generate-btn p-1.5 text-gray-500 hover:bg-blue-100 hover:text-blue-600 rounded-full transition-colors" data-index="${index}">➕</button>
                </div>
            `;

            if (item.isScenario) {
                return `
                    <div class="bg-blue-50 border-l-4 border-blue-500 rounded-lg shadow-md p-6 question-card" data-question="${item.scenario}" data-answer="${item.answer}">
                        <h3 class="text-xl font-bold text-blue-900 mb-2">${item.title}</h3>
                        <p class="text-slate-700 mb-4">${item.scenario}</p>
                        <div class="flex justify-end items-start">
                            <button class="toggle-answer-btn text-sm bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors duration-300 flex-shrink-0">Mostrar Análisis</button>
                        </div>
                        <div class="question-answer mt-4 border-t border-blue-200 pt-4 text-slate-700">${item.answer}${aiButtons}</div>
                    </div>`;
            } else {
                return `
                    <div class="bg-white rounded-lg shadow-md p-6 question-card" data-question="${item.q}" data-answer="${item.a}">
                        <div class="flex justify-between items-start gap-4">
                            <h3 class="text-lg font-semibold text-gray-800">${item.q}</h3>
                            <button class="toggle-answer-btn text-sm bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors duration-300 flex-shrink-0">Mostrar Respuesta</button>
                        </div>
                        <div class="question-answer mt-4 border-t pt-4 text-slate-700">${item.a}${aiButtons}</div>
                    </div>`;
            }
        }
        
        function renderQuestions() {
            for (const sectionId in fullContent) {
                const sectionDiv = document.getElementById(sectionId);
                if (sectionDiv) {
                    const content = fullContent[sectionId].map((item, index) => createQuestionCard(item, `${sectionId}-${index}`)).join('');
                    sectionDiv.innerHTML = content;
                }
            }
        }

        // --- GEMINI API INTEGRATION ---
        async function callGeminiAPI(prompt) {
            modalContent.innerHTML = '';
            modalLoader.classList.remove('hidden');
            modal.classList.remove('hidden');

            const apiKey = ""; // Leave empty for automatic injection
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;
            
            let chatHistory = [{ role: "user", parts: [{ text: prompt }] }];
            const payload = { contents: chatHistory };

            try {
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    throw new Error(`Error en la API: ${response.statusText}`);
                }

                const result = await response.json();
                
                if (result.candidates && result.candidates.length > 0 &&
                    result.candidates[0].content && result.candidates[0].content.parts &&
                    result.candidates[0].content.parts.length > 0) {
                    const text = result.candidates[0].content.parts[0].text;
                    // A basic conversion of Markdown-like lists to HTML
                    const htmlText = text.replace(/\* \b/g, '<li>').replace(/(\r\n|\n|\r)/gm, "<br>");
                    modalContent.innerHTML = htmlText;
                } else {
                     modalContent.textContent = 'No se pudo obtener una respuesta válida de la IA.';
                }
            } catch (error) {
                console.error("Error al llamar a la API de Gemini:", error);
                modalContent.textContent = 'Hubo un problema al contactar al asistente de IA. Por favor, inténtalo de nuevo más tarde.';
            } finally {
                modalLoader.classList.add('hidden');
            }
        }


        // --- EVENT HANDLING ---
        function handleNavClick(event) {
            const targetButton = event.target.closest('.nav-button');
            if (!targetButton) return;
            const targetId = targetButton.dataset.target;
            questionsContainer.querySelectorAll('.question-set').forEach(set => set.classList.add('hidden'));
            navContainer.querySelectorAll('.nav-button').forEach(btn => btn.classList.remove('active'));
            const targetSet = document.getElementById(targetId);
            if (targetSet) targetSet.classList.remove('hidden');
            targetButton.classList.add('active');
        }

        function handleToggleAnswer(event) {
            const targetButton = event.target.closest('.toggle-answer-btn');
            if (!targetButton) return;
            const card = targetButton.closest('.question-card');
            const answerDiv = card.querySelector('.question-answer');
            answerDiv.classList.toggle('visible');
            const isScenario = card.matches('.bg-blue-50');
            const isVisible = answerDiv.classList.contains('visible');
            targetButton.textContent = isVisible ? (isScenario ? 'Ocultar Análisis' : 'Ocultar Respuesta') : (isScenario ? 'Mostrar Análisis' : 'Mostrar Respuesta');
        }

        function handleAiButtonClick(event) {
            const button = event.target.closest('.ai-explain-btn, .ai-generate-btn');
            if (!button) return;

            const card = button.closest('.question-card');
            const question = card.dataset.question;
            const answer = card.dataset.answer;
            
            let prompt = '';
            if (button.classList.contains('ai-explain-btn')) {
                modalTitle.textContent = 'Explicación del Concepto';
                prompt = `Actúa como un profesor experto en ingeniería de sistemas. Explica el concepto detrás de la siguiente pregunta y respuesta de una manera más sencilla y con una analogía del mundo real. Sé claro y conciso. Pregunta: "${question}". Respuesta: "${answer}"`;
            } else {
                modalTitle.textContent = 'Nueva Pregunta para Practicar';
                prompt = `Actúa como un profesor experto en ingeniería de sistemas creando un examen. Basado en la siguiente pregunta y respuesta, genera una nueva pregunta similar que evalúe el mismo concepto pero con un enfoque o datos diferentes. Provee únicamente la nueva pregunta y su correspondiente respuesta. Pregunta Original: "${question}". Respuesta Original: "${answer}"`;
            }
            
            callGeminiAPI(prompt);
        }

        // Initial setup
        renderQuestions();
        navContainer.addEventListener('click', handleNavClick);
        questionsContainer.addEventListener('click', (e) => {
            handleToggleAnswer(e);
            handleAiButtonClick(e);
        });
        closeModalBtn.addEventListener('click', () => modal.classList.add('hidden'));

    });
</script>
</div> 