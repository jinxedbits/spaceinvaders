import pygame, random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

player = {'size': 50, 'pos': [400, 550], 'speed': 20}
enemies = [
    {
        'pos': [i, 50], 
        'fire_time': 0, 
        'fire_delay': random.randint(1000, 3000)
    } 
    for i in range(150, 650, 200)
]
bullets = [None] * len(enemies)

def update_game():
    global running
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    player['pos'][0] += (
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        * player['speed'])
    player['pos'][0] = max(
        0, 
        min(800 - player['size'], 
            player['pos'][0]
        )
    )

    for enemy in enemies: 
        pygame.draw.rect(
            screen, 
            (255, 0, 0), 
            (*enemy['pos'], 50, 50)
        )
    pygame.draw.rect(
        screen, 
        (255, 255, 255), 
        (*player['pos'], 
         player['size'], 
         player['size'])
    )

    current_time = pygame.time.get_ticks()
    for i, enemy in enumerate(enemies):
        if bullets[i] is None and (
            current_time - enemy['fire_time'] >= enemy['fire_delay']):
            bullets[i] = [
                enemy['pos'][0] + 22, enemy['pos'][1] + 50
            ]
            enemy['fire_time'], enemy['fire_delay'] = (
                current_time, random.randint(1000, 3000)
            )
        if bullets[i]:
            bullets[i][1] += 10
            pygame.draw.rect(screen, (255, 0, 0), (*bullets[i], 5, 20))
            if (player['pos'][0] < bullets[i][0] < player['pos'][0] + 50 
                and player['pos'][1] < bullets[i][1] < player['pos'][1] + 50):
                running = False
            elif bullets[i][1] > 600:
                bullets[i] = None  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update_game()
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
