import another, press_square, hi

def setup():
    size(200, 200)
    
def draw():
    background(150, 100, 20)
    hi.draw()
    press_square.draw()
    another.draw()
    line(0, 25, 200, 25)
    line(0, 50, 200, 50)
    line(0, 75, 200, 75)
    line(0, 125, 200, 125)
    line(0, 150, 200, 150)
    line(0, 175, 200, 175)
    line(25, 0, 25, 200)
    line(50, 0, 50, 200)
    line(75, 0, 75, 200)
    line(125, 0, 125, 200)
    line(150, 0, 150, 200)
    line(175, 0, 175, 200)
