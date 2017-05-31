from random_table import *
from swapper import *
import matplotlib.pyplot as plt
import seaborn as sns


differences = []
N = 1000
nsteps = 7
for steps in range(1, nsteps+1):
    print steps
    local_diff = []
    for schedule_count in range(N):
        if schedule_count % 200 == 0:
            print schedule_count/200*1/5.*100, "%"
        
        test = random_table()
        init_score = test.score()
        for swap in range(steps):
            test = swap_activity(test)
        diff = test.score() - init_score
        local_diff.append((diff))

    
    differences.append(local_diff)


for i in range(nsteps):
    plt.figure(i)
    plt.hist(differences[i])
    plt.xlabel("Score change")
    plt.ylabel("Frequency")
    plt.title("Differences after " + str(i+1) + " steps")
    plt.show()
            
