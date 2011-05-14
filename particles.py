from pymt import *

class ParticleWidget(MTWidget):
    def __init__(self):
        MTWidget.__init__(self)
        # robe con la coda a striscie
    
    # chiamata ogni frame
    def on_update(self):
        super(ParticleWidget, self).on_update()
        # robe con la coda a striscie
    
    # chiamata ogni frame
    def draw(self):
        # robe con la coda a striscie
        # eg. set_color(0, 1, 0)
        #     drawCircle(pos=(x, y), radius=20.0, linewidth=0)
        pass
        
    def on_touch_down(self, touch):
        # robe con la coda a striscie
        # hai touch.pos (tupla di x,y)
        #     touch.dpos (posizione precedente)
        #     touch.opos (posizione iniziale)
        pass
    
    def on_touch_move(self, touch):
        pass
    
    def on_touch_up(self, touch):
        pass
    
if __name__ == '__main__':
    par = ParticleWidget()
    runTouchApp(par)


