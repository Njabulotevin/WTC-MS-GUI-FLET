from flet import *
from Modules import Modules

primary_color: str = "#3C3C3C"
secondary_color = "#D7D7D7"
blue = "#095FB0"
background_color = "#323232"


class Topics():
    topics = {}
    show_topics = {}
    for i in Modules.modules:
            topics[i[0]] = [f"topic 1: {i[0]}",
                            f"topic 2 : {i[0]}", f"topic 3 : {i[0]}", f"topic 4 : {i[0]}", f"topic 5 : {i[0]}"]
    for module in topics:
            show_topics[module] = [
                Container(Row([Icon(name="chevron_right", color=secondary_color), Text(i, color=secondary_color)]), bgcolor=primary_color, padding=padding.all(10), border_radius=5) for i in topics[module]]
        