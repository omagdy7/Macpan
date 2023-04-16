from typing import List
import pygame
import math
from Direction import DIRECTION
import map as Map
import random

class Ghost():
    def __init__(self):
        self.x = 75
        self.y = 75
        self.tx = 0
        self.ty = 0
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

        # print(f"nx: {nx}, ny: {ny}")
        # print()

        # print(maze[3][13], self.is_valid(maze, 13, 3))
        print()
        if nx == 391 and ny == 79:
            print("----------------------")

        for i in range(len(direct_x)):
            px = nx + direct_x[i] * 14
            py = ny + direct_y[i] * 14
            print(px, py)
            x = px // gx
            y = py // gy
            # print(f"x: {x}, y: {y} is_valid({x}, {y}) = {self.is_valid(maze, x, y)}")
            if not self.is_valid(maze, x, y):
                return False

        return True

    def get_possible_moves(self, maze):
        possible_directions = {}

        up    = (0, -self.speed)
        down  = (0, self.speed)
        right = (self.speed, 0)
        left  = (-self.speed, 0)

        if self.check_collision(up[0], up[1], 30, 30, maze):
            possible_directions[up] = DIRECTION.UP
        if self.check_collision(down[0], down[1], 30, 30, maze):
            possible_directions[down] = DIRECTION.DOWN
        if self.check_collision(right[0], right[1], 30, 30, maze):
            possible_directions[right] = DIRECTION.RIGHT
        if self.check_collision(left[0], left[1], 30, 30, maze):
            possible_directions[left] = DIRECTION.LEFT

        return possible_directions
        

    # def get_next_move(self, pacman_pos, maze):
    #     possible_directions = self.get_possible_moves(maze)
    #
    #     next_move = DIRECTION.RIGHT
    #     mn = 1000000 # really big number
    #
    #     for pos, dir in possible_directions.items():
    #         h = self.heuristic(pacman_pos, pos)
    #         if h < mn:
    #             mn = h
    #             print("dir: ", dir)
    #             next_move = dir
    #
    #     print("Min h:", mn)
    #     # print("Left: ", self.heuristic(pacman_pos))
    #     print("Best: next_move", next_move)
    #     return next_move


    def get_next_move(self, pacman_pos, maze):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]


        ret = len(dx) * [math.inf]
        
        for i in range(len(dx)):
            nx = self.x + dx[i] * self.speed
            ny = self.y + dy[i] * self.speed
            if self.check_collision(nx, ny, 30, 30, maze):
                ret[i] = self.heuristic((nx, ny), pacman_pos)


        min_idx = ret.index(min(ret))
        # if min_idx == 1:
        #     print(f"({self.x}, {self.y})")
        #     print(self.check_collision(391, 79, 30, 30, maze))
        return (dx[min_idx] * self.speed, dy[min_idx] * self.speed)







    def move(self, maze, player_pos):
        next_move = self.get_next_move(player_pos, maze)

        dx = 0
        dy = 0

        self.x += next_move[0]
        self.y += next_move[1]

        # if next_move == DIRECTION.UP:
        #     self.ty = -self.speed
        #     self.tx = 0
        # elif next_move == DIRECTION.DOWN:
        #     self.ty = self.speed
        #     self.tx = 0
        # elif next_move == DIRECTION.RIGHT:
        #     self.tx = self.speed
        #     self.ty = 0
        # elif next_move == DIRECTION.LEFT:
        #     self.tx = -self.speed
        #     self.ty = 0
        #
        #
        # if self.check_collision(self.tx, self.ty, 30, 30, maze):
        #     dx = self.tx
        #     dy = self.ty
        #
        # if dx < 0:
        #     self.direction = DIRECTION.LEFT
        # elif dx > 0:
        #     self.direction = DIRECTION.RIGHT
        # elif dy < 0:
        #     self.direction = DIRECTION.UP
        # elif dy > 0:
        #     self.direction = DIRECTION.DOWN
        #
        # if self.check_collision(dx, dy, 30, 30, maze):
        #     self.x += dx
        #     self.y += dy

    def draw(self, screen):
        radius = 30 // 2
        pos = (self.x , self.y)
        pygame.draw.circle(screen, 'green', pos, radius)


