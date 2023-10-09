from flet import *
from utils.format_data import Data
import subprocess


class Modules:
    modules = Data.get_modules()
    def __init__(
        self,
        page: Page,
        get_icon_name,
        get_icon_color,
        breadcrumb,
        content,
        show_topics,
    ) -> None:
        self.page = page
        self.get_icon_name = get_icon_color
        self.get_icon_color = get_icon_color
        self.breadcrumb = breadcrumb
        self.content = content
        self.show_topics = show_topics

        self.render_modules = [
            Container(
                Row(
                    [
                        Icon(
                            name=get_icon_name(i[1]),
                            color=get_icon_color(i[1]),
                            size=16,
                        ),
                        Text(spans=[TextSpan(i[0])]),
                    ]
                ),
                on_hover=self.handle_hover_module,
                on_click=lambda e: self.handle_module_click(
                    e, breadcrumb, content, show_topics
                ),
                key=i,
            )
            for i in self.modules
        ]

    def handle_module_click(self, e, breadcrumb, content, show_topics):
        breadcrumb.spans = [TextSpan("Modules"), (TextSpan(f" > {e.control.key[0]}"))]

        content.content.controls[1].controls = show_topics[e.control.key[0]]

        print(f"Getting topics for {e.control.key[0]}...")
        self.page.update()
    
    def handle_hover_module(self, e):
        for target in self.render_modules:
            if target.key == e.control.key:
                target.content.controls[1].spans[0].style = TextStyle(
                    decoration=TextDecoration.UNDERLINE)
            else:
                target.content.controls[1].spans[0].style = TextStyle(
                    decoration=TextDecoration.NONE)
        self.page.update()


class Module():
    def __init__(self, name, status, command, uuid) -> None:
        self.name = name
        self.status = status
        self.command = command
        self.uuid = uuid

    def get_topics(self):
        result = subprocess.run(["wtc-lms" ,"topics", self.uuid], capture_output=True, text=True)
        with open("./data/new_data.txt", "w") as my_file:
            my_file.write(result.stdout)
            print("File created!")     


module = Module("Fundamentals", "[Not Started]", "wtc-lms topics giant-green-cycle", "giant-green-cycle")
module.get_topics()