from Utils import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.width = 50
        self.height = 25
        self.stillAlive = True

        self.angle = 90
        self.moveAngle = 90
        self.radians = 0
        self.cosR = 0
        self.sinR = 1

        self.velocity = 0
        self.maxVelocity = 7
        self.acceleration = 0.7
        self.drag = 0.1

        self.vec = np.array([0, 1])

        # self.trailPoints = []
        self.carPoints = []


        self.og_image = pygame.transform.smoothscale(pygame.image.load("Assets/car.png").convert_alpha(), (self.width, self.height))
        self.image = pygame.transform.rotate(self.og_image, self.angle)
        self.rect = pygame.surface.Surface.get_rect(self.image)
        self.rect = self.image.get_rect(center=self.rect.center)



        self.rect.x = 180
        self.rect.y = 840

        self.x = self.rect.x
        self.y = self.rect.y

        self.RAY_MAX_MAG = WIDTH*2
        self.rays = []
        self.draw_raycast = False



    def rotate(self, right, left):
        rotationSpeed = 3
        if right:
            self.angle -= rotationSpeed
            self.angle = self.angle % 360
        elif left:
            self.angle += rotationSpeed
            self.angle = self.angle % 360


        # Rotates Image with anchor point on center
        self.image = pygame.transform.rotate(self.og_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        self.x = self.rect.x
        self.y = self.rect.y



    def draw(self):
        surface.blit(self.image, self.rect)
        pygame.draw.circle(surface, (255, 255, 255), self.rect.center, 5)

    def moveF(self):
        self.moveAngle = self.angle

        self.radians = self.moveAngle * math.pi / 180
        self.cosR = math.cos(self.radians)
        self.sinR = math.sin(self.radians)

        self.velocity += self.acceleration
        self.vec = np.array([self.cosR, self.sinR])

        # Adds player location to trail array
        # self.trailPoints.append(self.rect.center)

    def moveB(self):
        self.moveAngle = self.angle

        self.radians = self.moveAngle * math.pi / 180
        self.cosR = math.cos(self.radians)
        self.sinR = math.sin(self.radians)

        self.velocity -= self.acceleration
        self.vec = np.array([self.cosR, self.sinR])

        # Adds player location to trail array
        # self.trailPoints.append(self.rect.center)

    # def drawTrail(self):
    #     if len(self.trailPoints) >= 2:
    #         pygame.draw.aalines(surface, (30, 237, 19), False, self.trailPoints, 1)

    def calcSpeed(self):
        if self.velocity > 0:
            self.velocity -= self.drag
            self.velocity = min(self.maxVelocity, self.velocity)
        if self.velocity < 0:
            self.velocity += self.drag
            self.velocity = max(-(self.maxVelocity/2), self.velocity)

        self.x += self.velocity * self.vec[0]
        self.y += (-self.velocity) * self.vec[1]

        self.rect.x = self.x
        self.rect.y = self.y



    def rotatePoints(self):
        radians = self.angle * math.pi / 180
        rightRadians = (self.angle + 90) * math.pi / 180
        offsetX = self.rect.center[0]
        offsetY = self.rect.center[1]

        '''
            Offsets the points of the car such that the first point is at 0, 0
            then rotates X2,Y2 based on angle
            then X3, Y3 are calculated based on X2 Y2 
        '''

        x1 = 0
        y1 = 0

        x2 = math.cos(radians) * self.width
        y2 = -math.sin(radians) * self.width

        x3 = (x2 - self.height * math.cos(rightRadians))
        y3 = (y2 + self.height * math.sin(rightRadians))

        x4 = -self.height*math.cos(rightRadians)
        y4 = self.height*math.sin(rightRadians)

        '''
            Finds center of all 4 points, and offsets the car to the
            position its supposed to be
            We gonna use these points to calculate collisions
        '''

        centerX = (x1+x2+x3+x4)/4
        centerY = (y1+y2+y3+y4)/4

        x_1 = x1-(centerX - offsetX)
        x_2 = x2-(centerX - offsetX)
        x_3 = x3-(centerX - offsetX)
        x_4 = x4-(centerX - offsetX)

        y_1 = y1-(centerY - offsetY)
        y_2 = y2-(centerY - offsetY)
        y_3 = y3-(centerY - offsetY)
        y_4 = y4-(centerY - offsetY)

        self.carPoints = [(x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4)]

        center_X = (x_1 + x_2 + x_3 + x_4) / 4
        center_Y = (y_1 + y_2 + y_3 + y_4) / 4


        # Uncomment this to draw points connected
        # pygame.draw.lines(surface, (255, 255, 255), True, self.carPoints)


    def hitWall(self):

        carLine1 = self.carPoints[0][0], self.carPoints[0][1], self.carPoints[1][0], self.carPoints[1][1]
        carline2 = self.carPoints[1][0], self.carPoints[1][1], self.carPoints[2][0], self.carPoints[2][1]
        carline3 = self.carPoints[2][0], self.carPoints[2][1], self.carPoints[3][0], self.carPoints[3][1]
        carline4 = self.carPoints[3][0], self.carPoints[3][1], self.carPoints[0][0], self.carPoints[0][1]

        for wall in WALLS:
            if linesCollided(carLine1[0], carLine1[1], carLine1[2], carLine1[3], wall.x1, wall.y1, wall.x2, wall.y2):
                self.stillAlive = False
        for wall in WALLS:
            if linesCollided(carline2[0], carline2[1], carline2[2], carline2[3], wall.x1, wall.y1, wall.x2, wall.y2):
                self.stillAlive = False
        for wall in WALLS:
            if linesCollided(carline3[0], carline3[1], carline3[2], carline3[3], wall.x1, wall.y1, wall.x2, wall.y2):
                self.stillAlive = False
        for wall in WALLS:
            if linesCollided(carline4[0], carline4[1], carline4[2], carline4[3], wall.x1, wall.y1, wall.x2, wall.y2):
                self.stillAlive = False

        if self.stillAlive is False:
            self.x = 180
            self.y = 840
            self.rect.x = 180
            self.rect.y = 840
            self.angle = 90
            self.moveAngle = 90
            self.velocity = 0
            self.image = pygame.transform.rotate(self.og_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.stillAlive = True
            return True




    # Takes a player as an argument
    # I don't even remember how the fuck I made this code
    def calcRaycast(self):
        radians = self.angle * math.pi / 180
        RAY_MAG = WIDTH * 4
        points = []

        start_x1 = self.carPoints[1][0]
        start_y1 = self.carPoints[1][1]
        start_x3 = self.carPoints[2][0]
        start_y3 = self.carPoints[2][1]
        start_x2 = (start_x1 + start_x3) / 2
        start_y2 = (start_y1 + start_y3) / 2
        start_x4 = start_x1
        start_y4 = start_y1
        start_x5 = start_x3
        start_y5 = start_y3

        end_x1 = (math.sin(radians + 135 * math.pi / 180) * RAY_MAG) + start_x1
        end_y1 = (math.cos(radians + 135 * math.pi / 180) * RAY_MAG) + start_y1
        end_x2 = (math.sin(radians + 90 * math.pi / 180) * RAY_MAG) + start_x2
        end_y2 = (math.cos(radians + 90 * math.pi / 180) * RAY_MAG) + start_y2
        end_x3 = (math.sin(radians + 45 * math.pi / 180) * RAY_MAG) + start_x3
        end_y3 = (math.cos(radians + 45 * math.pi / 180) * RAY_MAG) + start_y3
        end_x4 = (math.sin(radians + 180 * math.pi / 180) * RAY_MAG) + start_x4
        end_y4 = (math.cos(radians + 180 * math.pi / 180) * RAY_MAG) + start_y4
        end_x5 = (math.sin(radians) * RAY_MAG) + start_x5
        end_y5 = (math.cos(radians) * RAY_MAG) + start_y5

        points.append([(start_x1, start_y1), (end_x1, end_y1)])
        points.append([(start_x2, start_y2), (end_x2, end_y2)])
        points.append([(start_x3, start_y3), (end_x3, end_y3)])
        points.append([(start_x4, start_y4), (end_x4, end_y4)])
        points.append([(start_x5, start_y5), (end_x5, end_y5)])

        # For each vision ray, calculate collision point for all walls then choose the closest one
        # IDK how this code works anymore
        # Was a nightmare to write this

        rayMagnitude_old_C = self.RAY_MAX_MAG
        old_C = 0, 0
        self.rays = []
        for x, point in enumerate(points):
            old_C = point[1][0], point[1][1]
            rayMagnitude_old_C = WIDTH * 2
            for wall in WALLS:
                # Get collision point from ray to a wall
                c = getCollisionPoint(point[0][0], point[0][1], point[1][0], point[1][1], wall.x1, wall.y1, wall.x2,
                                      wall.y2)
                if c is not None:
                    rayMagnitude_C = math.sqrt((c[0] - point[0][0]) ** 2 + (c[1] - point[0][1]) ** 2)
                    if rayMagnitude_C < rayMagnitude_old_C:
                        old_C = c
                        rayMagnitude_old_C = rayMagnitude_C

            self.rays.append(math.sqrt((old_C[0] - point[0][0]) ** 2 + (old_C[1] - point[0][1]) ** 2))

            if self.draw_raycast:
                pygame.draw.line(surface, 0, (point[0][0], point[0][1]), (old_C[0], old_C[1]), 1)
                pygame.draw.circle(surface, 0, (old_C[0], old_C[1]), 8)

    def drawWinner(self):
        self.og_image = pygame.transform.smoothscale(pygame.image.load("Assets/carGreen.png").convert_alpha(),
                                                     (self.width, self.height))

    def drawNormal(self):
        self.og_image = pygame.transform.smoothscale(pygame.image.load("Assets/car.png").convert_alpha(),
                                                     (self.width, self.height))

