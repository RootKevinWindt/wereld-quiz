add_library('controlP5')

def setup():
    size(1280, 700)
    font = createFont("arrial", 20)
    font2 = createFont("arrial", 40)
    font3 = createFont("arrial", 30)
    global cp5, font, font2, font3
    cp5 = ControlP5(this)
    
def draw():
    textFont(font2)
    fill(0)
    text(str("Vraag kaart"), width/2 - 125, 90)
    textFont(font3)
    text(str("Kies een continent:"), 50, 180)
# Noord-Amerika
    fill(200)
    rect(50, 210, 400, 60)
    fill(0)
    text(str("Noord-Amerika"), 80, 250)
# Zuid-Amerika
    fill(200)
    rect(50, 280, 400, 60)
    fill(0)
    text(str("Zuid-Amerika"), 80, 320)
# Europa
    fill(200)
    rect(50, 350, 400, 60)
    fill(0)
    text(str("Europa"), 80, 390)
# Azië 
    fill(200)
    rect(50, 420, 400, 60)
    fill(0)
    text(str(".."), 123, 441)
    text(str("Azie"), 80, 460)
# Afrika
    fill(200)
    rect(50, 490, 400, 60)
    fill(0)
    text(str("Afrika"), 80, 530)
# Oceanië/Antarctica
    fill(200)
    rect(50, 560, 400, 60)
    fill(0)
    text(str(".."), 175, 581)
    text(str("Oceanie/Antarctia"), 80, 600)
    
