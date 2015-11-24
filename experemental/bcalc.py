##!/usr/bin/env python
# -*- coding: utf-8 -*-
# # Балистический калькулятор

import ballistic
import convert

# Создаем пулю и стволл
a = ballistic.Bullet()
b = ballistic.Barrel()
m = ballistic.Meteo()

# Описываем пулю и ствол
a.velocity = convert.mps_to_fps(930)
a.diametr = 0.308
a.lenght = 1.225
a.stability = 1.8
a.mass = 168

b.twist = 12

print("Начальная скорость - " + str(a.velocity))
print "Угловая скорость равняется - fps = " + str(a.get_rpm(b.twist))
print "Оптимальный шаг нарезов ствола для пули длинной " + str(
    a.lenght) + ' in. и занном факторе гироскопической стабильности SG ' + str(a.stability) + ' равна ' + str(
    b.get_optimal_twist(a.diametr, a.lenght, a.mass, a.stability))
print("Оптимальная длина пули для ствола с шагом нарезов  ") + str(b.twist) + " равняеться " + str(
    a.get_bullet_length(b.twist))
print ("Фактор гироскопической стабильности Sg равняется ") + str(a.get_stability_factor(b.twist))
