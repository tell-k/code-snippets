#!/usr/bin/env python
#-*- coding:utf8 -*-
"""         
    01_syncdir
    ~~~~~~~~~~~~~~~~~~

    お題１：ファイルの同期

    二つのディレクトリ下のタイムスタンプを比較して、
    同期を取るプログラムを作りたい。

    二つのディレクトリ(フォルダ)を指定すると、そのディレクトリの
    下の全てのファイルについて「片方にしかないファイルはもう片方へコピーし、
    両方にあるけどもタイムスタンプ(更新時刻)の異なるファイルは新しい方で古
    い方を上書きする」という処理を行うプログラムを作りなさい。

    :author: tell-k
    :copyright: tell-k. All Rights Reserved.
    :ref: http://www.nishiohirokazu.org/pwe2007/2007/06/post.html
"""

import os
import sys
import shutil
import argparse

parser = argparse.ArgumentParser(description='syncdir')
parser.add_argument('dir1')
parser.add_argument('dir2')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

def parse_dirs(dir):
    ret_dirs = [] 
    ret_files = [] 
    for (root, dirs, files) in os.walk(dir):
        path = root.replace(dir, '')
        ret_dirs.append(path)
        ret_files += [path + '/'  +  file for file in files]
    return (ret_dirs, ret_files)

def copy_dirs(from_path, to_path, from_dirs, to_dirs):
    for target in list(set(from_dirs) - set(to_dirs)):
        if not os.path.exists(to_path + target):
            shutil.copytree(from_path + target, to_path + target)
        else: 
            print 'Error: dir(%s) cannot copy. "%s" is exists same name file.' %(target, to_path + target)

def copy_files(from_path, to_path, from_files, to_files):
    for target in list(set(from_files) - set(to_files)):
        if not os.path.exists(to_path + target):
            shutil.copy2(from_path + target, to_path + target)
        else: 
            print 'Error: file(%s) cannot copy. "%s" is exists same name dir.' %(target, to_path + target)

def update_latest_file(from_path, to_path, from_files, to_files):
    pass

def sync_dirs(dirpath1, dirpath2):
    dirs1, files1 = parse_dirs(dirpath1)
    dirs2, files2 = parse_dirs(dirpath2)
    #sync directory 
    copy_dirs(dirpath1, dirpath2, dirs1, dirs2)
    copy_dirs(dirpath2, dirpath1, dirs2, dirs1)
    #sync files copy no exists file
    copy_files(dirpath1, dirpath2, files1, files2)
    copy_files(dirpath2, dirpath1, files2, files1)
#    #sync file -> comparing timestamp. copy latest file to old file

if __name__ == '__main__':
    args = parser.parse_args()
    if not os.path.isdir(args.dir1) or not os.path.isdir(args.dir2):
        print 'Error: %s or %s is not directory' % (args.dir1, args.dir2)
        sys.exit()

    sync_dirs(args.dir1, args.dir2)
