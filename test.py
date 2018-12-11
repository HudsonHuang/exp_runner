#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 01:05:14 2018

@author: yy
"""

import argparse

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('--a',help='a sourcedir')
    args = parse.parse_args()
    print(args.a)