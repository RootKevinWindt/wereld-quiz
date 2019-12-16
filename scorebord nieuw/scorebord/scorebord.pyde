add_library('controlP5')

def setup():
    global cp5, a, b, c, d, e, f, g, na, za, eu, az, af, oa, pechIndex, buttonwidthCont, buttonheightCont, rand, DiceButtonClicked, QButtonClicked, PButtonClicked, diceSize, font, font2, font3, speler1, side, speler2, speler3, speler4, punten1, punten2, punten3 , punten4
    size(1280, 700)
    fill(0)
    background(240)
    font = createFont("arrial", 30)
    font2 = createFont("arrial", 80)
    punten1 = 0
    punten2 = 0
    punten3 = 0
    DiceButtonClicked = False
    QButtonClicked = False
    PButtonClicked = False
    punten4 = 0
    cp5 = ControlP5(this)
    # Dice Func:
    diceSize = 117
    size(1280, 700)
    pfont = createFont("Arial",20)
    font4 = ControlFont(pfont,241)
    side = int(random(1,7))
    pechIndex = ['Sla een beurt over (niet vergeten!)', 'Vlieg terug naar het begin van het vorige continent', 'Geef een punt aan de volgende speler ', 'Je volgende worp is het aantal stappen dat je terug moet doen in plaats van naar voren', '2 punten van je score af', '1 punt van je score af']
    rand = int(random(6))
    
    a = cp5.addButton("Vragen kaart").setValue(0).setPosition(75, 500).setSize(350, 125)
    a.getCaptionLabel().setFont(font4).setSize(35)
    b = cp5.addButton("Dobbelsteen").setValue(0).setPosition(455, 500).setSize(350, 125)
    b.getCaptionLabel().setFont(font4).setSize(35)
    c = cp5.addButton("Pech kaart").setValue(0).setPosition(835, 500).setSize(350, 125)
    c.getCaptionLabel().setFont(font4).setSize(35)
    d = cp5.addButton("Spel Afsluiten").setValue(0).setPosition(1050, 30).setSize(200, 70)
    d.getCaptionLabel().setFont(font4).setSize(20)
    e = cp5.addButton("TERUG").setValue(0).setPosition(455, 500).setSize(350, 125)
    e.getCaptionLabel().setFont(font4).setSize(35)
    f = cp5.addButton("Terug").setValue(0).setPosition(75, 500).setSize(350, 125)
    f.getCaptionLabel().setFont(font4).setSize(35)
    g = cp5.addButton("terug").setValue(0).setPosition(835, 500).setSize(350, 125)
    g.getCaptionLabel().setFont(font4).setSize(35)
    
    buttonNA = False
    buttonZA = False
    buttonEU = False
    buttonAZ = False
    buttonAF = False
    buttonOA = False
    
    font3 = createFont("arrial", 30)
    buttonwidthCont = 400
    buttonheightCont = 60
    
    na = cp5.addButton("Noord-Amerika").setValue(0).setPosition(75, 80).setSize(buttonwidthCont,buttonheightCont)
    na.getCaptionLabel().setFont(font3).setSize(25)
    za = cp5.addButton("Zuid-Amerika").setValue(0).setPosition(75, 150).setSize(buttonwidthCont,buttonheightCont)
    za.getCaptionLabel().setFont(font3).setSize(25)
    eu = cp5.addButton("Europa").setValue(0).setPosition(75, 220).setSize(buttonwidthCont,buttonheightCont)
    eu.getCaptionLabel().setFont(font3).setSize(25)
    az = cp5.addButton("Azie").setValue(0).setPosition(75, 290).setSize(buttonwidthCont,buttonheightCont)
    az.getCaptionLabel().setFont(font3).setSize(25)
    af = cp5.addButton("Afrika").setValue(0).setPosition(75, 360).setSize(buttonwidthCont,buttonheightCont)
    af.getCaptionLabel().setFont(font3).setSize(25)
    oa = cp5.addButton("Oceanie/Antarctica").setValue(0).setPosition(75, 430).setSize(buttonwidthCont,buttonheightCont)
    oa.getCaptionLabel().setFont(font3).setSize(25)
    
def draw():
    global DiceButtonClicked, cp5, a, b, c, d, e, f, side, rand
    background(unhex("FFFFFF"))
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
    text(str(punten1), 695, 190)
    text(str("speler2"), 270, 260)
    text(str("Punten:"), 570, 260)
    text(str(punten2), 695, 260)
    text(str("speler3"), 270, 330)
    text(str("Punten:"), 570, 330)
    text(str(punten3), 695, 330)
    text(str("speler4"), 270, 400)
    text(str("Punten:"), 570, 400)
    text(str(punten4), 695, 400)
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
    global DiceButtonClicked, cp5, a, b, c, d, e, f, na, za, eu, az, af, oa, side
    if DiceButtonClicked == True:
        background(unhex("FFFFFF"))
        a.setVisible(False)
        b.setVisible(False)
        c.setVisible(False)
        d.setVisible(False)
        e.setVisible(True)
        f.setVisible(False)
        g.setVisible(False)
        na.setVisible(False)
        za.setVisible(False)
        eu.setVisible(False)
        az.setVisible(False)
        af.setVisible(False)
        oa.setVisible(False)
        global diceSize
        background(unhex("FFFFFF"))
        text(str(side), width / 2, height / 2)
    elif QButtonClicked == True:
        background(unhex("FFFFFF"))
        a.setVisible(False)
        b.setVisible(False)
        c.setVisible(False)
        d.setVisible(False)
        e.setVisible(False)
        f.setVisible(True)
        g.setVisible(False)
        na.setVisible(True)
        za.setVisible(True)
        eu.setVisible(True)
        az.setVisible(True)
        af.setVisible(True)
        oa.setVisible(True)
        text(str("Kies een continent:"), 75, 50)
    elif PButtonClicked == True:
        background(unhex("FFFFFF"))
        a.setVisible(False)
        b.setVisible(False)
        c.setVisible(False)
        d.setVisible(False)
        e.setVisible(False)
        f.setVisible(False)
        g.setVisible(True)
        na.setVisible(False)
        za.setVisible(False)
        eu.setVisible(False)
        az.setVisible(False)
        af.setVisible(False)
        oa.setVisible(False)
        text(pechIndex[rand], 510, height / 2 - 60, 300, 450)
        text(str("Pech kaart"), width/2 - 95, 90)
        fill(unhex("FFFFF"))
        rect(490, 120, 330, 450, 10)
        
    else:
        a.setVisible(True)
        b.setVisible(True)
        c.setVisible(True)
        d.setVisible(True)
        e.setVisible(False)
        f.setVisible(False)
        g.setVisible(False)
        na.setVisible(False)
        za.setVisible(False)
        eu.setVisible(False)
        az.setVisible(False)
        af.setVisible(False)
        oa.setVisible(False)
        if mousePressed:
            if isMouseWithinSpace(455, 500, 350, 125):
                DiceButtonPressed = False
            if isMouseWithinSpace(1050, 30, 200, 70):
                exit()
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    global punten1, pechIndex, rand, punten2, punten3, punten4, side, DiceButtonClicked, QButtonClicked, PButtonClicked
    # De + buttons punten erbij
    if DiceButtonClicked == False and QButtonClicked == False and PButtonClicked == False :
        if isMouseWithinSpace(740, 160, 45, 45):
            punten1 = punten1 + 1
            #What the button should do
        elif isMouseWithinSpace(740, 230, 45, 45):
            punten2 = punten2 + 1
        elif isMouseWithinSpace(740, 300, 45, 45):
            punten3 = punten3 + 1
        elif isMouseWithinSpace(740, 370, 45, 45):
            punten4 = punten4 + 1
        # De - buttons punten er af    
        elif isMouseWithinSpace(800, 160, 45, 45):
            punten1 = punten1 - 1
            if punten1 < 0:
                punten1 = 0
        elif isMouseWithinSpace(800, 230, 45, 45):
            punten2 = punten2 - 1
            if punten2 < 0:
                punten2 = 0
        elif isMouseWithinSpace(800, 300, 45, 45):
            punten3 = punten3 - 1
            if punten3 < 0:
                punten3 = 0
        elif isMouseWithinSpace(800, 370, 45, 45):
            punten4 = punten4 - 1
            if punten4 < 0:
                punten4 = 0
    global DiceButtonClicked, side, QButtonClicked, PButtonClicked
    if isMouseWithinSpace(455, 500, 350, 125):
        if DiceButtonClicked == True:
            side = int(random(1, 7))
        DiceButtonClicked = not DiceButtonClicked
    if isMouseWithinSpace(75, 500, 350, 125):
        QButtonClicked = not QButtonClicked
    if isMouseWithinSpace(835, 500, 350, 125):
        if PButtonClicked == True:
            pechIndex = ['Sla een beurt over (niet vergeten!)', 'Vlieg terug naar het begin van het vorige continent', 'Geef een punt aan de volgende speler ', 'Je volgende worp is het aantal stappen dat je terug moet doen in plaats van naar voren', '2 punten van je score af', '1 punt van je score af']
            rand = int(random(6))
        PButtonClicked = not PButtonClicked
    else:
        pass
