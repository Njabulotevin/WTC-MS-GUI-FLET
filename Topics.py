from flet import *
from Modules import Modules
from utils.format_data import Data, TopicFiles
from Status import Status

primary_color: str = "#3C3C3C"
secondary_color = "#D7D7D7"
blue = "#095FB0"
background_color = "#323232"


class Topics:
    topics = {}
    show_topics = {}
    status = Status()
    for i in Modules.modules:
        topics[i[0]] = Data.get_topics(target=i[0].replace(" ", "_"))

    for module in topics:
        show_topics[module] = [
            Container(
                Row(
                    [
                        Icon(name="chevron_right", color=secondary_color),
                        Text(i[0], color=secondary_color),
                        Container(Text(str(i[1]), size=12), bgcolor=Status.get_icon_color(i[1]), padding=padding.all(5), border_radius=border_radius.all(10))
                    ]
                ),
                bgcolor=primary_color,
                padding=padding.all(10),
                border_radius=5,
            )
            for i in topics[module]
        ]
