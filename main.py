import numpy as np

# assume we get real-time data on sensor info: assume we get 
buffer = 0.1   # to allow for error/stopping before we actually hit something

collisionThreshold = 0.5 + buffer # chair has a 0.5m braking distance
sensorHeight = .7  # MAKE SURE YOU CHANGE THIS LATER
sensorAngle = np.deg2rad(60)    # ALSO CHANGE THIS
rampAngle = np.deg2rad(7.5) 
slowThreshold = sensorHeight/(np.cos(sensorAngle)) + buffer # slow down if we may be approaching a ramp

mathvalue = (sensorHeight*np.tan(sensorAngle) - collisionThreshold)*np.sin(rampAngle) # see diagram
stopThreshold = slowThreshold + mathvalue/np.cos(rampAngle + sensorAngle) + buffer # stop if not a ramp

# output 3 ints: 0 (T), 1 (F), 2 (S)
def detection(left, right, front, threshold, slow_stop, original_values): 
    l_out, r_out, f_out = original_values
    if left >= threshold: l_out = slow_stop
    if right >= threshold: r_out = slow_stop 
    if front >= threshold: f_out = slow_stop
    return (l_out, r_out,  f_out) 
   
def collisionDetection(left_forw, right_forw, front_forw): # assume these are distances 
    l_out, r_out, f_out = 0,0,0
    if left_forw <= collisionThreshold: l_out = 1
    if right_forw <= collisionThreshold: r_out = 1
    if front_forw <= collisionThreshold: f_out = 1
    return (l_out, r_out,  f_out) 
#    return detection(left_forw, right_forw, front_forw, collisionThreshold, 1, (0,0,0))


def stairDetection(left_tilt, right_tilt, front_tilt): 
    slow_vals = detection(left_tilt, right_tilt, front_tilt, slowThreshold, 2, (0,0,0))
    print(slow_vals)
    return detection(left_tilt, right_tilt, front_tilt, stopThreshold, 1, slow_vals)

if __name__ == "__main__":
    l, r, f, l_t, r_t, f_t = .5, .5, .5, 2, 2, 2
    print(collisionDetection(l, r, f))
    print(stairDetection(l_t, r_t, f_t))
    
    