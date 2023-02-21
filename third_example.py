from kivy.lang import Builder
from kivy.app import runTouchApp

kvlang = '''
<PressDirectionImage@Image>:
    # is_up is a custom property, defined here
    is_up: False
    source: 'button_up.png' if self.is_up else 'button_down.png'

BoxLayout:
    Button: 
        id: controller_button
        text: 'Press to change image'
    PressDirectionImage:
        is_up: controller_button.state == 'normal'
'''

root_widget = Builder.load_string(kvlang)
runTouchApp(root_widget)