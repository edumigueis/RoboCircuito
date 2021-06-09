#codigo por
#Eduardo Migueis
#Illy Bordini
#Guilherme Lima

from controller import Robot, Motor, DistanceSensor, Camera
import requests
from PIL import Image

# cria a instancia do robo
robot = Robot()

time_step = 64
max_speed = 6.28


# motor

# rodas da frente
right_motor_front = robot.getDevice('wheel_rf')
right_motor_front.setPosition(float('inf'))
right_motor_front.setVelocity(0.0)

left_motor_front = robot.getDevice('wheel_lf')
left_motor_front.setPosition(float('inf'))
left_motor_front.setVelocity(0.0)

# rodas de traz
right_motor_back = robot.getDevice('wheel_rb')
right_motor_back.setPosition(float('inf'))
right_motor_back.setVelocity(0.0)

left_motor_back = robot.getDevice('wheel_lb')
left_motor_back.setPosition(float('inf'))
left_motor_back.setVelocity(0.0)


# sensor de IR
right_ir = robot.getDevice('RIGHT')
right_ir.enable(time_step)
mid_ir = robot.getDevice('MID')
mid_ir.enable(time_step)
left_ir = robot.getDevice('LEFT')
left_ir.enable(time_step)


camera = robot.getDevice("camera")
camera.enable(time_step)

def sendImg():
    img = camera.getImage()
    camera.saveImage("photo.png", 720)
    #rawImg = Image.frombytes('RGBA', (camera.getWidth(), camera.getHeight()), img)
    #image = Image.open("photo.jpg")
    #print(rawImg)
    msg = str(img)
    myObj = {'img': msg}
    requests.post('http://localhost:5000/api/img', json = myObj)
    return

# Main loop:
# - efetua os passos da simulacao ate que o Webots pare o controller
while robot.step(time_step) != -1:
    sendImg()
    # le-se os sensores:
    right_ir_val = right_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    left_ir_val = left_ir.getValue()

    left_speed_f = max_speed # _f for front
    right_speed_f = max_speed # _f for front
    left_speed_b = max_speed # _b for back
    right_speed_b = max_speed # _b for back

    # Processamento dos dados do sensor.
    if left_ir_val < 300 and right_ir_val < 300 and mid_ir_val >= 300:
        left_motor_front.setVelocity(left_speed_f)
        right_motor_front.setVelocity(right_speed_f)
        left_motor_back.setVelocity(left_speed_b)
        right_motor_back.setVelocity(right_speed_b)

    if left_ir_val < 300 and right_ir_val >= 300 and mid_ir_val >= 300:
        left_motor_front.setVelocity(left_speed_f)
        right_motor_front.setVelocity(0)
        left_motor_back.setVelocity(left_speed_b)
        right_motor_back.setVelocity(0)

    if left_ir_val >= 300 and right_ir_val < 300 and mid_ir_val >= 300:
        left_motor_front.setVelocity(0)
        right_motor_front.setVelocity(right_speed_f)
        left_motor_back.setVelocity(0)
        right_motor_back.setVelocity(right_speed_b)

    if left_ir_val >= 300 and right_ir_val < 300 and mid_ir_val < 300:
        left_motor_front.setVelocity(0)
        right_motor_front.setVelocity(right_speed_f)
        left_motor_back.setVelocity(0)
        right_motor_back.setVelocity(right_speed_b)

    if left_ir_val < 300 and right_ir_val >= 300 and mid_ir_val < 300:
        left_motor_front.setVelocity(left_speed_f)
        right_motor_front.setVelocity(0)
        left_motor_back.setVelocity(left_speed_b)
        right_motor_back.setVelocity(0)

    if left_ir_val < 300 and right_ir_val < 300 and mid_ir_val < 300:
        left_motor_front.setVelocity(left_speed_f)
        right_motor_front.setVelocity(right_speed_f)
        left_motor_back.setVelocity(left_speed_b)
        right_motor_back.setVelocity(right_speed_b)

        pass
