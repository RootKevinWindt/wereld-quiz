add_library('controlP5')

def setup():
    size(1280, 700)
    fill(0)
    background(240)
    font = createFont("arrial", 30)
    font2 = createFont("arrial", 80)
    global cp5, font, font2, speler1, speler2, speler3, speler4, punten1, punten2, punten3 , punten4
    cp5 = ControlP5(this)
    
def draw():
    fill(0)
    textFont(font)
    fill(240)
    rect(250, 150, 200, 60) #speler 1
    rect(250, 220, 200, 60) #speler 2
    rect(250, 290, 200, 60) #speler 3
    rect(250, 360, 200, 60) #speler 4
    fill(0)
    textFont(font2)
    text(str("Scorebord"), width / 2 - 190 , 90)
    textFont(font)
    text(str("speler1"), 270, 190)
    text(str("Punten:"), 570, 190)
    punten1 = text(int(1), 695, 190)
    text(str("speler2"), 270, 260)
    text(str("Punten:"), 570, 260)
    punten2 = text(int(1), 695, 260)
    text(str("speler3"), 270, 330)
    text(str("Punten:"), 570, 330)
    punten3 = text(int(1), 695, 330)
    text(str("speler4"), 270, 400)
    text(str("Punten:"), 570, 400)
    punten4 = text(int(1), 695, 400)

#Vraag kaart button
    fill(200)
    rect1 = rect(75, 500, 350, 125, 15)
# Gooi dobbelsteen button
    rect2 = rect(455, 500, 350, 125, 15)
# Pech kaart button
    rect3 = rect(835, 500, 350, 125, 15)
#Spel afstluiten button
    rect4 = rect(1050, 30, 200, 70, 15)
    fill(0)
    text(str("Vragen kaart"), width/8, height/10 * 8)
    text(str("Gooi dobbelsteen"), width/3 + 85, height/10 * 8)
    text(str("Pech kaart"), 930, height/10 * 8)
    text(str("Spel afsluiten"), 1060, 70)


# + buttons in volgorde
    fill(200)
    rect(740, 160, 45, 45, 7)
    rect(740, 230, 45, 45, 7)
    rect(740, 300, 45, 45, 7)
    rect(740, 370, 45, 45, 7)
# - buttons in volgorde
    rect(800, 160, 45, 45, 7)
    rect(800, 230, 45, 45, 7)
    rect(800, 300, 45, 45, 7)
    rect(800, 370, 45, 45, 7)
    fill(0)
    text(str("+"), 754, 193)
    text(str("+"), 754, 263)
    text(str("+"), 754, 333)
    text(str("+"), 754, 403)
    text(str("-"), 817, 191)
    text(str("-"), 817, 261)
    text(str("-"), 817, 331)
    text(str("-"), 817, 401)
    
