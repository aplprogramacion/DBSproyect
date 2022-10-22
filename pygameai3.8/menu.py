import pygame
import nuevoproyecto
screen_width = 700
screen_height = 350
BLANCO = (255, 255, 255)
ventana = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("boton prueba")

start_img = pygame.image.load("play.png").convert()
start_img.set_colorkey(BLANCO)
exit_img = pygame.image.load("exit.png").convert()
exit_img.set_colorkey(BLANCO)
options_img = pygame.image.load("options.png").convert()
options_img.set_colorkey(BLANCO)
resume_img = pygame.image.load("resume.png").convert()
resume_img.set_colorkey(BLANCO)

class FondoPantalla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fondoimagen = pygame.image.load("fondo menu700x350.jpg")
        self.fondoy = 0
        self.fondox = 0

    def render(self):
        ventana.blit(self.fondoimagen, (self.fondox, self.fondoy))

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action



fondo = FondoPantalla()
start_button = Button(0, 10, start_img, 1)
exit_button = Button(630, 10, exit_img, 1)
options_button = Button(330, 10, options_img, 1)
resume_button = Button(330, 50, resume_img, 1)
class Menu:
    run = True
    while run:

        ventana.fill((0, 0, 0))
        fondo.render()

        if start_button.draw(ventana):
            run = False
        if exit_button.draw(ventana):
            run = False
            pygame.quit()
        if options_button.draw(ventana):
            pass
        if resume_button.draw(ventana):
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()
    pygame.quit()
Menu()