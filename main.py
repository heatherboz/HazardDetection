import numpy as np

# assume we get real-time data on sensor info
buffer = 0.1        # to allow for error/stopping before we actually hit something

stopDist = 0.5
detectDist = stopDist + buffer
sensorHeight = 0  # MAKE SURE YOU CHANGE THIS LATER
sensorAngle = 0    # ALSO CHANGE THIS
stairThreshold = 0  # ALSO CHANGE THIS

slowThreshold = sensorHeight/(np.cos(sensorAngle)) + buffer


# output 3 ints: 0 (T), 1 (F), 2 (S)
def collisionDetection(left, right, front):




