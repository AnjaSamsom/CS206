import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim


# This creates an object, physicsClient, which handles the physics, 
# and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("robot.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

for i in range(2000):
    time.sleep(1/60)
    p.stepSimulation()
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(frontLegTouch)
p.disconnect()