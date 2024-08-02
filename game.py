import pygame as pyg

# Initialize pygame
pyg.init()

# Screen size
size = (800, 600)

# Create the screen and change the color with the Fill function
screen = pyg.display.set_mode(size)
screen.fill(pyg.Color(255, 255, 0))

drawing = False
# Start a loop that will run forever since we don't want to game to stop unless it is forced to
while True:
    # check for events
    for event in pyg.event.get():
        if (event.type == pyg.MOUSEBUTTONDOWN):
            drawing = True
        if (event.type == pyg.MOUSEBUTTONUP):
            drawing = False
        if event.type == pyg.KEYDOWN:
            if (event.key == pyg.K_e):
                screen.fill(pyg.Color(255, 255, 0))
        if (event.type == pyg.QUIT):
            pyg.quit() 
    if drawing: 
            # Set variables that we will use when drawing a circle
        mouse_position = pyg.mouse.get_pos()
        circle_thickness = 5
            # Draw the circle
        pyg.draw.circle(screen, pyg.Color(0, 0, 0), mouse_position, circle_thickness)
    pyg.display.update()