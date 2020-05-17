## Subpart 3
Assesment for this part be like,
<p align="center">
   <img  width="400" height="250" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI7wa5iwd1LxQvKFdWPVBdAT_UhKeotX94SXfUZSCF9smt7Mx3&s">
</p>

On a more serious note,**Control Theory** is one crucial element in robotics and needs quite the time to master. However, as always we will aim to give you a head start with the fundamental definitions.

## What is Robot control ?

_Robotic control is the system that contributes to the movement of robots. Fairly Intuitive huh ?__

_Q.So,is it a mechanical aspect / software aspect of the bot?_

_Ans.Simply the bridge between both !!_

Thus a controller involves the mechanical aspects and program systems that makes possible to control robots. Robotics could be controlled in various ways, which includes using manual control, wireless control, semi-autonomous (which is a mix of fully automatic and wireless control), and fully autonomous (which is when it uses AI to move on its own, but there could be options to make it manually controlled).But controllers can be broadly classified based on their design and irrespective of their field of deployment.

## Types and topologies:
There are surplus material available to learn this in-depth but for the light weight introduction we recommend the 5 part mini-video series from **Matlab**

<div align="center">
  
[Understanding Control Systems](https://in.mathworks.com/videos/series/understanding-control-systems-123420.html)

</div>

**Note:** This series is just for learning the theory, no need to worry about using Matlab as shown in the videos.

## P.I.D

<p align="center">
   <img  width="428" height="118" src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRmRDuAZ93j7fWf02FDvuFXpNAljOY6OZwKdmzuLm2-oerp8L5g&usqp=CAU">
</p>

PID is perhaps the most important,popular and simplistic **feed back controller**,out there.The significance of which could be done justice only by the videos below and *not even us !!*


1. [What is PID?](https://www.youtube.com/watch?v=4Y7zG48uHRo)
2. [Introduction to PID control ?](https://www.youtube.com/watch?v=wkfEZmsQqiA)
3. Wanna C PID,..here it's in action..
    1. [Single motor target tracking](https://www.youtube.com/watch?v=fusr9eTceEo).
    2. [Self-balancing PID-ball tracker](https://www.youtube.com/watch?v=57DbEEBF7sE)

## Task for the part
Hope,you have gone through the above content about **PID** well, as far as this task goes, in a nutshell we implement a _PD controller_.So,most of you might have a intutive understanding about PID for now.

Hence, the essential components will be
1. **A target point**- such that the error is 0 when setpoint == targetpoint
2. **A Sensor**- to find the current _setpoint_.
3.**Actuators/Motors:** - to actually apply a action and try decrease the error.

Thus,in this task we will try implementing a PD controller to control the turning motion of the car about a constrained axis so as to fix a target box in the centre of the camera frame.It could be better understood from the illustrations below.
<p align="center">
   <img  width="800" height="450" src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part3/Subpart3/pid_demo.gif">
  
   
</p>

Thus,in our case.
1. **A target point**- is to align the camera frame centre with that of the centre of the box(ie the contour you will be detecting)
2. **A Sensor**- is the camera,which gives you the current set point ie how much deviated from the current alignment.
3. **Actuators/Motors:** - is the motors of the car,that makes the car align.

Hence the error can be easily calculated as,

<div align = "center">
   error = current x co-ordinate of target contour detected - center x cordinate of the camera frame 
</div>

**Key Points to note:**
1. We have constrained the car to only rotoate about the **z-axis**,thus no translation motion will happen.Only **clockwise and anticlockwise motion rotation** is allowed dependeing on the relative rotation of *left and right set of wheels*.

2. We recomend using **openCV** for contour detection and **cv2.moments** method to find the x cordinate of the contour.
For the ones **who are not familiar with openCV can contact use for the boilerplate code as th main motive here is to build the controller**.

3. The starter code [pid_control_starter.py](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part3/Subpart3/pid_control_starter.py), has the necessary structure for the code,with the following user inputs alredy implemented,
   1. **right arrow**- anti clockwise rotation about z axis,essentially to give a initial disturbance and switch on PID to correct the alignment.
   2. **left arrow** - clockwise rotation about z axis,,essentially to give a initial disturbance and switch on PID to correct the alignment.
   3. **c key**      - to start PID control
   4. **r key**      - to stop PID control and go back to manual control to cause a error.
4.Thus,you are expected 
   1. to get a image frame like in *subpart-1, of Part 3*
   2. detect the contour, find moments.
   3. calculate the error and use PID to align your car back from the **initial user created disturbance** when _the key c_ is pressed.

5.Its worthy to highlight that for the given task, a **PD controller** is enough.Meaning we wont need any _integral term_ as ther is no error that is getting accumulated in our case. So,it enough if you PD update has only P and D terms.

