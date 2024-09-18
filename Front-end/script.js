document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.selectable-button');
    const hiddenInput = document.getElementById('interests');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            button.classList.toggle('selected'); // Toggle selection

            // Update the hidden input value
            const selectedValues = Array.from(document.querySelectorAll('.selectable-button.selected'))
                .map(selectedButton => selectedButton.getAttribute('data-value'));
            hiddenInput.value = selectedValues.join(','); // Store selected interests as a comma-separated string
        });
    });
});
