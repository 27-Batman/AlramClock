#Python Alarm Clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

if __name__=="__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS)")
    set_alarm(alarm_time)