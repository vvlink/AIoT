#main program code prototype
proto_code_program = """
# -*- coding: utf-8 -*-

%(imports)s
from remi import start, App

%(code_classes)s

#Configuration
configuration = %(configuration)s

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(%(classname)s, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
"""

#typical widget class prototype
proto_code_class = """
class %(classname)s( %(superclassname)s ):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        super( %(classname)s, self ).__init__(*args, **kwargs)
        %(nested_code)s
"""

#function prototype
proto_code_function = "    def %(funcname)s%(parameters)s:\n        pass\n\n"

#here the prototype of the main class
proto_code_main_class = """
class %(classname)s(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(%(classname)s, self).__init__(*args, static_file_path={'my_res':'%(config_resourcepath)s'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return %(classname)s.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        %(code_nested)s

        self.%(mainwidgetname)s = %(mainwidgetname)s
        return self.%(mainwidgetname)s
    
"""

proto_export_app_template = """
from remi.gui import *

class %(classname)s( %(superclassname)s ):                                                                                                          #cheak:Maybe change class name to name of root container

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)                                                                                                #cheak:remove Comments
        self.AppInst = AppInst                                                                                                           #cheak:remove Comments
        self.constructUI()                                                                                                               #cheak:instead we just call it
        self.userInit(args, kwargs)                                                                                                      #more. Register events. Add custom widgets. Add css classes etc.
                                                                                                                                         # pass kwargs to user init in case user needs it.

    def constructUI(self):
        %(nested_code)s
        %(events_registration)s

    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Menu Name'
        self.menuTitle = 'My View Name'

    def updateView(self):
        # Here you can update the view if it needs updates
        pass
"""

proto_widget_allocation = "%(varname)s = %(classname)s()\n        "

proto_attribute_setup = """%(varname)s.attributes.update({%(attr_dict)s})\n        """

proto_property_setup = """%(varname)s.%(property)s = %(value)s\n        """

proto_style_setup = """%(varname)s.style.update({%(style_dict)s})\n        """

proto_layout_append = "%(parentname)s.append(%(varname)s)\n        "

proto_set_listener = "%(sourcename)s.%(register_function)s.do(%(listenername)s.%(listener_function)s)\n        "
