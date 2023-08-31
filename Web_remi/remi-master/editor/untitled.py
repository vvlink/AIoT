
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
        vbox0 = VBox()
        vbox0.attr_class = "VBox"
        vbox0.attr_editor_newclass = False
        vbox0.css_align_items = "center"
        vbox0.css_display = "flex"
        vbox0.css_flex_direction = "column"
        vbox0.css_height = "250px"
        vbox0.css_justify_content = "space-around"
        vbox0.css_left = "276.625px"
        vbox0.css_position = "absolute"
        vbox0.css_top = "117.71875px"
        vbox0.css_width = "250px"
        vbox0.variable_name = "vbox0"
        label0 = Label()
        label0.attr_class = "Label"
        label0.attr_editor_newclass = False
        label0.css_height = "30px"
        label0.css_order = "-1"
        label0.css_position = "static"
        label0.css_top = "173.71875px"
        label0.css_width = "100px"
        label0.text = "label"
        label0.variable_name = "label0"
        vbox0.append(label0,'label0')
        dropdown0 = DropDown()
        dropdown0.attr_class = "DropDown"
        dropdown0.attr_editor_newclass = False
        dropdown0.css_height = "30px"
        dropdown0.css_order = "-1"
        dropdown0.css_position = "static"
        dropdown0.css_top = "306.71875px"
        dropdown0.css_width = "100px"
        dropdown0.variable_name = "dropdown0"
        vbox0.append(dropdown0,'dropdown0')
        vbox0.children['dropdown0'].onchange.do(vbox0.children['label0'].innerHTML)
        

        self.vbox0 = vbox0
        return self.vbox0
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
