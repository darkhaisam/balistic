#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Формула Greenhill
# Формула определения соответвия шагу нарезов канала ствола размерам пули пули
#
#

import argparse
UtilName = 'Balistic Tools'
__author__ = 'DarkHaisam'
__version__='0.1'

print 'Balistic Tools'
parser=argparse.ArgumentParser(description=UtilName)
parser.add_argument('-v','--version', action='version', version='Balistic Tools ' '%(prog)s ' +'version '+ __version__)
args = parser.parse_args()
