function setupModal(modalId, openModalId, closeButtonClass) {
    let modal = document.getElementById(modalId);
    let btn = document.getElementById(openModalId);
    let span = document.querySelector('.' + closeButtonClass);

    btn.onclick = function() {
        modal.style.display = "block";
    }

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}