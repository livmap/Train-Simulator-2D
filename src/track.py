class Track:
    def __init__(self, x, y, w, h, t):
        self.w = w
        self.yChange = h
        self.t = t
        self.friction = 0.01
        self.x = x
        self.y = y
        self.endX = 0
        self.endY = 0
        
        self.endX = self.x
        self.endY = self.y - self.yChange
        

