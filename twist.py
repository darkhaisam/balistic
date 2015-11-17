#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Формула Greenhill
# Формула определения соответвия шагу нарезов канала ствола размерам пули пули
# Optimal Rifling Twist Rate
#

import argparse

UtilName = 'Balistic Tools : Optimal Rifling Twist Rate '
__author__ = 'DarkHaisam'
__version__ = '0.1'

print UtilName + ' ver ' + __version__

parser = argparse.ArgumentParser(description=UtilName + __version__)
parser.add_argument('-v', '--version', action='version',
                    version='Balistic Tools ' '%(prog)s ' + 'version ' + __version__)
parser.add_argument('-V', '--velocity', type=int, required=True, help='Velocity bullet (ft/s)')
parser.add_argument('-D', '--dbullet', type=float, required=True, help='Diametr  bullet (in)')
parser.add_argument('-L', '--lbullet', type=float, help='Length bullet (in)')
parser.add_argument('-T', '--twist', type=float, help='Twist range')
parser.add_argument('-g', '--greenhill', action='store_true', help='Use formula of Greenhill ')

args = parser.parse_args()

if args.velocity <= 0:
    print "Error velocity option"
    exit()
elif args.velocity <= 2800:
    C = 150
elif args.velocity > 2800:
    C = 180


def m_twist_rate():
    v_twist_rate = round(((C * pow(args.dbullet, 2)) / args.lbullet), 2)
    return (v_twist_rate)


def m_lenght_bullet():
    v_lbullets = round(((C * pow(args.dbullet, 2)) / args.twist), 2)
    return (v_lbullets)


def formula_greenhill():
    if args.lbullet is None and args.twist is None:
        print 'Option -T twist range or -L lenght bullet must by used'
        exit()
    elif args.lbullet is not None:
        print 'Optimal Rifling Twist Rate ' + str(m_twist_rate()) + ' in.'
    elif args.twist is not None:
        print  'Optimal Bullet lenght is  ' + str(m_lenght_bullet()) + ' in.'
    return ()


if args.greenhill is True:
    formula_greenhill()
