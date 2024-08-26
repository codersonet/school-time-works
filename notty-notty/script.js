document.addEventListener("DOMContentLoaded", function() {
    const typingText = document.getElementById('typingText');
    const noButton = document.getElementById('noButton');

    const text = "WILL YOU BE MY GIRLFRIEND? â¤ï¸";
    let typingSpeed = 100; // Typing speed in milliseconds
    let eraseSpeed = 50; // Erasing speed in milliseconds
    let pauseAfterTyping = 2000; // Pause after typing the whole text

    function typeText() {
        typingText.textContent = ''; // Clear text
        let index = 0;

        function type() {
            if (index < text.length) {
                typingText.textContent += text.charAt(index);
                index++;
                setTimeout(type, typingSpeed);
            } else {
                setTimeout(() => {
                    eraseText();
                }, pauseAfterTyping);
            }
        }

        function eraseText() {
            if (index > 0) {
                typingText.textContent = text.substring(0, index - 1);
                index--;
                setTimeout(eraseText, eraseSpeed);
            } else {
                setTimeout(type, 500); // Pause before retyping
            }
        }

        type();
    }

    function moveButton() {
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;
        const buttonWidth = noButton.clientWidth;
        const buttonHeight = noButton.clientHeight;

        function getRandomPosition() {
            const x = Math.random() * (viewportWidth - buttonWidth);
            const y = Math.random() * (viewportHeight - buttonHeight);
            return { x, y };
        }

        function updatePosition() {
            const { x, y } = getRandomPosition();
            noButton.style.left = `${x}px`;
            noButton.style.top = `${y}px`;
        }

        noButton.addEventListener('click', function() {
            updatePosition();
        });

        updatePosition(); // Set initial position
    }

    // Start typing animation and button movement
    typeText();
    moveButton();

    // Ensure button position is recalculated if the window is resized
    window.addEventListener('resize', moveButton);
});
