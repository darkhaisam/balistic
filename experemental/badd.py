#!/usr/bin/env python
# -*- coding: utf-8 -*-
# # Балистический калькулятор

import argparse
import csv

UtilName = 'Ballistic tool: Add bullet to bulletDB'
__author__ = 'DarkHaisam'
__version__ = '1.2 Beta'

parser = argparse.ArgumentParser(description=UtilName + __version__)
parser.add_argument('-m', '--metric', action='store_true', help=' Use for metric unit')
parser.add_argument('-b', '--bulletname', help=' Use bullet paramter from bullet name in bulletDB ')
parser.add_argument('-v', '--verbose', help=' Verbose output')
parser.add_argument('-D', '--dbullet', type=float, help='Diametr bullet')
parser.add_argument('-L', '--lbullet', type=float, help='Length bullet ')
parser.add_argument('-SG', '--stability', type=float, help='Factor Gyroscopic Stabilit ')
parser.add_argument('-M', '--mass', type=float, help='Bullet mass')

args = parser.parse_args()
if not args.stability:
    args.stability = ''

with open('bulletsDB', 'a') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONE)
    BulletsParam = args.bulletname, args.dbullet, args.lbullet, args.mass, args.stability
    writer.writerow(BulletsParam)
