# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor, Camera

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

time_step = 32
max_speed = 6.28


#motor
#front wheels
left_motor_front = robot.getDevice('wheel_lf')
left_motor_front.setPosition(float('inf'))
left_motor_front.setVelocity(0.0)


right_motor_front = robot.getDevice('wheel_rf')
right_motor_front.setPosition(float('inf'))
right_motor_front.setVelocity(0.0)

#back wheels
left_motor_back = robot.getDevice('wheel_lb')
left_motor_back.setPosition(float('inf'))
left_motor_back.setVelocity(0.0)


right_motor_back= robot.getDevice('wheel_rb')
right_motor_back.setPosition(float('inf'))
right_motor_back.setVelocity(0.0)


#Ir sensor
right_ir = robot.getDevice('RIGHT')
right_ir.enable(time_step)
mid_ir = robot.getDevice('MID')
mid_ir.enable(time_step)
left_ir = robot.getDevice('LEFT')
left_ir.enable(time_step)


cv = robot.getDevice("camera")
cv.enable(timestep)
img = cv.getImage()
print(img)
  
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
   right_ir_val = right_ir.getValue()
   mid_ir_val = mid_ir.getValue()
   left_ir_val = left_ir.getValue()

   print("left: {} mid: {} right: {}" .format(left_ir_val,mid_ir_val,right_ir_val))

   left_speed_f =  max_speed   
   right_speed_f =  max_speed     
   left_speed_b =  max_speed   
   right_speed_b =  max_speed
   
  

    # Process sensor data here.
   if left_ir_val<300 and right_ir_val<300 and mid_ir_val>=300:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(right_speed_b)
    
   if left_ir_val<300 and right_ir_val>=300 and mid_ir_val>=300:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(0)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(0)
    
   if left_ir_val>=300 and right_ir_val<300 and mid_ir_val>=300:
    left_motor_front.setVelocity(0)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(0)
    right_motor_back.setVelocity(right_speed_b)
    
   if left_ir_val>=300 and right_ir_val<300 and mid_ir_val<300:
    left_motor_front.setVelocity(0)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(0)
    right_motor_back.setVelocity(right_speed_b)
    
   if left_ir_val<300 and right_ir_val>=300 and mid_ir_val<300:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(0)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(0)
    
   if left_ir_val<300 and right_ir_val<300 and mid_ir_val<300:
    left_motor_front.setVelocity(left_speed_f)
    right_motor_front.setVelocity(right_speed_f)
    left_motor_back.setVelocity(left_speed_b)
    right_motor_back.setVelocity(right_speed_b)


    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.