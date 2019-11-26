def setup():
    global rectSize, circleSize, rectColor, rectHighlight, circleColor, circleHighlight, baseColor, currentColor, circleX, circleY, rectX, rectY
    size(1280, 700)
    rectSize = 90
    circleSize = 93
    rectColor = color(0)
    rectHighlight = color(51)
    circleColor = color(255)
    circleHighlight = color(204)
    baseColor = color(102)
    currentColor = baseColor
    circleX = width/2+circleSize/2+10
    circleY = height/2
    rectX = width/2-rectSize-10
    rectY = height/2-rectSize/2
    ellipseMode(CENTER)

def draw():
    global mouseX, mouseY, currentColor, rectOver, rectColor, circleHighlight, circleOver
    update(mouseX, mouseY)
    background(currentColor)
    #rect(30, 30, 150, 75, 7)
    #rect(width / 2 - 150 / 2, height / 7 * 5, 75, 75, 7)

    textAlign(CENTER)
    textSize(40)
    text("De Grote Wereld Quiz", width / 2, height / 5)
    textSize(35)

    fill(255, 255, 255, 255)
    rect(width / 2 - 350 / 2, height / 7 * 5, 350, 125, 7)
    fill(0, 0, 0, 255)
    text("Afsluiten", width / 2, height / 7 * 5 + 125 / 2 + 10)

    fill(255, 255, 255, 255)
    rect(width / 2 - 350 / 2, height / 7 * 3, 350, 125, 7)
    fill(0, 0, 0, 255)
    text("Spel Starten", width / 2, height / 7 * 3 + 125 / 2 + 10)

    if rectOver:
        fill(rectHighlight)
    else:
        fill(rectColor)
    stroke(255)
    #rect(rectX, rectY, rectSize, rectSize)

    if circleOver:
        fill(circleHighlight)
    else:
        fill(circleColor)
    stroke(0)
    #ellipse(circleX, circleY, circleSize, circleSize)

def update(x, y):
    global circleX, circleY, circleSize, circleOver, rectOver
    if(overCircle(circleX, circleY, circleSize)):
        circleOver = True
        rectOver = False
    elif(overRect(rectX, rectY, rectSize, rectSize)):
        rectOver = True
        circleOver = False
    else:
        circleOver = rectOver = False

def mousePressed():
    if(circleOver):
        currentColor = circleColor
    if(rectOver):
        currentColor = rectColor
        exit()

def overRect(x, y, width, height):
    if(mouseX >= x and mouseX <= x+width and mouseY >= y and mouseY <= y+height):
        return True
    else:
        return False

def overCircle(x, y, diameter):
    disX = x - mouseX
    disY = y - mouseY
    if(sqrt(sq(disX) + sq(disY)) < diameter/2):
        return True
    else:
        return False
