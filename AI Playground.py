import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set the window size
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up the perspective and camera
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Function to draw a simple cube (this will represent an item like a sword)
def draw_cube():
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1),
    )
    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    run_game = True

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # Rotate the scene to give it some motion
        glRotatef(1, 3, 1, 1)  # Rotate 1 degree around the x, y, and z axes

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw a cube to represent a forged item
        draw_cube()

        # Update the screen
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        clock.tick(60)

    pygame.quit()

# Start the game loop
game_loop()