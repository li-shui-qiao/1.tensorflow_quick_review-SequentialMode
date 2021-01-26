#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:19:44 2021

@author: li-shui-qiao
"""
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Flatten 

import tensorflow as tf


'''
one way to create model
'''
model1 = Sequential([
    Dense(255, activation='relu', input_shape=(4096,)),
    Dense(64, activation='relu'),
    Dense(2,activation='softmax')
    ])


'''
another way to create model
'''
model2 = Sequential()
model2.add(Dense(255, activation='relu',input_shape=(4096,)))
model2.add(Dense(64, activation='relu'))
model2.add(Dense(2, activation='softmax'))

'''
to flatten the image
'''
Flatten(input_shape=(64,64))

model1.summary()

model2.summary()

Dense()