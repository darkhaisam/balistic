#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Формула Greenhill
# Формула определения соответвия шагу нарезов канала ствола размерам пули пули
#
#

import argparse
UtilName = 'Balistic Tools : Twist  Range '
__author__ = 'DarkHaisam'
__version__='0.1'

print 'Balistic Tools'
parser=argparse.ArgumentParser(description=UtilName + __version__)
parser.add_argument('-v','--version', action='version', version='Balistic Tools ' '%(prog)s ' +'version '+ __version__)
parser.add_argument('-V','--velocity', type=int, required=True, help='Velocity bullet')
parser.add_argument('-D','--dbullet', type=float, required=True, help='Diametr  bullet')
parser.add_argument('-L','--lbullet', type=float, help='Leigth bullet')
parser.add_argument('-T','--twist', type=float, help='Twist range')
args = parser.parse_args()
