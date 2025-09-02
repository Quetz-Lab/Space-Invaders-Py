import math
import pygame
import random

#init pygame

pygame.init()

#set Window

screen = pygame.display.set_mode((600,400))
running = True;

#Window settings
pygame.display.set_caption("Space Invaders")

#LoadFont
font = pygame.font.Font('arial.ttf' , 32)

def showScore(x,y):
	textScore = font.render("Score: "+str(Score),True,(255,255,255))
	screen.blit(textScore,(x,y))

#Player value

playerX = 300
playerPosY = 350
playerSpeed = 0
Size = 25

#ScoreValue
Score = 0

#EnemyValues
numOfEnemies = 6
enemyX = []
enemyY = []
enemySpeed = []
for i in range(numOfEnemies):
	enemyX.append(random.randint(0,575))
	enemyY.append(random.randint(0,575))
	enemySpeed.append(0.1)
	



#bulletValues

bulletPosX = 0
bulletPosY = 400
bulletSpeed = 0.1
bulletState = "ready"

#Change Pos Bullet

def fireBullet(x,y):
	global bulletState #Variables Global accesible desde cualquier lugar
	bulletState = "fire"
	pygame.draw.circle(screen,(255,0,255),(x,y),5)

#EnemyConstruct
def Enemy(x,y,size):
	enemy = pygame.Rect(x,y,size,size)
	pygame.draw.rect(screen,(255,0,0), enemy)


#PlayerConstruct
def Player(x,y,size):
	player=pygame.Rect(x,y,size,size)
	pygame.draw.rect(screen,(255,255,255), player)

#CollisionConstruct
def IsCollision(enemyX,enemyY,bulletX,bulletY):
	distance = math.sqrt(math.pow((enemyX - bulletX),2) + math.pow((enemyY - bulletY),2))

	if distance < 30:
		
		return True
	else:
		return False



#game Loop
while running:
	screen.fill((150,75,100))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerSpeed = -0.1
				print ("Left")
			if event.key == pygame.K_RIGHT:
				playerSpeed = 0.1
				print ("Right")
			if event.key == pygame.K_SPACE:
				if bulletState is "ready":
					bulletPosY = playerPosY
					bulletPosX = playerX+12
					fireBullet(bulletPosX, bulletPosY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerSpeed = 0
				print ("stop")

	#pyshics 2
	#MovePlayer
	playerX+=playerSpeed
	#MoveEnemy
	# for i in range(numOfEnemies):
	# 	enemyX[i] += enemySpeed[i]
	# 	getDist = IsCollision(enemyX[i], enemyY[i], bulletPosY, bulletPosX)
	# 	if getDist == True:
	# 		enemyY[i] += 1
		#enemyY[i] += enemySpeed[i]
		#check borders
	if playerX <= 0:
		playerX = 0
	elif playerX >= 575:
		playerX = 575

	for i in range(numOfEnemies):

		getDist = IsCollision(enemyX[i], enemyY[i], bulletPosX, bulletPosY)
		if getDist == True:
		
			print ("Enemy: Te voy a picotear eh")
			print("isCollision")

			enemyX[i] = random.randint(0,575)
			enemyY[i] = random.randint(0,275)
		
		else:
			print("isNot")
			Enemy(enemyX[i],enemyY[i],Size)
		#bullet Check borders
	if bulletPosY <= 0:
		bulletPosY = 400
		bulletState = "ready"

		#Render 3
	if bulletState is "fire":
		fireBullet(bulletPosX, bulletPosY)
		bulletPosY -=bulletSpeed

	Player(playerX,playerPosY,Size)
	showScore(100,50)
	pygame.display.update()
	