import pygame
import random
import math
#游戏的初始化
pygame.init()#初始化pygame包
screen = pygame.display.set_mode((400,600))#设置窗口大小，参数为元组
pygame.display.set_caption("Beat that Monster！")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)#设置图标
bgImage = pygame.image.load('background.png')#设置背景图
#添加背景音效
pygame.mixer.init()
pygame.mixer.music.load('bg.mp3')
pygame.mixer.music.play(-1)
#添加击中音效
bombSound = pygame.mixer.Sound('explode.mp3')

#飞机参数
number_of_enemies = 5 #敌人数量
hitDistance = 20 #子弹杀伤范围
#分数
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
def show_score():
    text = f"Score: {score}"
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))
#敌人类
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.x = random.randint(100, 300)
        self.y = random.randint(100, 300)
        self.step = random.randint(1, 4)
    def reset(self):#被射中时恢复原始位置
        self.x =  random.randint(100, 300)
        self.y = random.randint(100, 300)
enemies = []
score = 0
#游戏结束
is_over = False
#子弹类
class Bullet():


    def __init__(self):
        self.img = pygame.image.load('bullet_true.png')
        self.x = player_X+65#子弹位置
        self.y = player_Y+10
        self.step = 10#子弹移动速度\
    def hit(self):
        global score


        for e in enemies:
            if (distance(self.x, self.y, e.x+23, e.y+23)) < hitDistance:
                    #射中
                screen.blit(bombImage, (e.x, e.y))
                bombSound.play()
                score = score +1
                bullets.remove(self)
                e.reset()
bullets = []
for i in range(number_of_enemies):
    enemies.append(Enemy())
planeImage = pygame.image.load('player.png')#设置飞机
player_X = 130
player_Y = 450
playerStep = 0
playerVertical = 0
#敌人参数
enemyImage = pygame.image.load('enemy.png')
enemyStep = 2 #敌人移动速度
enemy_X = random.randint(100, 300)
enemy_Y = random.randint(100, 300)
gameSpeed = 20
#爆炸
bombImage = pygame.image.load('boom_true.png')
#显示敌人
def show_enemy():
    global enemyStep, is_over
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 343 or e.x < 0:
            e.step = e.step * -1
            e.y += gameSpeed
        if player_Y+142 > e.y and player_Y < e.y +57 and e.x+57 > player_X and e.x < player_X+102:
            is_over = True
            enemies.clear()

#显示子弹
def show_bullets():
    b = Bullet()
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()  # 看是否击中目标敌人
        b.y -= b.step
    if b.y < 0:
        bullets.remove(b)
is_over = False
font_2 = pygame.font.Font("freesansbold.ttf", 16)
def check_is_over():
    if is_over:
        text = f"The game is over,  your total score is: {score}"
        score_render = font_2.render(text, True, (255, 0, 0))
        screen.blit(score_render, (50, 200))

def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    c = math.sqrt(a * a + b * b)
    return c


#游戏主循环
running = True
while running:

    screen.blit(bgImage, (0, 0))#画出背景图
    show_score()#显示分数
    screen.blit(planeImage, (player_X, player_Y))
    #通过键盘事件控制飞机移动
    for event in pygame.event.get(): #反馈所有的用户界面操作
        if event.type == pygame.QUIT: #QUIT是pygame包里面的退出常量
            running = False
        if event.type == pygame.KEYDOWN:#（事件类型）键盘按下任意一个键
            if event.key == pygame.K_RIGHT:
                playerStep = 3
            elif event.key == pygame.K_LEFT:
                playerStep = -3
            elif event.key == pygame.K_SPACE: #空格键发射子弹
                bullets.append(Bullet())
            if event.key == pygame.K_UP:
                playerVertical = -3
            elif event.key == pygame.K_DOWN:
                playerVertical = 3
        if event.type == pygame.KEYUP:#抬起键，飞机不动
            playerStep = 0
            playerVertical = 0
    player_X += playerStep
    player_Y += playerVertical
    #防止飞机出界
    if player_X > 214:
        player_X = 214
    if player_X < 0:
        player_X = 0#横坐标范围
    if player_Y < 0:
        player_Y = 0
    if player_Y > 466:
        player_Y = 466
    show_enemy()
    show_bullets()
    check_is_over()
    pygame.display.update()#界面更新