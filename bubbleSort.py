import pygame, sys, time, random

from pygame.locals import*
pygame.init()

W = 600 
H = 600
DISPLAY = pygame.display.set_mode( (W, H) )
pygame.display.set_caption( "Visualising insertion sort" )
WHITE = ( 255, 255, 255 )
CYAN = ( 0, 255, 255 )
GREEN = ( 0, 255, 0 )
BLUE = ( 0, 0, 255 )
running = True
A = []
A = [0 for x in range( 200 )]
for x in range( 200 ):
    A[x] = x
random.shuffle( A )

def showSet( A ):
    x = W/2 - (len( A )/2)*2
    for a in A :
        pygame.draw.line(DISPLAY, WHITE, (x, 600), (x, 600-a*2.5), 2 )
        pygame.display.update()
        x += 2
    DISPLAY.fill((0, 0, 0))

def showCount( count ):
    font = pygame.font.Font( "UbuntuMono-Bold.ttf", 26 )
    text = font.render( "Bubble Sort took " + str(count) + " steps to complete", True, GREEN, BLUE )
    textRect = text.get_rect()
    textRect.center = ( W//2, H//2 )
    DISPLAY.fill( (0, 0, 0) )
    DISPLAY.blit( text, textRect )
    pygame.display.update()
    time.sleep( 5 )

def swap( A, I ):
    temp = A[I]
    A[I] = A[I-1]
    A[I-1] = temp

def bubbleSort( A ):
    count = 0 
    while True :
        didSort = False
        for i in range( 1, len( A ), 1 ):
            if( A[i] < A[i-1] ):
                swap( A, i )
                didSort = True
            count += 1
        if didSort == False:
            break
        showSet( A )
    time.sleep( 2 )
    print( count )
    showCount( count )
    pygame.quit()
    sys.exit()

while( running ):
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    showSet( A )
    bubbleSort( A )