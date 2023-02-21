from kivy.lang import Builder 
from kivy.app import runTouchApp

kv = '''\
Button:
    text: 'Click me!'
'''
root_widget = Builder.load_string(kv)
runTouchApp(root_widget)
