import gpiozero
# IN1 -> GPIO20, IN2 -> GPIO16
# IN3 -> GPIO19, IN4 -> GPIO26
from gpiozero import Robot, Motor

robot = None

def init_robot():
    global robot
    # Ensure GND is connected to pin 39 (Pinout may vary slightly by board revision)
    robot = Robot(
        left=Motor(20, 16),
        right=Motor(19, 26)
    )

def stop():
    if robot:
        robot.stop()

def forward():
    if robot: robot.forward()

def backward():
    if robot: robot.backward()

def left():
    if robot: robot.left()

def right():
    if robot: robot.right()
