#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:03:52 2018

@author: yy
"""
import subprocess
import time 
import sys 

def get_n_space(n):
    space = ''
    for i in range(n):
        space += '-'
    return space

def getCurrentDate():
    strDate = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())) #这里格式是‘%Y-%m-%d’，可有其他格式，也可只求年和月。
    return strDate

def run_command(command):
    result = []
    proc = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
    pid = proc.pid
    output = proc.stdout
    raw_report  = output.readlines()
    for line in raw_report:
        result.append(line.decode("utf-8"))
#    print("report," ,result)
    return result

def result_print(result_list,depth=0): 
    depth +=1
    if type(result_list) == list and len(result_list)!=1:
        for i,result in enumerate(result_list):
            space = get_n_space(depth)
            print("{}{}:".format(space,depth))
            result_print(result,depth)
    elif type(result_list) == list and len(result_list)==1:
        space = get_n_space(depth)
        print(space+result_list[0])
    elif len(result_list)!=0:
        space = get_n_space(depth)
        print(space+result_list)
        
def result_to_file(result_list):
    sys.stdout = open('run_log_{}.txt'.format(getCurrentDate()), 'w')
    result_print(result_list)
    
if __name__ == '__main__':
    command = 'ls'
    result = run_command(command)
    result_print(result)