#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:14:10 2017

@author: developer
"""

import tensorflow as tf
a = tf.add(3,5)

''' one-time execution
sess = tf.Session()
print(sess.run(a))
sess.close()'''

#within the session, evaluate the graph to fetch a
with tf.Session() as sess:
    print(sess.run(a))