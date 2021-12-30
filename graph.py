import numpy as np
import matplotlib.pyplot
import json

def plot():
    data = open("output.json", "r")
    dt = json.load(data)

    # initializing values and keys in variables
    values = dt.values()
    values = list(values)

    keys = dt.keys()
    keys = list(keys)

    # processing data for graph building
    y_val = np.arange(len(keys))
    fig = matplotlib.pyplot.figure(figsize = (35,18))

    # make graph full-screen
    wm = matplotlib.pyplot.get_current_fig_manager()
    wm.window.state('zoomed')

    # fig.canvas.manager.full_screen_toggle()

    matplotlib.pyplot.bar(y_val, values, align = "center")
    matplotlib.pyplot.xticks(y_val, keys)
    matplotlib.pyplot.ylabel('values')
    matplotlib.pyplot.title('Christmas songs')
    matplotlib.pyplot.xticks(rotation=90)
    matplotlib.pyplot.subplots_adjust (bottom = 0.5)
    matplotlib.pyplot.text(0.1, 16, "Total number of songs: "+str(sum(values)))
    matplotlib.pyplot.show()
    data.close()