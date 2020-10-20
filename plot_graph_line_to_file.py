# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:25:42 2020

@author: oldel

PY1010-1 20H Python-programmering
@author: odd lie 239207
Benytter Spyder til å løse oppgaven.
mudul beregner linjer og gjennomsnitt
"""
import numpy as np
import matplotlib.pyplot as plt
import math


def f_linje(nx):
    test = 0
    for t in nx:
      test=test+t
    return test

def plot_lines_details(list_black,list_red,list_yellow,list_green,list_sum,list_len):
    #n_x1 = []
    #test_xx = f_linje(12)
    b_sum=f_linje(list_black)
    r_sum=f_linje(list_red)
    y_sum=f_linje(list_yellow)
    g_sum=f_linje(list_green)
    #summerer tabell
    tabell_sum=math.ceil(b_sum+r_sum+y_sum+g_sum)
    #beregner gjennomsnitt
    avg_tabell=tabell_sum/25
    #skaper ut like verdier langs plotet vektorisert 
    avg_plot_value=np.ones(9)*avg_tabell
    print(avg_plot_value,' gjennomsnitt')
    #rint(type(f_linje(list_black+list_red,list_yellow,list_green)))
    #n_x1.append(test_xx)
    #print(n_x1,' nx')
    plt.plot(list_yellow,'mo-')
    plt.plot(list_black,'ko-')
    plt.plot(list_red,'r*--')
    plt.plot(list_green,'g*--')
    plt.plot(avg_plot_value,'bo-')
    plt.ylabel('Antall saker = '+str(tabell_sum))
    plt.xlabel('Punkt i tabell')
    plt.grid()
    #styrer størrelse og DPI på bilse for å passe under tabell
    plt.width = 8
    plt.height =3
    plt.savefig('Risk_fig_line_02.png', dpi = 60)
    #styrer størrelse og DPI på bilse for å passe under tabell
    plt.show()