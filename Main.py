

from kivymd.app import MDApp
from kivymd.uix.list import IconLeftWidget,IconRightWidget, OneLineAvatarIconListItem
from kivy.uix.screenmanager import ScreenManager ,Screen,NoTransition
from kivy.properties import StringProperty ,ObjectProperty
from kivymd.icon_definitions import md_icons
from kivymd.uix.filemanager import MDFileManager
from plyer import filechooser
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.toast import toast
import os
import random
from kivy.core.window import Window
from kivymd.uix.bottomsheet import MDGridBottomSheet

array_music=[]



class MusicPlay_page(Screen):
   
    
    def color_change_f(self):
        pass
        
        

    def play_pause(self):
        play_action=True
        if self.ids.play_pause_changer.icon =="play-circle":
            self.ids.play_pause_changer.icon="stop-circle-outline"
            print("play")
           
            self.ids.progress_music.start
        else:
            self.ids.play_pause_changer.icon ="play-circle"
            print("pause")
            self.ids.progress_music.stop
           
            
    
    icon_for_button=[]
    def callback_for_menu_items(self, *args):
        toast(args[0])
        if args[0]=="color":
            MusicPlay_page.color_change_f(self)
        
            
            
    def show_example_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
        "Favorite": "heart",
        "Light Mode": "lightbulb-on-outline",
        "Dark Mode": "brightness-3",
        "Share": "share-all-outline",
        "Set as ringtone": "phone-classic",
        "Bluetooth":"bluetooth",
        "color":"cookie"
        
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
            item[0],
            lambda x, y=item[0]: self.callback_for_menu_items(y),
            icon_src=item[1],
            )
        bottom_sheet_menu.open()
    

class Folder_page(Screen):
    def file_manager_open(self):
        Folder_page.path=os.path.expanduser("~")# output manager to the screen
        Folder_page.manager_open = True
        print(Folder_page.file_manager.show(Folder_page.path))
     
    def select_path_1(self,path):
        #print("ji",(Front_page.select_path.)) 
         
        Folder_page.exit_manager(self)
        print(path)
        
    
    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.
        :param path: path to the selected directory or file;
        '''
        print("hi")
        #self.exit_manager()
        #toast(path)
    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''
        print(*args)
        Folder_page.manager_open = False
        Folder_page.file_manager.close()
    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''
        if keyboard in (1001, 27):
            if Folder_page.manager_open:
                Folder_page.file_manager.back()
        return True
 
    def on_start(self):
        if array_music==[]:
            Folder_page.file_manager_open(self)
            
            pass
        else:
            for i in range(len(array_music)):
                self.ids.container.add_widget(
                OneLineAvatarIconListItem(IconLeftWidget(
                    icon='music-circle',disabled= 'True'),
                                        
                    IconRightWidget(icon="play-circle"),text="heloo") ) 
            
    
    def on_settings(self):
        print("hi")
    


class Tracks_Paage(Screen):
    def on_start(self):
        global array_music
        if array_music==[]:
            #Folder_page.file_manager_open(self)
            
            pass
        else:
            for i in range(len(array_music)):
                self.ids.container.add_widget(
                OneLineAvatarIconListItem(IconLeftWidget(
                    icon='music-circle',disabled= 'True'),
                                        
                    IconRightWidget(icon="play-circle"),text=array_music[i]) ) 
    
            
    
    def on_settings(self):
        print("hi")
    


class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        Folder_page.manager_open = False
        Folder_page.file_manager = MDFileManager(
        exit_manager=Folder_page.exit_manager, select_path=Folder_page.select_path_1
        )
        global array_music
        path="D:\MUSICS"
        songs=os.listdir(path)
        array_music=[fi for fi in songs if fi.endswith(".mp3")]
        
        
 
    def build(self):
        self.theme_cls.material_style="M3"
        global mode_changer ,change_mode
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "Orange"
        
            
        
    
    

       
    
         

if __name__ =='__main__':
        Main().run()