# cooling schemes

import matplotlib.pyplot as plt

def cool(scheme, T0, time):
    """ general cooling function called by other modules """
    T = 0
    if scheme == "lin":
        T = cool_linear(T0, time)
    elif scheme == "exp":
        T = cool_exponential(T0, time)

    ### more schemes

    else:
        return None

    
    if T >=0:
        return T
    else:
        return 0

def cool_linear(T0, time):
    """ a linear cooling scheme """
    # modeled after http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/
    alpha = .9
    return T0 - alpha*time
    
    

def cool_exponential(T0, time):
    """ an exponential cooling scheme """
    # modeled after http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/
    alpha = .99
    return T0*alpha**(float(time))


    
##t = []
##T = []
##T0 = 300
##for time in range(1000):
##    t.append(time)
##    T.append(cool("lin", T0, time))
##
##plt.plot(t, T)
##plt.show()
