// script.js

// Select all elements with the "bounce" class
const bounceLetters = document.querySelectorAll('.bounce');
let currentIndex = 0;

function bounceSequentially() {
    // Reset animations
    bounceLetters.forEach(letter => {
        letter.style.animation = 'none';
    });

    // Apply bounce animation to the current letter
    bounceLetters[currentIndex].style.animation = 'bounce 0.5s ease-in-out';

    // Move to the next letter
    currentIndex = (currentIndex + 1) % bounceLetters.length;

    // Repeat after 500ms
    setTimeout(bounceSequentially, 500);
}

// Start the animation loop
bounceSequentially();
