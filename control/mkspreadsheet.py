#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MKSPREADSHEET.PY

Created on Wed Jun 22 12:25:52 2022

@author: hudsonnash
"""

import os
import pandas as pd
def table_from_txt(udir):
    with open(os.path.join(udir,f),'r') as fobj:
        contents = fobj.read().splitlines()
    return pd.DataFrame([pd.Series(line) for line in contents])
            
    return frame
if __name__ == '__main__':
    _dir = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__))),'data','unzipped')
    dflist = []
    print(_dir)
    for f in os.listdir(_dir):
        if f[f.find('.')+1:] == 'txt':
            df = table_from_txt(_dir)
            dflist.append(df)
    print(df)
# Make dataframes wider for viewing:
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)