from random_table import *
from hill_climber import *


schedule = random_table()
schedule.plot()
#schedule.plot_course("Programmeren in Java 2")


schedule = hill_climber_activities(schedule, 30)

schedule.plot()
