from random_table import *
from swapper import *

schedule = random_table()
# print schedule
for i in range(100):
    schedule = swap_rooms(schedule)
# print schedule

