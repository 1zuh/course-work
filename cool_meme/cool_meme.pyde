page = 0
x = 50
y = color(155, 3, 255)
framecount = 0
def setup():
    size (300, 300)
    frameRate (60)
    global d, d1, d2, d3, d4, d5, d6
    d = loadImage("00.gif")
    d1 = loadImage("01.gif")
    d2 = loadImage("02.gif")
    d3 = loadImage("03.gif")
    d4 = loadImage("04.gif")
    d5 = loadImage("05.gif")
    d6 = loadImage("06.gif")
def draw():
    global x, y, page, framecount
    framecount = frameCount % 50
    if page == 0:
        text("doot doot", width/2 + 40, height/2 + 40)
        text("""if you see this pyde file while checking
for completion""", 20, 20)
        text("""you have been visited by mr skeletal 
good bones and calcium will come to you
but only if you print to console
"thank mr skeletal' """, 20, 240)
        y = color(155, 3, 255)
    elif page == 1:
        text("doot doot", width/2 + 40, height/2 + 40)
        text("""if you see this pyde file while checking
for completion""", 20, 20)
        text("""you have been visited by mr skeletal 
good bones and calcium will come to you
but only if you print to console
"thank mr skeletal' """, 20, 240)
        y = color(255, 255, 0)
    elif page == 2:
        text("doot doot", width/2 + 40, height/2 + 40)
        text("""if you see this pyde file while
checking for completion""", 20, 20)
        text("""you have been visited by mr skeletal 
good bones and calcium will come to you
but only if you print to console
"thank mr skeletal' """, 20, 240)
        y = color(255, 0, 3)
    if framecount == 5:
        background (y)
        image (d, x, x, 209, 190)
    if framecount == 10:
        background (y)
        image (d1, x, x, 209, 190)
    if framecount == 15:
        background (y)
        image (d2, x, x, 209, 190)
    if framecount == 20:
        background (y)
        image (d3, x, x, 209, 190)
    if framecount == 25:
        background (y)
        image (d4, x, x, 209, 190)
    if framecount == 30:
        background (y)
        image (d5, x, x, 209, 190)
    if framecount == 35:
        background (y)
        image (d6, x, x, 209, 190)
    if framecount == 40:
        background (y)
        image (d5, x, x, 209, 190)
    if framecount == 45:
        background (y)
        image (d6, x, x, 209, 190)
    if framecount == 50:
        background (y)
        image (d5, x, x, 209, 190)
        #for z in range(0, 24, 3):
        #z += 1 #images are called d1, d2, d3, etc. 
        # # the way this for loop is intended to work is by
        # # abusing the naming scheme of the images to 
        # # print "d", then the value of z as a string.
        # background(0)
        # image("d" + str(z), x, y, 209, 190)
def keyPressed():
    global page
    page += 1
    if page == 3:
        page = 0
