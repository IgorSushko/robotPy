// Track current active direction (null means stopped)
let activeDirection = null;

// ADDED: persistent button state variables
let isButtonUp = false;
let isButtonDown = false;
let isButtonLeft = false;
let isButtonRight = false;

const buttons = {
    up: document.getElementById('up-btn'),
    down: document.getElementById('down-btn'),
    left: document.getElementById('left-btn'),
    right: document.getElementById('right-btn')
};

// WiFi signal indicator
function updateWiFiSignal() {
    fetch('/wifi/signal', { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            const wifiLevel = document.getElementById('wifi-level');
            const wifiPercentage = document.getElementById('wifi-percentage');

            const width = data.signal_percentage;
            wifiLevel.style.width = width + '%';
            wifiPercentage.textContent = ' ' + Math.round(width) + '%';

            if (width >= 70) {
                wifiLevel.style.backgroundColor = '#4CAF50';
            } else if (width >= 40) {
                wifiLevel.style.backgroundColor = '#FFC107';
            } else {
                wifiLevel.style.backgroundColor = '#f44336';
            }
        })
        .catch(error => console.error('Error fetching WiFi signal:', error));
}

updateWiFiSignal();
setInterval(updateWiFiSignal, 5000);

// MODIFIED: fixed function, added state checks
function handleStart(direction, event) {
    event.preventDefault();

    // ADDED: prevent duplicate requests
    if (direction === 'up' && !isButtonUp) {
        isButtonUp = true;
        activeDirection = direction;
        fetch('/control/move/' + direction, { method: 'POST' });
    } else if (direction === 'down' && !isButtonDown) {
        isButtonDown = true;
        activeDirection = direction;
        fetch('/control/move/' + direction, { method: 'POST' });
    } else if (direction === 'left' && !isButtonLeft) {
        isButtonLeft = true;
        activeDirection = direction;
        fetch('/control/move/' + direction, { method: 'POST' });
    } else if (direction === 'right' && !isButtonRight) {
        isButtonRight = true;
        activeDirection = direction;
        fetch('/control/move/' + direction, { method: 'POST' });
    }
}

// MODIFIED: send only one stop request
function handleStop() {
    if (activeDirection !== null) { // ADDED: prevent duplicate stop calls
        fetch('/control/stop', { method: 'POST' });
    }

    // ADDED: reset all states
    isButtonUp = false;
    isButtonDown = false;
    isButtonLeft = false;
    isButtonRight = false;

    activeDirection = null;
}

// Setup Listeners (MODIFIED: pass event)
buttons.up.addEventListener('mousedown', (e) => handleStart('up', e));
buttons.down.addEventListener('mousedown', (e) => handleStart('down', e));
buttons.left.addEventListener('mousedown', (e) => handleStart('left', e));
buttons.right.addEventListener('mousedown', (e) => handleStart('right', e));

// Release logic
document.body.addEventListener('mouseup', handleStop);
document.body.addEventListener('mouseleave', handleStop);