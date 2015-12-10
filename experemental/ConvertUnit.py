#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Converter unit for ballistics calculator


def mps_to_fps(mps):
    __fps = int(round(mps * 3.28084))
    return (__fps)


def fps_to_mps(fps):
    __mps = int(round(fps / 3.28084))
    return (__mps)

def gramm_to_grain(gramm):
    __grain = round(gramm * 15.4324, 0)
    return (__grain)


def mm_to_in(mm):
    __in = round(mm * 0.0393701, 3)
    return (__in)


def temperature_C_to_F(C):
    __F = C * (9.0 / 5.0) + 32
    return (__F)
