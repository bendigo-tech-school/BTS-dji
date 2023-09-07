from BTS_dji import Robomaster as robot
from time import sleep

robot.start()


def drive():  # drive function

    w1 = 1000
    w2 = 1000
    w3 = 1000
    w4 = 1000
    robot.driveWheels(w1=w1, w2=w2, w3=w3, w4=w4)

    sleep(1)

    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    robot.driveWheels(w1=w1, w2=w2, w3=w3, w4=w4)


def gripper():  # gripper function

    robot.gripper(0.5, 1)
    robot.gripper(0.5, -1)


def arm():  # arm function
    robot.arm(10, 10)
    sleep(2)
    robot.arm(30, 30)
    sleep(2)
    robot.arm(60, 60)
    sleep(2)
    robot.arm(-30, -30)
    robot.arm(-30, -30)
    robot.arm(-30, -30)


def led():  # led function
    robot.LED(255, 255, 255)
    sleep(2)
    robot.LED(0, 255, 0)
