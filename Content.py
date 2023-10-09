from flet import *

class Content():
    def __init__(self, show_topics) -> None:
        self.breadcrumb = Text(spans=[TextSpan("Modules"),
                      TextSpan(" > Fundamentals")], size=12)
        self.content = Container(
        Column([self.breadcrumb, Column(show_topics["Fundamentals"])]), expand=1,  padding=20)