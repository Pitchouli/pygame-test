# import the pygame module, so you can use it
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of <HORIZONTAL> x <VERTICAL>
    screen = pygame.display.set_mode((240,180))
     
    # define a variable to control the main loop
    running = True
    
	# Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
	# Parameters: surface, color, center point, radius
    pygame.draw.circle(screen, (0, 0, 255), (90, 120), 20)
	
    # Update the window, because I guess that's not built-in
    pygame.display.flip()
	
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
	 
	 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()