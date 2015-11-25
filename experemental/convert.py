#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Converter unit for ballistic calculator


def mps_to_fps(mps):
    __fps = int(round(mps * 3.28084))
    return (__fps)


def fps_to_mps(fps):
    __mps = int(round(fps / 3.28084))
    return (__mps)

def gramm_to_grain(gramm):
    __grain = gramm * 15.4324
    return (__grain)


def mm_to_in(mm):
    __in = mm * 0.0393701
    return (__in)
