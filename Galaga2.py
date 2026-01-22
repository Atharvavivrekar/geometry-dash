import pgzrun
import random, pyautogui
#screen dimensions
#WIDTH = 1200
#HEIGHT = 600
WIDTH, HEIGHT = pyautogui.size()
HEIGHT = HEIGHT - 100
WIDTH = WIDTH - 100
print(WIDTH, HEIGHT)
#definiting colours
WHITE = (255,255,255)
BLUE = (0,0,255)

#create a ship
ship = Actor('wave')
bug = Actor('spike')

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 20

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

def create_enemies():
    enemies.append(Actor('spike'))
    #now the enemies will be ina straight line
    enemies[-1].x = random.randint(50,WIDTH - 50)
    #starting off the screen thats why putting it at -100,
    #slowly the enemy will come down
    enemies[-1].y = -100
lives = 3
gamestate = "start"
score = 0
direction = 1
ship.dead = False
ship.countdown = 90

def game_over():
    screen.draw.text("Game_over",(250,300))

#for updating the score
def displayScore():
    screen.draw.text("score:" + str(score), (50,30))
    screen.draw.text("lives:" + str(lives), (50,80))
def on_key_down(key):
    global gamestate
    if key == keys.SPACE and gamestate == "start":
        gamestate = "play"
    if key == keys.SPACE and gamestate == "play":
        bullets.append(Actor('bullet'))
        #the last bullet added , set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50


def update():
    global score
    global direction, gamestate, lives
    #move the ship left or right with arrow keys
    if gamestate == "play":
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0

        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH

        for bullet in bullets:
            if bullet.y <=0 :
                bullets.remove(bullet)
            else:
                bullet.y -= 10

        for enemy in enemies:
            enemy.y += 5

            if enemy.y >= HEIGHT:
                enemies.remove(enemy)
            if enemy.colliderect(ship):
                enemies.remove(enemy)
                lives = lives - 1
                if lives == 0:
                    gamestate = "over"


            for bullet in bullets :
                if enemy.colliderect(bullet):
                    score +=100

                    bullets.remove(bullet)

                    enemies.remove(enemy)
        if len(enemies) == 0:
            game_over()


def draw():
    screen.clear()
    #screen.fill(BLUE)
    screen.blit('geometrydash.png',(0,0))
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    ship.draw()
    displayScore()
    if gamestate == "start":
        screen.draw.text("Press SPACE to Start", center=(WIDTH//2, HEIGHT//2))
    elif gamestate == "over":
        screen.draw.text("Game Over", center=(WIDTH//2, HEIGHT//2))


clock.schedule_interval(create_enemies, 2.0)
pgzrun.go()# Write your code here :-)