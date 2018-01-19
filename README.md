# 后缀文件替换 - ReplaceSuffix

    usage: ReplaceSuffix.py [-h] [-dir DIR] [-old OLDSUFFIX] [-new NEWSUFFIX]
                        [-start]

	optional arguments:
  		-h, --help            show this help message and exit
  		-dir DIR, --dir DIR   path:default ./
  		-old OLDSUFFIX, --oldSuffix OLDSUFFIX
                        	  need to replace the suffix. e.g:txt or ALL
  		-new NEWSUFFIX, --newSuffix NEWSUFFIX
                        	  new suffix. e.g:py
  		-start, --start       start replace.  

-dir 默认当前目录,后面跟文件夹目录,不存在的目录将会提示错误  
-old 后面直接跟老文件后缀名称,也可以ALL替换所有的文件  
-new 后面直接跟新文件后缀名称  
-start 直接照打表示开始替换  

**Author: Tea  
Date: 2016/07/04**
