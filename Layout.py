from flet import *
from Theme import ThemeColors

class Layout():
    def __init__(self, page) -> None:
        self.page = page
        self.nav_items = [("Modules", "dashboard"), ("Reviews", "assignment_turned_in"),
                 ("Assessmenents", "school")]
        self.active_border = Border(bottom=BorderSide(3, ThemeColors.blue))
        self.render_nav_items = [Container(Row([Icon(name=i[1], color=ThemeColors.blue if i[0].lower() == page.active else ThemeColors.secondary_color), Text(
        i[0], color=ThemeColors.blue if i[0].lower() == page.active else ThemeColors.secondary_color, weight=FontWeight.W_700)]), key=i[0], on_click=self.handle_nav_click, data=i, padding=padding.all(16), border=self.active_border if i[0].lower() == page.active else None) for i in self.nav_items]
        self.navigation = Container(Row(self.render_nav_items, spacing=30),
                           bgcolor=ThemeColors.primary_color, border=Border(
        bottom=BorderSide(0.5, ThemeColors.secondary_color)))

    def handle_nav_click(self, e: ContainerTapEvent):
        key = e.control.key
        for target in self.navigation.content.controls:
            targeted = target.content.controls
            if target.key == str(key):
                targeted[0].color = ThemeColors.blue
                targeted[1].color = ThemeColors.blue
                target.border = self.page.active_border
                self.page.active = str(key)
            else:
                targeted[0].color = ThemeColors.secondary_color
                targeted[1].color = ThemeColors.secondary_color
                target.border = None

        self.page.update()