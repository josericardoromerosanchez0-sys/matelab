// Game state
let timeLeft = 30;
let timer;
let gameActive = true;
let canAnswer = true;
let correctAnswerIndex = 0;

// Initialize the game
function initGame(correctIndex) {
    correctAnswerIndex = correctIndex || 0;
    setupEventListeners();
    startTimer();
}

// Set up event listeners
function setupEventListeners() {
    const options = document.querySelectorAll('.option-btn');
    options.forEach(option => {
        option.addEventListener('click', handleAnswerClick);
    });

    const restartBtn = document.getElementById('restart-btn');
    if (restartBtn) {
        restartBtn.addEventListener('click', restartGame);
    }
}

// Handle answer selection
function handleAnswerClick(event) {
    if (!canAnswer) return;

    const selectedIndex = parseInt(event.currentTarget.getAttribute('data-index'));
    checkAnswer(selectedIndex, correctAnswerIndex);
}

// Start the game timer
function startTimer() {
    const timerElement = document.getElementById('timer');
    if (!timerElement) {
        console.error("Timer element not found");
        return;
    }

    clearInterval(timer);
    updateTimerDisplay();
    timer = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateTimerDisplay();
        } else {
            clearInterval(timer);
            timeUp();
        }
    }, 1000);
}

// Update the timer display
function updateTimerDisplay() {
    const timerElement = document.getElementById('timer');
    if (timerElement) {
        timerElement.textContent = `${timeLeft}s`;

        if (timeLeft <= 5) {
            timerElement.classList.add('text-danger', 'fw-bold');
            timerElement.style.animation = 'pulse 0.5s infinite';
        } else {
            timerElement.classList.remove('text-danger', 'fw-bold');
            timerElement.style.animation = 'none';
        }
    }
}

// Check the selected answer
function checkAnswer(selectedIndex, correctIndex) {
    if (!canAnswer) return;

    canAnswer = false;
    clearInterval(timer);

    const buttons = document.querySelectorAll('.option-btn');
    const feedbackElement = document.getElementById('feedback');

    if (!feedbackElement) {
        console.error("Feedback element not found");
        return;
    }

    // Disable all buttons
    buttons.forEach(btn => {
        if (btn) btn.disabled = true;
    });

    // Highlight selected and correct answers
    if (selectedIndex === correctIndex) {
        if (buttons[selectedIndex]) buttons[selectedIndex].classList.add('correct');
        feedbackElement.textContent = "✅ ¡Respuesta correcta! ¡Buen trabajo!";
        feedbackElement.className = "text-success h4";
    } else {
        if (buttons[selectedIndex]) buttons[selectedIndex].classList.add('incorrect');
        if (buttons[correctIndex]) {
            buttons[correctIndex].classList.add('correct');
            feedbackElement.textContent = `❌ Incorrecto. La respuesta correcta es: ${buttons[correctIndex].textContent}`;
        } else {
            feedbackElement.textContent = "❌ Respuesta incorrecta";
        }
        feedbackElement.className = "text-danger h4";
    }

    // Show restart button
    const restartBtn = document.getElementById('restart-btn');
    if (restartBtn) {
        restartBtn.style.display = 'inline-block';
    }
}

// Handle time up
function timeUp() {
    if (!canAnswer) return;

    canAnswer = false;
    const buttons = document.querySelectorAll('.option-btn');
    const feedbackElement = document.getElementById('feedback');

    if (!feedbackElement) {
        console.error("Feedback element not found");
        return;
    }

    // Disable all buttons
    buttons.forEach(btn => {
        if (btn) btn.disabled = true;
    });

    // Highlight the correct answer
    if (buttons[correctAnswerIndex]) {
        buttons[correctAnswerIndex].classList.add('correct');
        feedbackElement.textContent = "⏱️ ¡Tiempo agotado! La respuesta correcta está resaltada.";
        feedbackElement.className = "text-warning h4";
    }

    // Show restart button
    const restartBtn = document.getElementById('restart-btn');
    if (restartBtn) {
        restartBtn.style.display = 'inline-block';
    }
}

// Restart the game
function restartGame() {
    // Reset game state
    timeLeft = 30;
    gameActive = true;
    canAnswer = true;

    // Reset UI
    const buttons = document.querySelectorAll('.option-btn');
    buttons.forEach(btn => {
        if (btn) {
            btn.disabled = false;
            btn.classList.remove('correct', 'incorrect');
        }
    });

    const feedbackElement = document.getElementById('feedback');
    if (feedbackElement) {
        feedbackElement.textContent = '';
        feedbackElement.className = '';
    }

    const restartBtn = document.getElementById('restart-btn');
    if (restartBtn) {
        restartBtn.style.display = 'none';
    }

    // Restart timer
    startTimer();
}

// Make functions available globally
window.initGame = initGame;
window.checkAnswer = checkAnswer;
window.restartGame = restartGame;