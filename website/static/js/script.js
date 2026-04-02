// Track current active direction (null means stopped)
let activeDirection = null;

const buttons = {
    up: document.getElementById('up-btn'),
    down: document.getElementById('down-btn'),
    left: document.getElementById('left-btn'),
    right: document.getElementById('right-btn')
};

function handleStart(direction) {
    // Prevent default to stop scrolling when pressing arrow keys if used as HTML input logic later
    event.preventDefault(); 
    activeDirection = direction;
    fetch('/control/move/' + direction, { method: 'POST' });
}

function handleStop() {
    fetch('/control/stop', { method: 'POST' });
    activeDirection = null;
}

// Setup Listeners
buttons.up.addEventListener('mousedown', (e) => handleStart('up'));
buttons.down.addEventListener('mousedown', (e) => handleStart('down'));
buttons.left.addEventListener('mousedown', (e) => handleStart('left'));
buttons.right.addEventListener('mousedown', (e) => handleStart('right'));

// Release logic (mouseup or mouse leaving the area to stop all motors if needed)
document.body.addEventListener('mouseup', handleStop);
document.body.addEventListener('mouseleave', handleStop);

// Note: Since we only have buttons, 'mouseup' on the button handles release. 
// We attach a global listener for safety in case mouse drags out fast.
