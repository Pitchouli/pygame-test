# import the pygame module, so you can use it
import pygame

# Code I found that adds button functionality
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))
     
    # define a variable to control the main loop
    running = True
    
	# Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
	# Parameters: surface, color, center point, radius
    pygame.draw.circle(screen, (0, 0, 255), (90, 120), 20)
	
	# Add the button at the bottom
            button("test",150,450,100,50,green,bright_green,buttontest)
	
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