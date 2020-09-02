from kivymd.app import MDApp
#from kivy.app import App
#from kivy.uix.button import Button
#from kivy.uix.boxlayout import BoxLayout
#from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition
from kivy.core.window import Window
from kivy.lang.builder import Builder
from screen_nav import screen_helper
#from kivy.base import runTouchApp
#from kivy.uix.scrollview import ScrollView

# Window.size = (720, 1280)
Window.size = (480, 853)


# Объявляем экраны
class MenuScreen(Screen):
    pass

class CanapeScreen(Screen):
    pass

class BasketScreen(Screen):
    pass


"""
class CanapeScroll(ScrollView):
    pass

    def __init__(self, canapescroll, **kwargs):
        super().__init__(**kwargs)
        for c_scroll in CanapeScroll:
            self.add_widget(Label(text=Привет))

class CanapeScreen(Screen):
    def animup(self, sy):
        scr = self, ids['scroller']
        lab = self, ids['head']

        lab.pos[1] = lab.parent.parent.height*0.85 +scr.scroll_y * 48
        lab.pos[0] = lab.parent.parent.width * 0.30 + scr.scroll_y * 150
        print = lab.pos[1], lab.pos[0]
        print = scr.scroll_y
"""




# Создание ScreenManager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(CanapeScreen(name='canape'))
sm.add_widget(BasketScreen(name='basket'))


# Ссылка на kv файл > перенесено в build
# screen = Builder.load_string(screen_helper)


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.root_widget = Builder.load_string(screen_helper)
        return self.root_widget




if __name__ == "__main__":
    MyApp().run()
