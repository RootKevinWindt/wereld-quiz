add_library('controlP5')

def setup():
    size(1280, 700)
    font = createFont("arrial", 20)
    global cp5
    cp5 = ControlP5(this)

    speler1 = cp5.addTextfield("Speler 1").setPosition(20, 30).setSize(
        200, 40).setFont(font).setFocus(True).setColor(color(240, 240, 240))

    speler2 = cp5.addTextfield("Speler 2").setPosition(20, 120).setSize(
        200, 40).setFont(font).setFocus(True).setColor(color(240, 240, 240))

    speler3 = cp5.addTextfield("Speler 3").setPosition(20, 210).setSize(
        200, 40).setFont(font).setFocus(True).setColor(color(240, 240, 240))
    
    speler4 = cp5.addTextfield("Speler 4").setPosition(20, 300).setSize(
        200, 40).setFont(font).setFocus(True).setColor(color(240, 240, 240))
  
def draw():
    background(200)
    fill(200)
    text(cp5.get(Textfield, "Speler 1").getText(), 360, 130)
    text(cp5.get(Textfield, "Speler 2").getText(), 360, 180)
    text(cp5.get(Textfield, "Speler 2").getText(), 360, 230)
    text(cp5.get(Textfield, "Speler 2").getText(), 360, 280)
