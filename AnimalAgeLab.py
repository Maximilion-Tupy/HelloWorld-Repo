'''
Maximilion Tupy
August 31st

Translates Human years into Animal years.
'''
import math
''' Input For Human Years '''
HumanYears=float(input("Enter your age: "))

'''Calculation for Dog Years '''
DogYears=float(math.floor((HumanYears * 7)))
''' Calculation for Dog Months '''
DogMonths=float(math.floor((((HumanYears * 7) % 1) * 12)))
''' Calculation for Dog Days '''
DogDays=float(math.floor((((HumanYears * 7) % 1) * 360)-DogMonths*30))
''' Print Function For Dog '''
print(f'Your age in dog years is {DogYears} years {DogMonths} months {DogDays} days')

''' Calulation for Cat Years '''
CatYears=float(math.floor((HumanYears / 9)))
''' Calulation for Cat Months '''
CatMonths=float(math.floor((((HumanYears / 9) % 1) * 12)))
''' Calulation for Cat Days '''
CatDays=float(math.floor(((HumanYears / 9) % 1) * 360)-CatMonths*30)
''' Print Function For Cat '''
print(f'Your age in cat years is {CatYears} years {CatMonths} months {CatDays} days')

''' Calulation for Horse Years '''
HorseYears=float(math.floor(3*((((((HumanYears)*(HumanYears))-47)/7))+12)))
''' Calulation for Horse Months '''
HorseMonths=float(math.floor((((3*((((((HumanYears)*(HumanYears))-47)/7))+12))) % 1) * 12))
''' Calulation for Horse Days '''
HorseDays=float(math.floor(((((3*((((((HumanYears)*(HumanYears))-47)/7))+12))) % 1) * 360) -HorseMonths*30))
''' Print Function For Horse '''
print(f'Your age in horse years is {HorseYears} years {HorseMonths} months {HorseDays} days')
