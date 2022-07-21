#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SHEET.PY

Created on Wed Jul 20 17:28:59 2022

@author: hudsonnash

OBJECTIVE: Try a new table extractor.
"""

from tabula import read_pdf
import os
import pandas as pd

_dir1 = os.path.join(os.path.dirname(os.getcwd()),'data/unzipped')

for f in os.listdir(_dir1):
    dfs=[]
    if os.path.splitext(f)[1] == '.pdf':
        dfs=read_pdf(os.path.join(_dir1,f),output_format='dataframe')
writer = pd.ExcelWriter('phil.xlsx')
for df in dfs:
    df.to_excel(writer,'new_sheet')
    writer.save()