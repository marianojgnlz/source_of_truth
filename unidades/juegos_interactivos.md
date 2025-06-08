# Juegos Interactivos

<div id="games-wrapper">
    <div class="container mx-auto p-4 lg:p-8">
        <header class="text-center mb-8">
            <h1 class="text-4xl md:text-5xl font-bold text-indigo-900">Juegos Interactivos</h1>
            <p class="text-xl text-slate-600 mt-2">Pon a prueba tus conocimientos con estos juegos interactivos.</p>
        </header>

        <nav class="flex flex-wrap justify-center gap-2 md:gap-4 mb-8" id="games-nav">
            <button data-target="crossword-game" class="game-nav-button active w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-indigo-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Crucigrama (U6)</button>
            <button data-target="dnd-game" class="game-nav-button w-full sm:w-auto text-sm md:text-base bg-white shadow-sm hover:bg-sky-600 hover:text-white transition-all duration-300 py-2 px-4 rounded-lg font-medium">Conexión de Conceptos (U4)</button>
        </nav>

        <main id="games-container">
            <!-- Crossword Game -->
            <div id="crossword-game" class="game-section">
                <div class="flex flex-col lg:flex-col gap-8">
                    <div class="w-full lg:w-2/3 flex justify-center items-center">
                        <div id="crossword-grid"></div>
                    </div>

                    <div class="w-full lg bg-white p-6 rounded-2xl shadow-lg">
                        <div id="clues-container">
                            <div>
                                <h2 class="text-2xl font-bold text-indigo-800 border-b-2 border-indigo-200 pb-2 mb-4">Horizontales</h2>
                                <ul id="across-clues" class="space-y-3 text-slate-700"></ul>
                            </div>
                            <div class="mt-8">
                                <h2 class="text-2xl font-bold text-indigo-800 border-b-2 border-indigo-200 pb-2 mb-4">Verticales</h2>
                                <ul id="down-clues" class="space-y-3 text-slate-700"></ul>
                            </div>
                        </div>
                        <div id="controls" class="mt-8 pt-6 border-t border-indigo-200 flex flex-wrap gap-3 justify-center">
                            <button id="check-btn" class="bg-indigo-600 text-white font-bold py-2 px-6 rounded-lg hover:bg-indigo-700 transition-colors">Verificar</button>
                            <button id="reveal-btn" class="bg-amber-500 text-white font-bold py-2 px-6 rounded-lg hover:bg-amber-600 transition-colors">Revelar Todo</button>
                            <button id="reset-btn" class="bg-slate-400 text-white font-bold py-2 px-6 rounded-lg hover:bg-slate-500 transition-colors">Reiniciar</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Drag and Drop Game -->
            <div id="dnd-game" class="game-section">
                <div class="container mx-auto max-w-6xl" style="background-color: #f0f9ff; padding: 2rem;">
                    <!-- Encabezado del Juego -->
                    <header class="text-center mb-8">
                        <h1 class="text-3xl md:text-5xl font-extrabold text-sky-800">Conexión de Conceptos de RRHH</h1>
                        <p class="text-lg md:text-xl text-slate-600 mt-2">Arrastra el término a su definición correcta. ¡Pon a prueba tus conocimientos de la Unidad 4!</p>
                    </header>

                    <!-- Contenedor principal del juego -->
                    <div class="grid grid-cols-2 gap-8">
                        <!-- Columna de Términos -->
                        <div class="p-4 bg-white rounded-xl shadow-lg">
                            <h2 class="text-2xl font-bold text-center text-sky-700 mb-4 border-b-2 border-sky-200 pb-2">Términos Clave</h2>
                            <div id="dnd-terms-container" class="space-y-4">
                                <!-- Los términos se cargarán aquí con JS -->
                            </div>
                        </div>

                        <!-- Columna de Definiciones -->
                        <div class="p-4 bg-white rounded-xl shadow-lg">
                            <h2 class="text-2xl font-bold text-center text-sky-700 mb-4 border-b-2 border-sky-200 pb-2">Definiciones</h2>
                            <div id="dnd-definitions-container" class="space-y-4">
                                <!-- Las definiciones se cargarán aquí con JS -->
                            </div>
                        </div>
                    </div>

                    <!-- Controles y puntuación -->
                    <div class="mt-8 text-center">
                        <p class="text-2xl font-bold text-slate-700">Aciertos: <span id="dnd-score" class="text-green-600">0</span> / <span id="dnd-total-terms"></span></p>
                        <button id="dnd-reset-button" class="mt-4 bg-sky-600 text-white font-bold py-2 px-6 rounded-lg hover:bg-sky-700 transition-transform transform hover:scale-105 shadow-md">
                            Reiniciar Juego
                        </button>
                    </div>

                </div>

                <!-- Modal de Finalización -->
                <div id="dnd-completion-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center hidden opacity-0">
                    <div class="bg-white p-8 rounded-2xl shadow-2xl text-center transform transition-transform scale-95" id="dnd-modal-content">
                        <h2 class="text-4xl font-extrabold text-green-600 mb-4">¡Felicitaciones!</h2>
                        <p class="text-xl text-slate-700 mb-6">Has completado el desafío y demostrado tu dominio de los conceptos de la Unidad 4.</p>
                        <button id="dnd-play-again-button" class="bg-green-600 text-white font-bold py-3 px-8 rounded-lg text-lg hover:bg-green-700 transition-transform transform hover:scale-105 shadow-lg">
                            Jugar de Nuevo
                        </button>
                    </div>
                </div>
            </div>

        </main>
    </div>
</div>

<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #f1f5f9;
        color: #1e293b;
    }
    #crossword-grid {
        display: grid;
        grid-template-columns: repeat(15, minmax(0, 1fr));
        grid-template-rows: repeat(15, minmax(0, 1fr));
        gap: 1px;
        width: 100%;
        max-width: 600px;
        aspect-ratio: 1 / 1;
    }
    .grid-cell {
        position: relative;
        width: 100%;
        height: 100%;
        background-color: #1e1b4b;
        border: 1px solid #312e81;
    }
    .grid-cell.letter {
        background-color: #ffffff;
    }
    .grid-cell input {
        width: 100%;
        height: 100%;
        text-align: center;
        text-transform: uppercase;
        font-weight: 700;
        font-size: 1.125rem;
        color: #1e293b;
        border: none;
        background: transparent;
        padding: 0;
        caret-color: #4f46e5;
    }
    .grid-cell input:focus {
        outline: none;
        background-color: #e0e7ff;
    }
    .grid-cell .clue-number {
        position: absolute;
        top: 2px;
        left: 2px;
        font-size: 0.6rem;
        font-weight: 700;
        color: #4338ca;
        z-index: 1;
    }
    .clue-item.active {
        background-color: #e0e7ff;
        color: #312e81;
    }
    .grid-cell.active {
        background-color: #e0e7ff;
    }
    .grid-cell.correct input {
        color: #16a34a;
    }
    .grid-cell.incorrect input {
        color: #dc2626;
    }
    .game-section {
        display: none;
    }
    .game-section.active {
        display: block;
    }
    .game-nav-button.active {
        background-color: #4f46e5;
        color: white;
    }

    /* Drag and Drop Game Styles */
    .term-card {
        cursor: grab;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .term-card:active {
        cursor: grabbing;
        transform: scale(1.05);
        box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        z-index: 10;
    }
    .drop-zone {
        transition: background-color 0.3s ease, border-color 0.3s ease;
        border-style: dashed;
    }
    .drop-zone.over {
        background-color: #dbeafe; /* blue-100 */
        border-color: #3b82f6; /* blue-500 */
    }
    .drop-zone.correct {
        background-color: #dcfce7; /* green-100 */
        border-color: #22c55e; /* green-500 */
        border-style: solid;
    }
    .drop-zone.correct .term-placeholder {
        display: none;
    }
    .drop-zone.incorrect {
        background-color: #fee2e2; /* red-100 */
        border-color: #ef4444; /* red-500 */
    }
    .term-card.matched {
        opacity: 0.5;
        cursor: default;
        pointer-events: none;
    }
    #dnd-completion-modal {
        transition: opacity 0.3s ease-in-out;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Game navigation functionality
        const gameNavButtons = document.querySelectorAll('.game-nav-button');
        const gameSections = document.querySelectorAll('.game-section');
        
        // Show crossword by default
        document.getElementById('crossword-game').classList.add('active');
        
        gameNavButtons.forEach(button => {
            button.addEventListener('click', () => {
                const targetId = button.dataset.target;
                
                // Hide all game sections
                gameSections.forEach(section => {
                    section.classList.remove('active');
                });
                
                // Remove active class from all nav buttons
                gameNavButtons.forEach(btn => {
                    btn.classList.remove('active');
                });
                
                // Show target section and activate button
                document.getElementById(targetId).classList.add('active');
                button.classList.add('active');
            });
        });

        // Crossword game logic
        const crosswordData = [
            { clue: 'Pilar de la seguridad que asegura que la información es exacta y no ha sido modificada.', answer: 'INTEGRIDAD', startx: 1, starty: 8, direction: 'across', number: 1 },
            { clue: 'Revisión sistemática de los sistemas para emitir una opinión profesional.', answer: 'AUDITORIA', startx: 3, starty: 1, direction: 'down', number: 2 },
            { clue: 'Acción, manual o automática, para prevenir, corregir errores o irregularidades.', answer: 'CONTROL', startx: 9, starty: 4, direction: 'down', number: 3 },
            { clue: 'Potencial de que una amenaza determinada explote las vulnerabilidades de un activo.', answer: 'RIESGO', startx: 1, starty: 5, direction: 'down', number: 4 },
            { clue: 'Copia de seguridad de datos para facilitar la recuperación ante desastres.', answer: 'BACKUP', startx: 6, starty: 1, direction: 'across', number: 5 },
            { clue: 'Documento que define el nivel de seguridad y las reglas generales sobre lo que está permitido.', answer: 'POLITICA', startx: 8, starty: 1, direction: 'across', number: 6 },
            { clue: 'Tipo de ataque que altera la comunicación o los sistemas, a diferencia del pasivo.', answer: 'ACTIVO', startx: 11, starty: 4, direction: 'down', number: 7 },
            { clue: 'Punto de vista de la seguridad relacionado con el cumplimiento de normativas y leyes.', answer: 'LEGAL', startx: 4, starty: 11, direction: 'across', number: 8 },
            { clue: 'Pilar de la seguridad que asegura que los sistemas son accesibles para usuarios autorizados.', answer: 'DISPONIBILIDAD', startx: 1, starty: 13, direction: 'across', number: 9 }
        ];

        const gridElement = document.getElementById('crossword-grid');
        const acrossCluesElement = document.getElementById('across-clues');
        const downCluesElement = document.getElementById('down-clues');
        const gridSize = 15;
        let cells = [];

        function initializeGrid() {
            cells = Array.from({ length: gridSize }, () => Array(gridSize).fill(null));
            gridElement.innerHTML = '';
            acrossCluesElement.innerHTML = '';
            downCluesElement.innerHTML = '';

            for (let y = 0; y < gridSize; y++) {
                for (let x = 0; x < gridSize; x++) {
                    const cell = document.createElement('div');
                    cell.id = `cell-${x}-${y}`;
                    cell.classList.add('grid-cell');
                    gridElement.appendChild(cell);
                }
            }

            crosswordData.forEach(word => {
                let { answer, startx, starty, direction, number } = word;
                let x = startx;
                let y = starty;
                
                if (direction === 'across') {
                     for (let i = 0; i < answer.length; i++) {
                        placeLetter(x + i, y, answer[i], word);
                    }
                } else if (direction === 'down') {
                    for (let i = 0; i < answer.length; i++) {
                        placeLetter(x, y + i, answer[i], word);
                    }
                }

                const startCellElement = document.getElementById(`cell-${startx}-${starty}`);
                if (startCellElement) {
                     const numberSpan = document.createElement('span');
                     numberSpan.textContent = number;
                     numberSpan.classList.add('clue-number');
                     startCellElement.appendChild(numberSpan);
                }
            });
            
            populateClues();
            addEventListeners();
        }

        function placeLetter(x, y, char, wordData) {
             if (x < gridSize && y < gridSize) {
                const cellElement = document.getElementById(`cell-${x}-${y}`);
                if (cellElement && !cellElement.classList.contains('letter')) {
                    cellElement.classList.add('letter');
                    const input = document.createElement('input');
                    input.type = 'text';
                    input.maxLength = 1;
                    input.dataset.x = x;
                    input.dataset.y = y;
                    input.dataset.correct = char;
                    cellElement.appendChild(input);

                    cells[y][x] = { element: cellElement, input, correct: char, words: [] };
                }
                if (cells[y][x] && !cells[y][x].words.includes(wordData)) {
                    cells[y][x].words.push(wordData);
                }
            }
        }
        
        function populateClues() {
            crosswordData.sort((a, b) => a.number - b.number).forEach(word => {
                const clueItem = document.createElement('li');
                clueItem.innerHTML = `<span class="font-bold">${word.number}.</span> ${word.clue}`;
                clueItem.classList.add('clue-item', 'p-2', 'rounded-lg', 'cursor-pointer', 'transition-colors');
                clueItem.dataset.number = word.number;

                if (word.direction === 'across') {
                    acrossCluesElement.appendChild(clueItem);
                } else {
                    downCluesElement.appendChild(clueItem);
                }
            });
        }

        function addEventListeners() {
            gridElement.addEventListener('keyup', handleInput);
            gridElement.addEventListener('click', handleCellClick);
            
            document.querySelectorAll('.clue-item').forEach(item => {
                item.addEventListener('click', handleClueClick);
            });

            document.getElementById('check-btn').addEventListener('click', checkAnswers);
            document.getElementById('reveal-btn').addEventListener('click', revealAnswers);
            document.getElementById('reset-btn').addEventListener('click', resetGrid);
        }

        function handleInput(e) {
            if (e.target.tagName !== 'INPUT' || e.target.value.length !== 1) return;
            
            const x = parseInt(e.target.dataset.x);
            const y = parseInt(e.target.dataset.y);
            const activeWord = getActiveWord(x, y);

            if (!activeWord) return;

            if (activeWord.direction === 'across' && x + 1 < gridSize && cells[y][x + 1]) {
                cells[y][x + 1].input.focus();
            } else if (activeWord.direction === 'down' && y + 1 < gridSize && cells[y + 1][x]) {
                cells[y + 1][x].input.focus();
            }
        }

        function handleCellClick(e) {
             if (e.target.tagName !== 'INPUT') return;
             const x = parseInt(e.target.dataset.x);
             const y = parseInt(e.target.dataset.y);
             highlightClueAndWord(x, y);
        }

        function handleClueClick(e) {
            const clueItem = e.currentTarget;
            const number = parseInt(clueItem.dataset.number);
            const wordData = crosswordData.find(w => w.number === number);
            if (wordData) {
                highlightClueAndWord(wordData.startx, wordData.starty, number);
                cells[wordData.starty][wordData.startx].input.focus();
            }
        }

        function getActiveWord(x, y) {
            const cellData = cells[y][x];
            if (!cellData || cellData.words.length === 0) return null;
            
            const activeClueNumber = document.querySelector('.clue-item.active')?.dataset.number;
            if (activeClueNumber && cellData.words.some(w => w.number == activeClueNumber)) {
                return cellData.words.find(w => w.number == activeClueNumber);
            }
            return cellData.words[0];
        }

        function highlightClueAndWord(x, y, forceNumber = null) {
            clearHighlights();
            let wordToHighlight;

            if (forceNumber) {
                 wordToHighlight = crosswordData.find(w => w.number === forceNumber);
            } else {
                 wordToHighlight = getActiveWord(x,y);
            }
            
            if (!wordToHighlight) return;

            document.querySelector(`.clue-item[data-number='${wordToHighlight.number}']`)?.classList.add('active');
            
            let currentX = wordToHighlight.startx;
            let currentY = wordToHighlight.starty;
            for (let i = 0; i < wordToHighlight.answer.length; i++) {
                cells[currentY][currentX].element.classList.add('active');
                if (wordToHighlight.direction === 'across') currentX++;
                else currentY++;
            }
        }

        function clearHighlights() {
            document.querySelectorAll('.clue-item.active').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.grid-cell.active').forEach(el => el.classList.remove('active'));
        }

        function checkAnswers() {
            cells.forEach(row => {
                row.forEach(cell => {
                    if (cell && cell.input.value !== '') {
                        cell.element.classList.remove('correct', 'incorrect');
                        if (cell.input.value.toUpperCase() === cell.correct) {
                            cell.element.classList.add('correct');
                        } else {
                            cell.element.classList.add('incorrect');
                        }
                    }
                });
            });
        }

        function revealAnswers() {
             cells.forEach(row => {
                row.forEach(cell => {
                    if (cell) {
                        cell.element.classList.remove('incorrect');
                        cell.element.classList.add('correct');
                        cell.input.value = cell.correct;
                    }
                });
            });
        }

        function resetGrid() {
             cells.forEach(row => {
                row.forEach(cell => {
                    if (cell) {
                        cell.input.value = '';
                        cell.element.classList.remove('correct', 'incorrect', 'active');
                    }
                });
            });
            clearHighlights();
        }

        initializeGrid();
        
        // Drag and Drop game logic
        function initializeDragAndDropGame() {
            // --- DATOS DEL JUEGO ---
            const gameData = [
                { id: 1, term: 'Análisis Organizacional', definition: 'Examina objetivos futuros, cultura y planes estratégicos para definir necesidades de formación a nivel macro.' },
                { id: 2, term: 'Ley del Efecto', definition: 'Principio que establece que un comportamiento tiende a mantenerse si es percibido como recompensador.' },
                { id: 3, term: 'Desarrollo Organizacional (DO)', definition: 'Aborda a la organización como un sistema total para mejorar la efectividad y la salud a largo plazo.' },
                { id: 4, term: 'Remuneración Variable', definition: 'Porción de la compensación que depende de los resultados logrados por la empresa, un área o un individuo.' },
                { id: 5, term: 'Método de Jerarquización', definition: 'Ordena los cargos del más al menos importante en su conjunto, sin analizar sus componentes.' },
                { id: 6, term: 'Equilibrio Externo (Salarios)', definition: 'Se logra comparando los salarios de la empresa con los del mercado laboral para ser competitivo.' },
                { id: 7, term: 'Beneficio Voluntario', definition: 'Beneficio concedido por liberalidad de la empresa, no exigido por ley (ej. seguro médico privado).' },
                { id: 8, term: 'Plan de Sucesión', definition: 'Herramienta para identificar y desarrollar talento interno para futuras posiciones de liderazgo.' },
                { id: 9, term: 'Indicador a Posteriori', definition: 'Problema ya ocurrido que señala una carencia de entrenamiento (ej. alto número de accidentes).' },
                { id: 10, term: 'Teoría de la Inequidad', definition: 'Sostiene que las personas comparan su ratio de recompensas/contribuciones con el de otros para juzgar la justicia.' }
            ];

            // --- REFERENCIAS AL DOM ---
            const termsContainer = document.getElementById('dnd-terms-container');
            const definitionsContainer = document.getElementById('dnd-definitions-container');
            const scoreElement = document.getElementById('dnd-score');
            const totalElement = document.getElementById('dnd-total-terms');
            const resetButton = document.getElementById('dnd-reset-button');
            const completionModal = document.getElementById('dnd-completion-modal');
            const modalContent = document.getElementById('dnd-modal-content');
            const playAgainButton = document.getElementById('dnd-play-again-button');

            if (!termsContainer) return; // Don't run if the game is not on the active page

            let score = 0;
            let draggedItem = null;

            // --- FUNCIONES DEL JUEGO ---
            function shuffle(array) {
                for (let i = array.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [array[i], array[j]] = [array[j], array[i]];
                }
                return array;
            }

            function initGame() {
                score = 0;
                if(scoreElement) scoreElement.textContent = score;
                if(totalElement) totalElement.textContent = gameData.length;
                if(termsContainer) termsContainer.innerHTML = '';
                if(definitionsContainer) definitionsContainer.innerHTML = '';

                const shuffledTerms = shuffle([...gameData]);
                const shuffledDefinitions = shuffle([...gameData]);

                shuffledTerms.forEach(item => {
                    const termDiv = document.createElement('div');
                    termDiv.id = `term-${item.id}`;
                    termDiv.draggable = true;
                    termDiv.className = 'term-card bg-sky-100 border-l-4 border-sky-500 text-sky-900 font-semibold p-4 rounded-lg shadow-sm';
                    termDiv.textContent = item.term;
                    if(termsContainer) termsContainer.appendChild(termDiv);
                });

                shuffledDefinitions.forEach(item => {
                    const defDiv = document.createElement('div');
                    defDiv.dataset.id = item.id;
                    defDiv.className = 'drop-zone bg-slate-50 border-2 border-slate-300 p-4 rounded-lg min-h-[80px] flex items-center justify-center';
                    
                    const placeholder = document.createElement('p');
                    placeholder.className = 'term-placeholder text-slate-400 text-center';
                    placeholder.textContent = item.definition;
                    
                    const definitionText = document.createElement('p');
                    definitionText.className = 'definition-text hidden font-medium text-slate-800 text-center';
                    definitionText.innerHTML = `<strong>${item.term}:</strong> ${item.definition}`;

                    defDiv.appendChild(placeholder);
                    defDiv.appendChild(definitionText);
                    if(definitionsContainer) definitionsContainer.appendChild(defDiv);
                });
                
                addDragAndDropListeners();
            }
            
            function addDragAndDropListeners() {
                const terms = document.querySelectorAll('#dnd-game .term-card');
                const dropZones = document.querySelectorAll('#dnd-game .drop-zone');

                terms.forEach(term => {
                    term.addEventListener('dragstart', (e) => {
                        draggedItem = e.target;
                        setTimeout(() => e.target.style.display = 'none', 0);
                    });

                    term.addEventListener('dragend', (e) => {
                        setTimeout(() => {
                            if (draggedItem) {
                              draggedItem.style.display = 'block';
                            }
                            draggedItem = null;
                        }, 0);
                    });
                });

                dropZones.forEach(zone => {
                    zone.addEventListener('dragover', (e) => {
                        e.preventDefault();
                        if (!zone.classList.contains('correct')) {
                            zone.classList.add('over');
                        }
                    });

                    zone.addEventListener('dragleave', (e) => {
                        zone.classList.remove('over');
                    });

                    zone.addEventListener('drop', (e) => {
                        e.preventDefault();
                        zone.classList.remove('over');
                        if (zone.classList.contains('correct') || !draggedItem) return;

                        const draggedId = draggedItem.id.split('-')[1];
                        const zoneId = zone.dataset.id;

                        if (draggedId === zoneId) {
                            zone.classList.add('correct');
                            draggedItem.classList.add('matched');
                            draggedItem.draggable = false;
                            
                            zone.querySelector('.term-placeholder').style.display = 'none';
                            const definitionText = zone.querySelector('.definition-text');
                            definitionText.classList.remove('hidden');

                            score++;
                            scoreElement.textContent = score;

                            if (score === gameData.length) {
                               showCompletionModal();
                            }
                        } else {
                            zone.classList.add('incorrect');
                            setTimeout(() => zone.classList.remove('incorrect'), 500);
                        }
                    });
                });
            }
            
            function showCompletionModal() {
                if(!completionModal) return;
                completionModal.classList.remove('hidden');
                setTimeout(() => {
                    completionModal.style.opacity = '1';
                    if (modalContent) modalContent.style.transform = 'scale(1)';
                }, 50);
            }

            function hideCompletionModal() {
                if(!completionModal) return;
                completionModal.style.opacity = '0';
                if(modalContent) modalContent.style.transform = 'scale(0.95)';
                setTimeout(() => {
                     completionModal.classList.add('hidden');
                }, 300);
            }

            if(resetButton) resetButton.addEventListener('click', initGame);
            if(playAgainButton) playAgainButton.addEventListener('click', () => {
                hideCompletionModal();
                initGame();
            });
            
            initGame();
        }

        initializeDragAndDropGame();

    });
</script> 