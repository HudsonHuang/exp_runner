#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:13:46 2018

@author: yy
"""
from batch_run import batch_run_commands

def run_commands():
    command_mat = []
    dir_list = list(range(10))
    base_command_with_placeholder = "python test.py --a {}"
    
    for d in dir_list:
        command_mat.append(['cd ~/workspace/exp_runner',base_command_with_placeholder.format(d)])
    result = batch_run_commands(command_mat)
    result_print(result)
    result_to_file(result)


if __name__ == '__main__':
    run_commands()
    
