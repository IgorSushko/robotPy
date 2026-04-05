import sys
from os.path import abspath, dirname

# Add parent directory to path so it can find 'hardware'
sys.path.insert(0, dirname(abspath(__file__)) + '/..') 

from flask import Flask, render_template, jsonify
from hardware.robot import init_robot, stop, forward, backward, left, right

app = Flask(__name__)

# Initialize GPIO on start
init_robot()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/control/stop', methods=['POST'])
def control_stop():
    stop()
    return '', 204


@app.route('/control/move/<direction>', methods=['POST'])
def control_move(direction):
    if direction == 'left':
        left()
    elif direction == 'right':
        right()
    elif direction == 'up':
        forward()
    elif direction == 'down':
        backward()
    return '', 204


@app.route('/wifi/signal', methods=['GET'])
def get_wifi_signal():
    """Get WiFi signal strength percentage (0-100)"""
    import subprocess
    import re

    try:
        result = subprocess.run(
            ['iwconfig', 'wlan0'],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            text = result.stdout

            # ✅ Case 1: RSSI in dBm (your case)
            match_dbm = re.search(r'Signal level[=|:]\s*(-?\d+)\s*dBm', text)
            if match_dbm:
                rssi = int(match_dbm.group(1))
                signal_percentage = max(0, min(100, int((rssi + 100) * 2)))

                return jsonify({
                    'signal_percentage': signal_percentage,
                    'rssi': rssi,
                    'unit': 'dBm'
                })

            # ✅ Case 2: Link Quality (fallback)
            match_quality = re.search(r'Link Quality[=|:]\s*(\d+)/(\d+)', text)
            if match_quality:
                current = int(match_quality.group(1))
                max_val = int(match_quality.group(2))
                signal_percentage = int((current / max_val) * 100)

                return jsonify({
                    'signal_percentage': signal_percentage,
                    'unit': 'quality'
                })

        # ❌ Parsing failed
        return jsonify({
            'signal_percentage': 0,
            'rssi': -120,
            'error': 'Unable to parse iwconfig output'
        }), 503

    except subprocess.TimeoutExpired:
        return jsonify({
            'signal_percentage': 0,
            'error': 'iwconfig command timed out'
        }), 503

    except FileNotFoundError:
        # 🔄 Fallback: nmcli
        try:
            result = subprocess.run(
                ['nmcli', '-t', '-f', 'IN-USE,SIGNAL', 'dev', 'wifi'],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if line.startswith('*'):
                        signal = int(line.split(':')[1])
                        return jsonify({
                            'signal_percentage': signal,
                            'unit': 'percentage'
                        })

        except Exception:
            pass

    # 🔄 Final fallback (dev mode)
    return jsonify({
        'signal_percentage': 50,
        'rssi': -70,
        'simulated': True,
        'note': 'Fallback value'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)