#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:13:46 2018

@author: yy
"""
from multiprocessing import Pool
from sequence_exp import sequence_run
from single_exp import result_print,result_to_file


def batch_run_commands(command_mat):
    p = Pool()
    results = p.map(sequence_run,command_mat)
    return results


   
if __name__ == '__main__':
    command_mat = []
    dir_list = list(range(10))
    base_command_with_placeholder = "python test.py --a {}"
    
    for d in dir_list:
        command_mat.append(['cd ~/workspace/exp_runner',base_command_with_placeholder.format(d)])
    result = batch_run_commands(command_mat)
    result_print(result)
    result_to_file(result)
    
