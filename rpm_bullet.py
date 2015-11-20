#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Расчет начальной угловой скорости пули по шагу нарезов и дульной скорости скорости
#
#
#

import argparse

UtilName = 'Balistic Tools : RPM Bullet '
__author__ = 'DarkHaisam'
__version__ = '0.1'

print UtilName + ' ver ' + __version__

parser = argparse.ArgumentParser(description=UtilName + __version__)
parser.add_argument('-v', '--version', action='version',
                    version='Balistic Tools ' '%(prog)s ' + 'version ' + __version__)
parser.add_argument('-V', '--velocity', type=int, required=True, help='Velocity bullet (ft/s)')
parser.add_argument('-T', '--twist', type=float, help='Twist range in in.')

args = parser.parse_args()


def rpm_bullet(twist, velocity):
    rpm = round(velocity / (twist * 0.0254))
    return (rpm)
