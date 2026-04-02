import sys
from os.path import abspath, dirname

# Add parent directory to path so it can find 'hardware'
sys.path.insert(0, dirname(abspath(__file__)) + '/..') 

from flask import Flask, render_template, request
from hardware.robot import init_robot, stop, forward, backward, left, right

app = Flask(__name__)

# Initialize GPIO on start (Warning: Only run once per restart)
init_robot() 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control/stop', methods=['POST'])
def control_stop():
    stop()
    return '', 204 # No content, OK

@app.route('/control/move/<direction>', methods=['POST'])
def control_move(direction):
    global current_movement_state # Simple state tracker for continuous movement simulation
    
    if direction == 'left': left()
    elif direction == 'right': right()
    elif direction == 'up': forward()
    elif direction == 'down': backward()
    
    return '', 204

if __name__ == '__main__':
    # Run with threading=True to handle multiple HTTP requests simultaneously
    app.run(host='0.0.0.0', port=5000, threaded=True)
