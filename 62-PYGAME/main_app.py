import pygame;

#init
pygame.init()
#variable running game
isRun = True

#membuat display surface object
window = pygame.display.set_mode((500,500))

#object game
x=250
y=250

#ukuran
panjang = 20
lebar = 20

#kecepatan gerak
speed = 10

while isRun:
    pygame.time.delay(10)
    
    #user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun=False

        #ambil semua keyboard pressed
        keys = pygame.key.get_pressed()

        #ambil kekiri
        if keys[pygame.K_LEFT] and x>0:
            x-= speed

        #ambil kekanan
        if keys[pygame.K_RIGHT] and x<500-lebar:
            x+= speed

        #ambil ke atas
        if keys[pygame.K_UP] and y>0:
            y-= speed

        #ambil kebawah
        if keys[pygame.K_DOWN] and y<500-panjang:
            y+= speed

    #update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))
    #render ke display
    pygame.display.update()

pygame.quit()


