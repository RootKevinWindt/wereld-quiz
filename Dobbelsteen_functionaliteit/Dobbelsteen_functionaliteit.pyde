add_library('controlP5')
def setup():
    global cp5, diceSize
    diceSize = 117
    size(1280, 700)
    noLoop()
def draw():
    global diceSize
    background(unhex("43936B"))
    noStroke()
    fill(unhex("FFF3D6"))
    rectMode(CENTER)
    rect(width/2, height/2, diceSize, diceSize)
    fill(50)
    side = int(random(1, 7))
    if (side == 1 or side == 3 or side == 5):
        ellipse(width/2, height/2, diceSize/5, diceSize/5)
    if (side == 2 or side == 3 or side == 4 or side == 5 or side == 6):
        ellipse(width/2 - diceSize/4, height/2 - diceSize/4, diceSize/5, diceSize/5)
        ellipse(width/2 + diceSize/4, height/2 + diceSize/4, diceSize/5, diceSize/5)
    if (side == 4 or side == 5 or side == 6):
        ellipse(width/2 - diceSize/4, height/2 + diceSize/4, diceSize/5, diceSize/5)
        ellipse(width/2 + diceSize/4, height/2 - diceSize/4, diceSize/5, diceSize/5)
    if (side == 6):
        ellipse(width/2, height/2 - diceSize/4, diceSize/5, diceSize/5)
        ellipse(width/2, height/2 + diceSize/4, diceSize/5, diceSize/5)
    if (mousePressed and mouseButton == LEFT):
        noLoop()
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False 
def mousePressed():
    if isMouseWithinSpace(width/2, height/2, diceSize, diceSize): 
        loop()
