# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:25:42 2020

@author: oldel

PY1010-1 20H Python-programmering
@author: odd lie 239207
Benytter Spyder til å løse oppgaven.
Modulen produserer opp søylediagram for plassering på skjerm
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_bar_details(list_black,list_red,list_yellow,list_green,list_sum,list_len):
    # Plotting av temperaturene:
    #temp =list_sum
    #temp_list = ''
    #list_all = []
    #list_all.append(list_black)
    #list_all.append(list_red)
    #list_all.append(list_yellow)
    #list_all.append(list_green)
    #print(list_all,' list all')
    #max_limit = max(list_all)
    #print(max_limit,' max_limit ',type(max_limit)) 
    #Count_black=len(list_black)
    #print(Count_black,' count black')
    #list_black_x=["0.0,4.0","1.4,2.5"]
    #B_X = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    #B_Y = np.array(list_black)
    #print(B_X,' B  x y ',B_Y)    
    #R_X = np.array([0,1,2,3,4,5])
    #R_Y = np.array(list_red)
    #print(R_X,' R x y ',R_Y)
    #Y_X = np.array([0,1,2,3,4,5,6,7,8])
    #Y_Y = np.array(list_yellow)
    #print(Y_X,' Y x y ',Y_Y)
    #G_X = np.array([0,1,2,3,4,5,6,7,8])
    #G_Y = np.array(list_green)
    #print(G_X,' G x y ',B_Y+R_Y+Y_Y+G_Y)
    #Sum_values = [list_black,list_red,list_yellow,list_green]
    #skaper array for plassering i graph
    B=np.array([list_black,list_red,list_yellow,list_green])
    #print(B,' B xxxxx')
    #setter fargekoder
    Color_code = ['Black','Red','Yellow','Green']
    plt.close('all')
    
    plt.figure(1)
    plt.bar(Color_code,B,width=1.0,color=('Black','Red','Yellow','Green'))
    #plt.bar(R_X,R_Y)
    #plt.bar(Y_X,Y_Y)
    #plt.bar(G_X,G_Y)
    #plt.plot(B_Y, B_X, 'k*-')
    #plt.plot(R_Y, R_X, 'r*-')
    #plt.plot(Y_Y, Y_X, 'm*-.')
    #plt.plot(G_Y, G_X, 'g*--')
    #plt.xlim(0, 25)
    #plt.ylim(0, 12)
    plt.title('Risiko matrise Pyton for beregninger')
    plt.xlabel('Sak kode')
    plt.ylabel('Antall saker')
    plt.grid()
    plt.width = 8
    plt.height =3
    #plt.xticklabels(labels=('Black', 'Red','Yellow','Green'))
    #plt.legend(labels=('Black', 'Red','Yellow','Green'))
    #figure = plt.gcf()
    #figure.set_size_inches(0.5, 0.5)
    plt.savefig('Risk_fig_01.png', dpi = 60)
    plt.show()
    
    #import matplotlib.pyplot as plt
# plot whatever you need...
# now, before saving to file:
#figure = plt.gcf() # get current figure
#figure.set_size_inches(8, 6)
# when saving, specify the DPI
#plt.savefig("myplot.png", dpi = 100) 