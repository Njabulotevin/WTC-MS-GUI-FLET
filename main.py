from flet import *

primary_color: str = "#3C3C3C"
secondary_color = "#D7D7D7"
blue = "#095FB0"
background_color = "#323232"


def main(page: Page):
    page.title = "Flet counter example"
    page.padding = 0
    page.bgcolor = background_color
    page.active = "modules"
    menu_items = ["File", "Edit", "View", "Settings", "Help"]
    render_menu_items = [Container(Text(item, size=12)) for item in menu_items]
    nav_items = [("Modules", "dashboard"), ("Reviews", "assignment_turned_in"),
                 ("Assessmenents", "school")]
    active_border = Border(bottom=BorderSide(3, blue))

    breadcrumb = Text(spans=[TextSpan(page.active),
                      TextSpan(" > Fundamentals")], size=12)

    modules = [("Fundamentals", "completed"), ("Object Orientation",
                                               "in_progress"), ("Web Development", "not_started")]

    status_icons = {"completed": ("check_circle", colors.GREEN_400),
                    "in_progress": ("pending", colors.ORANGE_400), "not_started": ("cancel", colors.RED_400)}

    topics = {}

    for i in modules:
        topics[i[0]] = [f"topic 1: {i[0]}",
                        f"topic 2 : {i[0]}", f"topic 3 : {i[0]}", f"topic 4 : {i[0]}", f"topic 5 : {i[0]}"]

    show_topics = {}

    for module in topics:
        show_topics[module] = [
            Container(Row([Icon(name="chevron_right", color=secondary_color), Text(i, color=secondary_color)]), bgcolor=primary_color, padding=padding.all(10), border_radius=5) for i in topics[module]]

    def get_topics(module):
        return show_topics[module]

    print(show_topics)

    def get_icon_name(status):
        return status_icons[status][0]

    def get_icon_color(status):
        return status_icons[status][1]

    def handle_hover_module(e):
        for target in render_modules:
            if target.key == e.control.key:
                target.content.controls[1].spans[0].style = TextStyle(
                    decoration=TextDecoration.UNDERLINE)
            else:
                target.content.controls[1].spans[0].style = TextStyle(
                    decoration=TextDecoration.NONE)
        page.update()

    def handle_module_click(e):
        breadcrumb.spans = [
            TextSpan("Modules"), (TextSpan(f" > {e.control.key[0]}"))]

        content.content.controls[1].controls = show_topics[e.control.key[0]]

        print(f"Getting topics for {e.control.key[0]}...")
        page.update()

    render_modules = [
        Container(Row([Icon(name=get_icon_name(i[1]), color=get_icon_color(i[1]), size=16), Text(spans=[TextSpan(i[0])])]), on_hover=handle_hover_module, on_click=handle_module_click, key=i) for i in modules]

    def handle_nav_click(e: ContainerTapEvent):
        key = e.control.key
        for target in navigation.content.controls:
            targeted = target.content.controls
            if target.key == str(key):
                targeted[0].color = blue
                targeted[1].color = blue
                target.border = active_border
                page.active = str(key)
            else:
                targeted[0].color = secondary_color
                targeted[1].color = secondary_color
                target.border = None

        page.update()

    render_nav_items = [Container(Row([Icon(name=i[1], color=blue if i[0].lower() == page.active else secondary_color), Text(
        i[0], color=blue if i[0].lower() == page.active else secondary_color, weight=FontWeight.W_700)]), key=i[0], on_click=handle_nav_click, data=i, padding=padding.all(16), border=active_border if i[0].lower() == page.active else None) for i in nav_items]

    top_menu = Container(Row(render_menu_items, spacing=25), border=Border(
        bottom=BorderSide(0.5, secondary_color)), padding=padding.symmetric(vertical=6, horizontal=20), bgcolor=primary_color)

    navigation = Container(Row(render_nav_items, spacing=30),
                           bgcolor=primary_color, border=Border(
        bottom=BorderSide(0.5, secondary_color)))

    content = Container(
        Column([breadcrumb, Column(show_topics["Fundamentals"])]), expand=1,  padding=20)

    main_view = Container(Row(vertical_alignment=CrossAxisAlignment.STRETCH, controls=[Container(Container(Column(render_modules, spacing=30), padding=padding.all(
        20)), width=230, bgcolor=primary_color, padding=padding.all(10), border=border.only(right=BorderSide(0.2, secondary_color))), content],  spacing=0), height=900)

    page.add(Column([top_menu, navigation, main_view],
             spacing=0))

    page.update()


app(target=main)
