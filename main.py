from flet import *
from Modules import Modules
from Status import Status
from Content import Content
from Topics import Topics
from Theme import ThemeColors
from Layout import Layout


def main(page: Page):
    page.title = "Flet counter example"
    page.padding = 0
    page.bgcolor = ThemeColors.background_color
    page.active = "modules"
    menu_items = ["File", "Edit", "View", "Settings", "Help"]
    render_menu_items = [Container(Text(item, size=12)) for item in menu_items]
    status = Status()
    content_1 = Content(Topics.show_topics)
    modules_1 = Modules(
        page,
        status.get_icon_name,
        status.get_icon_color,
        content_1.breadcrumb,
        content_1.content,
        Topics.show_topics,
    )
    render_modules = modules_1.render_modules
    layout = Layout(page)

    top_menu = Container(
        Row(render_menu_items, spacing=25),
        border=Border(bottom=BorderSide(0.5, ThemeColors.secondary_color)),
        padding=padding.symmetric(vertical=6, horizontal=20),
        bgcolor=ThemeColors.primary_color,
    )
    main_view = Container(
        Row(
            vertical_alignment=CrossAxisAlignment.STRETCH,
            controls=[
                Container(
                    Container(
                        Column(render_modules, spacing=30), padding=padding.all(20)
                    ),
                    width=230,
                    bgcolor=ThemeColors.primary_color,
                    padding=padding.all(10),
                    border=border.only(
                        right=BorderSide(0.2, ThemeColors.secondary_color)
                    ),
                ),
                content_1.content,
            ],
            spacing=0,
        ),
        height=900,
    )

    page.add(Column([top_menu, layout.navigation, main_view], spacing=0))
    page.update()


app(target=main)
