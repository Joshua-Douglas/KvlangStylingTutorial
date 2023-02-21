from kivy.lang import Builder
from kivy.app import runTouchApp
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class SaveLabel(Label):

    entry_cntr = NumericProperty(0)

    def save(self, text_to_save):
        # Do not save empty strings or null values
        if not text_to_save:
            return
        self.entry_cntr += 1
        self.text += f'Entry {self.entry_cntr}:\n{text_to_save}\n'

kvlang = '''
<SaveLabel>:
    text_size: self.width, self.height
    halign: 'left'
    valign: 'top'

BoxLayout:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Save Text Input'
            on_press: save_label.save(text_input.text)
        Button:
            text: 'Clear'
            id: clear_button
            on_press: save_label.text = ''
    TextInput:
        id: text_input
    SaveLabel: 
        id: save_label
'''

root_widget = Builder.load_string(kvlang)
runTouchApp(root_widget)