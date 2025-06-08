<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">

<div class="pasapalabra-game-wrapper">
    <div class="game-container">
        <!-- Status Panel (Top) -->
        <div class="panel flex justify-between items-center">
            <div>
                 <h1 class="text-xl font-bold">PASAPALABRA</h1>
                 <p class="text-slate-400 text-sm">Unidad 3: Subsistema de Aplicación</p>
            </div>
            <div class="flex gap-4 sm:gap-8 text-center">
                <div>
                    <span class="block text-green-400 font-bold text-2xl" id="correct-count">0</span>
                    <span class="text-xs sm:text-sm">Aciertos</span>
                </div>
                <div>
                    <span class="block text-red-400 font-bold text-2xl" id="incorrect-count">0</span>
                    <span class="text-xs sm:text-sm">Errores</span>
                </div>
            </div>
            <div class="text-4xl sm:text-6xl font-bold text-yellow-400" id="timer">200</div>
        </div>

        <!-- Rosco Panel (Center) -->
        <div id="rosco-container">
            <!-- Letters will be injected here -->
        </div>

        <!-- Info & Actions Panel (Bottom) -->
        <div class="panel">
            <div>
                <h2 class="text-lg font-bold mb-2">Definición:</h2>
                <p class="text-slate-300 text-base sm:text-lg min-h-[7rem]" id="question-display"></p>
            </div>
            <div class="space-y-4 mt-4">
                <input type="text" id="answer-input" class="w-full bg-slate-700 border border-slate-600 rounded-lg p-3 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-400" placeholder="Escribe tu respuesta...">
                <div class="flex flex-col sm:flex-row gap-4">
                    <button id="pass-btn" class="btn btn-secondary w-full">Pasapalabra</button>
                    <button id="answer-btn" class="btn btn-primary w-full">Responder</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal -->
    <div id="modal-container">
        <div class="panel text-center p-8 max-w-sm">
            <h2 class="text-3xl font-bold mb-4" id="modal-title">¡Juego Terminado!</h2>
            <p class="text-lg mb-6" id="modal-message">Este es tu resultado final.</p>
            <div class="flex justify-center gap-8 text-3xl mb-8">
                <div>
                    <span class="block text-green-400 font-bold" id="modal-correct">0</span>
                    <span class="text-sm">Aciertos</span>
                </div>
                <div>
                    <span class="block text-red-400 font-bold" id="modal-incorrect">0</span>
                    <span class="text-sm">Errores</span>
                </div>
            </div>
            <button id="restart-btn" class="btn btn-primary w-full">Jugar de Nuevo</button>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    
    .pasapalabra-game-wrapper {
        font-family: 'Montserrat', sans-serif;
        color: #f1f5f9;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        min-height: 100vh;
        padding: 1rem;
    }

    .game-container {
        width: 100%;
        max-width: 700px;
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    
    #rosco-container {
        position: relative;
        width: 100%;
        padding-top: 100%; /* Aspect ratio 1:1 */
        margin: 1rem 0;
    }

    .letter-circle {
        position: absolute;
        width: 11%;
        height: 11%;
        background-color: #1e293b;
        border: 2px solid #334155;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: clamp(0.8rem, 3vw, 1.2rem);
        font-weight: 700;
        color: #f1f5f9;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }
    
    .letter-circle.current {
        background-color: #fbbf24;
        color: #1e293b;
        transform: scale(1.25);
        border-color: #f59e0b;
        z-index: 10;
    }

    .letter-circle.correct {
        background-color: #22c55e;
        color: #fff;
        border-color: #16a34a;
    }

    .letter-circle.incorrect {
        background-color: #ef4444;
        color: #fff;
        border-color: #dc2626;
    }

    .panel {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 1rem;
        padding: 1.5rem;
        border: 1px solid #334155;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .btn {
        padding: 0.75rem 1.5rem;
        border-radius: 9999px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }

    .btn-primary {
        background-color: #22c55e;
        color: white;
    }
    .btn-primary:hover:not(:disabled) {
        background-color: #16a34a;
    }
    
    .btn-secondary {
        background-color: #3b82f6;
        color: white;
    }
    .btn-secondary:hover:not(:disabled) {
        background-color: #2563eb;
    }

    .btn:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }
    
    #modal-container {
        position: fixed;
        inset: 0;
        background-color: rgba(0,0,0,0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s ease, visibility 0.3s ease;
        z-index: 50;
    }
    
    #modal-container.visible {
        opacity: 1;
        visibility: visible;
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const roscoContainer = document.getElementById('rosco-container');
        const questionDisplay = document.getElementById('question-display');
        const answerInput = document.getElementById('answer-input');
        const answerBtn = document.getElementById('answer-btn');
        const passBtn = document.getElementById('pass-btn');
        const timerDisplay = document.getElementById('timer');
        const correctCountDisplay = document.getElementById('correct-count');
        const incorrectCountDisplay = document.getElementById('incorrect-count');

        const modalContainer = document.getElementById('modal-container');
        const modalTitle = document.getElementById('modal-title');
        const modalMessage = document.getElementById('modal-message');
        const modalCorrect = document.getElementById('modal-correct');
        const modalIncorrect = document.getElementById('modal-incorrect');
        const restartBtn = document.getElementById('restart-btn');

        let questions = [];
        let currentQuestionIndex = 0;
        let correctAnswers = 0;
        let incorrectAnswers = 0;
        let timer;
        let timeLeft;

        function setupQuestions() {
             return [
                { letter: 'A', answer: 'AUTONOMIA', question: 'Empieza por A: Grado de independencia y criterio personal que tiene el empleado para planear y ejecutar su trabajo.', status: 'unanswered' },
                { letter: 'B', answer: 'BENCHMARKING', question: 'Empieza por B: Programas estándares para simular una carga genérica, utilizados para comparar sistemas informáticos.', status: 'unanswered' },
                { letter: 'C', answer: 'CARGA', question: 'Empieza por C: Conjunto de todas las demandas que realizan los usuarios al sistema durante un intervalo de tiempo.', status: 'unanswered' },
                { letter: 'D', answer: 'DESEMPEÑO', question: 'Empieza por D: Apreciación sistemática del rendimiento de cada persona en su cargo o del potencial de desarrollo futuro.', status: 'unanswered' },
                { letter: 'E', answer: 'ENTREVISTA', question: 'Empieza por E: Método de análisis de cargos que garantiza una interacción frente a frente entre el analista y el empleado.', status: 'unanswered' },
                { letter: 'F', answer: 'FIABILIDAD', question: 'Empieza por F: Probabilidad de que el sistema trabaje correctamente a lo largo de un intervalo de tiempo dado.', status: 'unanswered' },
                { letter: 'G', answer: 'GERENTE', question: 'Empieza por G: Persona que en el modelo de evaluación tradicional tiene la responsabilidad de línea sobre el desempeño.', status: 'unanswered' },
                { letter: 'H', answer: 'HORIZONTAL', question: 'Empieza por H: Tipo de enriquecimiento de cargo que consiste en la adición de responsabilidades del mismo nivel.', status: 'unanswered' },
                { letter: 'I', answer: 'INTERACTIVO', question: 'Empieza por I: Sistema en que la generación de una nueva petición depende de la recepción de la respuesta a la anterior.', status: 'unanswered' },
                { letter: 'J', answer: 'JUZGAR', question: 'Empieza por J: Verbo que describe una de las finalidades de la evaluación de desempeño, además de estimular el desarrollo.', status: 'unanswered' },
                { letter: 'K', answer: 'KERNEL', question: 'Empieza por K: Programa o fragmento de programa representativo de la carga, considerado una carga de prueba artificial y ejecutable.', status: 'unanswered' },
                { letter: 'L', answer: 'LINEA', question: 'Contiene la L: Tipo de responsabilidad del gerente en la evaluación del desempeño, en contraposición a la de staff.', status: 'unanswered' },
                { letter: 'M', answer: 'MONITORIZACION', question: 'Empieza por M: Técnica que utiliza herramientas para medir el comportamiento de un sistema real en producción.', status: 'unanswered' },
                { letter: 'N', answer: 'NATURAL', question: 'Empieza por N: Tipo de carga de prueba sintética que consta de un conjunto de programas extraídos de la carga real.', status: 'unanswered' },
                { letter: 'Ñ', answer: 'DISEÑO', question: 'Contiene la Ñ: Proceso de establecer las tareas, métodos, responsabilidades y autoridad de un cargo.', status: 'unanswered' },
                { letter: 'O', answer: 'OVERHEAD', question: 'Empieza por O: Costo de recursos del sistema utilizados en tareas propias del SO no atribuibles a los programas de usuario.', status: 'unanswered' },
                { letter: 'P', answer: 'PRODUCTIVIDAD', question: 'Empieza por P: Cantidad de trabajo útil ejecutado por unidad de tiempo en un entorno de carga determinado.', status: 'unanswered' },
                { letter: 'Q', answer: 'QUANTUM', question: 'Empieza por Q: Cantidad de tiempo de CPU que un sistema de tiempo compartido asigna a un trabajo.', status: 'unanswered' },
                { letter: 'R', answer: 'ROL', question: 'Empieza por R: Conjunto de actividades y comportamientos que se solicitan a un individuo que ocupa determinada posición.', status: 'unanswered' },
                { letter: 'S', answer: 'SOCIALIZACION', question: 'Empieza por S: Proceso permanente de inculcar en los empleados las actitudes, normas y valores esperados por la organización.', status: 'unanswered' },
                { letter: 'T', answer: 'TAREA', question: 'Empieza por T: Actividad individual que ejecuta el ocupante del cargo, generalmente simple y rutinaria.', status: 'unanswered' },
                { letter: 'U', answer: 'UTILIZACION', question: 'Contiene la U: Factor que mide el porcentaje de tiempo durante el cual un componente del sistema ha estado realmente ocupado.', status: 'unanswered' },
                { letter: 'V', answer: 'VERTICAL', question: 'Empieza por V: Tipo de enriquecimiento de cargo que añade responsabilidades de nivel gradualmente más elevado.', status: 'unanswered' },
                { letter: 'W', answer: 'SOFTWARE', question: 'Contiene la W: Parte lógica de un sistema informático, que incluye el conjunto de los componentes lógicos necesarios.', status: 'unanswered' },
                { letter: 'X', answer: 'EXITO', question: 'Contiene la X: Resultado positivo de un comportamiento que se registra en el método de incidentes críticos.', status: 'unanswered' },
                { letter: 'Y', answer: 'JERARQUIA', question: 'Contiene la Y: Estructura que se establece en orden de grado, importancia o autoridad dentro de una organización.', status: 'unanswered' },
                { letter: 'Z', answer: 'ORGANIZACIONAL', question: 'Contiene la Z: Adjetivo que califica a la cultura o al proceso de socialización dentro de una empresa.', status: 'unanswered' },
            ];
        }
        
        function createRosco() {
            if (!roscoContainer) return;
            roscoContainer.innerHTML = '';
            const radius = roscoContainer.clientWidth / 2 * 0.85;
            const centerX = roscoContainer.clientWidth / 2;
            const centerY = roscoContainer.clientHeight / 2;

            questions.forEach((q, i) => {
                const angle = (i / questions.length) * 2 * Math.PI - (Math.PI / 2);
                const letterDiv = document.createElement('div');
                letterDiv.className = 'letter-circle';
                letterDiv.textContent = q.letter;
                letterDiv.id = `letter-${q.letter}`;
                const size = roscoContainer.clientWidth * 0.11;
                letterDiv.style.left = `${centerX + radius * Math.cos(angle) - size / 2}px`;
                letterDiv.style.top = `${centerY + radius * Math.sin(angle) - size / 2}px`;
                roscoContainer.appendChild(letterDiv);
            });
        }

        function updateUI() {
            correctCountDisplay.textContent = correctAnswers;
            incorrectCountDisplay.textContent = incorrectAnswers;

            questions.forEach(q => {
                const letterDiv = document.getElementById(`letter-${q.letter}`);
                if (letterDiv) {
                    letterDiv.className = 'letter-circle'; 
                    if (q.status === 'correct') {
                        letterDiv.classList.add('correct');
                    } else if (q.status === 'incorrect') {
                        letterDiv.classList.add('incorrect');
                    }
                }
            });
            
            if (currentQuestionIndex >= 0 && currentQuestionIndex < questions.length){
                const currentLetterDiv = document.getElementById(`letter-${questions[currentQuestionIndex].letter}`);
                if (currentLetterDiv) currentLetterDiv.classList.add('current');
                questionDisplay.textContent = questions[currentQuestionIndex].question;
            }

            answerInput.value = '';
            answerInput.focus();
        }

        function findNextQuestion() {
            const totalQuestions = questions.length;
            let attempts = 0;
            let nextIndex = currentQuestionIndex;

            if (questions.every(q => q.status !== 'unanswered')) {
                return -1; // Game over
            }

            do {
                nextIndex = (nextIndex + 1) % totalQuestions;
                attempts++;
            } while (questions[nextIndex].status !== 'unanswered' && attempts <= totalQuestions);
            
            return nextIndex;
        }

        function handleAnswer() {
            const userAnswer = answerInput.value.trim().toUpperCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            const correctAnswer = questions[currentQuestionIndex].answer;

            if (userAnswer === correctAnswer) {
                questions[currentQuestionIndex].status = 'correct';
                correctAnswers++;
            } else {
                questions[currentQuestionIndex].status = 'incorrect';
                incorrectAnswers++;
            }
            moveToNext();
        }
        
        function handlePass() {
             moveToNext();
        }

        function moveToNext(){
            const nextIndex = findNextQuestion();

            if (nextIndex === -1) {
                endGame();
            } else {
                currentQuestionIndex = nextIndex;
                updateUI();
            }
        }
        
        function startTimer() {
            timerDisplay.textContent = timeLeft;
            clearInterval(timer); // Clear any existing timer
            timer = setInterval(() => {
                timeLeft--;
                timerDisplay.textContent = timeLeft;
                if (timeLeft <= 0) {
                    endGame('¡Se acabó el tiempo!');
                }
            }, 1000);
        }

        function setControlsState(enabled) {
            answerBtn.disabled = !enabled;
            passBtn.disabled = !enabled;
            answerInput.disabled = !enabled;
        }

        function endGame(message = '¡Has completado el rosco!') {
            clearInterval(timer);
            setControlsState(false);
            modalTitle.textContent = message;
            modalCorrect.textContent = correctAnswers;
            modalIncorrect.textContent = incorrectAnswers;
            modalContainer.classList.add('visible');
        }

        function initGame() {
            questions = setupQuestions();
            currentQuestionIndex = 0;
            correctAnswers = 0;
            incorrectAnswers = 0;
            timeLeft = 200;
            
            if (modalContainer) modalContainer.classList.remove('visible');
            setControlsState(true);
            
            // Use a timeout to ensure the container has dimensions
            setTimeout(() => {
                createRosco();
                updateUI();
                startTimer();
            }, 0);
        }

        answerBtn.addEventListener('click', handleAnswer);
        answerInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleAnswer();
        });
        passBtn.addEventListener('click', handlePass);
        restartBtn.addEventListener('click', initGame);
        window.addEventListener('resize', createRosco);

        initGame();
    });
</script> 