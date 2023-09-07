# BTS-dji
#### Table of Contents
- [BTS-dji.Robomaster](#BTS-djirobomaster)
- [BTS-dji.Tello](#BTS-djitello)
- [BTS-dji.Controler](#BTS-djicontroler)
- [BTS-dji.Keyboard](#BTS-djikeyboard)

## Description
BTS-dji is a library designed to assist children in programming the DJI Robomasters and DJI Tellos in a simple way. It includes additional features to provide extra help to children, and it was specifically created for the Bendigo Tech School.
## BTS-dji.Robomaster

`BTS-dji.Robomaster` is a Python library for controlling a robot. Below is a list of functions that can be used to interact with the robot:

- `robot.start()`: This function starts the robot and shows the camera feed.

- `robot.driveWheels(fr, fl, bl, br)`: This function controls the speed of each wheel individually, setting it to a value between 200 and -200. The variables are:
  - Wheels
  - fr = front right
  - fl = front left
  - bl = back left
  - br = back right
  Example: `robot.driveWheels(w1=w1, w2=w2, w3=w3, w4=w4)  # drive each wheel at a given speed`


- `sleep(t)`: This function pauses your code for a specific amount of time. The variable is:
  - t = time
  Example: `sleep(10)  # sleep for 10 seconds`


- `robot.gripper(t, d)`: Use this function to open or close the gripper on the robot's arm, with "d" indicating the direction (-1 for close, 1 for open). The variables are:
  - t = time
  - d = direction
  Example: `robot.gripper(0.5, 1)  # time | direction 1 or -1`


- `robot.arm(x, y)`: This function moves the robot's arm relative to its current position. For example, if it's currently at position (20, 20), a movement command of (10, 10) would move it to (30, 30). The variables are:
  - x = forward
  - y = up/down
  Example: `robot.arm(10, 10)  # move arm by 10 x and 10 y`


- `robot.LED(r, g, b)`: Use this function to set the color of the robot's LEDs using RGB values ranging from 0 to 255. The variables are:
  - r = red
  - g = green
  - b = blue
  Example: `robot.LED(255, 255, 255)  # r g b`


Here is an example code snippet that demonstrates how to use the `Robomaster` library to control a robot:

```python
from BTS-dji import Robomaster as robot  # import the Robomaster module from BTS-dji library
from time import sleep  # import the sleep function from the time module

robot.start()  # start the robot

def drive():  # define the drive function

    # set the speed of each wheel to 1000 for one second
    w1 = 1000
    w2 = 1000
    w3 = 1000
    w4 = 1000
    robot.driveWheels(w1=w1, w2=w2, w3=w3, w4=w4)
    sleep(1)  # pause for one second

    # set the speed of all wheels to 0
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    robot.driveWheels(w1=w1, w2=w2, w3=w3, w4=w4)

def gripper():  # define the gripper function

    # open and close the gripper on the robot's arm
    robot.gripper(0.5, 1)
    robot.gripper(0.5, -1)

def arm():  # define the arm function

    # move the robot's arm to two different positions and pause for two seconds in between
    robot.arm(10, 10)
    sleep(2)
    robot.arm(30, 30)

def led():  # define the led function

    # set the color of the robot's LEDs to white for two seconds, then to green
    robot.LED(255, 255, 255)
    sleep(2)
    robot.LED(0, 255, 0)
    
drive()  # calls drive
arm()  # calls arm
gripper()  # calls gripper
led()  # calls led
```
## BTS-dji.Tello

`BTS-dji.Tello` is still in development and not yet available.

## BTS-dji.Controler

`BTS-dji.Controler` is a simple gamepad/joystick input library designed for beginners in Python. To use it, follow these steps:
1. Import the module.
2. Start the script by running `Controler.start()`.
3. To check if a button or joystick is pressed, run `input = Controler.get_state(0)`.
4. The `input` variable is a dictionary that contains the states of all buttons and joysticks. You can access the state of a specific button or joystick by looking it up in the dictionary using its name, for example: `print(input["button_a"])` will return either 0 or 1 depending on whether the 'A' button is currently pressed or not.
```py
from BTS-dji import Controler  # import controler

Controler.start()  # start the controler listener

while True:
    input = Controler.get_state(0)  # get the state of the controler
    print(input["a"])  # print the state of the "a" button
```



## BTS-dji.kbd

`BTS-dji.kbd` is a simple keyboard input library designed for beginners in Python. To use it, follow these steps:
1. Import the module.
2. Start the script by running `kbd.start()`.
3. To check if a key is pressed, run `input = kbd.get_state(0)`.
4. The `input` variable is a dictionary that contains the states of all keys. You can access the state of a specific key by looking it up in the dictionary using its name, for example: `print(input["b"])` will return either 0 or 1 depending on whether the 'b' key is currently pressed or not.

```py
from BTS-dji import kbd  # import kbd

kbd.start()  # start the kbd listener

while True:
    input = kbd.get_state(0)  # get the state of the kbd
    print(input["a"])  # print the state of the "a" key
```
