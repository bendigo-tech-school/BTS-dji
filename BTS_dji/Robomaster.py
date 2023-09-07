from time import sleep
from robomaster import robot
from robomaster import camera
from robomaster import led
import robomaster
import math


def start():
    global ep_chassis, ep_arm, ep_gripper, ep_led
    ep_robot = robot.Robot()  # create robot instance
    ep_robot.initialize(conn_type='ap')  # access point connection initialization
    # ep_robot.initialize(conn_type='rndis')  # usb connection initialization
    ep_chassis = ep_robot.chassis  # get the chassis module

    ep_camera = ep_robot.camera  # get the camera module
    ep_camera.start_video_stream(display=True)  # start video stream

    ep_led = ep_robot.led  # get the led module
    ep_led.set_led(comp=led.COMP_ALL, r=255, g=0, b=0,
                   effect=led.EFFECT_ON)  # set led to red just to say have conected and started your code

    ep_arm = ep_robot.robotic_arm  # get the robotic arm module
    ep_gripper = ep_robot.gripper  # get the gripper module
    return ep_chassis

def driveWheels(frWheel, flWheel, blWheel, brWheel):
    
    min_limit = -200
    max_limit = 200

    frWheel = max(min(frWheel, max_limit), min_limit)
    flWheel = max(min(flWheel, max_limit), min_limit)
    blWheel = max(min(blWheel, max_limit), min_limit)
    brWheel = max(min(brWheel, max_limit), min_limit)

    ep_chassis.drive_wheels(w1=frWheel, w2=flWheel, w3=blWheel, w4=brWheel, timeout=None)

def arm(x, y):
    ep_arm.move(x=x).wait_for_completed()
    ep_arm.move(y=y).wait_for_completed()


def gripper(time, direction):

    if direction < 0:
        ep_gripper.close(power=50)
    else:
        ep_gripper.open(power=50)

    sleep(time)
    ep_gripper.pause()


def LED(r,g,b):
    ep_led.set_led(comp=led.COMP_ALL, r=r, g=g, b=b, effect=led.EFFECT_ON)

