##!/usr/bin/env python
# -*- coding: utf-8 -*-
# # Балистический калькулятор

import ballistic
import convert

# Создаем пулю и стволл
a = ballistic.Bullet()
b = ballistic.Barrel()

# Описываем пулу и ствол
a.velocity = convert.mps_to_fps(930)
a.diametr = 0.308
a.lenght = 1.35
a.stability = 1.4

b.twist = 12

print("Начальная скорость - " + str(a.velocity))

print "Угловая скорость равняется - fps = " + str(a.get_rpm(b.twist))

print "Оптимальный шаг нарезов ствола для пули " + str(a.lenght) + ' равна ' + str(
    b.get_optimal_twist(a.velocity, a.diametr, a.lenght))

print("Оптимальная длина пули для ствола с шагом нарезов  ") + str(b.twist) + " равняеться " + str(
    a.get_bullet_length(b.twist))
