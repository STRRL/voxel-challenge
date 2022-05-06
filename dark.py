from scene import Scene
import taichi as ti
from taichi.math import *
# nyaacat with dark theme
# PLEASE TO NOT WRITE EVIL CODES LIKE WHAT I DO
# I HAVE NO IDEA ABOUT HOW TO COMPACT THESE LINES OF CODES
COLOR_WHITE = vec3(1.0, 1.0, 1.0);COLOR_BLACK = vec3(0.0, 0.0, 0.0);
COLOR_GRAY = vec3(0.2, 0.2, 0.2);COLOR_PINK = vec3(170 / 255.0, 102 / 255.0, 170 / 255.0);
COLOR_MAGENTA = vec3(1.0, 0.2, 0.6);COLOR_BLUSH = vec3(1.0, 0.2, 0.2);
COLOR_CREAM = vec3(1.0, 0.8, 0.4);COLOR_RAINBOW_RED = vec3(231 / 255.0, 8 / 255.0, 15 / 255.0);
COLOR_RAINBOW_ORANGE = vec3(231 / 255.0, 145 / 255.0, 15 / 255.0);
COLOR_RAINBOW_YELLOW = vec3(231 / 255.0, 237 / 255.0, 15 / 255.0);
COLOR_RAINBOW_GREEN = vec3(47 / 255.0, 237 / 255.0, 15 / 255.0);
COLOR_RAINBOW_BLUE = vec3(2 / 255.0, 29 / 255.0, 244 / 255.0);
COLOR_RAINBOW_PURPLE = vec3(93 / 255.0, 54 / 255.0, 244 / 255.0);
scene = Scene();scene.set_floor(-0.02, vec3(15 / 255.0, 77 / 255.0, 143 / 255.0))
scene.set_background_color(vec3(15 / 255.0, 77 / 255.0, 143 / 255.0));
@ti.func
def draw_rect(left_bottom_x, left_bottom_y, base_z, width, height, color, material=1):
    for i in range(left_bottom_x, left_bottom_x + width):
        for j in range(left_bottom_y, left_bottom_y + height):
            scene.set_voxel(vec3(i, j, base_z), material, color)
    return
@ti.kernel
def initialize_voxels():
    draw_rect(12, 4, 2, 16, 13, COLOR_GRAY, 1);draw_rect(15, 4, 2, 10, 1, COLOR_BLACK, 1);
    draw_rect(13, 6, 2, 1, 1, COLOR_BLACK, 1);draw_rect(25, 5, 2, 1, 1, COLOR_BLACK, 1);
    draw_rect(26, 6, 2, 1, 1, COLOR_BLACK, 1);draw_rect(14, 5, 2, 1, 1, COLOR_BLACK, 1);
    draw_rect(12, 7, 2, 1, 5, COLOR_BLACK, 1);draw_rect(13, 12, 2, 1, 4, COLOR_BLACK, 1);
    draw_rect(14, 16, 2, 2, 1, COLOR_BLACK, 1);draw_rect(16, 15, 2, 1, 1, COLOR_BLACK, 1);
    draw_rect(17, 14, 2, 1, 1, COLOR_BLACK, 1);draw_rect(18, 13, 2, 4, 1, COLOR_BLACK, 1);
    draw_rect(22, 14, 2, 1, 1, COLOR_BLACK, 1);draw_rect(23, 15, 2, 1, 1, COLOR_BLACK, 1);
    draw_rect(24, 16, 2, 2, 1, COLOR_BLACK, 1);draw_rect(26, 12, 2, 1, 4, COLOR_BLACK, 1);
    draw_rect(27, 7, 2, 1, 5, COLOR_BLACK, 1);draw_rect(12, 4, 2, 2, 2, COLOR_BLACK, 0);
    draw_rect(26, 4, 2, 2, 2, COLOR_BLACK, 0);draw_rect(12, 6, 2, 1, 1, COLOR_BLACK, 0);
    draw_rect(14, 4, 2, 1, 1, COLOR_BLACK, 0);draw_rect(27, 6, 2, 1, 1, COLOR_BLACK, 0);
    draw_rect(25, 4, 2, 1, 1, COLOR_BLACK, 0);draw_rect(12, 12, 2, 1, 5, COLOR_BLACK, 0);
    draw_rect(13, 16, 2, 1, 1, COLOR_BLACK, 0);draw_rect(27, 12, 2, 1, 5, COLOR_BLACK, 0);
    draw_rect(26, 16, 2, 1, 1, COLOR_BLACK, 0);draw_rect(26, 16, 2, 1, 1, COLOR_BLACK, 0);
    draw_rect(16, 16, 2, 8, 1, COLOR_BLACK, 0);draw_rect(17, 15, 2, 6, 1, COLOR_BLACK, 0);
    draw_rect(18, 14, 2, 4, 1, COLOR_BLACK, 0);draw_rect(17, 6, 2, 7, 1, COLOR_BLACK, 1);
    draw_rect(17, 7, 2, 1, 1, COLOR_BLACK, 1);draw_rect(20, 7, 2, 1, 1, COLOR_BLACK, 1);
    draw_rect(23, 7, 2, 1, 1, COLOR_BLACK, 1);draw_rect(16, 9, 2, 2, 1, COLOR_BLACK, 1);
    draw_rect(16, 10, 2, 1, 1, COLOR_WHITE, 1);draw_rect(17, 10, 2, 1, 1, COLOR_BLACK, 1);
    draw_rect(23, 9, 2, 2, 1, COLOR_BLACK, 1);draw_rect(23, 10, 2, 1, 1, COLOR_WHITE, 1);
    draw_rect(24, 10, 2, 1, 1, COLOR_BLACK, 1);draw_rect(21, 9, 2, 1, 1, COLOR_BLACK, 1);
    draw_rect(14, 7, 2, 2, 2, COLOR_BLUSH, 1);draw_rect(25, 7, 2, 2, 2, COLOR_BLUSH, 1);
    draw_rect(0, 3, 0, 21, 18, COLOR_CREAM, 1);draw_rect(0, 3, 0, 2, 2, COLOR_BLACK, 0);
    draw_rect(0, 19, 0, 2, 2, COLOR_BLACK, 0);draw_rect(19, 3, 0, 2, 2, COLOR_BLACK, 0);
    draw_rect(19, 19, 0, 2, 2, COLOR_BLACK, 0);draw_rect(0, 5, 0, 1, 14, COLOR_BLACK, 1);
    draw_rect(20, 5, 0, 1, 14, COLOR_BLACK, 1);draw_rect(2, 3, 0, 17, 1, COLOR_BLACK, 1);
    draw_rect(2, 20, 0, 17, 1, COLOR_BLACK, 1);draw_rect(1, 4, 0, 1, 1, COLOR_BLACK, 1);
    draw_rect(19, 4, 0, 1, 1, COLOR_BLACK, 1);draw_rect(1, 19, 0, 1, 1, COLOR_BLACK, 1);
    draw_rect(19, 19, 0, 1, 1, COLOR_BLACK, 1);draw_rect(2, 7, 1, 1, 10, COLOR_PINK, 1);
    draw_rect(3, 6, 1, 1, 12, COLOR_PINK, 1);draw_rect(4, 5, 1, 13, 14, COLOR_PINK, 1);
    draw_rect(17, 6, 1, 1, 12, COLOR_PINK, 1);draw_rect(18, 7, 1, 1, 10, COLOR_PINK, 1);
    draw_rect(4, 6, 1, 1, 1, COLOR_MAGENTA, 1);draw_rect(6, 7, 1, 1, 1, COLOR_MAGENTA, 1);
    draw_rect(3, 9, 1, 1, 1, COLOR_MAGENTA, 1);draw_rect(6, 9, 1, 1, 1, COLOR_MAGENTA, 1);
    draw_rect(10, 8, 1, 1, 1, COLOR_MAGENTA, 1);draw_rect(9, 11, 1, 1, 1, COLOR_MAGENTA, 1);
    draw_rect(4, 16, 1, 1, 1, COLOR_MAGENTA, 1);draw_rect(9, 17, 1, 1, 1, COLOR_MAGENTA, 1);
    draw_rect(9, 13, 1, 1, 1, COLOR_MAGENTA, 1);draw_rect(12, 17, 1, 1, 1, COLOR_MAGENTA, 1);
    draw_rect(16, 15, 1, 1, 1, COLOR_MAGENTA, 1);draw_rect(-3, 1, 1, 5, 4, COLOR_GRAY, 1);
    draw_rect(-3, 1, 1, 4, 1, COLOR_BLACK, 1);draw_rect(-3, 1, 1, 1, 3, COLOR_BLACK, 1);
    draw_rect(1, 1, 1, 2, 2, COLOR_BLACK, 1);draw_rect(-3, 4, 1, 5, 1, COLOR_BLACK, 1);
    draw_rect(2, 2, 1, 1, 3, COLOR_BLACK, 1);draw_rect(-3, 4, 1, 1, 1, COLOR_BLACK, 0);
    draw_rect(2, 4, 1, 1, 1, COLOR_BLACK, 0);draw_rect(2, 1, 1, 1, 1, COLOR_BLACK, 0);
    draw_rect(4, 1, -1, 4, 3, COLOR_BLACK, 1);draw_rect(5, 2, -1, 2, 1, COLOR_GRAY, 1);
    draw_rect(13, 1, -1, 4, 3, COLOR_BLACK, 1);draw_rect(14, 2, -1, 2, 1, COLOR_GRAY, 1);
    draw_rect(13, 1, -1, 1, 1, COLOR_BLACK, 0);draw_rect(18, 1, 1, 4, 3, COLOR_BLACK, 1);
    draw_rect(19, 2, 1, 2, 1, COLOR_GRAY, 1);draw_rect(18, 1, 1, 1, 1, COLOR_BLACK, 0);
    draw_rect(21, 1, 1, 1, 1, COLOR_BLACK, 0); draw_rect(-6, 11, -1, 4, 3, COLOR_BLACK, 1);
    draw_rect(-5, 10, -1, 4, 3, COLOR_BLACK, 1); draw_rect(-4, 9, -1, 4, 3, COLOR_BLACK, 1);
    draw_rect(-3, 8, -1, 4, 3, COLOR_BLACK, 1);draw_rect(-1, 7, -1, 4, 3, COLOR_BLACK, 1);
    draw_rect(-5, 12, -1, 2, 1, COLOR_GRAY, 1);    draw_rect(-4, 11, -1, 2, 1, COLOR_GRAY, 1);
    draw_rect(-3, 10, -1, 2, 1, COLOR_GRAY, 1);    draw_rect(-2, 9, -1, 2, 1, COLOR_GRAY, 1);
    draw_rect(-3, 5, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1);    draw_rect(-3, 7, -2, 5, 2, COLOR_RAINBOW_BLUE, 1);
    draw_rect(-3, 9, -2, 5, 2, COLOR_RAINBOW_GREEN, 1);    draw_rect(-3, 11, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1);
    draw_rect(-3, 13, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1);    draw_rect(-3, 15, -2, 5, 2, COLOR_RAINBOW_RED, 1);
    draw_rect(-8, 4, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1);    draw_rect(-8, 6, -2, 5, 2, COLOR_RAINBOW_BLUE, 1);
    draw_rect(-8, 8, -2, 5, 2, COLOR_RAINBOW_GREEN, 1);    draw_rect(-8, 10, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1);
    draw_rect(-8, 12, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1);    draw_rect(-8, 14, -2, 5, 2, COLOR_RAINBOW_RED, 1);
    draw_rect(-13, 5, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1);    draw_rect(-13, 7, -2, 5, 2, COLOR_RAINBOW_BLUE, 1);
    draw_rect(-13, 9, -2, 5, 2, COLOR_RAINBOW_GREEN, 1);    draw_rect(-13, 11, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1);
    draw_rect(-13, 13, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1);    draw_rect(-13, 15, -2, 5, 2, COLOR_RAINBOW_RED, 1);
    draw_rect(-18, 4, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1);    draw_rect(-18, 6, -2, 5, 2, COLOR_RAINBOW_BLUE, 1);
    draw_rect(-18, 8, -2, 5, 2, COLOR_RAINBOW_GREEN, 1);    draw_rect(-18, 10, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1);
    draw_rect(-18, 12, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1);    draw_rect(-18, 14, -2, 5, 2, COLOR_RAINBOW_RED, 1);
    draw_rect(-23, 5, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1);    draw_rect(-23, 7, -2, 5, 2, COLOR_RAINBOW_BLUE, 1);
    draw_rect(-23, 9, -2, 5, 2, COLOR_RAINBOW_GREEN, 1);    draw_rect(-23, 11, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1);
    draw_rect(-23, 13, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1);    draw_rect(-23, 15, -2, 5, 2, COLOR_RAINBOW_RED, 1);
    draw_rect(-28, 4, -2, 5, 2, COLOR_RAINBOW_PURPLE, 1);    draw_rect(-28, 6, -2, 5, 2, COLOR_RAINBOW_BLUE, 1);
    draw_rect(-28, 8, -2, 5, 2, COLOR_RAINBOW_GREEN, 1);    draw_rect(-28, 10, -2, 5, 2, COLOR_RAINBOW_YELLOW, 1);
    draw_rect(-28, 12, -2, 5, 2, COLOR_RAINBOW_ORANGE, 1);    draw_rect(-28, 14, -2, 5, 2, COLOR_RAINBOW_RED, 1);
    return
initialize_voxels()
scene.finish()
