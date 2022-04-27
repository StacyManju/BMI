# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:20:39 2022

@author: jenny
"""
Weight = float(input('請輸入體重: (公斤)'))
Height = float(input('請輸入身高: (公分)'))

Height = Height / 100
print (Height)

BMI = Weight / Height / Height
print(BMI)


if BMI < 18.5:
    print('您的BMI為', BMI, '為體重過輕')
elif BMI >= 18.5 and BMI<24:
    print('您的BMI為', BMI, '為體重正常')
elif BMI >= 24 and BMI<27:
    print('您的BMI為', BMI, '為體重過重')
elif BMI >= 27 and BMI<30:
    print('您的BMI為', BMI, '為體重輕度肥胖')
elif BMI >= 30 and BMI<35:
    print('您的BMI為', BMI, '為體重中度肥胖')
elif BMI >= 35:
    print('您的BMI為', BMI, '為體重重度肥胖')
    
