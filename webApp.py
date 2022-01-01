import plotly.graph_objects as go
import json


def run_webapp():
    def most_frequent(list):
        return max(set(list), key=list.count)

    data = open("output.json", "r")
    dt = json.load(data)

    # initializing values and keys in variables
    base = dt.values()
    base = list(base)
    freq_list = [combo[0] for combo in base]
    frequency = sum(freq_list)
    genrelist = [combo[1] for combo in base]
    main_genre = most_frequent(genrelist)

    y = list(dt.values())
    x = list(dt.keys())
    y = [item[0] for item in y]

    fig = go.Figure(
        data=[go.Bar(x=x,y=y)],
        layout_title_text="Recognized songs"
    )
    fig.update_layout(
        xaxis = go.layout.XAxis(
            tickangle = 90
        ),
        title_text = f"Number of songs played: {frequency}                                "
                     f""
                     f"             Most played genre: {main_genre}"
    )

    fig.show()
