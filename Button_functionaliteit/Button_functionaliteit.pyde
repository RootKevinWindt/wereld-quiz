add_library('controlP5')
def setup():
    global sizewidth, sizeheight, buttonwidth, buttonheight, cp5, points
    sizewidth = 1280
    sizeheight = 700
    buttonwidth = 350
    buttonheight = 125
    points = 0
    size(1280, 700)
    cp5 = ControlP5(this)

    pfont = createFont("Arial",20)
    font = ControlFont(pfont,241)

    b = cp5.addButton("Spel Starten").setValue(0).setPosition(sizewidth / 2 - buttonwidth / 2, sizeheight / 2 - buttonheight / 2).setSize(buttonwidth,buttonheight)
    b.getCaptionLabel().setFont(font).setSize(35)

def draw():
    background(255)
    fill(0)
    text(str(points), 50, 50)
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
def mousePressed():
    global points
    if isMouseWithinSpace(sizewidth / 2 - buttonwidth / 2, sizeheight / 2 - buttonheight / 2, buttonwidth, buttonheight ):
        points = points +1
        #What the button should do
    else:
        print("is not within space")
