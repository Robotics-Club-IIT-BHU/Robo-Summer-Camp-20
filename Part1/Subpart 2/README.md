# Subpart 2

Given that pybullet is running, its time to define or rather redefine what a robot is !!!
<p align="center">
   <img width="400" height="300" src="https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%202/redefine.gif">
</p>

## Universal Robot Structure
<p align="center">
   <img width="444" height="500" src="https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%202/robo.png">
</p>


Any robot is constructed by a combination of rigid bodies and joints.These rigid bodies are called Links.These links are inter related by means of different types of joints.

**Base:**
As the name suggests , this is the primary link of the bot to which all the other links are joined.(Link 1 in the picture)

**Parent and Child links:**
          A link is named as a parent link with respect to a joint.For instance  wrt the joint 2 ,Link 1 is the parent and Link 3 is a child.

**Joints:**
	Any form of motion causing inter linkages are called as Joints.Joints are broadly classified into 3 types.
1. Revolute
2. Prismatic
3. Universal

**Note:** In simulations we don't consider the electronic systems required for the control of the robots rather we program joint level controllers (will be explained in future parts)
