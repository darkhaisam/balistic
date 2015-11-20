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
parser.add_argument('-T', '--twist', type=float, help='Twist range in in.')
parser.add_argument('-g', '--greenhill', action='store_true', help='Use formula of Greenhill ')
parser.add_argument('-s', '--SierraBullets', action='store_true', help='Use formula of Sierra Bullets')

args = parser.parse_args()


def formula_greenhill():
    cb = 150  # Constant Greenhiil by Default
    if args.velocity <= 0:
        print "Error velocity option"
        exit()
    elif args.velocity <= 2800:
        cb = 150
    elif args.velocity > 2800:
        cb = 180

    if args.lbullet is None and args.twist is None:
        print 'Option -T twist range or -L lenght bullet must by used'
        exit()
    elif args.lbullet is not None:
        g_twist = round(((cb * pow(args.dbullet, 2)) / args.lbullet), 2)
        print 'Optimal Rifling Twist Rate ' + str(g_twist) + ' in.'
    elif args.twist is not None:
        g_lbullet = round(((cb * pow(args.dbullet, 2)) / args.twist), 2)
        print 'Optimal Bullet lenght is  ' + str(g_lbullet) + ' in.'
    return ()


def formula_sierra_bullets():
    if args.lbullet is None and args.twist is None:
        print 'Option -T twist range or -L lenght bullet must by used'
        exit()
    elif args.lbullet is not None:
        s_twist = round(((0.06 * args.velocity * pow(args.dbullet, 2)) / args.lbullet), 2)
        print 'Optimal Rifling Twist Rate Sierra Bullet ' + str(s_twist) + ' in.'
    elif args.twist is not None:
        s_lbullet = round(((0.06 * args.velocity * pow(args.dbullet, 2)) / args.twist), 2)
        print 'Optimal Bullet lenght is  ' + str(s_lbullet) + ' in.'
    return ()


if args.greenhill or not args.SierraBullets:
    formula_greenhill()

elif args.SierraBullets:
    formula_sierra_bullets()
