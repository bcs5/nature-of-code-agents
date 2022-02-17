# The "Food" class

class Food():

    def __init__(self, margin):
        self.margin = margin
        self.position = self.randPos()
        self.eaten = 0

    def randPos(self):
        x = random(self.margin, width-self.margin)
        y = random(self.margin, height-self.margin)
        return PVector(x, y)

    # Method to update location
    def update(self, vehicle_position):
        if (vehicle_position.dist(self.position) <= 5):
            self.position = self.randPos()
            self.eaten += 1

    def display(self):
        fill(127)
        stroke(200)
        strokeWeight(1)
        textSize(self.margin);
        text("comida: {}".format(self.eaten), self.margin, self.margin);
        with pushMatrix():
            ellipse(self.position.x, self.position.y, 10, 10)
