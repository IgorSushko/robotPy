#!/bin/bash

echo "=== Checking Python 3.11 ==="

if ! command -v /usr/bin/python3.11 &> /dev/null
then
    echo "Python 3.11 not found. Installing..."
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv python3-gpiozero python3-rpi.gpio
else
    echo "Python 3.11 found."
fi

echo "=== Creating hardware virtual environment ==="

ENV_NAME="venv_hw311"

if [ -d "$ENV_NAME" ]; then
    echo "Environment already exists."
else
    /usr/bin/python3.11 -m venv $ENV_NAME --system-site-packages
    echo "Environment created."
fi

echo "=== Activating environment ==="
source $ENV_NAME/bin/activate

echo "=== Python version inside venv ==="
python --version

echo "=== Checking GPIO import ==="
python -c "import RPi.GPIO; print('RPi.GPIO OK')"

echo ""
echo "Hardware environment ready!"
echo "To activate later use:"
echo "source $ENV_NAME/bin/activate"