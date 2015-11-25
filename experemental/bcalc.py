#!/usr/bin/env python
# -*- coding: utf-8 -*-
# # Балистический калькулятор

import argparse

import ballistic
import convert

UtilName = 'Balistic Calculator'
__author__ = 'DarkHaisam'
__version__ = '1.1 Beta'

parser = argparse.ArgumentParser(description=UtilName + __version__)
parser.add_argument('-m', '--metric', action='store_true', help=' Use for metric unit')
parser.add_argument('-V', '--velocity', type=float, required=True, help='Velocity bullet ')
parser.add_argument('-D', '--dbullet', type=float, required=True, help='Diametr bullet')
parser.add_argument('-L', '--lbullet', type=float, help='Length bullet ')
parser.add_argument('-SG', '--stability', type=float, help='Factor Gyroscopic Stabilit ')
parser.add_argument('-M', '--mass', type=float, help='Bullet mass')
parser.add_argument('-T', '--twist', type=float, help='Rifle twist')
parser.add_argument('-P', '--pressure', type=float, help='Pressure Atmosphere ')
parser.add_argument('-t', '--temperature', type=float, help='Temperature Atmoshere')
parser.add_argument('-v', '--verbose', action='store_true', help='Show verbose')

args = parser.parse_args()

# Создаем пулю и ствол и описываем метеоусловия
a = ballistic.Bullet()
b = ballistic.Barrel()
m = ballistic.Meteo()

# Описываем пулю, ствол, метеоусловия
if args.metric:
    a.velocity = convert.mps_to_fps(args.velocity)
    a.diametr = convert.mm_to_in(args.dbullet)
    a.lenght = convert.mm_to_in(args.lbullet)
    a.stability = args.stability
    a.mass = convert.gramm_to_grain(args.mass)

    b.twist = convert.mm_to_in(args.twist)

    m.pressure = args.pressure
    m.temperature = convert.temperature_C_to_F(args.temperature)
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
        convert.fps_to_mps(a.velocity)) + ' м/с )'
    print("Заданный диаметр пули - " + str(a.diametr) + " in. ")
    print("Заданная длина пули - " + str(a.lenght) + " in. ")
    print("Заданный фактор гироскопической стабильности SG - " + str(a.stability))
    print("Задданая масса пули - " + str(a.mass) + " grain")
    print("Заданный шаг нарезов ствола - 1:" + str(int(b.twist)))
    print("Заданное давление атмосферы - " + str(m.pressure) + " inchs of mercury")
    print("Заданная температура воздуха - " + str(m.temperature) + " F")

# print "Угловая скорость равняется - fps = " + str(a.get_rpm(b.twist))
# print "Оптимальный шаг нарезов ствола для пули длинной " + str(
#    a.lenght) + ' in. и заданном факторе гироскопической стабильности SG - ' + str(a.stability) + ' равна 1:' + str(
#    b.get_optimal_twist(a.diametr, a.lenght, a.mass, a.stability))
# print("Оптимальная длина пули для ствола с шагом нарезов  ") + str(b.twist) + " равняеться " + str(
#    a.get_bullet_length(b.twist))
print ("Расчетный Фактор гироскопической стабильности Sg равняется ") + str(
    a.get_stability_factor(b.twist, m.pressure, m.temperature))
