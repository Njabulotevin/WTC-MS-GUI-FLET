from flet import *


class Status():
    def __init__(self) -> None:
        self.status_icons = {"completed": ("check_circle", colors.GREEN_400),
                    "in_progress": ("pending", colors.ORANGE_400), "not_started": ("cancel", colors.RED_400)}

    def get_icon_name(self,status):
        return self.status_icons[status][0]

    def get_icon_color(self, status):
        return self.status_icons[status][1]