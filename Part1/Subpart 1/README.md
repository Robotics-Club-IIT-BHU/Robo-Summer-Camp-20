# What is  Simulation?
Simulation software is based on the process of modeling a real phenomenon with a set of **mathematical formulas**. It is, essentially, a program that allows the user to observe an operation through simulation without actually performing that operation.Thus, it proves to be a very close proxy to the real-world i.e. a mathematical model of the real world processes. The simulation plays a very important role in robotics. Different tools are used for the analysis of kinematics(does not include the cause of motion), dynamics(includes the cause of motion) of robotic manipulators, for off-line programming, to design different control algorithms, to design mechanical structure of robots, to design robotic cells and production lines, etc.

# Simulation Vs Emulation:
Two of the terms that are often misused are simulation and emulation.
**Simulation** is when you are replicating, by the means of software, the general behavior of a system starting from a conceptual model.
Eg :- Softwares used by Space agencies to model the unknown planet conditions.
**Emulation** is when you are replicating, in a different system, how the original system internally works considering each function and their relations.
Eg:-Android emulators for windows like Bluestacks, Andy, etc
Thus, we as robotic technicians need a mathematical model of the world/environments and the physics that govern them, for us experimenting out our robots. Hence, simulation is what we do.

# Why use simulations?
..* Simulations are the best place to start when developing a new robot. By using a simulator to develop your robot, you can quickly identify if your idea is feasible or not with almost no expense. Additionally, you can easily test and discover which are the physical constraints that your robot must face to accomplish its goal.
..* Simulators allow the easy and quick test of many different ideas for the same robotic problem, test them, and then decide which one to build based on actual data.
..* Since your robot has been defined and tested in the simulator, you can start its physical construction. The good thing with simulators is that they allow you to keep doing tests even if your robot is not built yet.
..* Bugs found in your robot software can be debugged first in the simulator.
..* By debugging in the simulator you will save a lot of time since testing on the real robot is very time-consuming.
..* Given that simulation is the way to go, there are plenty of options available for robotics  namely Bullet, Gazebo, V-Rep, Webots, Open Dynamics Engine, MujoCo, etc
