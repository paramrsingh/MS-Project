#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:28:03 2017

@author: developer
"""

import tensorflow as tf

x = 2
y = 3

add_op = tf.add(x,y)
mul_op = tf.multiply(x,y)
useless = tf.multiply(x, add_op)
pow_op = tf.pow(add_op, mul_op)

with tf.Session() as sess:
    z = sess.run(pow_op)
    print(z)