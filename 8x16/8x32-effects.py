#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

# changed a

import re
import time
import argparse
from random import random

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

speed = 0.5

def demo(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse, contrast=1)

    while True:
        incremental(device)
        bouncing_ball(device)
        mid_wipe(device)
        left_fill(device)
        random_on_off(device)


def incremental(device):
    dev = canvas(device)
    w, h = device.width, device.height
    for x in range(w):
        with dev as d:
            d.point((x, 3), fill="white")
        time.sleep(0.20 / speed)

def bouncing_ball(device):
    for repetitions in range(5):
        w, h = device.width, device.height + 1
        x, y = 3, 0
        dx, dy = 1, 1
        for moves in range(100):
            with canvas(device) as draw:
                draw.point(xy=(x, y), fill="white")
            time.sleep(0.01 / speed)
            x += dx
            if x >= w or x == -1:
                dx = -dx
                x += (2 * dx)
            y += dy
            if y >= h or y == -1:
                dy = -dy
                y += (2 * dy)

def random_on_off(device):
    for repetitions in range(10):
        w, h = device.width, device.height
        points = {(x,y) for x in range(w) for y in range(h)}
        while points:
            p = points.pop()
            with canvas(device) as draw:
                for d in points:
                    draw.point(xy=d, fill="white")
        points = {(x,y) for x in range(w) for y in range(h)}
        points2 = set()
        while points:
            p = points.pop()
            points2.add(p)
            with canvas(device) as draw:
                for d in points2:
                    draw.point(xy=d, fill="white")
        time.sleep(0.10 / speed)


def left_fill(device):
    for repetitions in range(5):
        w, h = device.width, device.height
        for bars in range(1, w + 1):
            with canvas(device) as draw:
                for b in range(bars):
                    draw.line([(b, 0), (b, h)], fill="white", width=1)
            time.sleep(0.05 / speed)

def mid_wipe(device):
    for repetitions in range(5):
        w, h = device.width, device.height
        for bars in range(0, (w + 1) // 2 + 1):
            with canvas(device) as draw:
                for b in range(w//2 - bars, w//2 + bars):
                    draw.line([(b, 0), (b, h)], fill="white", width=1)
            time.sleep(0.08 / speed)


def effect_1(device):
    for angle in range(9):    
        for col in range(16):
            with canvas(device) as draw:
                draw.line([(col, 0), (col + angle, 8)], fill="white", width=1)
            time.sleep(0.05)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=4, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=2, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=True, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
    except KeyboardInterrupt:
        pass
