<style>
        body {
            background-color: #f0f9ff;
        }
        .nav-button.active {
            background-color: #0891b2;
            color: white;
            font-weight: 600;
        }
        .question-answer {
            display: none;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s ease-in-out;
        }
        .question-answer.visible {
            display: block;
            max-height: 1000px; /* Adjust as needed */
        }
    </style>
<div id="interactive-exam-wrapper">
    <div class="container mx-auto max-w-5xl">
        <header class="text-center mb-8">
            <h1 class="text-4xl md:text-5xl font-bold text-cyan-800">Guía de Estudio Rigurosa</h1>
            <p class="text-xl text-slate-600 mt-2">Unidad 4: Subsistemas de Desarrollo y Mantenimiento de RRHH</p>
        </header>

        <nav class="flex flex-wrap justify-center gap-2 md:gap-4 mb-8" id="section-nav">
            <button data-target="section-a" class="nav-button active w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">A: Fundamentos del Desarrollo</button>
            <button data-target="section-b" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">B: El Proceso de Entrenamiento</button>
            <button data-target="section-c" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">C: Compensación y Equidad</button>
            <button data-target="section-d" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">D: Higiene, Seguridad y Relaciones</button>
            <button data-target="section-e" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">E: Desarrollo Organizacional</button>
            <button data-target="section-f" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">F: Escenarios de Aplicación</button>
        </nav>

        <main id="questions-container">
            <div id="section-a" class="question-set space-y-4"></div>
            <div id="section-b" class="question-set space-y-4 hidden"></div>
            <div id="section-c" class="question-set space-y-4 hidden"></div>
            <div id="section-d" class="question-set space-y-4 hidden"></div>
            <div id="section-e" class="question-set space-y-4 hidden"></div>
            <div id="section-f" class="question-set space-y-4 hidden"></div>
        </main>
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const navContainer = document.getElementById('section-nav');
        const questionsContainer = document.getElementById('questions-container');
        const questionSets = document.querySelectorAll('.question-set');
        const navButtons = document.querySelectorAll('.nav-button');

        const fullContent = {
            'section-a': [
                { q: '1. ¿Cuál es la finalidad fundamental del <strong>Desarrollo de RRHH</strong> y qué brecha busca disminuir?', a: 'Su finalidad es <strong>equilibrar las necesidades del cargo y la organización</strong> con el conjunto de competencias (conocimientos y habilidades) actuales y futuras de las personas. Busca <strong>disminuir la brecha</strong> entre las competencias de las personas y las necesidades de la organización, pensando siempre a futuro.' },
                { q: '2. Explique la diferencia conceptual entre <strong>entrenamiento</strong> y <strong>educación</strong> según el texto.', a: 'El <strong>entrenamiento</strong> tiene como propósito la preparación de la persona para el cargo específico que ocupa (corto plazo). En cambio, la <strong>educación</strong> tiene un propósito más amplio: preparar a la persona para enfrentar el ambiente dentro o fuera de su trabajo.' },
                { q: '3. Describa las tres etapas interdependientes de la <strong>educación profesional</strong>.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Formación profesional:</strong> Prepara al hombre para ejercer una profesión en general (objetivos amplios, largo plazo). Se imparte en escuelas y empresas.</li><li><strong>Perfeccionamiento o desarrollo profesional:</strong> Perfecciona al hombre para una carrera dentro de una profesión (mediano plazo). Se enfoca en una dedicación específica.</li><li><strong>Entrenamiento:</strong> Adapta al hombre para cumplir un cargo o función específica (corto plazo, puntual).</li></ul>' },
                { q: '4. ¿Qué es el <strong>aprendizaje</strong> y cuál es el rol del <strong>refuerzo</strong> en este proceso?', a: 'El aprendizaje es el proceso que permite adquirir conocimientos y modificar el comportamiento en respuesta a una experiencia. El <strong>refuerzo</strong> (recompensas o castigos) es crucial porque el individuo tiende a mantener un comportamiento que percibe como recompensador. Lo aprendido se olvida si no se practica y refuerza.' },
                { q: '5. El texto menciona siete "leyes del aprendizaje". Elija tres y explíquelas con sus propias palabras.', a: 'Ejemplo de respuesta: <ul class="list-disc list-inside space-y-2"><li><strong>Ley del efecto:</strong> Las personas repiten comportamientos que les traen consecuencias positivas.</li><li><strong>Ley de la frecuencia:</strong> La repetición constante de una práctica fortalece el aprendizaje.</li><li><strong>Ley del descongelamiento:</strong> Para aprender algo nuevo, a menudo es necesario "olvidar" o dejar atrás viejas costumbres, lo cual puede ser un proceso difícil.</li></ul>' },
                { q: '6. Compare un enfoque de entrenamiento <strong>reactivo</strong> con uno <strong>proactivo</strong> según el continuum de evaluación de los procesos de desarrollo.', a: 'Un enfoque <strong>reactivo</strong> se utiliza para resolver problemas o carencias que ya existen (corto plazo, apagar incendios). Un enfoque <strong>proactivo</strong> se orienta hacia el futuro, alineándose con la estrategia de la organización para anticipar necesidades y fomentar cambios definitivos (largo plazo, visión estratégica).' }
            ],
            'section-b': [
                { q: '7. Defina <strong>entrenamiento</strong> y nombre los cuatro tipos de cambio de comportamiento que puede incluir.', a: 'Es un proceso de educación a corto plazo, sistemático, mediante el cual las personas aprenden conocimientos, actitudes y habilidades para objetivos definidos. Puede incluir: <ul class="list-disc list-inside"><li>Transmisión de información</li><li>Desarrollo de habilidades</li><li>Desarrollo o modificación de actitudes</li><li>Desarrollo de conceptos</li></ul>' },
                { q: '8. Describa el <strong>ciclo del entrenamiento</strong> en sus cuatro etapas. ¿Quién es el responsable de línea en este proceso?', a: 'El ciclo consta de: 1) <strong>Diagnóstico</strong> (inventario de necesidades), 2) <strong>Programación</strong> (diseño del entrenamiento), 3) <strong>Ejecución</strong> (implementación), y 4) <strong>Evaluación</strong> de resultados. La responsabilidad de detectar las necesidades de entrenamiento recae en la <strong>línea</strong> (supervisores, gerentes).' },
                { q: '9. ¿Qué tres niveles de análisis se consideran para la <strong>detección de necesidades de entrenamiento</strong>?', a: '1. <strong>Análisis organizacional:</strong> Se enfoca en la estrategia, objetivos y cultura de toda la empresa para determinar dónde hacer énfasis. 2. <strong>Análisis de los recursos humanos:</strong> Verifica si la fuerza laboral es suficiente en cantidad y calidad. 3. <strong>Análisis de operaciones y tareas:</strong> Compara los requisitos del cargo con las habilidades actuales del ocupante.' },
                { q: '10. Diferencie entre <strong>indicadores a priori</strong> e <strong>indicadores a posteriori</strong> de necesidades de entrenamiento. Proporcione un ejemplo de cada uno.', a: 'Los <strong>indicadores a priori</strong> son eventos futuros que anticipan una necesidad (ej: la expansión de la empresa y la admisión de nuevos empleados). Los <strong>indicadores a posteriori</strong> son problemas actuales que revelan una necesidad no atendida (ej: baja productividad o un elevado número de accidentes).' },
                { q: '11. Al programar el entrenamiento, se deben responder 8 preguntas clave (qué, quién, cuándo, etc.). ¿Cuál considera usted la más importante y por qué?', a: 'Respuesta abierta, pero una buena justificación podría centrarse en: <strong>¿Para qué se debe entrenar?</strong> (Objetivos). Si no se tienen claros los objetivos, el resto de la planificación carece de dirección y es imposible medir el éxito del programa.' },
                { q: '12. ¿Cómo se puede evaluar el impacto del entrenamiento en el <strong>nivel organizacional</strong> y en el <strong>nivel de las tareas y operaciones</strong>?', a: 'En el <strong>nivel organizacional</strong>, se evalúa a través de mejoras en la imagen de la empresa, el clima organizacional o la eficacia general. En el <strong>nivel de las tareas</strong>, se mide por resultados concretos como el aumento de la productividad, la mejora en la calidad del servicio o la reducción del índice de accidentes.' },
            ],
            'section-c': [
                { q: '13. ¿Cuál es el objetivo del subsistema de <strong>mantenimiento de RRHH</strong>?', a: 'Su objetivo es <strong>retener al empleado adecuado, manteniéndolo satisfecho y motivado</strong>, induciéndolo a permanecer en la organización. Esto se logra mediante la compensación, beneficios, higiene, seguridad y relaciones laborales.' },
                { q: '14. Explique la <strong>Teoría de la Inequidad</strong>. ¿Qué sentimiento experimenta una persona cuando percibe que sus contribuciones/retribuciones son menores que las de otros?', a: 'La teoría postula que las personas comparan la relación entre sus contribuciones (esfuerzo, habilidades) y sus retribuciones (salario, reconocimiento) con la de sus pares. Si perciben que su relación es menor, experimentan un sentimiento de <strong>injusticia e insatisfacción</strong>.' },
                { q: '15. Diferencie entre <strong>compensación financiera directa</strong> e <strong>indirecta</strong>.', a: 'La <strong>directa</strong> es el pago recibido por el trabajo realizado (salario, bonos, comisiones). La <strong>indirecta</strong> es el "salario indirecto" que no está ligado directamente a la tarea, sino a la pertenencia a la organización (vacaciones, beneficios sociales, seguros).' },
                { q: '16. ¿Qué es el <strong>compuesto salarial</strong> y qué dos tipos de equilibrio busca la administración de salarios?', a: 'El compuesto salarial es el conjunto de factores internos (organizacionales) y externos (ambientales) que condicionan los salarios. La administración de salarios busca un <strong>equilibrio interno</strong> (equidad entre los cargos de la empresa) y un <strong>equilibrio externo</strong> (competitividad con el mercado laboral).' },
                { q: '17. Compare el <strong>método de jerarquización</strong> con el <strong>método de evaluación por puntos</strong> para la evaluación de cargos. ¿Cuál es analítico y cuantitativo, y por qué?', a: 'El <strong>método de jerarquización</strong> es no analítico y no cuantitativo; simplemente ordena los cargos de forma global. El <strong>método de evaluación por puntos</strong> es analítico (descompone el cargo en factores) y cuantitativo (asigna puntos a cada factor), lo que lo hace mucho más preciso y objetivo.' },
                { q: '18. ¿Cuál es la finalidad de una <strong>investigación salarial</strong>? Nombre dos criterios para seleccionar las empresas participantes.', a: 'Su finalidad es obtener información del mercado para asegurar el <strong>equilibrio externo</strong> de los salarios. Dos criterios para seleccionar empresas pueden ser: <strong>localización geográfica</strong> y <strong>sector industrial</strong> (comparar con empresas similares).' },
                { q: '19. Explique la diferencia fundamental entre <strong>remuneración fija</strong> y <strong>remuneración variable</strong>. ¿Por qué la variable no presiona los costos fijos de la empresa?', a: 'La <strong>remuneración fija</strong> (salario) se paga independientemente del desempeño. La <strong>remuneración variable</strong> (bonos, incentivos) depende de los resultados logrados. No presiona los costos fijos porque se autofinancia con el aumento de productividad o reducción de costos que la genera.' },
                { q: '20. ¿Cuál es la diferencia principal entre un <strong>incentivo</strong> y un <strong>premio/reconocimiento</strong>?', a: 'Un <strong>incentivo</strong> se pacta de antemano y no es discrecional (si se cumple la meta, se paga). Un <strong>premio</strong> se otorga después del hecho, se centra en el comportamiento y es <strong>discrecional</strong> (el jefe elige a quién y cómo recompensar).' },
                { q: '21. ¿Qué son los <strong>beneficios sociales</strong> y en qué se diferencian de la remuneración variable?', a: 'Son facilidades, comodidades y servicios que la empresa ofrece a todos los empleados por el hecho de pertenecer a ella (ej. seguro médico, comedor). Se diferencian de la remuneración variable en que <strong>no están ligados a metas ni resultados específicos</strong>.' },
            ],
            'section-d': [
                { q: '22. Defina <strong>higiene en el trabajo</strong> y <strong>seguridad en el trabajo</strong>, destacando su principal diferencia de enfoque.', a: 'La <strong>higiene</strong> se enfoca en la protección de la salud física y mental del trabajador, previniendo <strong>enfermedades ocupacionales</strong> a largo plazo mediante el control del ambiente. La <strong>seguridad</strong> se enfoca en prevenir <strong>accidentes</strong> a corto plazo, eliminando condiciones y actos inseguros.' },
                { q: '23. ¿Cuáles son los tres elementos más importantes de las <strong>condiciones ambientales de trabajo</strong> que aborda la higiene laboral?', a: '1. <strong>Iluminación:</strong> Debe ser suficiente, constante y uniformemente distribuida. 2. <strong>Ruido:</strong> La exposición prolongada a niveles elevados puede causar pérdida de audición. 3. <strong>Condiciones atmosféricas:</strong> Incluye la temperatura y la humedad del ambiente.' },
                { q: '24. ¿Qué es un <strong>accidente laboral</strong>? Describa la diferencia entre una <strong>condición insegura</strong> y un <strong>acto inseguro</strong> como causas de accidentes.', a: 'Un accidente laboral es un evento derivado del trabajo que provoca una lesión o daño. Una <strong>condición insegura</strong> es una falla física o mecánica del entorno (ej. un piso resbaladizo). Un <strong>acto inseguro</strong> es una violación de un procedimiento seguro por parte del trabajador (ej. no usar el equipo de protección).' },
                { q: '25. ¿Qué son las <strong>relaciones laborales</strong> y qué rol juegan los sindicatos en ellas?', a: 'Son las políticas y prácticas que rigen la relación entre la organización y sus empleados. Los <strong>sindicatos</strong> actúan como representantes de los trabajadores, negociando las condiciones de trabajo a través de procesos como la negociación colectiva.' },
                { q: '26. Compare una política de relaciones laborales <strong>autocrática</strong> con una <strong>participativa</strong>.', a: 'Una política <strong>autocrática</strong> es rígida, impositiva y unilateral; la empresa solo hace concesiones obligadas por ley. Una política <strong>participativa</strong> busca el consenso, involucra a trabajadores y sindicatos en la negociación, y se basa en datos objetivos para resolver problemas de manera preventiva.' },
                { q: '27. ¿Qué es una <strong>huelga</strong>? Describa dos formas ilícitas de acción sindical como el "tortuguismo" o el "paro por esmero".', a: 'La <strong>huelga</strong> es la paralización colectiva del trabajo para reivindicar mejores condiciones. El <strong>tortuguismo</strong> consiste en realizar el trabajo con una lentitud deliberada. El <strong>paro por esmero</strong> implica cumplir el trabajo con una minuciosidad tan exagerada que impide la marcha normal de la producción.' },
                { q: '28. ¿Cuál es la finalidad de un <strong>plan de carrera</strong> y qué dos necesidades busca equilibrar?', a: 'Su finalidad es delinear una sucesión organizada de puestos para el avance de los empleados. Busca equilibrar las <strong>necesidades de la organización</strong> (planificar sucesiones, retener talento) con las <strong>necesidades de desarrollo individuales</strong> de las personas (oportunidades de progreso y crecimiento profesional).' },
                 { q: '29. Describa la diferencia entre un <strong>movimiento ascendente</strong> y un <strong>movimiento lateral</strong> en un plan de carrera. ¿Qué es la rotación de puestos?', a: 'Un <strong>movimiento ascendente</strong> implica subir de nivel jerárquico. Un <strong>movimiento lateral</strong> es un cambio de tareas o puesto en el mismo nivel. La <strong>rotación de puestos</strong> es un tipo de movimiento lateral donde los empleados pasan por diferentes funciones para ganar una visión más completa de los procesos.' },
            ],
            'section-e': [
                { q: '30. ¿Qué es el <strong>Desarrollo Organizacional (DO)</strong> y en qué se diferencia del entrenamiento individual?', a: 'El DO es un programa educativo a largo plazo que busca mejorar la eficacia y los procesos de toda la organización, viéndola como un sistema. Se diferencia del entrenamiento en que su enfoque es <strong>macroscópico y sistémico</strong>, mientras que el entrenamiento es microscópico e individual.' },
                { q: '31. Nombre y explique dos <strong>fuerzas (una exógena y una endógena)</strong> que pueden impulsar un proceso de cambio organizacional.', a: '<strong>Exógena (externa):</strong> Una nueva tecnología que obliga a la empresa a adaptar sus procesos para no quedar obsoleta. <strong>Endógena (interna):</strong> La tensión generada por conflictos de intereses o de objetivos entre diferentes departamentos, que crea la necesidad de un cambio estructural o de comportamiento.' },
                { q: '32. El DO utiliza un <strong>agente de cambio</strong> y se basa en el <strong>aprendizaje experimental</strong>. ¿Qué significan estos dos conceptos?', a: 'Un <strong>agente de cambio</strong> es una persona (interna o externa) que estimula y coordina el cambio. El <strong>aprendizaje experimental</strong> significa que los participantes aprenden resolviendo problemas reales en un ambiente de entrenamiento, discutiendo y aprendiendo de esa experiencia práctica.' },
                { q: '33. ¿Cuál es el objetivo de la técnica de intervención de DO para individuos llamada <strong>entrenamiento de la sensibilidad (T-Groups)</strong>?', a: 'Su objetivo es aumentar la sensibilidad de una persona en sus relaciones interpersonales, desarrollando el autoconocimiento y la comprensión del impacto que su comportamiento tiene en los demás para mejorar la comunicación.' },
                { q: '34. ¿Para qué se utiliza la técnica de <strong>reuniones de confrontación</strong> en el DO?', a: 'Se utiliza para tratar conflictos entre dos grupos antagónicos. Permite que cada grupo se autoevalúe y evalúe al otro, facilitando una confrontación constructiva que lleva a la comprensión y al entendimiento mutuo.' },
                { q: '35. Describa brevemente el modelo de DO conocido como <strong>Red o Malla Gerencial (Managerial Grid)</strong>. ¿Qué dos preocupaciones busca equilibrar?', a: 'Es un modelo gráfico que analiza los estilos de liderazgo en base a dos ejes: la <strong>preocupación por la producción</strong> (eje horizontal) y la <strong>preocupación por las personas</strong> (eje vertical). Busca maximizar ambos, llevando a la organización hacia un desempeño de excelencia.' },
            ],
            'section-f': [
                {
                    isScenario: true,
                    title: '36. Escenario: Crisis de Productividad',
                    scenario: 'Una empresa de desarrollo de software nota una caída sostenida en la productividad y un aumento en los errores de código. Los gerentes sospechan que el problema no es técnico, sino de habilidades. Usted es el consultor de RRHH.',
                    answer: `<div class="space-y-4">
                        <div>
                            <h4 class="font-semibold text-teal-900">a) Diagnóstico y Proceso de Entrenamiento</h4>
                            <p><strong>1. Diagnóstico (Inventario de Necesidades):</strong> Se debe iniciar un diagnóstico utilizando <strong>indicadores a posteriori</strong> como la baja productividad y el exceso de errores. La acción principal es realizar un <strong>análisis de operaciones y tareas</strong> para identificar con precisión la brecha entre las competencias requeridas por los cargos y las que poseen actualmente los desarrolladores. Este análisis se complementaría con entrevistas a supervisores y la revisión de las últimas evaluaciones de desempeño.</p>
                            <p><strong>2. Programación:</strong> Con base en el diagnóstico, se diseñaría un programa de entrenamiento con el objetivo claro (<strong>¿para qué?</strong>) de "mejorar la calidad del código y la eficiencia en el desarrollo". El contenido (<strong>¿qué?</strong>) incluiría técnicas avanzadas de depuración, buenas prácticas de codificación (código limpio) y profundización en metodologías ágiles.</p>
                            <p><strong>3. Ejecución:</strong> Se utilizarían <strong>técnicas mixtas de entrenamiento</strong>, combinando teoría y práctica. Por ejemplo, sesiones de <strong>estudios de caso</strong> para analizar proyectos pasados con errores recurrentes y <strong>entrenamiento en el lugar de trabajo (on the job)</strong>, donde un desarrollador senior actúe como instructor en un módulo real.</p>
                            <p><strong>4. Evaluación:</strong> El impacto se mediría en el <strong>nivel de las tareas y operaciones</strong> a través de métricas concretas como la reducción del número de bugs por línea de código, el aumento de la productividad (story points por sprint), y la reducción del tiempo de retrabajo. En el <strong>nivel de los recursos humanos</strong>, se observaría un aumento en la eficiencia individual y en las competencias técnicas del equipo.</p>
                        </div>
                    </div>`
                },
                {
                    isScenario: true,
                    title: '37. Escenario: Fuga de Talentos y Equidad Salarial',
                    scenario: 'Una startup tecnológica está perdiendo a sus desarrolladores senior, quienes se van a competidores por mejores salarios. La empresa actualmente no tiene una estructura salarial formal y asigna sueldos de manera subjetiva durante la contratación.',
                    answer: `<div class="space-y-4">
                        <div>
                            <h4 class="font-semibold text-teal-900">a) Aplicación del Subsistema de Mantenimiento</h4>
                            <p>El problema central es una falla en el subsistema de mantenimiento, específicamente en la administración de la compensación. Se evidencia una falta de <strong>equilibrio externo</strong> (competitividad con el mercado) e <strong>interno</strong> (equidad entre cargos). El plan de acción sería:</p>
                            <ul class="list-decimal list-inside space-y-2">
                                <li>Para establecer el <strong>equilibrio interno</strong>, es imperativo realizar una <strong>evaluación de cargos</strong>. El <strong>método de evaluación por puntos</strong> es el más adecuado por ser analítico y cuantitativo, permitiendo diferenciar con objetividad los niveles de responsabilidad y habilidad (ej. Junior, Semi-Senior, Senior).</li>
                                <li>Para asegurar el <strong>equilibrio externo</strong>, se debe promover una <strong>investigación salarial</strong> del sector tecnológico en la misma localización geográfica.</li>
                                <li>Con estos datos, se debe crear una <strong>política salarial</strong> formal, estableciendo una estructura de franjas salariales para cada clase de cargo. Esto ataca directamente la <strong>Teoría de la Inequidad</strong>, pues los empleados percibirán que su remuneración es justa y lógica en comparación con sus pares y el mercado.</li>
                            </ul>
                        </div>
                        <div>
                            <h4 class="font-semibold text-teal-900">b) Plan de Carrera y Remuneración Variable</h4>
                            <p>Para complementar la política salarial y fomentar la retención, es crucial implementar dos herramientas adicionales:</p>
                             <ul class="list-disc list-inside space-y-2">
                                <li>Un <strong>plan de carrera</strong> transparente que delinee las rutas de crecimiento, mostrando los <strong>movimientos ascendentes</strong> posibles (ej. de Senior a Líder Técnico) y <strong>laterales</strong> (rotación a otros proyectos) para enriquecer sus habilidades. Esto equilibra las necesidades de la organización con las del individuo.</li>
                                <li>Introducir un esquema de <strong>remuneración variable</strong> con <strong>incentivos</strong> no discrecionales ligados al cumplimiento de metas de proyectos y <strong>premios</strong> discrecionales para reconocer desempeños excepcionales. Esto motiva el alto rendimiento sin presionar los costos fijos, ya que se autofinancia con la productividad.</li>
                            </ul>
                        </div>
                    </div>`
                },
                {
                    isScenario: true,
                    title: '38. Escenario: Conflicto Interdepartamental',
                    scenario: 'En una empresa manufacturera, el departamento de Ventas constantemente promete a los clientes plazos de entrega que el departamento de Producción considera irreales. Esto genera un clima de hostilidad, acusaciones mutuas y retrasos.',
                    answer: `<div class="space-y-4">
                        <div>
                            <h4 class="font-semibold text-teal-900">a) Diagnóstico y Enfoque de DO</h4>
                            <p>Este es un problema clásico de <strong>relaciones intergrupales</strong>. Las <strong>fuerzas de cambio son endógenas</strong>, originadas por un conflicto de objetivos e intereses entre departamentos. Un simple entrenamiento individual sería ineficaz. Se requiere un enfoque de <strong>Desarrollo Organizacional (DO)</strong>, que es macroscópico y sistémico. El proceso del DO comenzaría con una fase de <strong>recolección de datos</strong> (entrevistas en ambos departamentos para entender sus perspectivas y presiones) seguido de un <strong>diagnóstico organizacional</strong> que identifique las causas raíz del conflicto (falta de comunicación, metas desalineadas, etc.).</p>
                        </div>
                        <div>
                            <h4 class="font-semibold text-teal-900">b) Técnica de Intervención Específica</h4>
                            <p>La técnica de intervención de DO más apropiada aquí es la de <strong>reuniones de confrontación</strong>. Actuando como agente de cambio, facilitaría una sesión estructurada donde cada equipo (Ventas y Producción) se autoevalúe y evalúe al otro, exponiendo sus percepciones. El objetivo es transitar desde las acusaciones hacia una comprensión mutua de las presiones y limitaciones de cada área. Esta confrontación constructiva es la base para, posteriormente, desarrollar en conjunto procesos de planificación y comunicación que sean realistas y beneficiosos para toda la organización, no solo para un departamento.</p>
                        </div>
                    </div>`
                },
            ],
        };
        
        function createQuestionCard(item) {
            if (item.isScenario) {
                return `
                    <div class="bg-teal-50 border-l-4 border-teal-500 rounded-r-lg shadow-lg p-6">
                        <h2 class="text-xl font-bold text-teal-800 mb-2">${item.title}</h2>
                        <p class="text-slate-700 mb-4">${item.scenario}</p>
                        <div class="flex justify-end items-start">
                            <button class="toggle-answer-btn text-sm bg-cyan-600 text-white py-2 px-4 rounded-lg hover:bg-cyan-700 transition-colors duration-300 flex-shrink-0">Mostrar Análisis</button>
                        </div>
                        <div class="question-answer mt-4 border-t border-teal-200 pt-4 text-slate-700">${item.answer}</div>
                    </div>`;
            } else {
                return `
                    <div class="bg-white rounded-xl shadow-lg p-6">
                        <div class="flex justify-between items-start gap-4">
                            <h3 class="text-lg font-semibold text-cyan-900">${item.q}</h3>
                            <button class="toggle-answer-btn text-sm bg-cyan-600 text-white py-2 px-4 rounded-lg hover:bg-cyan-700 transition-colors duration-300 flex-shrink-0">Mostrar Respuesta</button>
                        </div>
                        <div class="question-answer mt-4 border-t pt-4 text-slate-700">${item.a}</div>
                    </div>`;
            }
        }
        
        function renderQuestions() {
            for (const sectionId in fullContent) {
                const sectionDiv = document.getElementById(sectionId);
                if (sectionDiv) {
                    const content = fullContent[sectionId].map(createQuestionCard).join('');
                    sectionDiv.innerHTML = content;
                }
            }
        }

        function handleNavClick(event) {
            const targetButton = event.target.closest('.nav-button');
            if (!targetButton) return;

            const targetId = targetButton.dataset.target;
            
            questionSets.forEach(set => {
                set.classList.add('hidden');
                set.querySelectorAll('.question-answer').forEach(ans => ans.classList.remove('visible'));
            });

            navButtons.forEach(btn => {
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

            const card = targetButton.closest('.bg-white, .bg-teal-50');
            const answerDiv = card.querySelector('.question-answer');

            answerDiv.classList.toggle('visible');
            
            const isScenario = card.matches('.bg-teal-50');

            if (answerDiv.classList.contains('visible')) {
                targetButton.textContent = isScenario ? 'Ocultar Análisis' : 'Ocultar Respuesta';
            } else {
                targetButton.textContent = isScenario ? 'Mostrar Análisis' : 'Mostrar Respuesta';
            }
        }

        renderQuestions();
        navContainer.addEventListener('click', handleNavClick);
        questionsContainer.addEventListener('click', handleToggleAnswer);
    });
</script>