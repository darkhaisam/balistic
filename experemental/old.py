##!/usr/bin/env python
# -*- coding: utf-8 -*-
# Библиотека функций  для расчета балистических параметров.
# Тестовая версия

def rpm_bullet(velocity=0, twist=0):
    """"
    Расчет угловой скорости врашения пули в зависимости от шага нарезов ствола и начальной скорости пули
    В качестве аргумента принимает значения начальной скорости и шага нарезов ствола
    """""
    rpm = 0
    try:
        rpm = round(velocity / (twist * 0.0254))
    except:
        print "Error in function rpm_bullet"

    return (rpm)


def twist(velocity, lbullet, dbullet, formula):
    return ()


def lbullet(velocity, twist, dbullet):
    return ()


def unit_convert(metr=0):
    return ()


def bc_g1():
    return ()


def simple_print(text):
    text = text * 5
    return (text)
