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
            print(os.path.join(abspath, file))
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
    cmd = "zip -j " + dest_zip + " '" + "' '".join(path_list) + "'"
    print("command to be executed: ")
    print("`zip -j <zipfile> <each of the file paths>")
    completed_process = subprocess.run(cmd)
    if completed_process.check_returncode() != 0:
        sys.stderr.write(completed_process.check_output())
    print(completed_process.check_returncode())
    return completed_process.check_output()


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='source directory')
    ns = parser.parse_args(args)
    print(dir(ns))
    # args = parser.parse_args()

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    if ns.args == 

    

if __name__ == "__main__":
    main(sys.argv[1:])
