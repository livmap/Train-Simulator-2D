from track import Track
import math

class InterChange(Track):
    def __init__(self, x, y, w, t, a, xC):
        self.angle = a
        self.xChange = xC
        self.yChange = 0
        self.maxVeloc = 0
        self.x = x
        self.y = y
        self.w = w
        self.t = t
        self.endX = 0
        self.endY = 0

        if self.angle <= 90:
            self.yChange = math.tan(self.angle * (math.pi / 180)) * self.xChange
            self.endX = self.x + self.xChange
            self.endY = self.y - self.yChange
        elif self.angle > 90:
            self.angle = 180 - self.angle
            self.yChange = -math.tan(self.angle * (math.pi / 180)) * self.xChange
            self.endX = self.x - self.xChange
            self.endY = self.y + self.yChange

        # 40 at 30
        self.maxVeloc = 40 + ((self.angle - 30))

        