from random_table import *
from hill_climber import *


schedule = random_table()
#schedule.plot()
#schedule.personal("59289233", True)


schedule = hill_climber_activities(schedule, 100)

schedule.plot()
