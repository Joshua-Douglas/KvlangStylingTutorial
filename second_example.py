from kivy.lang import Builder
from kivy.app import runTouchApp

kvlang = '''
# Button is a fancy Label that responds to clicks, and 
# uses a background image to display its state
<PressDirectionButton@Button>:
    background_normal: 'button_up.png'
    background_down: 'button_down.png'
    font_size: 24
    color: 1, 1, 1, 1
    halign: 'left'
    valign: 'top'
    text_size: self.width, self.height

BoxLayout:
    PressDirectionButton:
        text: 'Show Pressed Direction'
'''

root_widget = Builder.load_string(kvlang)
runTouchApp(root_widget)