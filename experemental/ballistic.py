##!/usr/bin/env python
# -*- coding: utf-8 -*-
# Class bullet


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
        self.bc_g1 = 0
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

    def get_BC_G1(self):
        self.bc_g1 = 0
        return ()

    def show_attr(self):
        print "Caliber - " + str(self.diametr)
        print "Lenght - " + str(self.lenght)
        print "Velocity - " + str(self.velocity)
        print "RPM - " + str(self.rpm)


class Barrel:
    def __init__(self):
        self.twist = 0

    def get_optimal_twist(self, velocity=0, diametr=0, lenght=0):
        """"
        This function calculates the optimal step rifling according to the formula Sierra Bullets
        """""
        try:
            __twist = round(((0.06 * velocity * pow(diametr, 2)) / lenght), 2)
            return (__twist)
        except:
            print "Error in function get_optimal_twist"


class Meteo:
    def __init__(self):
        self.temperature = 0
        self.pressure = 0
