import pygame as pyg

# Screen size
size = (500, 400)

# Create the screen and change the color with the Fill function
screen = pyg.display.set_mode(size)
screen.fill(pyg.Color(255, 255, 0, 50))

# Initialize pygame
pyg.init()

# Start a loop that will run forever since we don't want to game to stop unless it is forced to
while True:
    # check for events
    for event in pyg.event.get():
        if (event == pyg.MOUSEBUTTONDOWN):
            # Set variables that we will use when drawing a circle
            mouse_position = pyg.mouse.get_pos()
            circle_thickness = 5
            border_thickness = 7
            screen.fill(pyg.Color(255, 255, 0, 50))

            # Draw the circle
            pyg.draw.circle(screen, (0, 0, 0), mouse_position, circle_thickness, border_thickness)