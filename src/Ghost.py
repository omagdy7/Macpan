import pygame
import math
from Direction import DIRECTION
import map as Map

class Ghost():
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.last_move = 3
        self.speed = 3

    def heuristic(self, pacman_pos, next_pos):
        return abs(next_pos[0] - pacman_pos[0]) + abs(next_pos[1] - pacman_pos[1])




    # checks if the current position of pacman is either a dot, big dot or free
    def is_valid(self, maze, x, y):
        is_dot = maze[y][x] == Map.D
        is_big_dot = maze[y][x] == Map.BD
        is_free = maze[y][x] == 0
        return (is_dot or is_free or is_big_dot)


    # checks collision with pacman and obstacles returns false if there is a collision and true otherwise
    def check_collision(self, nx, ny, gx, gy, maze):
        direct_x = [1, 0, -1, 0, 1, 1, -1, -1]
        direct_y = [0, 1, 0, -1, -1, 1, -1, 1]


        for i in range(len(direct_x)):
            px = nx + direct_x[i] * 14
            py = ny + direct_y[i] * 14
            x = px // gx
            y = py // gy
            if not self.is_valid(maze, x, y):
                return False

        return True


    def get_next_move(self, pacman_pos, maze):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        ret = len(dx) * [math.inf]

        forbidden = 0

        if self.last_move == 0:
            forbidden = 2
        if self.last_move == 1:
            forbidden = 3
        if self.last_move == 2:
            forbidden = 0
        if self.last_move == 3:
            forbidden = 1

        
        for i in range(len(dx)):
            if i != forbidden:
                nx = self.x + dx[i] * self.speed
                ny = self.y + dy[i] * self.speed
                if self.check_collision(nx, ny, 30, 30, maze):
                    ret[i] = self.heuristic((nx, ny), pacman_pos)

        min_idx = ret.index(min(ret))
        return min_idx







    def move(self, maze, player_pos):
        min_idx = self.get_next_move(player_pos, maze)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        new_dx = dx[min_idx] * self.speed
        new_dy = dy[min_idx] * self.speed
        self.x += new_dx
        self.y += new_dy
        self.last_move = min_idx

    def draw(self, screen):
        radius = 30 // 2
        pos = (self.x , self.y)
        pygame.draw.circle(screen, self.color, pos, radius)


