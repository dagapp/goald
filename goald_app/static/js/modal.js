function setBlackout() {
    var blackout = document.getElementById('blackout');
    blackout.style.display = 'block';
}

function removeBlackout() {
    var blackout = document.getElementById('blackout');
    blackout.style.display = 'none';
}

function openModal() {
    var modal = document.getElementById('groupPlusPressed');
    modal.style.display = 'block';
    setBlackout();
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = 'none';
    removeBlackout();
}

function openCreateGroupWindow() {
    closeModal('groupPlusPressed');
    document.getElementById('groupPlusPressed').style.display = 'none';
    var modal = document.getElementById('createGroupWindow');
    modal.style.display = 'block';
    setBlackout();
}

function createGroupButtonPressed() {
    closeModal('createGroupWindow');
}