# cooling schemes

import matplotlib.pyplot as plt
import math

# define Tmin/Tn to avoid overflow errors. 
Tn = .1
Tmin = Tn
def cool(scheme, T0, Tn, N, time):
    """ general cooling function called by other modules """
    T = 0
    if scheme == "linN":
        T = cool_linearN(T0, Tn, N, time)
    elif scheme == "lin":
        T = cool_linear(T0, time)
    elif scheme == "expN":
        T = cool_exponentialN(T0, Tn, N, time)
    elif scheme == "exp":
        T = cool_exponential(T0, time)
    elif scheme == "log":
        T = cool_logarithm(T0, time)
    elif scheme == "log_mult":
        T = cool_logarithmic(T0, time)

    ### more schemes

    else:
        return None

    if T > Tmin:
        return T
    # minimum temperature to avoid overflow error. 
    elif T < Tmin:
        return Tmin

    
def cool_linear(T0, time):
    """ a linear cooling scheme; Linear multiplicative cooling """
    alpha = .5
    return T0/(1. + alpha*time)
def cool_linearN(T0, Tn, N, time):
    """ a linear cooling scheme with end T; Linear additive cooling"""
    # modeled after http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/
    return Tn + (T0 - Tn)*(N - time)/float(N)
    
def cool_exponential(T0, time):
    """ an exponential cooling scheme; Exponential multiplicative cooling """
    alpha = .8
    return T0*alpha**time
def cool_exponentialN(T0, Tn, N, time):
    """ an exponential cooling scheme with end T; Exponential additive cooling  """
    # modeled after http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/
    factor = 1+ math.exp(2*math.log(T0 - Tn)*(time-.5*N)/N)
    return Tn + (T0 + Tn)/(factor)

def cool_logarithm(T0, time):
    # modeled after http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/
    return T0/(1 + math.log(1 + time))
def cool_logarithmic(T0, time):
    """ a logarithmic cooling scheme;  Logarithmical multiplicative cooling"""
    alpha = 1.5
    return T0/(1. + alpha*math.log(1. + time))


# test code.   
##t = []
##T = []
##T0 = 10
##for time in range(20000):
##    t.append(time)
##    T.append(cool("log", T0, 3, 3, time))
##
##plt.plot(t, T)
##plt.show()
