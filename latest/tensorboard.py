#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:44:03 2017

@author: developer
"""

import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)

with tf.Session() as sess:
    writer = tf.summary.FileWriter('/graphs', sess.graph)
    print(sess.run(x))
    
writer.close()