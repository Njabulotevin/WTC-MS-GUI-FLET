from flet import *


class Status():

    status_icons = {'[Completed]': ("check_circle", colors.GREEN_400),
                    '[In Progress]': ("pending", colors.ORANGE_400), "[Not Started]": ("cancel", colors.RED_400)}

    @classmethod
    def get_icon_name(cls,status):
        return cls.status_icons[status][0]
    
    @classmethod
    def get_icon_color(cls, status):
        return cls.status_icons[status][1]