
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        hbox0 = HBox()
        hbox0.attr_class = "HBox"
        hbox0.attr_editor_newclass = False
        hbox0.css_align_items = "center"
        hbox0.css_display = "flex"
        hbox0.css_flex_direction = "row"
        hbox0.css_height = "105.0px"
        hbox0.css_justify_content = "space-around"
        hbox0.css_left = "205.3125px"
        hbox0.css_position = "absolute"
        hbox0.css_top = "85.40625px"
        hbox0.css_width = "270.0px"
        hbox0.variable_name = "hbox0"
        button0 = Button()
        button0.attr_class = "Button"
        button0.attr_editor_newclass = False
        button0.css_height = "30px"
        button0.css_order = "-1"
        button0.css_position = "static"
        button0.css_top = "187.40625px"
        button0.css_width = "100px"
        button0.text = "button"
        button0.variable_name = "button0"
        hbox0.append(button0,'button0')
        button1 = Button()
        button1.attr_class = "Button"
        button1.attr_editor_newclass = False
        button1.css_height = "30px"
        button1.css_order = "-1"
        button1.css_position = "static"
        button1.css_top = "202.40625px"
        button1.css_width = "100px"
        button1.text = "button"
        button1.variable_name = "button1"
        hbox0.append(button1,'button1')
        button2 = Button()
        button2.attr_class = "Button"
        button2.attr_editor_newclass = False
        button2.css_height = "30px"
        button2.css_order = "-1"
        button2.css_position = "static"
        button2.css_top = "214.40625px"
        button2.css_width = "100px"
        button2.text = "button"
        button2.variable_name = "button2"
        hbox0.append(button2,'button2')
        

        self.hbox0 = hbox0
        return self.hbox0
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
