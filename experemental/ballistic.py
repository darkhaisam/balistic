##!/usr/bin/env python
# -*- coding: utf-8 -*-
# Class bullet

import math

class Bullet:
    """
    Клас описывающий пулю, и вычисляющий ее характеристики
    """

    def __init__(self):
        self.diametr = 0
        self.lenght = 0
        self.mass = 0
        self.velocity = 0
        self.rpm = 0
        self.stability = 0  ## Stability factor

    def get_rpm(self, twist):
        try:
            rpm = round(self.velocity / (twist * 0.0254))
            return (rpm)
        except:
            print "Error in function get_rpm"

    def get_bullet_length(self, twist):
        """
        The function calculates the optimum length for a given bullet twist rifling formula Sierra Bullets
        """""
        try:
            __lenght = round(((0.06 * self.velocity * pow(self.diametr, 2)) / twist), 2)
            return (__lenght)
        except:
            print "Error in function get_bullet_length"

    def get_stability_factor(self, twist):
        try:
            l = self.lenght / self.diametr
            __stability = (30 * self.mass) / (pow(twist, 2) * pow(self.diametr, 3) * l * (1 + pow(l, 2)))
            __stability = round(__stability, 2)
            return (__stability)
        except:
            print "Error on function get_stability_factor "



    def show_attr(self):
        print "Caliber - " + str(self.diametr)
        print "Lenght - " + str(self.lenght)
        print "Velocity - " + str(self.velocity)
        print "RPM - " + str(self.rpm)


class Barrel:
    def __init__(self):
        self.twist = 0

    def get_optimal_twist(self, velocity=0, diametr=0, lenght=0, mass=0, stability=0):
        """"
        This function calculates the optimal step rifling according to the Miller twist rule
        """""
        try:
            l = lenght / diametr
            __twist = math.sqrt((30 * mass) / ((stability * diametr * l) * (1 + pow(l, 2))))
            __twist = round(__twist, 2)
            return (__twist)
        except:
            print "Error in function get_optimal_twist"


class Meteo:
    def __init__(self):
        self.temperature = 59
        self.pressure = 29.92
