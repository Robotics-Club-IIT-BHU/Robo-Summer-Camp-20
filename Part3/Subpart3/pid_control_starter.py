
import pybullet as p
import pybullet_data
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
p.connect(p.GUI)  
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)

huskypos = [0, 0, 0.1]
target_block=p.loadURDF("block0.urdf",-3,0,0)

husky = p.loadURDF("husky/husky.urdf", huskypos[0], huskypos[1], huskypos[2])
p.createConstraint(husky, -1, -1, -1, p.JOINT_POINT2POINT, [0, 1, 0], [0, 0,0 ], [0, 0,0])


maxForce = 200 #Newton.m
#camera should be facing in the direction of the car


def turn(speed):
    baseSpeed = 100
    targetVel_R = baseSpeed + speed
    targetVel_L = baseSpeed - speed
    for joint in range(1,3):
        p.setJointMotorControl2(husky,2* joint, p.VELOCITY_CONTROL, targetVelocity =targetVel_R,force = maxForce)
    for joint in range(1,3):
        p.setJointMotorControl2(husky,2* joint+1, p.VELOCITY_CONTROL,targetVelocity =targetVel_L,force = maxForce)
    p.stepSimulation()
'''
tune the kp and kd from experiments, 
a hint set kd = 10*kp
'''
Kp=0
Kd=0
last_error=0
PID_CONTROL=False


    
while (1):
    keys = p.getKeyboardEvents()
    if (PID_CONTROL):
    	# 1. Get the image feed, as in subpart-1.
    	hsv_lower=np.array([80,0,75])
    	hsv_upper=np.array([150,255,255])
    	# 2. using the above limits, mask the green colour 
      	#    and draw the area with maximuma contour and find 
      	#    its moments.
      	# 3. Calculate the error, and apply pid control to find the
      	#    optimal speed correction and call the turn function with
      	#    that speed.

      	# apply pid law to calulate this value,use Kp and Kd variable above
      	# and tune em properly.
    	speed_correction = 0 
    	error = 0 #find error
    	turn(speed_correction)
    	last_error=0 #initialize accordingly
        
    for k, v in keys.items():

            if (k == p.B3G_RIGHT_ARROW and (v & p.KEY_IS_DOWN) and PID_CONTROL==False):
                targetVel = 2
                for joint in range(1,3):
                    p.setJointMotorControl2(husky,2*joint, p.VELOCITY_CONTROL, targetVelocity =targetVel,force = maxForce)
                for joint in range(1,3):
                    p.setJointMotorControl2(husky,2*joint+1, p.VELOCITY_CONTROL,targetVelocity =-1*targetVel,force = maxForce)

                p.stepSimulation()
            if (k == p.B3G_RIGHT_ARROW and (v & p.KEY_WAS_RELEASED)):
                targetVel = 0
                for joint in range(2, 6):
                    p.setJointMotorControl2(husky, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel,force = maxForce)
                
            if (k == p.B3G_LEFT_ARROW and (v & p.KEY_IS_DOWN)and PID_CONTROL==False):
                targetVel = 2
                for joint in range(1,3):
                    p.setJointMotorControl2(husky,2* joint+1, p.VELOCITY_CONTROL,targetVelocity = targetVel,force = maxForce)
                for joint in range(1,3):
                    p.setJointMotorControl2(husky,2* joint, p.VELOCITY_CONTROL,targetVelocity =-1* targetVel,force = maxForce)

                p.stepSimulation()
            if (k == p.B3G_LEFT_ARROW and (v & p.KEY_WAS_RELEASED)):
                targetVel = 0
                for joint in range(2, 6):
                    p.setJointMotorControl2(husky, joint, p.VELOCITY_CONTROL, targetVelocity =targetVel,force = maxForce)

                p.stepSimulation()
            if (k == ord('c') and (v & p.KEY_WAS_TRIGGERED)):
                print("\nPID Control-on")
                PID_CONTROL = True
            if (k == ord('r') and (v & p.KEY_WAS_TRIGGERED)):
                print("\nPID Control-off ,back to manual")
                PID_CONTROL = False
p.disconnect()
