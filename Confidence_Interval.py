import numpy as np
import matplotlib.pyplot as plt

num_trials = 10000
obs_time_hr = 1. # Duration of observation in hours

num_obs_list = []
for i in range(num_trials):
    caught_flare = False
    num_obs = 0

    while not caught_flare:
        num_obs += 1
        #creates instantaneous fake flare
        flare_time = 24*np.random.random()

        #creates a random window of "observation"
        start_time = 24*np.random.random()

        #checks if flare happened in the observation window & updates caught_flare
        if 0 < flare_time-start_time <= obs_time_hr:
            caught_flare = True

    num_obs_list.append(num_obs)

#sorts values in ascending order and gets 75th percentile
num_obs_list.sort()
num_obs_list = np.array(num_obs_list)
print("75th percentile of values : ",
       np.percentile(num_obs_list, 75))

plt.hist(num_obs_list, bins=100)
plt.show()
