#!/usr/bin/env python
# coding: utf-8



import csv
with open('.~/ortalamalar', 'r') as ff:
    liste = csv.reader(ff,delimiter=',')
    eeg =list(liste)       

eeg
import pandas as pd
eeg=pd.read_csv('.~/ortalamalar')
eeg.head
eeg.shape
eeg.describe()
eeg.dtypes
import matplotlib.pyplot as plt
import plotly.plotly as py
import seaborn as sns
import numpy as np

x=eeg['labels'].value_counts



x = eeg['labels'].value_counts().plot(kind='barh', figsize=(10,6),
                                        color="coral", fontsize=15);
x.set_alpha(0.8)
x.set_title("labels", fontsize=20)
x.set_xlabel("adedi", fontsize=20);
x.set_xticks([0,1000])
totals = []
for i in x.patches:
    totals.append(i.get_width())
total = sum(totals)
x.set_xticks([0, 900])
for i in x.patches:
    x.text(i.get_width()+.1, i.get_y()+.31,             str(round((i.get_width()), 2)), fontsize=15, color='blue')
x.invert_yaxis()






