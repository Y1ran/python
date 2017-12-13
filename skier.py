import pygame, sys, random                # 所需要加载的模块

skier_images = ["skier_down.png","skier_right1.png",  #加载所需要的人物图像
               "skier_right2.png","skier_left2.png",
               "skier_left1.png"]

class SkierClass(pygame.sprite.Sprite):
 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png") # 获取人物图像
        self.rect = self.image.get_rect() # 获取人物形象
        self.rect.center = [320,100]  # 人物的起始位置
        self.angle = 0
        
    def turn(self, direction):     # 方向
        self.angle = self.angle + direction   # 角度+ 方向
        if self.angle < -2:  self.angle = -2  # 向左右只允许转2次
        if self.angle >  2:  self.angle =  2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 10 - abs(self.angle) * 2]  #左右移动后的速度    
        return speed

    def move(self, speed):   #  移动  左右移动
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:   self.rect.centerx = 20   #向左移动至 起始位置20 或向右移动至终止位置620
        if self.rect.centerx > 620:  self.rect.centerx = 620  

class ObstacleClass (pygame.sprite.Sprite):             #创建树和小旗
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)  
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False
                   
    def scroll(self, terrainPos):
        self.rect.centery = self.location[1] - terrainPos  # 让场景向上移动

def create_map(start, end):   # 创建一个“画面”地形：640×640.使用的64×64像素的“块”，这样的对象不是靠得太近
    obstacles = pygame.sprite.Group()
    locations = []
    gates = pygame.sprite.Group()
    for i in range(10):                 # 每屏10障碍
        row = random.randint(start, end)
        col = random.randint(0, 9)
        location  = [col * 64+20, row * 64+20]# 中心的x，y的障碍
        if not (location in locations):        # 避免在同一个地方2的障碍
            locations.append(location)
            type = random.choice(["tree", "flag"])
            if type == "tree": img = "skier_tree.png"   # 定义调用树的图
            elif type == "flag":  img = "skier_flag.png"  # 定义调用旗的图
            obstacle = ObstacleClass(img, location, type)  
            obstacles.add(obstacle)
    return obstacles


def animate():              # 重绘屏幕，包括所有的元素
    screen.fill([255, 255, 255])   #屏幕填充色
    pygame.display.update(obstacles.draw(screen))  # 显示更新障碍
    screen.blit(skier.image, skier.rect) #滑雪者图像
    screen.blit(score_text, [10, 10])   # 比例
    pygame.display.flip()  #显示屏转动

def updateObstacleGroup(map0, map1):
    obstacles = pygame.sprite.Group()
    for ob in map0:  obstacles.add(ob)   #添加障碍
    for ob in map1:  obstacles.add(ob)   #添加障碍
    return obstacles

pygame.init()      # 初始化示例
screen = pygame.display.set_mode([640,640])  # 初始化显示状态
clock = pygame.time.Clock()  # 初始化时间
skier = SkierClass()  # 初始化类型
speed = [0, 6]   #初始化速度
map_position = 0
points = 0
map0 = create_map(20, 29)    # 创建地图1
map1 = create_map(10, 19)    # 创建地图2
activeMap = 0     # 激活地图
obstacles = updateObstacleGroup(map0, map1)  #地图分数
font = pygame.font.Font(None, 50)   #  所有障碍做碰撞检测

while True:           #  开始地图循环
    clock.tick(30)    #  每秒更新地图的次数
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:          # 检查按键
            if event.key == pygame.K_LEFT:        # 左箭头向左转
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:     # 右箭头向右转
                speed = skier.turn(1)
    skier.move(speed)         # 移动滑雪者
    map_position += speed[1]                      # 滚动场景
    
    # 管理地图之间进行切换，并在底部创建新的地形
    if map_position >=640 and activeMap == 0:   
        activeMap = 1
        map0 = create_map(20, 29)              # 创建地图
        obstacles = updateObstacleGroup(map0, map1)  # 更新地图障碍
    if map_position >=1280 and activeMap == 1:                        
        activeMap = 0
        for ob in map0:
            ob.location[1] = ob.location[1] - 1280   # 环绕顶部
        map_position = map_position - 1280           # 地图位置
        map1 = create_map(10, 19)                    # 创建地图
        obstacles = updateObstacleGroup(map0, map1)
    
    for obstacle in obstacles:
        obstacle.scroll(map_position)


    # 检查是否碰到数或小旗
    hit =  pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:  #撞到树  
            points = points - 100                       # 撞树后扣掉100分
            skier.image = pygame.image.load("skier_crash.png")  # 创建跌倒图
            animate()  
            pygame.time.delay(100)
            skier.image = pygame.image.load("skier_down.png")  # 恢复滑雪图
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:   # 撞到旗子标志
            points += 100                    # 撞旗后加100分
            obstacles.remove(hit[0])                    # 删除旗子标志
    
    score_text = font.render("Score: " +str(points), 1, (0, 0, 0))
    animate()
   


