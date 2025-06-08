<div id="interactive-exam-wrapper">
    <div class="container mx-auto">
        <header class="text-center mb-8">
            <h1 class="text-4xl md:text-5xl font-bold text-blue-800">Guía de Estudio Interactiva</h1>
            <p class="text-xl text-slate-600 mt-2">Unidad 2: Subsistema de Provisión</p>
        </header>

        <nav class="flex flex-wrap justify-center gap-2 md:gap-4 mb-8" id="section-nav">
            <button data-target="section-a" class="nav-button active w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección A: Fundamentos de Provisión y Canales de SW</button>
            <button data-target="section-b" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección B: Evaluación y Selección de Soluciones</button>
            <button data-target="section-c" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección C: Provisión de Hardware y Plataformas</button>
            <button data-target="section-d" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección D: Provisión de Recursos Humanos (RRHH)</button>
            <button data-target="section-e" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-blue-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección E: Escenarios Prácticos</button>
        </nav>

        <main id="questions-container">
            <div id="section-a" class="question-set space-y-4"></div>
            <div id="section-b" class="question-set space-y-4 hidden"></div>
            <div id="section-c" class="question-set space-y-4 hidden"></div>
            <div id="section-d" class="question-set space-y-4 hidden"></div>
            <div id="section-e" class="question-set space-y-4 hidden"></div>
        </main>
    </div>
</div>

<style>
    .question-answer {
        display: none;
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
    }
    .question-answer.visible {
        display: block;
        opacity: 1;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const navContainer = document.getElementById('section-nav');
        const questionsContainer = document.getElementById('questions-container');
        const questionSets = document.querySelectorAll('.question-set');
        const navButtons = document.querySelectorAll('.nav-button');

        const fullContent = {
            'section-a': [
                { q: '1. Compare y contraste los enfoques de conversión "Paralelo" y "En Fases". ¿En qué tipo de proyecto o sistema recomendaría cada uno y por qué, considerando el impacto en el riesgo, costo y la gestión del cambio organizacional?', a: 'El enfoque <strong>Paralelo</strong> implica ejecutar el sistema nuevo y el antiguo simultáneamente por un período, comparando resultados. Es ideal para sistemas críticos (ej. contabilidad, finanzas) donde la continuidad y la precisión son vitales. Reduce el riesgo de fallas catastróficas, pero es el más costoso en recursos (doble carga de trabajo, hardware). El enfoque <strong>En Fases</strong> introduce el nuevo sistema por módulos o áreas funcionales. Es adecuado para sistemas grandes y complejos que pueden ser segmentados (ej. un ERP). Permite una gestión del cambio más gradual y un aprendizaje progresivo, distribuyendo el riesgo y el costo a lo largo del tiempo, aunque extiende la duración total del proyecto de implementación.' },
                { q: '2. Una organización define una característica como "Altamente Deseable" pero no "Obligatoria". ¿Cómo impacta esta decisión en el proceso de selección de un paquete de software y qué flexibilidad le otorga al proveedor y a la empresa?', a: 'Esta decisión introduce flexibilidad en el proceso. No descarta a un proveedor si no cumple con ella, a diferencia de una "Obligatoria". Permite a la empresa evaluar un rango más amplio de soluciones y a los proveedores ofrecer alternativas que quizás no cumplan al 100% pero compensan en otras áreas (costo, tecnología). En la <strong>técnica de puntaje y calificación</strong>, a esta característica se le asignaría un peso (valor de importancia) menor que a las obligatorias pero significativo. Durante la evaluación, se calificaría qué tan bien cada oferta cumple con esta característica, y el puntaje resultante (peso x calificación) contribuiría al puntaje total de la propuesta, permitiendo una comparación objetiva entre ofertas que cumplen lo esencial pero varían en lo deseable.' },
                { q: '3. El desarrollo interno se considera una opción para aplicaciones de alto impacto estratégico. Sin embargo, ¿cuáles son los tres riesgos más significativos inherentes a esta ruta de provisión y qué medidas de control son cruciales para mitigarlos?', a: '<ul class="list-disc list-inside space-y-2"><li><strong>1. Desviación de Costos y Plazos:</strong> Es el riesgo más común. Se mitiga con un <strong>control de proyecto efectivo</strong>, usando metodologías ágiles (Scrum, Kanban) para entregas incrementales, monitoreo continuo del valor ganado (EVM) y una gestión de alcance rigurosa.</li><li><strong>2. Incertidumbre Técnica:</strong> La complejidad inherente y la rápida evolución tecnológica pueden hacer que la solución sea obsoleta antes de terminarla. Se mitiga considerando el desarrollo como un <strong>proceso de producción de software</strong>, utilizando arquitecturas modulares, microservicios, y herramientas de integración y despliegue continuo (CI/CD) para adaptarse al cambio.</li><li><strong>3. Dificultad para Retener Talento:</strong> La alta demanda de personal calificado puede llevar a la pérdida de miembros clave del equipo. Se mitiga creando una cultura de desarrollo sólida, ofreciendo planes de carrera, capacitación continua y un ambiente de trabajo que fomente la innovación y el compromiso.</li></ul>' },
                { q: '4. Al adquirir un paquete estándar, surge una disparidad con los procesos de negocio. Analice críticamente las cuatro estrategias para manejar esta disparidad. ¿Cuál considera la más arriesgada y cuál la más alineada con una estrategia de "mejores prácticas"?', a: 'Las cuatro estrategias son: <strong>1. Adecuar el paquete:</strong> La más arriesgada. Implica modificar el código fuente del paquete, lo que generalmente invalida la garantía, el soporte y complica futuras actualizaciones. Es costosa y técnicamente compleja. <strong>2. Modificar el proceso empresarial:</strong> La más alineada con "mejores prácticas". Implica adaptar los flujos de trabajo de la empresa a la lógica del paquete, que a menudo encapsula las mejores prácticas de la industria. Requiere una fuerte gestión del cambio pero puede llevar a mejoras significativas en la eficiencia. <strong>3. Tolerar el desajuste:</strong> Viable solo si la funcionalidad faltante no es crítica. Es una solución temporal que puede generar ineficiencias a largo plazo. <strong>4. Complementar el paquete:</strong> Una opción pragmática. Se desarrolla una funcionalidad adicional (ej. un microservicio) que se integra con el paquete a través de APIs, sin alterar su núcleo. Es un buen equilibrio si la modificación del proceso no es factible.' },
                { q: '5. Explique la tensión inherente entre los objetivos de un contrato de outsourcing y la capacidad de innovación de una organización. ¿Bajo qué condiciones un outsourcing de "management completo de servicios" podría sofocar la agilidad tecnológica de la empresa?', a: 'La tensión reside en que el outsourcing busca <strong>eficiencia, estandarización y reducción de costos</strong> a través de un servicio definido en un contrato (SLA), mientras que la innovación requiere <strong>flexibilidad, experimentación y asunción de riesgos</strong>, aspectos difíciles de predefinir contractualmente. Un outsourcing de "management completo" puede sofocar la agilidad cuando: <ul class="list-disc list-inside space-y-2"><li><strong>El contrato es demasiado rígido:</strong> Si el SLA penaliza cualquier desviación de los procesos acordados, desincentiva la prueba de nuevas tecnologías o enfoques.</li><li><strong>El proveedor carece de cultura innovadora:</strong> Si el socio de outsourcing se enfoca únicamente en cumplir el contrato al menor costo, no propondrá mejoras proactivamente.</li><li><strong>La empresa pierde capacidades internas:</strong> Al tercerizar todo, la empresa puede perder el conocimiento técnico y de negocio ("aptitudes esenciales") necesario para identificar y evaluar oportunidades de innovación tecnológica.</li></ul>' }
            ],
            'section-b': [
                { q: '6. En el "Análisis de probabilidad de éxito y riesgo" para seleccionar un canal de provisión, describa un escenario donde un riesgo de "baja probabilidad" pero "alto impacto" debería descartar una alternativa.', a: 'Un escenario clásico es la <strong>quiebra del proveedor de un software crítico</strong>. Al evaluar un paquete de una startup innovadora (Alternativa A) vs. un paquete de un proveedor establecido (Alternativa B), la probabilidad de que la startup quiebre puede ser baja, pero si el software gestiona el núcleo del negocio (ej. sistema de producción), el <strong>impacto sería catastrófico</strong>: pérdida de soporte, datos inaccesibles, paralización de operaciones. Aunque la Alternativa A tenga un puntaje superior en funcionalidad y costo, el riesgo de "alto impacto" de discontinuidad del negocio debería llevar a la organización a descartarla en favor de la alternativa B, que aunque menos innovadora, ofrece mayor estabilidad y menor riesgo existencial.' },
                { q: '7. ¿Cuál es la diferencia fundamental entre los costos primarios, secundarios y terciarios de la rotación de personal? Proporcione un ejemplo concreto de un costo terciario en un departamento de TI.', a: 'La diferencia es su grado de tangibilidad e inmediatez. Los <strong>costos primarios</strong> son directos y cuantificables (ej. costo del proceso de selección y reclutamiento). Los <strong>costos secundarios</strong> son intangibles y cualitativos, relacionados con el impacto inmediato (ej. pérdida de productividad mientras el nuevo empleado aprende). Los <strong>costos terciarios</strong> son los efectos colaterales a mediano y largo plazo, solo estimables. <strong>Ejemplo de costo terciario en TI:</strong> La rotación constante en un equipo de desarrollo de un producto clave lleva a una <strong>pérdida de la "memoria técnica" del proyecto</strong>. Las decisiones de arquitectura importantes no están documentadas y solo existían en la cabeza de los que se fueron. Esto provoca que el nuevo personal tome decisiones que introducen deuda técnica o vulnerabilidades de seguridad, lo que a largo plazo se traduce en un <strong>aumento exponencial de los costos de mantenimiento y una menor velocidad para lanzar nuevas funcionalidades</strong>, afectando la competitividad del negocio.' },
                { q: '8. Al evaluar paquetes de SW, los criterios de "Flexibilidad" y "Performance" suelen estar en conflicto. Explique esta relación y cómo se utilizaría el Método de Evaluación Manual (MEM) para encontrar un equilibrio.', a: 'La relación es conflictiva porque, a menudo, una mayor <strong>Flexibilidad</strong> (capacidad de personalización, configuración de flujos de trabajo, agregado de campos) implica una arquitectura más compleja con más capas de abstracción y consultas a la base de datos, lo que puede degradar la <strong>Performance</strong> (velocidad de respuesta, capacidad de transacciones por segundo). Para equilibrarlos con el <strong>MEM</strong>: <ul class="list-disc list-inside space-y-2"><li><strong>Ponderación:</strong> En la "Tabla de Ponderación", se asignarían pesos a ambos criterios según la necesidad del negocio. Un sistema de back-office podría priorizar la flexibilidad, mientras que un sistema transaccional de cara al cliente priorizaría la performance.</li><li><strong>Evaluación Objetiva:</strong> En el "Cuestionario", se definirían parámetros medibles para cada uno. Para Performance: "Tiempo de respuesta en carga máxima (ms)". Para Flexibilidad: "¿Permite crear campos personalizados sin código? (Sí/No)".</li><li><strong>Análisis de Resultados:</strong> La "Planilla de Evaluación" calcularía la calificación ponderada. Un paquete podría tener una calificación alta en flexibilidad pero baja en performance. El resultado final del MEM no solo daría un puntaje total, sino que permitiría visualizar este trade-off, ayudando al equipo a tomar una decisión informada sobre qué están dispuestos a sacrificar.</li></ul>' },
                { q: '9. Dentro de un RDP, ¿por qué la sección "Descripción de la Aplicación" es tan crítica? Describa tres elementos detallados que debe incluir para evitar propuestas ambiguas.', a: 'Es crítica porque es la sección que traduce las necesidades del negocio en requerimientos funcionales para el proveedor. Si es ambigua, las propuestas serán incomparables y probablemente no satisfagan la necesidad real. Tres elementos detallados cruciales son: <ul class="list-disc list-inside space-y-2"><li><strong>1. Diagramas de Flujo de Procesos de Negocio (As-Is y To-Be):</strong> No basta con describir textualmente. Un diagrama de flujo (ej. BPMN) del proceso actual ("As-Is") y del proceso futuro deseado ("To-Be") clarifica inequívocamente la secuencia de actividades, los roles involucrados y los puntos de decisión.</li><li><strong>2. Casos de Uso Detallados:</strong> Para cada función principal, se deben describir casos de uso que especifiquen: Actor, Precondiciones, Flujo Principal (pasos exitosos), Flujos Alternativos (excepciones) y Postcondiciones. Esto elimina la ambigüedad sobre cómo debe comportarse el sistema.</li><li><strong>3. Requerimientos No Funcionales Cuantificados:</strong> Describir requerimientos como "el sistema debe ser rápido" es inútil. Deben ser cuantificados. Ejemplo: "El tiempo de respuesta para la búsqueda de clientes no debe exceder los 500 ms con 100 usuarios concurrentes". Otros ejemplos: disponibilidad (99.95%), volumen de datos a manejar, estándares de seguridad a cumplir (ej. ISO 27001).</li></ul>' },
                { q: '10. Compare el "Leasing simple" con el "Leasing con derecho a compra". ¿Qué opción sería más estratégica para una startup tecnológica que necesita equipamiento de última generación pero quiere mantener la opción de modificar el hardware?', a: 'La opción más estratégica para la startup sería el <strong>Leasing con derecho a compra (o leasing financiado)</strong>. Aunque la cuota es ligeramente más cara, ofrece dos ventajas cruciales para su situación: <ul class="list-disc list-inside space-y-2"><li><strong>Derecho de Propiedad y Modificación:</strong> El leasing simple, al ser un alquiler a largo plazo, prohíbe modificaciones en el hardware. En cambio, el leasing con derecho a compra otorga la propiedad al final del contrato, y a menudo permite modificaciones durante el mismo (previa negociación), lo cual es vital para una startup que puede necesitar adaptar o potenciar sus servidores.</li><li><strong>Combate la Obsolescencia con Opción de Salida:</strong> Transfiere el riesgo de obsolescencia al arrendador. Al final del contrato, si el equipo ya no es de "última generación", la startup puede ejercer su derecho de compra por un valor residual bajo y revenderlo, o simplemente no ejercerlo y firmar un nuevo leasing por equipamiento más moderno. El leasing simple no ofrece esta flexibilidad de propiedad al final.</li></ul>' }
            ],
            'section-c': [
                { q: '11. El "Downsizing" fue una tendencia fuerte, pero presenta "costos ocultos". Detalle tres costos ocultos significativos y explique por qué el "Rightsizing" es un concepto más evolucionado.', a: 'Tres costos ocultos del downsizing (migrar de mainframe a sistemas más pequeños/distribuidos) son: <ul class="list-disc list-inside space-y-2"><li><strong>1. Costos de Soporte y Administración de Red:</strong> Un mainframe es gestionado por un equipo centralizado. Una red de PCs/servidores distribuida requiere soporte técnico en múltiples ubicaciones, gestión de red compleja, y herramientas de monitoreo, lo que dispara los costos de personal y licencias de software de gestión.</li><li><strong>2. Costos de Integración:</strong> Lograr que aplicaciones heterogéneas en una red distribuida compartan datos de forma consistente y segura es mucho más complejo que en un entorno mainframe integrado. Los costos de middleware, desarrollo de APIs y gestión de la integridad de datos son significativos.</li><li><strong>3. Costos de Seguridad:</strong> La superficie de ataque en un entorno distribuido es inmensamente mayor. Proteger cientos de endpoints, servidores y conexiones de red es mucho más costoso y complejo que asegurar un único mainframe en un centro de datos físico.</li></ul><strong>Rightsizing</strong> es más evolucionado porque no presupone que "más pequeño es mejor". Es el proceso de elegir la plataforma <strong>más adecuada</strong> (mainframe, nube, local, híbrida) para cada carga de trabajo, basándose en un análisis estratégico de costos, rendimiento, seguridad y objetivos de negocio, en lugar de seguir una tendencia.' },
                { q: '12. Al calcular el espacio en disco, el texto diferencia entre "Crecimiento Acumulativo" y "Resguardo de información del año anterior". Modele ambos escenarios para una tabla de "facturas" que actualmente tiene 1M de registros y crece un 20% anual, proyectado a 3 años.', a: `
                    <div class="space-y-3">
                        <p><strong>Crecimiento Acumulativo:</strong> Se aplica el crecimiento sobre el total del año anterior. La fórmula es <strong>Total = Actual * (1 + Crecimiento)^N</strong>.</p>
                        <ul class="list-disc list-inside">
                            <li>Año 0: 1,000,000 registros</li>
                            <li>Año 1: 1,000,000 * 1.20 = 1,200,000</li>
                            <li>Año 2: 1,200,000 * 1.20 = 1,440,000</li>
                            <li>Año 3: 1,440,000 * 1.20 = <strong>1,728,000 registros</strong></li>
                        </ul>
                        <p><strong>Resguardo de información (Histórico):</strong> Se suman los registros generados cada año sin eliminar los anteriores. La fórmula es una sumatoria. <strong>Total = Σ [Actual * (1 + Crecimiento)^i]</strong> para i=0 hasta N-1.</p>
                        <ul class="list-disc list-inside">
                            <li>Registros generados en Año 1: 1,000,000 * 0.20 = 200,000</li>
                            <li>Registros generados en Año 2: 1,200,000 * 0.20 = 240,000</li>
                            <li>Registros generados en Año 3: 1,440,000 * 0.20 = 288,000</li>
                            <li>Total a 3 años: 1,000,000 (inicial) + 200,000 + 240,000 + 288,000 = <strong>1,728,000 registros</strong></li>
                        </ul>
                        <p class="font-bold text-blue-700">Nota: Para este caso específico, el total de registros al final de los 3 años es el mismo, pero el modelo de "Resguardo" implica que el volumen total almacenado es la suma de los registros de todos los años, mientras que "Acumulativo" solo representa el estado final. Si el cálculo fuera sobre el espacio total requerido sumando cada año, el de resguardo sería mayor.</p>
                    </div>` },
                { q: '13. Una empresa necesita calcular la cantidad de terminales para su centro de atención al cliente. Tienen un volumen de 50,000 transacciones/día, cada una requiriendo 300 caracteres de tipeo. Considerando los estándares del texto, ¿cuántas terminales se necesitarían? Muestre su cálculo.', a: `
                    <div class="space-y-3">
                        <p>1. <strong>Calcular caracteres totales por día:</strong></p>
                        <p class="ml-4">50,000 transacciones/día * 300 caracteres/transacción = <strong>15,000,000 caracteres/día</strong></p>
                        <p>2. <strong>Calcular capacidad de tipeo por terminal por día:</strong></p>
                        <ul class="list-disc list-inside ml-4">
                            <li>Jornada: 6 hs = 21,600 seg</li>
                            <li>Tiempo neto de tipeo (75%): 21,600 * 0.75 = 16,200 seg (El texto usa un ejemplo de 4hs netas, usaremos el 75% que es más genérico)</li>
                            <li>Velocidad estándar: 3 caracteres/seg</li>
                            <li>Capacidad por terminal: 16,200 seg/día * 3 car/seg = <strong>48,600 caracteres/día por terminal</strong></li>
                        </ul>
                        <p>3. <strong>Calcular número de terminales requeridas:</strong></p>
                        <p class="ml-4">Terminales = Caracteres totales / Capacidad por terminal</p>
                        <p class="ml-4">15,000,000 / 48,600 = 308.64</p>
                        <p class="font-bold text-blue-700">Se necesitarían como mínimo <strong>309 terminales</strong> para manejar el volumen de trabajo proyectado.</p>
                    </div>`},
                { q: '14. ¿Por qué la "confiabilidad y disponibilidad de los datos" es una cuestión central en el debate entre Upsizing (centralización) y Downsizing (distribución)? Argumente cuál de las dos tendencias favorece más la integridad de los datos.', a: 'Es una cuestión central porque la arquitectura de la plataforma define cómo se almacenan, gestionan y acceden los datos, impactando directamente en su consistencia y disponibilidad. <br/><br/> El <strong>Upsizing (centralización)</strong>, como en un mainframe, inherentemente favorece más la <strong>integridad de los datos</strong>. Al tener una única fuente de verdad (Single Source of Truth) y un control de concurrencia y transacciones centralizado, es mucho más sencillo garantizar que los datos sean consistentes, precisos y que no existan conflictos de versiones. La gestión de backups y recuperación también es más simple.<br/><br/> El <strong>Downsizing (distribución)</strong> introduce el riesgo de "islas de datos" o múltiples versiones de la verdad. Mantener la integridad transaccional a través de múltiples bases de datos distribuidas (ej. con transacciones de dos fases) es un desafío técnico enorme y propenso a errores, lo que puede comprometer la confiabilidad de la información.'},
                { q: '15. Describa cómo la elección de una topología de red (ej. Estrella vs. Bus) impacta en el diseño del "Layout del HW" y en la planificación de la adquisición de componentes de red.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Topología en Estrella:</strong> En el layout, todos los nodos (PCs, impresoras) se conectan a un punto central (switch o hub). Esto requiere un espacio físico para el dispositivo central y un cableado individual desde cada nodo hasta ese punto. En la adquisición, el componente clave es el <strong>switch central</strong>, cuya cantidad de puertos y capacidad de conmutación debe planificarse cuidadosamente según el número de nodos. El costo del cableado es mayor, pero ofrece mayor resiliencia (la falla de un nodo no afecta al resto).</li><li><strong>Topología en Bus:</strong> En el layout, todos los nodos se conectan a un único cable principal (backbone). El diseño del cableado es más simple y lineal, ideal para espacios alargados. La adquisición de hardware es más económica: se necesita un cable principal, conectores T y terminadores. No requiere un dispositivo central costoso. Sin embargo, es menos resiliente: una ruptura en el cable principal puede dejar inoperativa a toda la red, y la detección de fallas es más compleja.</li></ul>'}
            ],
            'section-d': [
                { q: '16. Explique la relación inversa entre el "Mercado Laboral" y el "Mercado de Recursos Humanos". ¿Qué consecuencias tiene para una empresa de software una situación de "Oferta de empleo > Demanda de empleo"?', a: 'La relación es inversa: El <strong>Mercado Laboral</strong> representa la oferta de puestos de trabajo por parte de las empresas. El <strong>Mercado de RRHH</strong> representa la oferta de talentos (personas) disponibles para trabajar. Cuando la oferta en uno es alta, la demanda en el otro es alta, y viceversa. <br/><br/> Una situación de "Oferta de empleo > Demanda de empleo" (muchos puestos, pocos candidatos) significa que el <strong>Mercado Laboral está en oferta</strong> y el <strong>Mercado de RRHH está en demanda</strong>. Para una empresa de software, las consecuencias son severas: <ul class="list-disc list-inside space-y-2"><li><strong>Fuerte competencia por talento:</strong> La empresa debe competir agresivamente con otras por los pocos desarrolladores disponibles.</li><li><strong>Inflación salarial:</strong> Para atraer y retener talento, debe ofrecer salarios más altos, lo que puede distorsionar su política salarial interna.</li><li><strong>Aumento de la rotación:</strong> Los empleados actuales reciben constantemente ofertas mejores y están más predispuestos a irse.</li><li><strong>Inversiones elevadas:</strong> Se debe invertir más en reclutamiento (head-hunters, bonos), beneficios atractivos (flexibilidad, capacitación) y en la retención del personal existente.</li></ul>'},
                { q: '17. Compare el reclutamiento interno y externo. Si una empresa necesita cubrir un puesto de "Arquitecto de Soluciones Cloud Senior", ¿qué enfoque mixto recomendaría y por qué?', a: 'Recomendaría un enfoque mixto de <strong>reclutamiento interno y externo simultáneo</strong>. <br/><br/><strong>Justificación:</strong> Un puesto de "Arquitecto Senior" es estratégico y requiere un alto nivel de especialización técnica y visión de negocio. <ul class="list-disc list-inside space-y-2"><li>Iniciar un proceso <strong>interno</strong> es crucial para la motivación. Da la oportunidad a ingenieros senior existentes de crecer (aprovecha la inversión en ellos, es más rápido y seguro si hay un candidato idóneo). Ignorar al talento interno para un rol tan visible puede ser desmoralizante.</li><li>Al mismo tiempo, iniciar un proceso <strong>externo</strong> es indispensable para traer "sangre nueva" y asegurar que se contrata al mejor talento posible, no solo al mejor talento disponible internamente. El mercado externo puede ofrecer experiencia en tecnologías o industrias que la empresa no posee, lo cual es vital para un rol de arquitecto.</li></ul> Realizar ambos procesos en paralelo permite a la empresa comparar a los mejores candidatos internos con los mejores externos, garantizando una decisión basada en la máxima competencia y no en la simple conveniencia. Esto asegura que el rol lo ocupe la persona más calificada, sea de adentro o de afuera.' },
                { q: '18. En el proceso de selección, ¿cuál es el propósito de utilizar la "técnica de los incidentes críticos"? ¿Qué tipo de información provee que un simple análisis de tareas no puede capturar?', a: 'El propósito de la técnica de los incidentes críticos es ir más allá de la descripción de tareas y responsabilidades de un cargo. Busca capturar los <strong>comportamientos específicos que diferencian un desempeño excepcional de uno deficiente</strong>. <br/><br/> A diferencia de un análisis de tareas que lista "qué" se hace (ej. "programar nuevas funcionalidades"), la técnica de incidentes críticos provee información sobre el "cómo" se hace exitosamente. Captura ejemplos concretos de: <ul class="list-disc list-inside space-y-2"><li><strong>Comportamientos efectivos:</strong> "Cuando el sistema de pagos falló, el desarrollador X proactivamente trabajó horas extra, identificó la causa raíz en un servicio de terceros y comunicó claramente el plan de acción a la gerencia".</li><li><strong>Comportamientos inefectivos:</strong> "Ante un bug crítico, el desarrollador Y culpó a otro equipo sin investigar a fondo, retrasando la solución por 48 horas".</li></ul> Esta información es oro para la selección, ya que permite formular preguntas en la entrevista basadas en comportamientos ("Cuénteme sobre una vez que tuvo que resolver una crisis técnica...") y evaluar competencias clave como la resolución de problemas, la iniciativa y la comunicación, que son difíciles de medir con un simple listado de tareas.' },
                { q: '19. La entrevista de selección es un proceso de comunicación propenso a "barreras". Describa tres barreras personales que un entrevistador debe superar y qué técnicas de entrenamiento son efectivas.', a: 'Tres barreras comunes son: <ul class="list-disc list-inside space-y-2"><li><strong>1. Efecto Halo:</strong> Permitir que una característica positiva del candidato (ej. se graduó de una universidad prestigiosa) influya positivamente en la evaluación de todas sus demás características, incluso las no relacionadas.</li><li><strong>2. Error de Contraste:</strong> Evaluar a un candidato comparándolo con el candidato inmediatamente anterior, en lugar de hacerlo contra el estándar del cargo. Un candidato promedio puede parecer excelente si el anterior fue muy malo.</li><li><strong>3. Sesgo de Afinidad ("similar a mí"):</strong> Sentir una afinidad personal con un candidato (ej. comparten hobbies, origen) y evaluarlo de manera más favorable e inconsciente.</li></ul> <strong>Técnicas de entrenamiento efectivas:</strong> <ul class="list-disc list-inside space-y-2"><li><strong>Entrevistas Estructuradas:</strong> Entrenar a los entrevistadores para usar un conjunto predefinido de preguntas basadas en competencias y aplicarlas a todos los candidatos. Esto reduce la improvisación y los sesgos.</li><li><strong>Role-Playing y Feedback:</strong> Grabar entrevistas de práctica (role-playing) y que otros entrevistadores experimentados brinden feedback específico sobre las preguntas formuladas, el lenguaje corporal y los posibles sesgos mostrados.</li><li><strong>Capacitación en Sesgos Inconscientes (Unconscious Bias Training):</strong> Programas diseñados para hacer conscientes a los entrevistadores de estos sesgos comunes, enseñándoles a reconocerlos y a aplicar técnicas para mitigarlos durante el proceso de evaluación.</li></ul>'},
                { q: '20. ¿Por qué se afirma que la selección de personal busca solucionar dos problemas: "adecuación del hombre al cargo" y "eficiencia del hombre en el cargo"? ¿Puede un candidato ser adecuado pero no eficiente? Justifique con un ejemplo.', a: 'Se afirma esto porque son dos dimensiones distintas del éxito. La <strong>adecuación del hombre al cargo</strong> se refiere a si el candidato posee las competencias, conocimientos y habilidades (el "puede hacer") y los rasgos de personalidad y valores (el "cómo encaja") requeridos por el puesto. Es una evaluación de compatibilidad en el momento de la selección. La <strong>eficiencia del hombre en el cargo</strong> se refiere a si el candidato, una vez contratado, realmente traduce ese potencial en resultados y un desempeño efectivo y productivo. <br/><br/> <strong>Sí, un candidato puede ser adecuado pero no eficiente.</strong> <br/><br/> <strong>Ejemplo:</strong> Se contrata a un desarrollador de software que en la selección demostró un conocimiento técnico excepcional de un lenguaje de programación (alta adecuación). Sin embargo, una vez en el puesto, resulta ser una persona con baja motivación, que no colabora con el equipo, entrega el trabajo tarde y no se adapta a la metodología ágil de la empresa. Aunque tenía el potencial técnico, su falta de habilidades blandas, motivación o adaptación a la cultura lo convierte en un empleado <strong>no eficiente</strong>, que no genera el valor esperado.' }
            ],
            'section-e': [
                {
                    isScenario: true,
                    title: 'Escenario 1: Decisión Crítica de CRM',
                    scenario: 'Una pyme industrial quiere implementar su primer CRM. La gerencia de ventas quiere un desarrollo a medida para replicar sus procesos manuales exactos. El gerente de TI, con un equipo pequeño, propone un paquete SaaS líder del mercado.',
                    answer: `<div class="space-y-4">
                        <div>
                            <h4 class="font-semibold text-sky-900">a) Análisis y Recomendación del Canal de Provisión</h4>
                            <p>El canal recomendado es la <strong>adquisición de un paquete estándar (SaaS)</strong>. Un CRM no es una aplicación de "ventaja competitiva" para una pyme industrial (su negocio es fabricar, no desarrollar software), sino una aplicación "clave para las operaciones". El desarrollo a medida sería un error estratégico: consumiría los escasos recursos de TI, tendría un alto riesgo de sobrecostos y retrasos, y crearía una solución rígida que no evolucionaría. El paquete SaaS ofrece rápida disponibilidad, menores costos iniciales y se beneficia de las mejores prácticas y actualizaciones continuas del proveedor.</p>
                        </div>
                        <div>
                            <h4 class="font-semibold text-sky-900">b) Estrategia para Manejar la Disparidad</h4>
                            <p>La mejor estrategia es <strong>Modificar el proceso empresarial</strong>. El deseo de replicar procesos manuales exactos es una falacia común. Es una oportunidad para que la pyme adopte los flujos de trabajo optimizados que el CRM líder del mercado ya ofrece. El gerente de TI debe liderar un proceso de gestión del cambio, mostrando al equipo de ventas cómo los nuevos procesos mejorarán su eficiencia, visibilidad y resultados.</p>
                        </div>
                        <div>
                            <h4 class="font-semibold text-sky-900">c) Criterios Prioritarios del MEM</h4>
                            <p>Para esta pyme, los criterios más importantes en el MEM serían: <strong>1. Facilidad de Uso:</strong> Para asegurar una rápida adopción por parte del equipo de ventas, que no es técnico. <strong>2. Costo Total de Propiedad (TCO):</strong> No solo el precio de la licencia, sino los costos de implementación, capacitación y soporte. <strong>3. Funcionalidad Clave:</strong> Que cubra los procesos esenciales de venta (gestión de contactos, oportunidades, pipeline) sin sobrecargar con funciones innecesarias. <strong>4. Soporte del Proveedor:</strong> Un buen soporte local o en español sería crucial. La flexibilidad y la performance, aunque importantes, estarían en un segundo plano.</p>
                        </div>
                    </div>`
                },
                {
                    isScenario: true,
                    title: 'Escenario 2: La Migración Universitaria',
                    scenario: 'Una universidad pública utiliza un sistema de gestión de alumnos desarrollado internamente hace 15 años sobre un mainframe. Planean una migración. Opción A: "Downsizing" a una red de servidores locales. Opción B: "Outsourcing" completo a una plataforma SaaS educativa en la nube.',
                    answer: `<div class="space-y-4">
                        <div><h4 class="font-semibold text-sky-900">a) Análisis de Rightsizing</h4><p>La plataforma más adecuada es la <strong>Opción B (SaaS en la nube)</strong>. La gestión de alumnos, aunque crítica, no es el "negocio" de una universidad. Un proveedor de SaaS especializado ofrece una solución moderna, móvil, escalable y con actualizaciones constantes, liberando a la universidad de la carga técnica para que pueda concentrarse en la educación. La opción A (servidores locales) mantendría la responsabilidad del desarrollo y mantenimiento, sufriendo de los costos ocultos del downsizing (soporte, seguridad, integración).</p></div>
                        <div><h4 class="font-semibold text-sky-900">b) Comparación de Riesgos y Costos Ocultos</h4><p><strong>Opción A (Downsizing):</strong> El mayor riesgo es la <strong>falta de aptitudes</strong> del personal interno para gestionar una arquitectura distribuida moderna y segura. Los costos ocultos serían altos en <strong>seguridad de red, integración de sistemas y soporte técnico</strong>. <strong>Opción B (Outsourcing):</strong> El mayor riesgo es la <strong>dependencia del proveedor (vendor lock-in)</strong> y la dificultad para migrar a otra plataforma en el futuro. Los costos ocultos pueden surgir en la <strong>integración con otros sistemas universitarios</strong> y en cargos adicionales por funcionalidades no incluidas en el plan básico.</p></div>
                        <div><h4 class="font-semibold text-sky-900">c) Puntos Críticos del Contrato de Outsourcing</h4><p>Sería un outsourcing de tipo <strong>Agencia de Servicios</strong> o incluso <strong>Management Completo</strong>. Los 3 puntos más críticos a negociar son: <strong>1. Propiedad y Portabilidad de los Datos:</strong> El contrato debe establecer inequívocamente que la universidad es la única propietaria de los datos. Debe definir un procedimiento claro y sin costos punitivos para exportar la totalidad de los datos en un formato estándar y legible en caso de terminar el contrato. <strong>2. Acuerdos de Nivel de Servicio (SLA) claros:</strong> Definir métricas cuantificables para disponibilidad (ej. 99.9%), tiempo de respuesta del soporte, y penalizaciones claras por incumplimiento. <strong>3. Cláusulas de Seguridad y Cumplimiento:</strong> Exigir que el proveedor cumpla con normativas de protección de datos (ej. GDPR, leyes locales) y presente certificaciones de seguridad (ej. ISO 27001), con derecho a auditoría por parte de la universidad.</p></div>
                    </div>`
                },
                 {
                    isScenario: true,
                    title: 'Escenario 3: Fuga de Talentos en el Equipo de Desarrollo',
                    scenario: 'Una empresa de fintech experimenta una alta rotación (25% anual) en su equipo de desarrolladores. Los salarios están por encima del mercado, pero los proyectos son muy demandantes y la gerencia promueve casi exclusivamente a personal de otras áreas a los roles de liderazgo técnico.',
                    answer: `<div class="space-y-4">
                        <div><h4 class="font-semibold text-sky-900">a) Diagnóstico de Causas de Rotación (Chiavenato)</h4><p>Las causas son principalmente <strong>fenómenos internos</strong>. Aunque el salario (factor extrínseco) es bueno, fallan factores intrínsecos y organizacionales: <strong>1. Tipo de supervisión y gestión:</strong> La alta demanda puede indicar un ambiente de "burnout". <strong>2. Políticas de la organización:</strong> La falta de oportunidades de progreso es la causa más evidente. Promover a gente externa a los roles de liderazgo técnico envía un mensaje claro de que no hay futuro para los desarrolladores dentro de la empresa. <strong>3. Falta de motivación y escaso desarrollo de carrera:</strong> Los desarrolladores no ven un camino para crecer, lo que anula el efecto de un buen salario.</p></div>
                        <div><h4 class="font-semibold text-sky-900">b) ¿Problema de Reclutamiento o Selección?</h4><p>El problema no es de <strong>reclutamiento ni de selección</strong>. La empresa parece ser capaz de atraer y contratar talento calificado (ya que tienen un equipo que funciona, aunque rote). El problema es de <strong>retención y desarrollo</strong> (subsistemas de Mantenimiento y Desarrollo de Personas). La falta de un plan de carrera y las políticas de promoción inadecuadas son las que provocan la desvinculación de los empleados ya contratados y con buen desempeño.</p></div>
                        <div><h4 class="font-semibold text-sky-900">c) Propuesta de Mitigación</h4><p>Proponer una política de <strong>Reclutamiento Mixto (Interno-Externo Simultáneo)</strong> para los roles de liderazgo, pero con una clara priorización del talento interno si se igualan las condiciones. Esto debe ir acompañado de la creación de un <strong>Plan de Carrera Técnico (Technical Ladder)</strong>: un camino de crecimiento que permita a los desarrolladores ascender y obtener mayor reconocimiento y salario sin necesidad de convertirse en gerentes, pudiendo llegar a roles como "Desarrollador Principal", "Arquitecto de Software", etc. Esto les daría un horizonte de crecimiento y haría que la inversión en su desarrollo valga la pena tanto para ellos como para la empresa.</p></div>
                    </div>`
                }
            ],
        };
        
        function createQuestionCard(item) {
            if (item.isScenario) {
                return `
                    <div class="bg-sky-50 border-l-4 border-sky-500 rounded-r-lg shadow-lg p-6">
                        <h2 class="text-xl font-bold text-sky-800 mb-2">${item.title}</h2>
                        <p class="text-slate-700 mb-4">${item.scenario}</p>
                        <div class="flex justify-end items-start">
                            <button class="toggle-answer-btn text-sm bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors duration-300 flex-shrink-0">Mostrar Análisis</button>
                        </div>
                        <div class="question-answer mt-4 border-t border-sky-200 pt-4 text-slate-700">${item.answer}</div>
                    </div>`;
            } else {
                return `
                    <div class="bg-white rounded-xl shadow-lg p-6">
                        <div class="flex justify-between items-start gap-4">
                            <h3 class="text-lg font-semibold text-blue-900">${item.q}</h3>
                            <button class="toggle-answer-btn text-sm bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors duration-300 flex-shrink-0">Mostrar Respuesta</button>
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

            const card = targetButton.closest('.bg-white, .bg-sky-50');
            const answerDiv = card.querySelector('.question-answer');

            answerDiv.classList.toggle('visible');
            
            const isScenario = card.matches('.bg-sky-50');

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