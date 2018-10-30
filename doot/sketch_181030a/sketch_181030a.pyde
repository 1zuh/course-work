page = 0
def setup():
    size (640, 480)
    background(0)
    global images0, images1, images2, images3, images4, images5, images6
    images0 = loadImage("frame_00_delay-0.2s.gif")
    images1 = loadImage("frame_02_delay-0.15s.gif")
    images2 = loadImage("frame_04_delay-0.15s.gif")
    images3 = loadImage("frame_05_delay-0.15s.gif")
    images4 = loadImage("frame_06_delay-0.25s.gif")
    images5 = loadImage("frame_05_delay-0.15s.gif")
    images6 = loadImage("frame_06_delay-0.25s.gif")
    
def draw():
    if page == 6:
        image(images0, 50, 50, 320, 240)
    if page == 12:
        image(images1, 50, 50, 320, 240)
    if page == 18:
        image(images2, 50, 50, 320, 240)
    if page == 24:
        image(images3, 50, 50, 320, 240)
    if page == 30:
        image(images4, 50, 50, 320, 240)
    if page == 36:
        image(images5, 50, 50, 320, 240)
    if page == 42:
        image(images6, 50, 50, 320, 240)
    if page == 48:
        image(images5, 50, 50, 320, 240)
def mousePressed():  # Triggers once per mouse-press
    global page
    page += 1
    if page == 49:
        page = 0

        
