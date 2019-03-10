#import mormir
from kivy.utils import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

global sl1
sl1 = 40

global sl2
sl2 = 40

global sl3
sl3 = 40

global sl4
sl4 = 40

if platform not in ('android', 'ios'):
    # Approximate dimensions of mobile phone.
    Window.size = (320, 460)

class Interface(GridLayout):

    def plus1(self):
        global sl1
        sl1 += 1
 
        self.display1.text = str(sl1)
    def minus1(self):
        global sl1
        sl1 -= 1

        self.display1.text = str(sl1)

    def plus2(self):
        global sl2
        sl2 += 1
        self.display2.text = str(sl2)
         
    def minus2(self):
        global sl2
        sl2 -= 1
        self.display2.text = str(sl2)

    def plus3(self):
        global sl3
        sl3 += 1
        self.display3.text = str(sl3)
         
    def minus3(self):
        global sl3
        sl3 -= 1
        self.display3.text = str(sl3)

    def plus4(self):
        global sl4
        sl4 += 1
        self.display4.text = str(sl4)
         
    def minus4(self):
        global sl4
        sl4 -= 1
        self.display4.text = str(sl4)

    
        
#mormir.imageget('Swamp', 'bl')
class MormirApp(App):
    pass
    
if __name__ == '__main__':
    MormirApp().run()
