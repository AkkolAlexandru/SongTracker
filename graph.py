import numpy as np
import matplotlib.pyplot
import json
import math
import pylab


def plot():

    def most_frequent(list):
        return max(set(list), key=list.count)

    data = open("output.json", "r")
    dt = json.load(data)

    # initializing values and keys in variables
    base = dt.values()
    base = list(base)
    frequency = [combo[0] for combo in base]
    print("frequencies: ", frequency)
    genrelist = [combo[1] for combo in base]
    main_genre = most_frequent(genrelist)

    # adjusting Y axis to only display integers
    new_Y = range(math.floor(min(frequency)), math.ceil(max(frequency))+1)
    keys = dt.keys()

    # processing data for graph building
    y_val = np.arange(len(keys))

    # build graph
    with matplotlib.pyplot.style.context('fivethirtyeight'):
        matplotlib.pyplot.figure(figsize=(14, 14))
        fig = pylab.gcf()
        fig.canvas.manager.set_window_title('Song Frequency')
        matplotlib.pyplot.bar(y_val, frequency, align = "center")
        matplotlib.pyplot.xticks(y_val, keys)
        matplotlib.pyplot.ylabel('frequency')
        matplotlib.pyplot.yticks(new_Y)
        matplotlib.pyplot.title('Recognized songs', fontsize=15)
        matplotlib.pyplot.xticks(rotation=90)
        matplotlib.pyplot.subplots_adjust (bottom = 0.5)
        matplotlib.pyplot.gcf().text(0.005, 0.97, "Number of songs: " + str(sum(frequency)), fontsize=12)
        matplotlib.pyplot.gcf().text(0.005, 0.94, "Most common genre: " + main_genre, fontsize=12)
        matplotlib.pyplot.show()
    data.close()