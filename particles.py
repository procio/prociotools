import math
from random import randint, random, choice

from pymt import *

class CircularParticle(object):
    _pool = []
    __slots__ = ["x", "y", "dx", "dy", "radius", "phase", "R", "G", "B", "A"]
    
    @staticmethod
    def draw_all():
        for p in CircularParticle._pool:
            p.draw()

    @staticmethod
    def random_particle():
        p = CircularParticle()
        p.x, p.y = random(), random()
        p.dx, p.dy = random(), random()
        p.radius = 30
        p.phase = random()*2
        p.R , p.G, p.B, p.A = random(), random(), random(), random()
        return p
    
    @staticmethod
    def new_particle():
        return CircularParticle()
    
    def draw(self):
        set_color(self.R, self.G, self.B, self.A)
        drawCircle(pos=(self.x, self.y), radius=self.radius*math.sin(getClock().get_time()+self.phase))
    
    def __init__(self):
        self._pool.append(self)

class ParticleWidget(MTWidget):
    def __init__(self, particles=16, borders=False, collision=False, particle_type = CircularParticle):
        MTWidget.__init__(self)
        self.particles = particles
        self.borders = borders
        self.collision = collision
        self.particle_type = particle_type
        self._pool = particle_type._pool
    
    def init_particles(self):
        for i in xrange(self.particles):
            p = self.particle_type.random_particle()
            p.x = int(p.x * self.width)
            p.y = int(p.y * self.height)
            p.dx = int(p.dx * 10 * choice([-1,1]))
            p.dy = int(p.dy * 10 * choice([-1,1]))
            
    
    def update_particle(self, p):
        p.x += p.dx
        p.y += p.dy
        if not self.collide_point(p.x, p.y):
            if self.borders == False:
                if p.x < 0:
                    p.x = self.width
                elif p.x > self.width:
                    p.x = 0
                if p.y < 0:
                    p.y = self.height
                elif p.y > self.height:
                    p.y = 0
            elif self.borders == True:
                if not 0 < p.x < self.width:
                    p.dx = -p.dx
                if not 0 < p.y < self.height:
                    p.dy = -p.dy
    
    def update_particles(self):
        map(self.update_particle, self._pool)
    
    # chiamata ogni frame
    def on_update(self):
        super(ParticleWidget, self).on_update()
        self.update_particles()
    
    # chiamata ogni frame
    def draw(self):
        self.particle_type.draw_all()
    
    def on_touch_down(self, touch):
        # robe con la coda a striscie
        # hai touch.pos (tupla di x,y)
        #     touch.dpos (posizione precedente)
        #     touch.opos (posizione iniziale)
        #     touch.spos (posizione in coordinate [0,1])
        pass
    
    def on_touch_move(self, touch):
        pass
    
    def on_touch_up(self, touch):
        pass
    
    def on_parent(self):
        self.size = self.parent.size
        self.init_particles()
    
if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass

    w = getWindow()
    pw = ParticleWidget(particles=16, borders=True)
    w.add_widget(pw)
    runTouchApp()


