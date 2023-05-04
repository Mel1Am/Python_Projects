document.addEventListener('DOMContentLoaded', function() {
    const revealButtons = document.querySelectorAll('.reveal-solution');
    revealButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            const solution = document.querySelectorAll('.solution')[index];
            solution.style.display = solution.style.display === 'none' ? 'block' : 'none';
        });
    });
});
