#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

# changed alot

import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def demo(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)

    while True:
        mid_wipe(device)

def left_fill(device):
    for repetitions in range(5):
        w, h = device.width, device.height
        for bars in range(1, w + 1):
            with canvas(device) as draw:
                for b in range(bars):
                    draw.line([(b, 0), (b, h)], fill="white", width=1)
            time.sleep(0.05)

def mid_wipe(device):
    for repetitions in range(5):
        w, h = device.width, device.height
        for bars in range(0, (w + 1) // 2 + 1):
            with canvas(device) as draw:
                for b in range(8 - bars, 8 + bars):
                    draw.line([(b, 0), (b, h)], fill="white", width=1)
            time.sleep(0.05)


def effect_1(device):
    for angle in range(9):    
        for col in range(16):
            with canvas(device) as draw:
                draw.line([(col, 0), (col + angle, 8)], fill="white", width=1)
            time.sleep(0.05)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=2, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=2, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
    except KeyboardInterrupt:
        pass
