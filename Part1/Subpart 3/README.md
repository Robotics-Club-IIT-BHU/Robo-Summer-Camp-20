# Subpart 3

Getting to know about robot models, its time to do some serious simulation !!

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
We will go through each line of the code and understand what it does,
1. First we import the required libraries i.e. pybullet, time and pybullet_data
2. **connect**
* After importing the PyBullet module, the first thing to do is 'connecting' to the physics simulation. PyBullet is designed around a client-server driven API, with a client sending commands and a physics server returning the status. PyBullet has some built-in physics servers: DIRECT and GUI. Both GUI and DIRECT connections will execute the physics simulation and rendering in the same process as PyBullet.
* The connect function returns a physics client id.
* The DIRECT connection sends the commands directly to the physics engine, without using any transport layer and no graphics visualization window, and directly returns the status after executing the command.
* The GUI connection will create a new graphical user interface (GUI) with 3D OpenGL rendering, within the same process space as PyBullet.
3. **setAdditionalSearchPath** is used to add pybullet_data to the path which contains many examples, urdf files, etc.
4. **setGravity**:By default, there is no gravitational force enabled. setGravity lets you set the default gravity force for all objects.
The setGravity input parameters are: (no return value):


parameter type  | Name | type | Description
--- | --- | --- | ---
required  | gravityX | float | gravity force along the X world axis
required  | gravityY | float | gravity force along the Y world axis
required  | gravityZ | float | gravity force along the Z world axis
optional  | physicsClientId | int | if you connect to multiple physics servers, you can pick which one.

5. **loadURDF**: The loadURDF will send a command to the physics server to load a physics model from a Universal Robot Description File (URDF).

Some important arguments of loadURDF are:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | fileName | string | a relative or absolute path to the URDF file on the file system of the physics server.
optional  | basePosition | vec3 | create the base of the object at the specified position in world space coordinates [X,Y,Z]. Note that this position is of the URDF link position. If the inertial frame is non-zero, this is different from the center of mass position. Use resetBasePositionAndOrientation to set the center of mass location/orientation.
optional  | baseOrientation | vec4 | create the base of the object at the specified orientation as world space quaternion [X,Y,Z,W]. See note in basePosition.

**For all the arguments of the above function you can refer PyBullet Quickstart Guide**

6. We store the initial position of our urdf file in the variable cubsStartPos.

7. We store the initial Quaternion orientation of our urdf file in cubeStartOrientation
**More details about Quaternions will be given in Part 2 of the camp**

8. We import our r2d2 robot urdf file in the desired position and orientation.

9. **stepSimulation**:stepSimulation will perform all the actions in a single forward dynamics simulation step. The default timestep is 1/240 second, it can be changed using the setTimeStep or setPhysicsEngineParameter API.

10.**getBasePositionAndOrientation**:getBasePositionAndOrientation reports the current position and orientation of the base (or root link) of the body in Cartesian world coordinates. The orientation is a quaternion in [x,y,z,w] format.
The arguments of getBasePositionAndOrientation are:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | objectUniqueId | int | object unique id, as returned from loadURDF.
optional  | physicsClientId | int | if you are connected to multiple servers, you can pick one.

11.**disconnect**: You can disconnect from a physics server. A 'DIRECT' or 'GUI' physics server will shutdown. A separate (out-of-process) physics server will keep on running. See also 'resetSimulation' to remove all items.
