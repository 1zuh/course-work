# while loop
# increase a variable
# use draw() for an animation

x = 1
z = 640
def setup():
    size (640, 480)
    background(148, 0, 211)
    noStroke()
    fill (255, 0, 0)
    rect (0, 0, 640, 80)
    fill (255, 165, 0)
    rect (0, 80, 640, 80)
    fill (255, 255, 0)
    rect (0, 160, 640, 80)
    fill (0, 255, 0)
    rect (0, 240, 640, 80)
    fill (0, 0, 255)
    rect (0, 320, 640, 80)
    
def draw():
    global x 
    x += 3
    if x >= 640:
        x = 0
    background(148, 0, 211)
    noStroke()
    fill (255, 0, 0)
    rect (0, 0, 640, 80)
    fill (255, 165, 0)
    rect (0, 80, 640, 80)
    fill (255, 255, 0)
    rect (0, 160, 640, 80)
    fill (0, 255, 0)
    rect (0, 240, 640, 80)
    fill (0, 0, 255)
    rect (0, 320, 640, 80)
    fill (148, 20, 0)
    ellipse (x, width/2, 30, 30)
    print (x)
