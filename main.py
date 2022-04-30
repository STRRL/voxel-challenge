from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene()
# scene.set_floor(-0.05, vec3(1, 1, 1))
scene.set_background_color((1, 1, 1))
scene.set_directional_light((1, 1, 1), 0.1, (0.8, 0.8, 0.8))

# 0f4d8f
COLOR_BACKGROUND = vec3(15 / 255.0, 77 / 255.0, 143 / 255.0)
# ffffff
COLOR_WHITE = vec3(1.0, 1.0, 1.0)
# 000000
COLOR_BLACK = vec3(0.0, 0.0, 0.0)
# 333333
COLOR_GRAY = vec3(0.2, 0.2, 0.2)
# aa66aa
COLOR_PINK = vec3(170 / 255.0, 102 / 255.0, 170 / 255.0)
# ff3399
COLOR_MAGENTA = vec3(1.0, 0.2, 0.6)
# ff3333
COLOR_BLUSH = vec3(1.0, 0.2, 0.2)
# ffcc66
COLOR_CREAM = vec3(1.0, 0.8, 0.4)


@ti.kernel
def initialize_voxels():
    draw_nyaa_cat()
    return


@ti.func
def draw_nyaa_cat():
    cat_head(12, 4, 2)
    cat_body(0, 3, 0)
    cat_legs(0, 3, 0)
    cat_tail(0, 3, 0)
    return


@ti.func
def cat_head(base_x, base_y, base_z: int):
    # base
    draw_rect(base_x + 0, base_y + 0, base_z, 16, 13, COLOR_GRAY, 1)
    # border
    draw_rect(base_x + 3, base_y, base_z, 10, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 1, base_y + 2, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 13, base_y + 1, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 14, base_y + 2, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 2, base_y + 1, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 0, base_y + 3, base_z, 1, 5, COLOR_BLACK, 1)
    draw_rect(base_x + 1, base_y + 8, base_z, 1, 4, COLOR_BLACK, 1)
    draw_rect(base_x + 2, base_y + 12, base_z, 2, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 4, base_y + 11, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 5, base_y + 10, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 6, base_y + 9, base_z, 4, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 10, base_y + 10, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 11, base_y + 11, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 12, base_y + 12, base_z, 2, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 14, base_y + 8, base_z, 1, 4, COLOR_BLACK, 1)
    draw_rect(base_x + 15, base_y + 3, base_z, 1, 5, COLOR_BLACK, 1)
    # prune
    draw_rect(base_x + 0, base_y + 0, base_z, 2, 2, COLOR_BLACK, 0)
    draw_rect(base_x + 14, base_y + 0, base_z, 2, 2, COLOR_BLACK, 0)
    draw_rect(base_x + 0, base_y + 2, base_z, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 2, base_y + 0, base_z, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 15, base_y + 2, base_z, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 13, base_y + 0, base_z, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 0, base_y + 8, base_z, 1, 5, COLOR_BLACK, 0)
    draw_rect(base_x + 1, base_y + 12, base_z, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 15, base_y + 8, base_z, 1, 5, COLOR_BLACK, 0)
    draw_rect(base_x + 14, base_y + 12, base_z, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 14, base_y + 12, base_z, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 4, base_y + 12, base_z, 8, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 5, base_y + 11, base_z, 6, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 6, base_y + 10, base_z, 4, 1, COLOR_BLACK, 0)
    # mouth
    draw_rect(base_x + 5, base_y + 2, base_z, 7, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 5, base_y + 3, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 8, base_y + 3, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 11, base_y + 3, base_z, 1, 1, COLOR_BLACK, 1)
    # eye
    draw_rect(base_x + 4, base_y + 5, base_z, 2, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 4, base_y + 6, base_z, 1, 1, COLOR_WHITE, 1)
    draw_rect(base_x + 5, base_y + 6, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 11, base_y + 5, base_z, 2, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 11, base_y + 6, base_z, 1, 1, COLOR_WHITE, 1)
    draw_rect(base_x + 12, base_y + 6, base_z, 1, 1, COLOR_BLACK, 1)
    # nose
    draw_rect(base_x + 9, base_y + 5, base_z, 1, 1, COLOR_BLACK, 1)
    # blush
    draw_rect(base_x + 2, base_y + 3, base_z, 2, 2, COLOR_BLUSH, 1)
    draw_rect(base_x + 13, base_y + 3, base_z, 2, 2, COLOR_BLUSH, 1)
    return


@ti.func
def cat_body(base_x, base_y, base_z: int):
    # base
    draw_rect(base_x + 0, base_y + 0, base_z, 21, 18, COLOR_CREAM, 1)
    # prune corner
    draw_rect(base_x + 0, base_y + 0, base_z, 2, 2, COLOR_BLACK, 0)
    draw_rect(base_x + 0, base_y + 16, base_z, 2, 2, COLOR_BLACK, 0)
    draw_rect(base_x + 19, base_y + 0, base_z, 2, 2, COLOR_BLACK, 0)
    draw_rect(base_x + 19, base_y + 16, base_z, 2, 2, COLOR_BLACK, 0)
    # border
    draw_rect(base_x + 0, base_y + 2, base_z, 1, 14, COLOR_BLACK, 1)
    draw_rect(base_x + 20, base_y + 2, base_z, 1, 14, COLOR_BLACK, 1)
    draw_rect(base_x + 2, base_y + 0, base_z, 17, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 2, base_y + 17, base_z, 17, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 1, base_y + 1, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 19, base_y + 1, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 1, base_y + 16, base_z, 1, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 19, base_y + 16, base_z, 1, 1, COLOR_BLACK, 1)
    # layer 2 body
    draw_rect(base_x + 2, base_y + 4, base_z + 1, 1, 10, COLOR_PINK, 1)
    draw_rect(base_x + 3, base_y + 3, base_z + 1, 1, 12, COLOR_PINK, 1)
    draw_rect(base_x + 4, base_y + 2, base_z + 1, 13, 14, COLOR_PINK, 1)
    draw_rect(base_x + 17, base_y + 3, base_z + 1, 1, 12, COLOR_PINK, 1)
    draw_rect(base_x + 18, base_y + 4, base_z + 1, 1, 10, COLOR_PINK, 1)
    # layer 3 spot
    draw_rect(base_x + 4, base_y + 3, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 6, base_y + 4, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 3, base_y + 6, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 6, base_y + 6, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 10, base_y + 5, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 9, base_y + 8, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 4, base_y + 13, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 9, base_y + 14, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 9, base_y + 10, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 12, base_y + 14, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    draw_rect(base_x + 16, base_y + 12, base_z + 1, 1, 1, COLOR_MAGENTA, 1)
    return


@ti.func
def cat_legs(base_x, base_y, base_z: int):
    # left 1 behind right
    # base
    draw_rect(base_x - 3, base_y - 2, base_z + 1, 5, 4, COLOR_GRAY, 1)
    # border
    draw_rect(base_x - 3, base_y - 2, base_z + 1, 4, 1, COLOR_BLACK, 1)
    draw_rect(base_x - 3, base_y - 2, base_z + 1, 1, 3, COLOR_BLACK, 1)
    draw_rect(base_x + 1, base_y - 2, base_z + 1, 2, 2, COLOR_BLACK, 1)
    draw_rect(base_x - 3, base_y + 1, base_z + 1, 5, 1, COLOR_BLACK, 1)
    draw_rect(base_x + 2, base_y - 1, base_z + 1, 1, 3, COLOR_BLACK, 1)
    # prune
    draw_rect(base_x - 3, base_y + 1, base_z + 1, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 2, base_y + 1, base_z + 1, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 2, base_y - 2, base_z + 1, 1, 1, COLOR_BLACK, 0)
    # left 2 behind left
    draw_rect(base_x + 4, base_y - 2, base_z - 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x + 5, base_y - 1, base_z - 1, 2, 1, COLOR_GRAY, 1)
    # left 3 front left
    draw_rect(base_x + 13, base_y - 2, base_z - 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x + 14, base_y - 1, base_z - 1, 2, 1, COLOR_GRAY, 1)
    draw_rect(base_x + 13, base_y - 2, base_z - 1, 1, 1, COLOR_BLACK, 0)
    # left 4 front right
    draw_rect(base_x + 18, base_y - 2, base_z + 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x + 19, base_y - 1, base_z + 1, 2, 1, COLOR_GRAY, 1)
    draw_rect(base_x + 18, base_y - 2, base_z + 1, 1, 1, COLOR_BLACK, 0)
    draw_rect(base_x + 21, base_y - 2, base_z + 1, 1, 1, COLOR_BLACK, 0)
    return


@ti.func
def cat_tail(base_x, base_y, base_z: int):
    draw_rect(base_x - 6, base_y + 8, base_z - 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x - 5, base_y + 7, base_z - 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x - 4, base_y + 6, base_z - 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x - 3, base_y + 5, base_z - 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x - 1, base_y + 4, base_z - 1, 4, 3, COLOR_BLACK, 1)
    draw_rect(base_x - 5, base_y + 9, base_z - 1, 2, 1, COLOR_GRAY, 1)
    draw_rect(base_x - 4, base_y + 8, base_z - 1, 2, 1, COLOR_GRAY, 1)
    draw_rect(base_x - 3, base_y + 7, base_z - 1, 2, 1, COLOR_GRAY, 1)
    draw_rect(base_x - 2, base_y + 6, base_z - 1, 2, 1, COLOR_GRAY, 1)
    return


@ti.func
def draw_rect(left_bottom_x, left_bottom_y, base_z, width, height, color, material=1):
    for i in range(left_bottom_x, left_bottom_x + width):
        for j in range(left_bottom_y, left_bottom_y + height):
            scene.set_voxel(vec3(i, j, base_z), material, color)
    return


initialize_voxels()

scene.finish()
