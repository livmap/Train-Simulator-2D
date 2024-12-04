class Train:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.velocity = 0
        self.maxVelocity = 0
        self.frontalArea = self.w * (2 * self.w)
        self.dragCoefficient = 0.295
        self.dangerThrottle = 87