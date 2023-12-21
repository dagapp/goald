function setBlackout() {
    var blackout = document.getElementById('blackout');
    blackout.style.display = 'block';
}

function removeBlackout() {
    var blackout = document.getElementById('blackout');
    blackout.style.display = 'none';
}

function openModal(moadalId) {
    var modal = document.getElementById(moadalId);
    modal.style.display = 'block';
    setBlackout();
}

function closeModal(modalId) {
    var groupActionWindow = document.getElementById('groupActionWindow');
    if (groupActionWindow.style.display === 'block')
        groupActionWindow.style.display = 'none';

    var modal = document.getElementById(modalId);
    modal.style.display = 'none';
    removeBlackout();
}

function createGroupButtonPressed() {
    closeModal('createGroupWindow');
}

function joinToGroupButtonPressed() {
    closeModal('joinToGroupWindow');
}

function acceptDeleteGroup() {
    closeModal('deleteGroupWindow');
}

function acceptDeleteGoal() {
    closeModal('deleteGoalWindow');
}

function pay() {
    closeModal('payWindow');
}
