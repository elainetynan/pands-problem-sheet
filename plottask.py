# plottask.py
#
# Displays a plot of the functions f(x)=x, g(x)=x squared and 
# h(x)=x cubed in the range [0, 4] on the one set of axes.
#
# Author: Elaine Tynan

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

min = 0
max = 5 # I put in 5 in because the numpy randint does not include the max value

fOfX = np.array(range(min,max))
gOfX = fOfX * fOfX
hOfX = fOfX * fOfX * fOfX

plt.plot(fOfX, gOfX, label="X squared", color="red")
plt.plot(fOfX, hOfX, label="X cubed", color="green")

# Found how to rotate the label for the axes on Stak overflow:
# https://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib
plt.minorticks_on()
plt.ylabel("f(x)", rotation="0")
plt.xlabel("g(x) and h(x)")

# Found how to format the Title on this web site:
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html
titleFont = {'family': 'sans-serif',
        'color':  'blue',
        'weight': 'bold',
        'size': 16,
        }
plt.title("Week 8 - Weekly Task", fontdict=titleFont)
plt.legend()

plt.show()
#plt.savefig("Week08Task.png")