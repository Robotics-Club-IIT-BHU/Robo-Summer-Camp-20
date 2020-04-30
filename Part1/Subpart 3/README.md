# Subpart 3
In this subpart we will see a basic code in PyBullet and understand the functions used in it.
```python
import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
```
We will go through each line of the code and understand what it does
1. First we import the required libraries i.e. pybullet, time and pybullet_data
2. **connect**
* After importing the PyBullet module, the first thing to do is 'connecting' to the physics simulation. PyBullet is designed around a client-server driven API, with a client sending commands and a physics server returning the status. PyBullet has some built-in physics servers: DIRECT and GUI. Both GUI and DIRECT connections will execute the physics simulation and rendering in the same process as PyBullet.
* The connect function returns a physics client id.
* The DIRECT connection sends the commands directly to the physics engine, without using any transport layer and no graphics visualization window, and directly returns the status after executing the command.
* The GUI connection will create a new graphical user interface (GUI) with 3D OpenGL rendering, within the same process space as PyBullet.
3. **setAdditionalSearchPath** is used to add pybullet_data to the path which contains many examples, urdf files, etc.
4. **setGravity**:By default, there is no gravitational force enabled. setGravity lets you set the default gravity force for all objects.
| Parameter type | Name              | type  | Description                                                             |
| -------------- |:-----------------:| -----:| ----------------------------------------------------------------------- |
| required       | gravityX          | float | gravity force along the X world axis                                    | 
| required       | gravityY          | float | gravity force along the Y world axis                                    |
| required       | gravityZ          | float | gravity force along the Z world axis                                    | 
| optional       | physicsClientId   | float | if you connect to multiple physics servers, you can pick which one.     |




