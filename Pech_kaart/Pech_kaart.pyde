add_library('controlP5')

def setup():
    size(1280, 700)
    font = createFont("arrial", 20)
    font2 = createFont("arrial", 40)
    global cp5, font, font2
    cp5 = ControlP5(this)
    
def draw():
    fill(0)
    textFont(font2)
    text(str("Pech kaart"), width/2 - 95, 90)
    fill(200)
# Pech kaart
    rect(490, 170, 300, 450, 10)
# Terug
    rect(50, 560, 350, 120, 10)
    fill(0)
    text(str("Terug"), 175, 635)
