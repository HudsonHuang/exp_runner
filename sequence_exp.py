#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:07:33 2018

@author: yy
"""
from single_exp import run_command,result_print

def sequence_run(command_list):
    results = []
    for command in command_list:
        result = run_command(command)
        results.append(result)
    return results

def command_genarator(base_command_with_placeholder,insert_list):
    command_list = []
    for i in insert_list:
        command = base_command_with_placeholder.format(i)
        command_list.append(command)
    return command_list
    
        
if __name__ == '__main__':
    command_list = ['cd ~/workspace/exp_runner/','sysctl -n machdep.cpu.brand_string']
    result = sequence_run(command_list)
    result_print(result)
    
    
    
    
