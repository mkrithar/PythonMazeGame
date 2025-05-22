import pygame

pygame.init() #ξεκιναει το εργοστασιο pygame
screen = pygame.display.set_mode((1000 , 800)) #φτιαχνει παραθυρο screen με διαστασεις
done = False #μεταβλητη false
x1=30
y1=30
x2=890
y2=30
while done == False: #οσο το done ειναι false to game παιζει
    for event in pygame.event.get():  #ενεργοποιησου μολις ο παιχτησ κανει event
        if event.type == pygame.QUIT: #αν ο παιχτησ πατησει esc,x
            done = True #stops for while and also the game
    pressed = pygame.key.get_pressed()  # Φτιάχνει μεταβλητή pressed που παίρνει σαν τιμή το πλήκτρο που πατήσαμε
    if pressed[pygame.K_UP]: y1 -= 3  # Αν πατιέται το ΠΑΝΩ βέλος, άλλαξε το Υ κατά -3
    if pressed[pygame.K_DOWN]: y1 += 3  # Αν πατιέται το ΚΑΤΩ βέλος
    if pressed[pygame.K_LEFT]: x1 -= 3  # Αν πατιέται το ΑΡΙΣΤΕΡΟ βέλος
    if pressed[pygame.K_RIGHT]: x1 += 3  # Αν πατιέται το ΔΕΞΙ βέλος

    if pressed[pygame.K_w]: y2 -= 3
    if pressed[pygame.K_s]: y2 += 3
    if pressed[pygame.K_a]: x2 -= 3
    if pressed[pygame.K_d]: x2 += 3
    screen.fill((0,0,0))
    Font = pygame.font.SysFont("comicsansms", 60, True)
    Title1 = Font.render("FAST MAZE", True, (255, 255, 255))
    screen.blit(Title1, (25, 550))

    Font = pygame.font.SysFont("comicsansms", 20, True)
    Title2 = Font.render("By NestoStrike", True, (255, 255, 255))
    screen.blit(Title2, (237, 625))

    player1 = pygame.draw.rect(screen,(221,187,45),pygame.Rect(x1,y1,60,60))
    player2 = pygame.draw.rect(screen, (0, 128, 225), pygame.Rect(x2, y2,60,60))
    player3 = pygame.draw.rect(screen, (10, 187, 45), pygame.Rect(500, 30, 60, 60))
    if player1.bottom > screen.get_rect().bottom:
        y1 -= 3
    if player1.top < screen.get_rect().top:
        y1 += 3
    if player1.left > screen.get_rect().left:
        x1 -= 3
    if player1.right < screen.get_rect().right:
        x1 += 3
    if player2.bottom > screen.get_rect().bottom:
        y2 -= 3
    if player2.top < screen.get_rect().top:
        y2 += 3
    if player2.left > screen.get_rect().left:
        x2 -= 3
    if player2.right < screen.get_rect().right:
        x2 += 3
    w1 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(700, 0, 60, 600))
    w2 = pygame.draw.rect(screen, (10, 244, 177), pygame.Rect(400, 400, 60, 600))
    w3 = pygame.draw.rect(screen,(200,179,50),pygame.Rect(470,100,40,600))
    w4 = pygame.draw.rect(screen,(200,59,60),pygame.Rect(200,0,70, 300))
    if player1.colliderect(player2):
        x1 = 30
        y1 = 30
        x2 = 890
        y2 = 30
    if player1.colliderect(player3):
        x1 = 30
        y1 = 30
    if player2.colliderect(player3):
        x2 = 890
        y2 = 30
    if player1.colliderect(w1) or player1.colliderect(w2) or player1.colliderect(w3) or player1.colliderect(w4)  :
        if pressed[pygame.K_UP]: y1 += 3
        if pressed[pygame.K_DOWN]: y1 -= 3
        if pressed[pygame.K_LEFT]: x1 += 3
        if pressed[pygame.K_RIGHT]: x1 -= 3
    if player2.colliderect(w1) or player2.colliderect(w2) or player2.colliderect(w3) or player2.colliderect(w4)  :
        if pressed[pygame.K_w]: y2 += 3
        if pressed[pygame.K_s]: y2 -= 3
        if pressed[pygame.K_a]: x2 += 3
        if pressed[pygame.K_d]: x2 -= 3

    pygame.display.flip() #τελευταια εντολη ΠΑΝΤΑ , εξaiτιασ τησ βλεπουμε το window

