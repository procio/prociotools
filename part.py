class board(list):
    def __init__(self, x=25, y=25):
        self.x = x
        self.y = y
        self.xbounds = [0,x]
        self.ybounds = [0,y]
        
        self.generate()
    
    def generate(self):
        for Y in range(self.y):
            l = list()
            for X in range(self.x):
                p = position(X,Y)
                l.append(p)
            self.append(l)
        #self.reverse()
            
    def drop(self, x=0, y=0):
        p = particle(x,y,ray=3)
        for pos in p.getArea():
            self[pos.y][pos.x].activate()
        
    def __str__(self):
        from pt.meta import join
        boardStr = str()
        lineList = list()
        
        for List in self:
            lineList.append(List)
        for List in lineList:
            for pos in List:
                List[List.index(pos)] = pos.getRepr()
            lineList[lineList.index(List)] = join(List,"")

        boardStr = join(lineList, "\n")
        return boardStr
        
class particle(object):
    def __init__(self, x=None, y=None, ray=None, weight=None):
        self.pos = position(x,y)
        self.ray = ray
        self.w = weight
        
    def update(self, x=None, y=None, ray=None):
        if x or y: self.pos.update(x,y)
        if ray: self.ray = ray
        
    def __str__(self):
        return "%s, %s" %(str(self.pos), str(self.ray))
        
    def getArea(self):
        area = list()
        area.append(self.pos)
        x = self.pos.x
        y = self.pos.y
        while x <= self.pos.x + self.ray -1:
            area.append(position(x,y))
            x += 1
        x = self.pos.x
        while x >= self.pos.x - self.ray +1:
            area.append(position(x,y))
            x -= 1
        x = self.pos.x
        while y <= self.pos.y + self.ray -1:
            area.append(position(x,y))
            y += 1
        y = self.pos.y
        while y >= self.pos.y - self.ray +1:
            area.append(position(x,y))
            y -= 1
            
        return area
        
class position(list):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.append(x)
        self.append(y)
        self.active = False
        
    def updateX(self, x):
        self.x = x
        self[0] = x
        
    def updateY(self, y):
        self.y = y
        self[1] = y
        
    def update(self, x=None, y=None):
        if x:
            self.updateX(x)
        if y:
            self.updateY(y)
            
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
        
    def getRepr(self):
        if self.active: return "[X]"
        else: return "[ ]"


    
    
    
