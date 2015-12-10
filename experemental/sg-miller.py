#!/usr/bin/env python
# -*- coding: utf-8 -*-
# # Балистический калькулятор

import argparse
import csv

import ConvertUnit
import CoreClass

UtilName = 'Ballistic tool: Get Stability Factor by Miller twist rule'
__author__ = 'DarkHaisam'
__version__ = '1.2 Beta'

parser = argparse.ArgumentParser(description=UtilName + __version__)
parser.add_argument('-m', '--metric', action='store_true', help=' Use for metric unit')
parser.add_argument('-b', '--bulletname', help=' Use bullet paramter from bullet name in bulletDB ')
parser.add_argument('-v', '--verbose', action='store_true', help=' Verbose output')
parser.add_argument('-V', '--velocity', type=float, help='Velocity bullet ')
parser.add_argument('-D', '--dbullet', type=float, help='Diametr bullet')
parser.add_argument('-L', '--lbullet', type=float, help='Length bullet ')
parser.add_argument('-SG', '--stability', type=float, help='Factor Gyroscopic Stabilit ')
parser.add_argument('-M', '--mass', type=float, help='Bullet mass')
parser.add_argument('-T', '--twist', type=float, help='Rifle twist')
parser.add_argument('-P', '--pressure', type=float, help='Pressure Atmosphere standart 29.92')
parser.add_argument('-t', '--temperature', type=float, help='Temperature Atmoshere Standart 59F or 15 C')

args = parser.parse_args()

# Создаем пулю и ствол и описываем метеоусловия
a = CoreClass.Bullet()
b = CoreClass.Barrel()
m = CoreClass.Meteo()

# Описываем пулю, ствол, метеоусловия
if args.bulletname:
    print ("Параметры пули будут браться из базы данных пуль по имени " + args.bulletname)
    with open('bulletsDB', 'rb') as f:
        reader = csv.reader(f, delimiter=";", quoting=csv.QUOTE_NONE)
        for row in reader:
            if args.bulletname in row:
                print row
                a.diametr = float(row[1])
                a.lenght = float(row[2])
                a.mass = float(row[3])
                a.velocity = args.velocity
                b.twist = args.twist

elif args.metric:
    a.velocity = ConvertUnit.mps_to_fps(args.velocity)
    a.diametr = ConvertUnit.mm_to_in(args.dbullet)
    a.lenght = ConvertUnit.mm_to_in(args.lbullet)
    a.stability = args.stability
    a.mass = ConvertUnit.gramm_to_grain(args.mass)

    b.twist = ConvertUnit.mm_to_in(args.twist)

    m.pressure = args.pressure
    m.temperature = ConvertUnit.temperature_C_to_F(args.temperature)
else:
    a.velocity = args.velocity
    a.diametr = args.dbullet
    a.lenght = args.lbullet
    a.stability = args.stability
    a.mass = args.mass

    b.twist = args.twist

    m.pressure = args.pressure
    m.temperature = args.temperature

if args.verbose:
    print("Заданная начальная скорость пули - " + str(a.velocity)) + ' fps ( ' + str(
        ConvertUnit.fps_to_mps(a.velocity)) + ' м/с )'
    print("Заданный диаметр пули - " + str(a.diametr) + " in. ")
    print("Заданная длина пули - " + str(a.lenght) + " in. ")
    print("Заданный фактор гироскопической стабильности S - " + str(a.stability))
    print("Задданая масса пули - " + str(a.mass) + " grain")
    print("Заданный шаг нарезов ствола - 1:" + str(int(b.twist))) + " in. "
    print("Заданное давление атмосферы - " + str(m.pressure) + " inchs of mercury")
    print("Заданная температура воздуха - " + str(m.temperature) + " F")

print ("Расчетный Фактор гироскопической стабильности S равняется ") + str(
    a.get_stability_factor(b.twist, m.pressure, m.temperature))
