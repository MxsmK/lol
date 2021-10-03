from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Список учеников"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Добавить ученика"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            
            OneLineListItem:
                text: "Кто ест, а кто нет"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Организация питания"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"
                
                MDLabel:
                    text: "Тут список учеников"
                    halign: "center"


            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Тут функция добавления ученика"
                    halign: "center"
                
                MDTextField:
                    hint_text: "Имя"
                    pos_hint: {"center_y": .45}
                
                MDTextField:
                    hint_text: "Фамилия"
                    pos_hint: {"center_y": .4}
                
                MDTextField:
                    hint_text: "Счет"
                    pos_hint: {"center_y": .35}
                
                MDFlatButton:
                    id: button_create
                    text: "Добавить"
                    pos_hint: {"center_x": .5, "center_y": .30}
                    
                    
            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: "Тут таблица кто ест, а кто нет"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''




class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def anything(self):
        btn = self.screen.ids.button_create
        if btn.on_press():
            print("anything")

    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()
