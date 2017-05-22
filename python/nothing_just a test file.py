import time
import progressbar

bar = progressbar.ProgressBar(max_value=30)
for i in range(30):
    x = 2349823498**.5
    time.sleep(0.1)
    bar.update(i)
