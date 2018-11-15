def setup():
    size (300, 300)
    frameRate (60)
    global d, d1, d2, d3, d4, d5, d6
    global page, colour
    d = loadImage("00.gif")
    d1 = loadImage("01.gif")
    d2 = loadImage("02.gif")
    d3 = loadImage("03.gif")
    d4 = loadImage("04.gif")
    d5 = loadImage("05.gif")
    d6 = loadImage("06.gif")
    page = 1
    colour = color(0)
    
def draw():
    meme_text()
    animation()
    change()

def meme_text():
    text("""if you see this pyde file while checking
for completion""", 20, 20)
    text("""you have been visited by mr skeletal 
good bones and calcium will come to you
but only if you comment "thank mr skeletal' """, 20, 240)

def change():
    global colour
    if page == 0:
        colour = color(155, 3, 255)
    elif page == 1:
        colour = color(0, 255, 255)
    elif page == 2:
        colour = color(255, 0, 3)
def animation():
    global colour    
    framecount = frameCount % 50
    if framecount == 5:
        background (colour)
        image (d, 50, 50, 209, 190)
    if framecount == 10:
        background (colour)
        image (d1, 50, 50, 209, 190)
    if framecount == 15:
        background (colour)
        image (d2, 60, 60, 209, 190)
    if framecount == 20:
        background (colour)
        image (d3, 66, 66, 209, 190)
    if framecount == 25:
        background (colour)
        image (d4, 70, 70, 209, 190)
    if framecount == 30:
        background (colour)
        image (d5, 66, 66, 209, 190)
    if framecount == 35:
        background (colour)
        image (d6, 60, 60, 209, 190)
    if framecount == 40:
        background (colour)
        image (d5, 50, 50, 209, 190)
    if framecount == 45:
        background (colour)
        image (d6, 33, 33, 209, 190)
    if framecount == 50:
        background (colour)
        image (d5, 45, 45, 209, 190)    

def keyPressed():
    global page
    page += 1
    if page == 3:
        page = 0
