#!/usr/bin/python
# encoding: utf-8
# author:Tea
# date:2016/07/04

import os
import sys
import datetime
import argparse


def main():
    args = getArg()
    replaceFile(args.dir, args.oldSuffix, args.newSuffix)


# 替换文件夹下面特定后缀文件或者所有文件为新后缀文件
def replaceFile(currentPath, oldSuffix, newSuffix):
    replaceTag = bool(oldSuffix.upper() == 'ALL') and True or False
    startTime = datetime.datetime.now()
    for dirPath, dirNames, fileNames in os.walk(currentPath):
        for fileName in fileNames:
            filePath = os.path.join(dirPath, fileName)
            newFilePath = os.path.join(dirPath, os.path.splitext(fileName)[0] + '.' + newSuffix)
            if replaceTag:
                os.rename(filePath, newFilePath)
            else:
                if os.path.splitext(fileName)[1] == '.' + oldSuffix:
                    os.rename(filePath, newFilePath)
    endTime = datetime.datetime.now()
    spend = (endTime - startTime).seconds
    print('Work is done. spend: %ds' % spend)


def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', '--dir', type=str, help='path:default ./', default='./')
    parser.add_argument('-old', '--oldSuffix', type=str, help='need to replace the suffix. e.g:txt or ALL')
    parser.add_argument('-new', '--newSuffix', type=str, help='new suffix. e.g:py')
    parser.add_argument('-start', '--start', help='start replace.', action='store_true')
    args = parser.parse_args()
    if not args.start or not args.oldSuffix or not args.newSuffix:
        parser.print_help()
        sys.exit()
    if not os.path.exists(args.dir):
        sys.exit('Path is not exists')
    return args


if __name__ == '__main__':
    main()
