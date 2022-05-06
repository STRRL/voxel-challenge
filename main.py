from scene import Scene
import taichi as ti
from taichi.math import *

# PLEASE DO NOT WRITE EVIL CODES LIKE WHAT I DO
# I HAVE NO IDEA ABOUT HOW TO COMPACT THESE LINES OF CODES
# see origin.py for the origin codes
COLOR_WHITE = vec3(1.0, 1.0, 1.0);
COLOR_BLACK = vec3(0.0, 0.0, 0.0);
COLOR_GRAY = vec3(0.2, 0.2, 0.2);
COLOR_PINK = vec3(170 / 255.0, 102 / 255.0, 170 / 255.0);
COLOR_MAGENTA = vec3(1.0, 0.2, 0.6);
COLOR_BLUSH = vec3(1.0, 0.2, 0.2);
COLOR_CREAM = vec3(1.0, 0.8, 0.4);
COLOR_RAINBOW_RED = vec3(231 / 255.0, 8 / 255.0, 15 / 255.0);
COLOR_RAINBOW_ORANGE = vec3(231 / 255.0, 145 / 255.0, 15 / 255.0);
COLOR_RAINBOW_YELLOW = vec3(231 / 255.0, 237 / 255.0, 15 / 255.0);
COLOR_RAINBOW_GREEN = vec3(47 / 255.0, 237 / 255.0, 15 / 255.0);
COLOR_RAINBOW_BLUE = vec3(2 / 255.0, 29 / 255.0, 244 / 255.0);
COLOR_RAINBOW_PURPLE = vec3(93 / 255.0, 54 / 255.0, 244 / 255.0);
scene = Scene();
scene.set_floor(-0.02, vec3(15 / 255.0, 77 / 255.0, 143 / 255.0))
scene.set_background_color(vec3(15 / 255.0, 77 / 255.0, 143 / 255.0));
scene.set_directional_light((1, 1, 1), 0.1, (0.8, 0.8, 0.8));

directives = [
    [12, 4, 2, 16, 13, COLOR_GRAY, 1], [15, 4, 2, 10, 1, COLOR_BLACK, 1], [13, 6, 2, 1, 1, COLOR_BLACK, 1],
    [25, 5, 2, 1, 1, COLOR_BLACK, 1], [26, 6, 2, 1, 1, COLOR_BLACK, 1], [14, 5, 2, 1, 1, COLOR_BLACK, 1],
    [12, 7, 2, 1, 5, COLOR_BLACK, 1], [13, 12, 2, 1, 4, COLOR_BLACK, 1], [14, 16, 2, 2, 1, COLOR_BLACK, 1],
    [16, 15, 2, 1, 1, COLOR_BLACK, 1], [17, 14, 2, 1, 1, COLOR_BLACK, 1], [18, 13, 2, 4, 1, COLOR_BLACK, 1],
    [22, 14, 2, 1, 1, COLOR_BLACK, 1], [23, 15, 2, 1, 1, COLOR_BLACK, 1], [24, 16, 2, 2, 1, COLOR_BLACK, 1],
    [26, 12, 2, 1, 4, COLOR_BLACK, 1], [27, 7, 2, 1, 5, COLOR_BLACK, 1], [12, 4, 2, 2, 2, COLOR_BLACK, 0],
    [26, 4, 2, 2, 2, COLOR_BLACK, 0], [12, 6, 2, 1, 1, COLOR_BLACK, 0], [14, 4, 2, 1, 1, COLOR_BLACK, 0],
    [27, 6, 2, 1, 1, COLOR_BLACK, 0], [25, 4, 2, 1, 1, COLOR_BLACK, 0], [12, 12, 2, 1, 5, COLOR_BLACK, 0],
    [13, 16, 2, 1, 1, COLOR_BLACK, 0], [27, 12, 2, 1, 5, COLOR_BLACK, 0], [26, 16, 2, 1, 1, COLOR_BLACK, 0],
    [26, 16, 2, 1, 1, COLOR_BLACK, 0], [16, 16, 2, 8, 1, COLOR_BLACK, 0], [17, 15, 2, 6, 1, COLOR_BLACK, 0],
    [18, 14, 2, 4, 1, COLOR_BLACK, 0], [17, 6, 2, 7, 1, COLOR_BLACK, 1], [17, 7, 2, 1, 1, COLOR_BLACK, 1],
    [20, 7, 2, 1, 1, COLOR_BLACK, 1], [23, 7, 2, 1, 1, COLOR_BLACK, 1], [16, 9, 2, 2, 1, COLOR_BLACK, 1],
    [16, 10, 2, 1, 1, COLOR_WHITE, 1], [17, 10, 2, 1, 1, COLOR_BLACK, 1], [23, 9, 2, 2, 1, COLOR_BLACK, 1],
    [23, 10, 2, 1, 1, COLOR_WHITE, 1], [24, 10, 2, 1, 1, COLOR_BLACK, 1], [21, 9, 2, 1, 1, COLOR_BLACK, 1],
    [14, 7, 2, 2, 2, COLOR_BLUSH, 1], [25, 7, 2, 2, 2, COLOR_BLUSH, 1], [0, 3, 0, 21, 18, COLOR_CREAM, 1],
    [0, 3, 0, 2, 2, COLOR_BLACK, 0], [0, 19, 0, 2, 2, COLOR_BLACK, 0], [19, 3, 0, 2, 2, COLOR_BLACK, 0],
    [19, 19, 0, 2, 2, COLOR_BLACK, 0], [0, 5, 0, 1, 14, COLOR_BLACK, 1], [20, 5, 0, 1, 14, COLOR_BLACK, 1],
    [2, 3, 0, 17, 1, COLOR_BLACK, 1], [2, 20, 0, 17, 1, COLOR_BLACK, 1], [1, 4, 0, 1, 1, COLOR_BLACK, 1],
    [19, 4, 0, 1, 1, COLOR_BLACK, 1], [1, 19, 0, 1, 1, COLOR_BLACK, 1], [19, 19, 0, 1, 1, COLOR_BLACK, 1],
    [2, 7, 1, 1, 10, COLOR_PINK, 1], [3, 6, 1, 1, 12, COLOR_PINK, 1], [4, 5, 1, 13, 14, COLOR_PINK, 1],
    [17, 6, 1, 1, 12, COLOR_PINK, 1], [18, 7, 1, 1, 10, COLOR_PINK, 1], [4, 6, 1, 1, 1, COLOR_MAGENTA, 1],
    [6, 7, 1, 1, 1, COLOR_MAGENTA, 1], [3, 9, 1, 1, 1, COLOR_MAGENTA, 1], [6, 9, 1, 1, 1, COLOR_MAGENTA, 1],
    [10, 8, 1, 1, 1, COLOR_MAGENTA, 1], [9, 11, 1, 1, 1, COLOR_MAGENTA, 1], [4, 16, 1, 1, 1, COLOR_MAGENTA, 1],
    [9, 17, 1, 1, 1, COLOR_MAGENTA, 1], [9, 13, 1, 1, 1, COLOR_MAGENTA, 1], [12, 17, 1, 1, 1, COLOR_MAGENTA, 1],
    [16, 15, 1, 1, 1, COLOR_MAGENTA, 1], [-3, 1, 1, 5, 4, COLOR_GRAY, 1], [-3, 1, 1, 4, 1, COLOR_BLACK, 1],
    [-3, 1, 1, 1, 3, COLOR_BLACK, 1], [1, 1, 1, 2, 2, COLOR_BLACK, 1], [-3, 4, 1, 5, 1, COLOR_BLACK, 1],
    [2, 2, 1, 1, 3, COLOR_BLACK, 1], [-3, 4, 1, 1, 1, COLOR_BLACK, 0], [2, 4, 1, 1, 1, COLOR_BLACK, 0],
    [2, 1, 1, 1, 1, COLOR_BLACK, 0], [4, 1, -1, 4, 3, COLOR_BLACK, 1], [5, 2, -1, 2, 1, COLOR_GRAY, 1],
    [13, 1, -1, 4, 3, COLOR_BLACK, 1], [14, 2, -1, 2, 1, COLOR_GRAY, 1], [13, 1, -1, 1, 1, COLOR_BLACK, 0],
    [18, 1, 1, 4, 3, COLOR_BLACK, 1], [19, 2, 1, 2, 1, COLOR_GRAY, 1], [18, 1, 1, 1, 1, COLOR_BLACK, 0],
    [21, 1, 1, 1, 1, COLOR_BLACK, 0], [-6, 11, -1, 4, 3, COLOR_BLACK, 1], [-5, 10, -1, 4, 3, COLOR_BLACK, 1],
    [-4, 9, -1, 4, 3, COLOR_BLACK, 1], [-3, 8, -1, 4, 3, COLOR_BLACK, 1], [-1, 7, -1, 4, 3, COLOR_BLACK, 1],
    [-5, 12, -1, 2, 1, COLOR_GRAY, 1], [-4, 11, -1, 2, 1, COLOR_GRAY, 1], [-3, 10, -1, 2, 1, COLOR_GRAY, 1],
    [-2, 9, -1, 2, 1, COLOR_GRAY, 1], [-3, 5, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1],
    [-3, 7, -2, 5, 2, COLOR_RAINBOW_BLUE, 1], [-3, 9, -2, 5, 2, COLOR_RAINBOW_GREEN, 1],
    [-3, 11, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1], [-3, 13, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1],
    [-3, 15, -2, 5, 2, COLOR_RAINBOW_RED, 1], [-8, 4, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1],
    [-8, 6, -2, 5, 2, COLOR_RAINBOW_BLUE, 1], [-8, 8, -2, 5, 2, COLOR_RAINBOW_GREEN, 1],
    [-8, 10, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1], [-8, 12, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1],
    [-8, 14, -2, 5, 2, COLOR_RAINBOW_RED, 1], [-13, 5, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1],
    [-13, 7, -2, 5, 2, COLOR_RAINBOW_BLUE, 1], [-13, 9, -2, 5, 2, COLOR_RAINBOW_GREEN, 1],
    [-13, 11, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1], [-13, 13, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1],
    [-13, 15, -2, 5, 2, COLOR_RAINBOW_RED, 1], [-18, 4, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1],
    [-18, 6, -2, 5, 2, COLOR_RAINBOW_BLUE, 1], [-18, 8, -2, 5, 2, COLOR_RAINBOW_GREEN, 1],
    [-18, 10, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1], [-18, 12, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1],
    [-18, 14, -2, 5, 2, COLOR_RAINBOW_RED, 1], [-23, 5, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1],
    [-23, 7, -2, 5, 2, COLOR_RAINBOW_BLUE, 1], [-23, 9, -2, 5, 2, COLOR_RAINBOW_GREEN, 1],
    [-23, 11, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1], [-23, 13, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1],
    [-23, 15, -2, 5, 2, COLOR_RAINBOW_RED, 1], [-28, 4, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1],
    [-28, 6, -2, 5, 2, COLOR_RAINBOW_BLUE, 1], [-28, 8, -2, 5, 2, COLOR_RAINBOW_GREEN, 1],
    [-28, 10, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1], [-28, 12, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1],
    [-28, 14, -2, 5, 2, COLOR_RAINBOW_RED, 1],
]


@ti.func
def draw_rect(left_bottom_x, left_bottom_y, base_z, width, height, color, material=1):
    for i in range(left_bottom_x, left_bottom_x + width):
        for j in range(left_bottom_y, left_bottom_y + height):
            scene.set_voxel(vec3(i, j, base_z), material, color)
    return


@ti.kernel
def initialize_voxels():
    ti.loop_config(serialize=True)
    for i in ti.static(range(136)):
        item = directives[i]
        draw_rect(item[0], item[1], item[2], item[3], item[4], item[5], item[6])


initialize_voxels()
scene.finish()
