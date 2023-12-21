function setBlackout() {
    var blackout = document.getElementById('blackout');
    blackout.style.display = 'block';
}

function removeBlackout() {
    var blackout = document.getElementById('blackout');
    blackout.style.display = 'none';
}

function openModal() {
    var modal = document.getElementById('groupActionWindow');
    modal.style.display = 'block';
    setBlackout();
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = 'none';
    removeBlackout();
}

function openCreateGroupWindow() {
    closeModal('groupActionWindow');
    var modal = document.getElementById('createGroupWindow');
    modal.style.display = 'block';
    setBlackout();
}

function createGroupButtonPressed() {
    closeModal('createGroupWindow');
}

function openJoinToGroupWindow() {
    closeModal('groupActionWindow');
    var modal = document.getElementById('joinToGroupWindow');
    modal.style.display = 'block';
    setBlackout();
}

function joinToGroupButtonPressed() {
    closeModal('joinToGroupWindow');
}