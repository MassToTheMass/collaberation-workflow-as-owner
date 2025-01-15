import pygame as pg
import sys

settings_dict = {}

with open("menus/settings/settings.txt", "r") as current_log:
    lines = current_log.readlines()
    for line in lines:
        split_line = line.split(":")
        settings_dict[split_line[0].strip()] = split_line[1].strip()

    print(settings_dict)


def getFPS():
    return int(settings_dict["fps"])

def setFPS(new_fps):
    settings_dict["fps"] = new_fps

def getResolution():
    resolution_str = settings_dict["resolution"]
    resolutions = resolution_str.split(", ")
    return int(resolutions[0]), int(resolutions[1])

def saveSettings():
    pass
