<div id="interactive-exam-wrapper">
    <div class="container mx-auto">
        <header class="text-center mb-8">
            <h1 class="text-4xl md:text-5xl font-bold text-cyan-800">Guía de Estudio Interactiva</h1>
            <p class="text-xl text-slate-600 mt-2">Unidad 6: Control del Ambiente Informático</p>
        </header>

        <nav class="flex flex-wrap justify-center gap-2 md:gap-4 mb-8" id="section-nav">
            <button data-target="section-a" class="nav-button active w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección A: Fundamentos</button>
            <button data-target="section-b" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección B: Políticas y Controles</button>
            <button data-target="section-c" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección C: Contingencias</button>
            <button data-target="section-d" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección D: Auditoría</button>
            <button data-target="section-e" class="nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-cyan-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Sección E: Escenarios Prácticos</button>
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

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const navContainer = document.getElementById('section-nav');
        const questionsContainer = document.getElementById('questions-container');
        const questionSets = document.querySelectorAll('.question-set');
        const navButtons = document.querySelectorAll('.nav-button');

        const fullContent = {
            'section-a': [
                { q: '1. ¿Cuál es el objetivo principal de controlar el <strong>ambiente informático</strong> y qué áreas de la organización abarca?', a: 'El objetivo principal es <strong>prevenir riesgos</strong> para evitar posibles pérdidas para la organización. Abarca no solo el departamento de SI/TI, sino <strong>todos los sectores</strong> que proveen datos, usan información procesada o procesan información localmente.' },
                { q: '2. Describa los <strong>tres puntos de vista</strong> desde los cuales los Sistemas de Información deben ser considerados "seguros".', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Organizacional/Técnico:</strong> Asegurar que la tecnología (servidores, redes) funcione correctamente y tenga medidas de prevención.</li><li><strong>Social/Ético:</strong> Actuar de forma "correcta" según los principios del bien y del mal en relación con clientes, proveedores y la sociedad.</li><li><strong>Judicial/Legal:</strong> Cumplir con las normativas y leyes internas y externas.</li></ul>' },
                { q: '3. Defina los tres pilares técnicos de la seguridad de la información: <strong>Integridad, Disponibilidad y Confidencialidad</strong>.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Integridad:</strong> La información es exacta y completa, y no ha sido modificada sin autorización.</li><li><strong>Disponibilidad:</strong> La información y los sistemas están accesibles y operativos para los usuarios autorizados cuando se necesitan.</li><li><strong>Confidencialidad:</strong> La información solo es accesible para las personas o sistemas autorizados.</li></ul>' },
                { q: '4. ¿Qué es un ataque de <strong>interrupción</strong> y a cuál de los tres pilares de la seguridad afecta principalmente? Proporcione un ejemplo.', a: 'Un recurso del sistema es destruido o se vuelve no disponible. Afecta principalmente a la <strong>Disponibilidad</strong>. <strong>Ejemplo:</strong> Cortar un cable de fibra óptica o un ataque de Denegación de Servicio (DoS) que sature un servidor.' },
                { q: '5. ¿Qué es un ataque de <strong>intercepción</strong> y a cuál de los tres pilares de la seguridad afecta principalmente? Proporcione un ejemplo.', a: 'Una entidad no autorizada consigue acceso a un recurso/información. Afecta principalmente a la <strong>Confidencialidad</strong>. <strong>Ejemplo:</strong> Pinchar una línea de comunicación (escuchar) o copiar archivos sin permiso.' },
                { q: '6. ¿Qué es un ataque de <strong>modificación</strong> y a cuál de los tres pilares de la seguridad afecta principalmente? Proporcione un ejemplo.', a: 'Una entidad no autorizada accede y manipula un recurso. Afecta principalmente a la <strong>Integridad</strong>. <strong>Ejemplo:</strong> Cambiar el monto de una transacción financiera o alterar un registro en una base de datos.' },
                { q: '7. ¿Qué es un ataque de <strong>fabricación</strong> y a cuál de los tres pilares de la seguridad afecta principalmente? Proporcione un ejemplo.', a: 'Una entidad no autorizada inserta objetos falsos en el sistema. Afecta principalmente a la <strong>Autenticidad</strong> (y como consecuencia, a la Integridad). <strong>Ejemplo:</strong> Añadir transacciones falsas a un sistema contable o enviar correos electrónicos fraudulentos haciéndose pasar por otra persona (phishing).' },
                { q: '8. Explique la diferencia fundamental entre un <strong>ataque pasivo</strong> y un <strong>ataque activo</strong>. ¿Cuál es más difícil de detectar y por qué?', a: 'Un ataque <strong>pasivo</strong> solo observa o monitoriza la comunicación (ej. escucha), mientras que un ataque <strong>activo</strong> altera la comunicación o los sistemas (ej. modificación, suplantación). El ataque <strong>pasivo</strong> es mucho más difícil de detectar porque no deja rastros evidentes de su actividad.' },
                { q: '9. La premisa fundamental del management de la seguridad es que "la seguridad total es imposible". ¿Qué busca entonces la gestión de riesgos en su lugar?', a: 'Busca encontrar un <strong>equilibrio óptimo</strong> entre los costos resultantes de una falla de seguridad y los costos de las medidas necesarias para aumentar la seguridad, logrando un <strong>nivel razonable de seguridad</strong>.' },
                { q: '10. ¿Cuáles son las <strong>cuatro etapas</strong> del ciclo de management de la seguridad de los SI?', a: '1) Identificación del riesgo, 2) Análisis del riesgo, 3) Manejo del riesgo, y 4) Recuperación ante el desastre.' },
                { q: '11. En la etapa de <strong>Identificación del riesgo</strong>, ¿qué tres elementos clave se deben determinar?', a: '1) Las fuentes de amenazas potenciales, 2) Los activos que son vulnerables a la pérdida, y 3) La ubicación de esos riesgos.' },
                { q: '12. Nombre dos factores de los que depende la <strong>vulnerabilidad</strong> de un área en particular.', a: 'El personal de la organización, el tamaño de la red, y la calidad de la transmisión de datos.' },
                { q: '13. ¿Cómo se calcula la <strong>Pérdida Esperada</strong> en la etapa de Análisis del Riesgo? Defina sus componentes.', a: 'Se calcula como: <strong>Pérdida Esperada = Pérdida Potencial ($) × Frecuencia de Pérdida</strong>. A su vez, la <strong>Frecuencia de Pérdida</strong> se calcula como: <strong>Probabilidad de Agresión × Probabilidad de Éxito de la Agresión</strong>.' },
                { q: '14. ¿Cuál es la diferencia entre una <strong>pérdida primaria</strong> y una <strong>pérdida secundaria</strong> resultante de una falla de seguridad?', a: 'Las <strong>pérdidas primarias</strong> se desprenden directamente de la falla de seguridad (ej. costo de reparar un servidor). Las <strong>pérdidas secundarias</strong> surgen como consecuencia de las primarias (ej. pérdida de confianza del cliente y de futuras ventas debido a la caída del servidor).' },
                { q: '15. Describa brevemente las <strong>cuatro estrategias genéricas</strong> para el manejo del riesgo.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Prevenir:</strong> Evitar la amenaza (ej. no conectar un sistema crítico a internet).</li><li><strong>Asumir:</strong> Aceptar el riesgo porque el costo de la pérdida es tolerable.</li><li><strong>Reducir:</strong> Implementar controles para disminuir la probabilidad o el impacto (la más común).</li><li><strong>Transferir:</strong> Pasar el costo financiero a un tercero (ej. contratando un seguro).</li></ul>' },
                { q: '16. ¿Qué es una <strong>Matriz de Riesgo</strong> y para qué se utiliza?', a: 'Es una herramienta visual que cruza la <strong>probabilidad de ocurrencia</strong> de una amenaza con la <strong>magnitud del daño (impacto)</strong> para calcular y visualizar el grado de riesgo (Bajo, Medio, Alto), ayudando a priorizar las acciones de mitigación.' },
                { q: '17. Compare el uso de <strong>personal interno</strong> vs. <strong>consultores externos</strong> para la identificación de riesgos. ¿Cuáles son las ventajas y desventajas de cada uno?', a: 'El <strong>personal interno</strong> ofrece un conocimiento profundo y específico de la empresa. Los <strong>consultores externos</strong> aportan un conocimiento amplio de amenazas y mejores prácticas de la industria. Lo ideal es una combinación de ambos.' },
                { q: '18. Defina qué es un <strong>delito informático</strong> según el texto.', a: 'Toda acción culpable realizada por un ser humano, que cause perjuicio a otros o produzca un beneficio ilícito, tipificado por la ley, que se realiza en un entorno informático y está sancionado con una pena.' },
            ],
            'section-b': [
                {q: '19. ¿Qué es una <strong>política de seguridad</strong> y qué cuatro aspectos mínimos debe cubrir su documento?', a: 'Es un documento que define el nivel de seguridad deseado y las reglas generales sobre lo que está y no está permitido. Debe cubrir: 1) La protección de la información, 2) El valor de la información, 3) El acceso a la información, y 4) La recuperación de la información.'},
                {q: '20. Explique la diferencia entre una política de seguridad <strong>prohibitiva</strong> y una <strong>permisiva</strong>. ¿Cuál se considera generalmente más segura?', a: 'Una política <strong>permisiva</strong> establece que todo lo que no está expresamente prohibido, está permitido. Una política <strong>prohibitiva</strong> establece que todo lo que no está expresamente permitido, está prohibido. La <strong>prohibitiva</strong> es más restrictiva y se considera más segura.'},
                {q: '21. Nombre las <strong>cuatro fases</strong> del ciclo de vida de una política de seguridad.', a: '1) Desarrollo, 2) Implementación, 3) Mantenimiento, y 4) Eliminación.'},
                {q: '22. ¿Qué es una <strong>contramedida</strong>? Diferencie entre contramedidas <strong>generales</strong> y controles de <strong>aplicación</strong>.', a: 'Es una acción, dispositivo o técnica que reduce una amenaza o vulnerabilidad. Las <strong>generales</strong> se aplican a toda la organización (ej. política de contraseñas), mientras que los controles de <strong>aplicación</strong> protegen un área específica (ej. validación de datos en un formulario).'},
                {q: '23. Describa las <strong>tres líneas de defensa</strong> de las contramedidas (Prevención, Detección, Recuperación) y dé un ejemplo de cada una.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>1ª Prevención:</strong> Evita que ocurra la amenaza. <strong>Ejemplo:</strong> Una puerta con cerradura.</li><li><strong>2ª Detección:</strong> Alerta cuando una amenaza ha superado la prevención. <strong>Ejemplo:</strong> Un sensor de movimiento que activa una alarma.</li><li><strong>3ª Recuperación:</strong> Permite volver a la normalidad tras una falla. <strong>Ejemplo:</strong> Una copia de seguridad (backup).</li></ul>'},
                {q: '24. ¿Cuál es la diferencia entre un <strong>control lógico</strong> y un <strong>control físico</strong>? Proporcione un ejemplo de cada uno.', a: 'Un control <strong>lógico</strong> se implementa en el software o en los sistemas (ej. una contraseña de acceso, un firewall). Un control <strong>físico</strong> se implementa en el mundo real para proteger activos físicos (ej. una cámara de vigilancia, un guardia de seguridad).'},
                {q: '25. ¿Por qué la <strong>división de responsabilidades</strong> es un control crucial en un ambiente informático?', a: 'Es crucial porque evita que una sola persona tenga control total sobre un proceso crítico, reduciendo el riesgo de fraude o error no detectado. Por ejemplo, la persona que aprueba un pago no debe ser la misma que lo emite.'},
                {q: '26. ¿Qué es la <strong>encriptación de datos</strong> y qué pilar de la seguridad busca proteger principalmente?', a: 'Es el proceso de convertir datos legibles en un formato codificado para que no puedan ser leídos por personas no autorizadas. Protege principalmente la <strong>Confidencialidad</strong>.'},
                {q: '27. ¿Por qué el uso de contraseñas, aunque común, a menudo se considera una medida de control inadecuada si no se gestiona correctamente?', a: 'Porque los usuarios tienden a elegir contraseñas débiles, las reutilizan, las comparten o las escriben, lo que las hace vulnerables a ataques de fuerza bruta o ingeniería social si no se combinan con otras medidas como la autenticación multifactor (MFA).'},
                {q: '28. ¿Qué tres factores del entorno de los SI son determinantes para el tipo de controles a implementar?', a: '1) La plataforma del Hardware, 2) El grado de distribución de la red, y 3) La integración de la infraestructura.'},
                {q: '29. ¿Qué implica la fase de <strong>Garantía de cumplimiento</strong> en el ciclo de vida de una política?', a: 'Implica identificar las omisiones o violaciones a la política, analizar sus causas y tomar acciones para prevenir que sigan ocurriendo.'},
                {q: '30. ¿Por qué es importante que la <strong>Dirección</strong> respalde la implantación de una política de seguridad?', a: 'Es fundamental porque legitima la política, le asigna la autoridad necesaria para ser cumplida en toda la organización y asegura la asignación de los recursos (dinero, personal) necesarios para su implementación y mantenimiento.'},
            ],
            'section-c': [
                {q: '31. ¿Cuál es el objetivo de la <strong>planificación de la contingencia</strong>?', a: 'Definir un conjunto de planes y recursos para permitir que la empresa sobreviva a un desastre y pueda continuar operando sus funciones críticas, además de establecer la metodología para recuperar el estado normal.'},
                {q: '32. Defina los siguientes términos en el contexto de la recuperación: <strong>Tiempo de inhabilitación</strong>, <strong>Respaldo</strong> y <strong>Reinstalación</strong>.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Tiempo de inhabilitación:</strong> El período durante el cual los sistemas no están disponibles.</li><li><strong>Respaldo (Backup):</strong> Mantener las operaciones críticas funcionando con sistemas alternativos.</li><li><strong>Reinstalación:</strong> Actualizar los sistemas recuperados con los datos generados durante la interrupción.</li></ul>'},
                {q: '33. ¿Cómo se clasifican los sistemas y aplicaciones según su <strong>grado de tolerancia a la interrupción</strong>? Nombre las cuatro categorías.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Críticos:</strong> Tolerancia muy baja a la interrupción.</li><li><strong>Vitales:</strong> Tolerancia moderada.</li><li><strong>Sensibles:</strong> Tolerancia flexible.</li><li><strong>No críticos:</strong> Tolerancia amplia.</li></ul>'},
                {q: '34. Describa la diferencia entre un <strong>Hot Site</strong>, un <strong>Warm Site</strong> y un <strong>Cold Site</strong>. ¿Cuál permite una recuperación más rápida?', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Hot Site:</strong> Una instalación completamente equipada y lista para operar de inmediato. Es la más rápida y costosa.</li><li><strong>Warm Site:</strong> Una instalación parcialmente equipada (generalmente falta el hardware principal como el servidor central).</li><li><strong>Cold Site:</strong> Un espacio físico con las conexiones básicas (energía, red) pero sin equipamiento informático. Es la más lenta y económica.</li></ul>'},
                {q: '35. ¿Qué es el <strong>lapso crítico de recuperación</strong> de un sistema?', a: 'Es el tiempo máximo que una interrupción puede durar antes de que la organización incurra en pérdidas significativas o inaceptables.'},
                {q: '36. ¿Qué es una <strong>catástrofe</strong> en el contexto de los niveles de emergencia?', a: 'La destrucción total de las instalaciones físicas, requiriendo el traslado a una sede alternativa de forma prolongada.'},
                {q: '37. ¿Qué es un <strong>desastre</strong> en el contexto de los niveles de emergencia?', a: 'Una interrupción prolongada (más de un día) pero con la posibilidad de reanudar operaciones en la sede original una vez solucionado el problema.'},
                {q: '38. ¿Qué es una situación de <strong>no desastre</strong>?', a: 'Interrupciones breves causadas por fallas menores de hardware o software que se corrigen rápidamente.'},
                {q: '39. Además de la disponibilidad de hardware, ¿qué otra capacidad es fundamental para recuperar las operaciones en una empresa moderna?', a: 'La capacidad de <strong>telecomunicaciones</strong> (redes, internet) es crucial para conectar usuarios, sistemas y sedes alternativas.'},
                {q: '40. ¿Por qué el personal debe ser entrenado y se deben realizar simulacros como parte del plan de contingencias?', a: 'Son vitales para asegurar que el personal conozca sus roles y responsabilidades durante una emergencia real, y para probar la efectividad y coherencia del plan, identificando fallos antes de que ocurra un desastre real.'},
            ],
            'section-d': [
                {q: '41. Defina <strong>auditoría de sistemas</strong> con sus propias palabras, mencionando su finalidad.', a: 'Es la revisión sistemática y profesional de los recursos y funciones informáticas de una organización. Su <strong>finalidad</strong> es emitir una opinión sobre si dichos sistemas operan de manera efectiva, eficiente y segura, de acuerdo con los objetivos y normativas establecidas.'},
                {q: '42. ¿Cuáles son las <strong>cuatro propiedades</strong> que una auditoría de sistemas busca verificar en los sistemas en funcionamiento?', a: '1) Vigencia de los objetivos originales, 2) Grado de consistencia con esos objetivos (efectividad), 3) Permanencia del diseño sin degradaciones, 4) Eficiencia del sistema (costo/beneficio).'},
                {q: '43. Explique la diferencia fundamental entre el <strong>Control Interno Informático</strong> y la <strong>Auditoría Informática</strong> en términos de periodicidad y a quién reportan.', a: 'El <strong>Control Interno</strong> es una función continua (del día a día) que reporta a la dirección de informática. La <strong>Auditoría</strong> es una revisión periódica (en un momento determinado) que reporta a la Dirección General para garantizar la objetividad.'},
                {q: '44. ¿Cuáles son los <strong>tres principios deontológicos (éticos) fundamentales</strong> del auditor informático? Explique brevemente el de <strong>Independencia</strong>.', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Independencia (de criterio):</strong> El auditor debe ser objetivo y no tener vínculos jerárquicos o de desarrollo con el área o sistema que audita.</li><li><strong>Segregación de funciones:</strong> El auditor debe tener un rol separado de las funciones que evalúa.</li><li><strong>Secreto profesional:</strong> El auditor no debe divulgar la información obtenida fuera de su informe oficial.</li></ul>'},
                {q: '45. ¿Qué es el <strong>riesgo de detección</strong> en una auditoría?', a: 'Es el riesgo de que el auditor no detecte errores o irregularidades materiales que existen en el sistema, debido a procedimientos de auditoría inadecuados o mal aplicados.'},
                {q: '46. Describa las <strong>seis etapas</strong> del proceso de auditoría.', a: '1) Identificar sujeto, objetivos y alcance, 2) Realizar estudio inicial, 3) Ejecutar programa de revisión, 4) Cierre de la revisión, 5) Realizar informe final, 6) Seguimiento.'},
                {q: '47. ¿Qué es una <strong>pista de auditoría</strong> y por qué es fundamental para un auditor?', a: 'Es un registro cronológico de eventos y operaciones que permite rastrear una transacción desde su origen hasta su destino (o viceversa). Es fundamental para verificar la integridad y reconstruir secuencias de eventos.'},
                {q: '48. Diferencie entre una <strong>prueba de cumplimiento</strong> y una <strong>prueba sustantiva</strong> en una auditoría.', a: 'Una <strong>prueba de cumplimiento</strong> verifica si los controles se aplican según las políticas (ej. ¿se sigue el procedimiento de alta de usuarios?). Una <strong>prueba sustantiva</strong> verifica la integridad de los datos y busca errores o fraudes en ellos (ej. ¿son correctos los saldos de las cuentas?).'},
                {q: '49. ¿Cuáles son los <strong>cuatro tipos de opinión</strong> que un auditor puede emitir en su informe final?', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Favorable (o sin salvedades):</strong> El sistema cumple adecuadamente con los controles y normativas.</li><li><strong>Con salvedades:</strong> El sistema cumple en general, pero existen algunas excepciones o debilidades específicas que se deben mencionar.</li><li><strong>Desfavorable (o adversa):</strong> El sistema presenta irregularidades o incumplimientos significativos.</li><li><strong>Denegada (o abstención de opinión):</strong> El auditor no pudo obtener evidencia suficiente para formarse una opinión.</li></ul>'},
                {q: '50. ¿Qué significa que la evidencia de auditoría debe ser <strong>relevante, fiable y suficiente</strong>?', a: '<ul class="list-disc list-inside space-y-2"><li><strong>Relevante:</strong> Tiene una relación lógica con el objetivo de la auditoría.</li><li><strong>Fiable:</strong> Es válida, objetiva y digna de confianza.</li><li><strong>Suficiente:</strong> La cantidad de evidencia es adecuada para soportar la conclusión del auditor.</li></ul>'},
                {q: '51. ¿Por qué la evidencia obtenida de <strong>fuentes externas</strong> se considera generalmente más confiable?', a: 'Se considera más confiable porque proviene de un tercero independiente, lo que reduce la posibilidad de que haya sido manipulada por la entidad auditada.'},
                {q: '52. Compare una <strong>auditoría interna</strong> con una <strong>auditoría externa</strong> en términos de vínculo laboral y destino del informe.', a: 'La <strong>interna</strong> la realiza un profesional con vínculo laboral y el informe es para uso interno. La <strong>externa</strong> la realiza un profesional independiente (sin vínculo laboral) y el informe puede ser para terceros, dando fe pública.'},
                {q: '53. ¿Cuál es la misión principal de la función de <strong>Control Interno Informático</strong>?', a: 'Asegurarse de que las medidas y controles implementados por cada responsable sean válidos y se cumplan, y que las actividades diarias se realicen según las normas y procedimientos establecidos.'},
                {q: '54. ¿Qué es el <strong>riesgo inherente</strong>?', a: 'Es el riesgo de que ocurra un error material por la propia naturaleza de la actividad, antes de considerar cualquier control interno. Por ejemplo, el riesgo inherente de error en cálculos complejos es mayor que en cálculos simples.'},
                {q: '55. ¿Qué es un <strong>programa de revisión</strong> en el contexto de una auditoría?', a: 'Es un documento detallado que contiene el conjunto de instrucciones, procedimientos y pruebas que el equipo de auditoría ejecutará para cumplir con los objetivos de la auditoría en un área específica. Sirve como guía y registro del trabajo realizado.'},
                {q: '56. ¿Por qué un auditor no debe estar involucrado en el desarrollo de los sistemas que audita? ¿A qué principio deontológico responde esto?', a: 'Un auditor no debe participar en el desarrollo porque comprometería su capacidad para evaluarlo de forma objetiva más adelante. Esto responde directamente al <strong>Principio de Independencia</strong>. No se puede ser juez y parte.'},
            ],
            'section-e': [
                {
                    isScenario: true,
                    title: '57. Escenario: El Dilema del Costo de la Seguridad',
                    scenario: 'Una cadena de hospitales ha sufrido un ataque de ransomware que cifró los registros de pacientes. Los atacantes exigen un rescate. La dirección debate entre pagar o intentar una recuperación desde backups de hace 48 horas, lo que implicaría pérdida de datos y tiempo de inactividad.',
                    answer: `<div class="space-y-4">
                        <div>
                            <h4 class="font-semibold text-teal-900">a) Análisis Multidimensional</h4>
                            <p><strong>Organizacional/Técnico:</strong> Pagar no garantiza la recuperación y marca a la organización como un objetivo futuro. La recuperación desde backups es un procedimiento controlado, aunque con pérdida de datos y tiempo de inactividad costoso.</p>
                            <p><strong>Social/Ético:</strong> Pagar financia a organizaciones criminales. No pagar es una postura ética más fuerte, aunque la pérdida de datos afecta la confianza del paciente.</p>
                            <p><strong>Judicial/Legal:</strong> Pagar podría violar leyes. La pérdida de datos acarreará multas, pero demuestra diligencia en la respuesta.</p>
                        </div>
                        <div>
                            <h4 class="font-semibold text-teal-900">b) Equilibrio de Costos Post-Falla</h4>
                            <p>Se debe equilibrar el "costo de la recuperación" contra el "costo del impacto continuo". No pagar, aunque doloroso a corto plazo, evita los riesgos incontrolables (legales, de reputación, técnicos) asociados al pago a criminales.</p>
                        </div>
                        <div>
                            <h4 class="font-semibold text-teal-900">c) Cambios Inmediatos en la Estrategia</h4>
                            <p><strong>Disponibilidad:</strong> Mejorar el plan de contingencias con backups más frecuentes (RPO más bajo). Implementar segmentación de red. <strong>Integridad:</strong> Aplicar el principio de menor privilegio en los accesos. Implementar sistemas de detección de intrusos (IDS/IPS) y reforzar la capacitación del personal contra phishing.</p>
                        </div>
                    </div>`
                },
                {
                    isScenario: true,
                    title: '58. Escenario: Ataques Pasivos vs. Activos',
                    scenario: 'Una empresa de software descubre que un competidor accedió a su código fuente. El ataque fue en dos fases: primero, una intercepción pasiva para robar credenciales; segundo, una suplantación de identidad activa para descargar el código.',
                    answer: `<div class="space-y-4">
                        <div><h4 class="font-semibold text-teal-900">a) Detección y Contramedidas del Ataque Pasivo</h4><p>Fue difícil de detectar porque no altera los datos. Contramedidas: Cifrado de comunicaciones de extremo a extremo (VPN, HTTPS), políticas de contraseñas robustas.</p></div>
                        <div><h4 class="font-semibold text-teal-900">b) Prevención del Ataque Activo</h4><p>Para prevenir la suplantación de identidad: Autenticación Multifactor (MFA), controles de acceso basados en ubicación (Geofencing), y Análisis de Comportamiento de Usuario (UBA).</p></div>
                        <div><h4 class="font-semibold text-teal-900">c) Detección de Manipulación</h4><p>Deberían buscar ataques de <strong>modificación</strong> o <strong>fabricación</strong>. Se usan herramientas como los logs de Git, firmas de commits (GPG), análisis estático de código (SAST) y revisión de código por pares.</p></div>
                    </div>`
                },
                {
                    isScenario: true,
                    title: '59. Escenario: La Ilusión de la Seguridad Total',
                    scenario: 'El CEO de una startup declara: "Nuestra plataforma debe ser 100% segura".',
                    answer: `<div class="space-y-4">
                        <div><h4 class="font-semibold text-teal-900">a) Argumento para el CEO</h4><p>Explicar que la seguridad es un proceso de <strong>management del riesgo</strong>, no un estado absoluto. El objetivo es alcanzar un <strong>nivel razonable de seguridad</strong> equilibrando el costo de los controles con el impacto de las amenazas, aceptando un riesgo residual.</p></div>
                        <div><h4 class="font-semibold text-teal-900">b) Recursos para Identificación de Riesgo</h4><p>Proponer un enfoque híbrido: <strong>Personal interno</strong> para un conocimiento profundo de los activos y <strong>consultores externos</strong> para una perspectiva amplia de las amenazas de la industria.</p></div>
                        <div><h4 class="font-semibold text-teal-900">c) Fuentes de Amenazas</h4><p><strong>Física Accidental:</strong> Corte de energía. <strong>Activo Vulnerable:</strong> Disponibilidad de la plataforma. <strong>Lógica Deliberada:</strong> Inyección SQL. <strong>Activo Vulnerable:</strong> Confidencialidad e integridad de la BBDD de clientes. <strong>Personal:</strong> Empleado víctima de phishing. <strong>Activo Vulnerable:</strong> Control de acceso a la infraestructura.</p></div>
                    </div>`
                },
                {
                    isScenario: true,
                    title: '60. Escenario: Vulnerabilidades en Trabajo Remoto',
                    scenario: 'Una compañía de seguros permite el trabajo remoto, aumentando el riesgo por "personal", "tamaño de la red" y "calidad de la transmisión".',
                    answer: `<div class="space-y-4">
                        <div><h4 class="font-semibold text-teal-900">a) Aumento del Riesgo</h4><p><strong>Personal:</strong> Más susceptible a ingeniería social. <strong>Tamaño de la Red:</strong> La red corporativa se extiende a redes domésticas inseguras. <strong>Calidad de Transmisión:</strong> El tráfico en Wi-Fi públicas puede ser interceptado.</p></div>
                        <div><h4 class="font-semibold text-teal-900">b) Contramedidas</h4><p><strong>Personal:</strong> Capacitación continua en ciberseguridad. <strong>Red:</strong> Soluciones de Endpoint Detection and Response (EDR). <strong>Transmisión:</strong> Uso obligatorio de VPN corporativa.</p></div>
                        <div><h4 class="font-semibold text-teal-900">c) Comparación de Intercepción</h4><p>Es inmensamente más fácil en una <strong>Wi-Fi pública</strong>. Requiere menos habilidad técnica y ningún acceso físico, a diferencia de una LAN cableada de oficina.</p></div>
                    </div>`
                },
                {
                    isScenario: true,
                    title: '61. Escenario: Fabricación de Datos',
                    scenario: 'Un sistema de logística sufre un ataque de fabricación, insertando registros falsos de "mercancía recibida".',
                    answer: `<div class="space-y-4">
                        <div><h4 class="font-semibold text-teal-900">a) Peligro a Largo Plazo</h4><p>Es más peligroso porque es <strong>silencioso</strong> y pasa desapercibido, erosionando la confianza y llevando a tomar decisiones de negocio basadas en datos falsos. La remediación es mucho más compleja que restaurar un sistema caído.</p></div>
                        <div><h4 class="font-semibold text-teal-900">b) Controles de Aplicación</h4><p>Validación de entradas rigurosa, segregación de funciones, autorización estricta y pistas de auditoría (logs) inmutables.</p></div>
                        <div><h4 class="font-semibold text-teal-900">c) Respuesta a Incidentes</h4><p>1. <strong>Contención:</strong> Aislar sistemas y cerrar la vulnerabilidad. 2. <strong>Identificación:</strong> Analizar logs para encontrar el alcance del ataque y los registros falsos. 3. <strong>Erradicación y Recuperación:</strong> Desarrollar y ejecutar scripts para eliminar específicamente los datos falsos sin perder datos legítimos. 4. <strong>Post-Incidente:</strong> Analizar la causa raíz y mejorar los controles.</p></div>
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

</rewritten_file>