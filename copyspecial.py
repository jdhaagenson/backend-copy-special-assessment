#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = 'Jordan Haagenson'

import re
import os
import sys
import shutil
import subprocess
import argparse
import pprint
import glob

pp = pprint.pprint


def get_special_paths(dirname):
    '''
    returns a list of the absolute paths of the special files in the given directory, 
    but not deeper (no recursive search)
    '''
    files = os.listdir(dirname)
    abspath = os.path.abspath(dirname)
    special = []
    for file in files:
        if re.search(r'__\w+__', file):
            special.append(os.path.join(abspath, file))
    # print(special)
    return special

def copy_to(path_list, dest_dir):
    '''given a list of file paths, copies those files into the given directory'''
    abspath = os.path.abspath(dest_dir)
    if not os.path.exists(abspath):
        os.makedirs(abspath)
    for path in path_list:
        shutil.copy(path, abspath)
    return

def zip_to(path_list, dest_zip):
    '''given a list of file paths, zip those files up into the given zip path'''
    cmd = ['zip', '-j', dest_zip]
    files = " ".join(path_list)
    cmd.extend(path_list)
    print("Command I'm going to do:")
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise 

def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('fromdir', default=".", help='source directory')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    pathlist = get_special_paths(ns.fromdir)
    if ns.todir:
        return copy_to(pathlist, ns.todir)
    elif ns.tozip:
        return zip_to(pathlist, ns.tozip)
    else:
        return pp(pathlist)
        
if __name__ == "__main__":
    main(sys.argv[1:])
