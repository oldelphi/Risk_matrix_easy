"""
PY1010-1 20H Python-programmering
@author: odd lie 239207
uses Spyder to solve task.
Egendefinert prosjekt oppgave
se beskrivelse i word + kommentarer i programmet og moduler
"""
import pygame
from pygame.locals import *
import numpy as np
import os.path
from os import path
from IPython.display import Image
from datetime import datetime
#%% import av egendefinerte moduler
import plot_graph_to_file as pg
import plot_graph_line_to_file as pg_l
#%% import av egendefinerte moduler
#%% egendefinerte funsjoner
def run_BLACK(screen1,xstart1,ystart1,xwidth1,yheight1):
    pygame.draw.rect(screen1,BLACK,(xstart1,ystart1,xwidth1,yheight1))

def run_RED(screen2,xstart2,ystart2,xwidth2,yheight2):
    pygame.draw.rect(screen2,RED,(xstart2,ystart2,xwidth2,yheight2))

def run_GREEN(screen3,xstart3,ystart3,xwidth3,yheight3):
    pygame.draw.rect(screen3,GREEN,(xstart3,ystart3,xwidth3,yheight3))

def run_YELLOW(screen4,xstart4,ystart4,xwidth4,yheight4):
    pygame.draw.rect(screen4,YELLOW,(xstart4,ystart4,xwidth4,yheight4))

def run_CYAN(screen5,xstart5,ystart5,xwidth5,yheight5):
    pygame.draw.rect(screen5,CYAN,(xstart5,ystart5,xwidth5,yheight5))

def run_BLUE(screen6,xstart6,ystart6,xwidth6,yheight6):
    pygame.draw.rect(screen6,BLUE,(xstart6,ystart6,xwidth6,yheight6))

def run_MAGENTA(screen7,xstart7,ystart7,xwidth7,yheight7):
    pygame.draw.rect(screen7,MAGENTA,(xstart7,ystart7,xwidth7,yheight7))

def run_GRAY(screen8,xstart8,ystart8,xwidth8,yheight8):
    pygame.draw.rect(screen8,GRAY,(xstart8,ystart8,xwidth8,yheight8))

def run_WHITE(screen9,xstart9,ystart9,xwidth9,yheight9):
    pygame.draw.rect(screen9,WHITE,(xstart9,ystart9,xwidth9,yheight9))

def run_BLACK_line(screen0,xstart0,ystart0,xwidth0,yheight0,tickness0):
    pygame.draw.rect(screen0,BLACK,(xstart0,ystart0,xwidth0,yheight0),tickness0)
#%% egendefinerte funsjoner
#def init_text_font:
    
"""
def run_draw_text(screenA,startA, stopA, val_text):
    # TrueType fonts
    font_H = pygame.font.Font('Roboto-Bold.ttf', 60)
    text1 = font1.render('Roboto | Size: 60 | Bold', True, (0, 0, 0))
    font_V = pygame.font.Font('Lacquer-Regular.ttf', 36)
    text2 = font2.render('Lacquer | Size: 36 | Colour: Red | Background: none', True, (255, 0, 0))
    # System fonts
    font3 = pygame.font.SysFont('Bauhaus 93', 36)
    text3 = font3.render('Bauhaus 93 | Size: 36 | Colour: White | Background: Blue', True, (255, 255, 255), (0, 0, 255))
    font4 = pygame.font.SysFont('Lucida Handwriting', 36, italic=True)
    text4 = font4.render('Lucida Handwriting | Size: 36 | Italic', True, (0, 0, 0))
    font5 = pygame.font.SysFont('OCR A Extended', 18, True, True)
    text5 = font5.render('OCR A Extended | Size: 18 | Bold | Italic | Colour: Green | Background: Purple', True, (0, 255, 0), (100, 100, 255))
    font6 = pygame.font.SysFont('Parchment', 60)
    text6 = font6.render('Parchment | Size: 60 ', True, (0, 0, 0))

"""
"""
def run_risk_table(Run_info):
    Risk_Matrix_row_1=True
    #Probability
    run_BLACK_line()
    Risk_Matrix_row_2=True
    #mal
    run_BLACK_line()
    #E
    run_BLACK_line()
    #D
    run_BLACK_line()
    #C
    run_BLACK_line()
    #B
    run_BLACK_line()
    #A
    run_BLACK_line()
    Risk_Matrix_row_3=True
    #tom
    run_BLACK_line()
    #tom
    run_BLACK_line()
    #Risk_Matrix_Function
    run_BLACK_line()
    #Risk_Matrix_Reputation
    run_BLACK_line()
    #Risk_Matrix_Economic
    run_BLACK_line()
    #Risk_Matrix_E_hedder
    run_BLACK_line()
    #Risk_Matrix_D_hedder
    run_BLACK_line()
    #Risk_Matrix_C_hedder
    run_BLACK_line()
    #Risk_Matrix_B_hedder
    run_BLACK_line()
    #Risk_Matrix_A_hedder
    run_BLACK_line()
    Risk_Matrix_row_4=True
    Risk_Matrix_col_1=True
    run_BLACK_line()
    screen.draw.text(Risk_Matrix_Consequence, (100, 100), angle=10)
    Risk_Matrix_col_2=True
    #hedder_nr_4
    run_BLACK_line()
    Risk_Matrix_col_3=True    
    #Function_4
    run_BLACK_line()
    Risk_Matrix_col_4=True
    #Reputation_4    
    run_BLACK_line()
    Risk_Matrix_col_5=True
    #Economic_4
    run_BLACK_line()
    Risk_Matrix_col_6=True    
    #E_4 red
    run_BLACK_line()
    Risk_Matrix_col_7=True    
    #D_4 red
    run_BLACK_line()
    Risk_Matrix_col_8=True    
    #C_4 red
    run_BLACK_line()
    Risk_Matrix_col_9=True    
    #B_4 black   
    run_BLACK_line()
    Risk_Matrix_col_10=True
    #A_4 black 
    run_BLACK_line()
    Risk_Matrix_row_5=True
    Risk_Matrix_col_1=False
    #    run_BLACK_line()
    #screen.draw.text(Risk_Matrix_Consequence, (100, 100), angle=10)
    Risk_Matrix_col_2=True
    #hedder nr 5
    run_BLACK_line()
    Risk_Matrix_col_3=True    
    #function_5
    run_BLACK_line()
    Risk_Matrix_col_4=True
    #Reputation_5
    run_BLACK_line()
    Risk_Matrix_col_5=True    
    #Economic_5
    run_BLACK_line()
    Risk_Matrix_col_6=True
    #E_5 red    
    run_BLACK_line()
    Risk_Matrix_col_7=True    
    #D_5 red
    run_BLACK_line()
    Risk_Matrix_col_8=True    
    #C_5 red
    run_BLACK_line()
    Risk_Matrix_col_9=True    
    #B_5 red
    run_BLACK_line()
    Risk_Matrix_col_10=True
    #A_5 red
    run_BLACK_line()
    Risk_Matrix_row_6=True
    Risk_Matrix_col_1=False
    #run_BLACK_line()
    #screen.draw.text(Risk_Matrix_Consequence, (100, 100), angle=10)
    Risk_Matrix_col_2=True
    #hedder nr 6
    run_BLACK_line()
    Risk_Matrix_col_3=True    
    #function_6
    run_BLACK_line()
    Risk_Matrix_col_4=True    
    #Reputation_6
    run_BLACK_line()
    Risk_Matrix_col_5=True
    #Economic_6
    run_BLACK_line()
    Risk_Matrix_col_6=True    
    #E_6 red
    run_BLACK_line()
    Risk_Matrix_col_7=True    
    #D_6 red
    run_BLACK_line()
    Risk_Matrix_col_8=True    
    #C_6 red
    run_BLACK_line()
    Risk_Matrix_col_9=True    
    #B_6 red
    run_BLACK_line()
    Risk_Matrix_col_10=True
    #A_6 red
    run_BLACK_line()
    Risk_Matrix_row_7=True
    Risk_Matrix_col_1=False
    #run_BLACK_line()
    #screen.draw.text(Risk_Matrix_Consequence, (100, 100), angle=10)
    Risk_Matrix_col_2=True
    #hedder nr 7
    run_BLACK_line()
    Risk_Matrix_col_3=True
    #function_7
    run_BLACK_line()
    Risk_Matrix_col_4=True    
    #Reputation_7 
    run_BLACK_line()
    Risk_Matrix_col_5=True    
    #Economic_7
    run_BLACK_line()
    Risk_Matrix_col_6=True    
    #E_7 red
    run_BLACK_line()
    Risk_Matrix_col_7=True    
    #D_7 red
    run_BLACK_line()
    Risk_Matrix_col_8=True    
    #C_7 red
    run_BLACK_line()
    Risk_Matrix_col_9=True    
    #B_7 red
    run_BLACK_line()
    Risk_Matrix_col_10=True
    #A_7 red
    run_BLACK_line()
    Risk_Matrix_row_8=True
    Risk_Matrix_col_1=False
    #run_BLACK_line()
    screen.draw.text(Risk_Matrix_Consequence, (5, 5), angle=0)
    Risk_Matrix_col_2=True
    #hedder nr 8
    run_BLACK_line()
    Risk_Matrix_col_3=True    
    #function_8
    run_BLACK_line()
    Risk_Matrix_col_4=True    
    #Reputation_8
    run_BLACK_line()
    Risk_Matrix_col_5=True    
    #Economic_8
    run_BLACK_line()
    Risk_Matrix_col_6=True    
    #E_8 red
    run_BLACK_line()
    Risk_Matrix_col_7=True    
    #E_8 red
    run_BLACK_line()
    Risk_Matrix_col_8=True    
    #E_8 red
    run_BLACK_line()
    Risk_Matrix_col_9=True    
    #E_8 red
    run_BLACK_line()
    Risk_Matrix_col_10=True
    #E_8 red
    run_BLACK_line()
"""  

#%% starter pygame                              
pygame.init()
#%% starter pygame

#%% setter verdier for tabell text
Risk_Matrix_Function = 'Function'
Risk_Matrix_Reputation = 'Reputation'
Risk_Matrix_Economic = 'Economic'
Risk_Matrix_Extreme = 'Extreme'
Risk_Matrix_High = 'High'
Risk_Matrix_Medium = 'Medium'
Risk_Matrix_Low = 'Low'
Risk_Matrix_Probability = 'Probability'
Risk_Matrix_Consequence = 'Consequence'
Risk_Matrix_A_hedder = 'A'
Risk_Matrix_B_hedder = 'B'
Risk_Matrix_C_hedder = 'C'
Risk_Matrix_D_hedder = 'D'
Risk_Matrix_E_hedder = 'E'
Risk_Matrix_Consequence_l2 = 'Sansynlighet'
Risk_Matrix_Consequence_1 = '1'
Risk_Matrix_Consequence_2 = '2'
Risk_Matrix_Consequence_3 = '3'
Risk_Matrix_Consequence_4 = '4'
Risk_Matrix_Consequence_5 = '5'
#%% setter verdier for tabell text
"""
ikke i bruk
Risk_Matrix_col_1 = False
Risk_Matrix_col_2 = False
Risk_Matrix_col_3 = False
Risk_Matrix_col_4 = False
Risk_Matrix_col_5 = False
Risk_Matrix_col_6 = False
Risk_Matrix_col_7 = False
Risk_Matrix_col_8 = False
Risk_Matrix_col_9 = False
Risk_Matrix_col_10 = False

Risk_Matrix_row_1 = False
Risk_Matrix_row_2 = False
Risk_Matrix_row_3 = False
Risk_Matrix_row_4 = False
Risk_Matrix_row_5 = False
Risk_Matrix_row_6 = False
Risk_Matrix_row_7 = False
Risk_Matrix_row_8 = False
"""

#%% setter fargekoder for skjermbruk
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
#%% setter fargekoder for skjermbruk

#%% plasserer text og blokker verdi
Strek_width = 2
text_label_nr_bredder = 30
bredde_start_boktav = 30
bredde_text_borstav = 50
bredde_text_borstav_plass=25
bredde_text_desc = 480
bredde_text_conseq = 20
hoyde_text_tall = 40
hoyde_text_tall_plass = 20
Text_a_row = 50
Text_b_row = 50
Text_c_row = 50
Text_d_row = 50
Text_e_row = 50
Text_function_row = 100
Text_reputation_row = 100
Text_Economic_row = 100
bredde_function_row = 250
bredde_reputation_row = 250
bredde_Economic_row = 180
bredde_hedder_char_row = 50
Text_hedder_row = 50
Text_hedder_start = 70
hoyde_hedder = 50
hoyde_bokstaver = 30
hoyde_v_text = 130
hoyde_number = 40
bredde_text_desc_title=250
# Text_hedder_56
# Text_hedder_33
# Text_hedder_333 


block_Cl_0 = 10
block_Cl_1 = block_Cl_0 + text_label_nr_bredder
block_Cl_2 = block_Cl_1+bredde_start_boktav
block_Cl_3 = block_Cl_2+bredde_function_row
block_Cl_4 = block_Cl_3+bredde_reputation_row
block_Cl_5 = block_Cl_4+bredde_Economic_row
block_Cl_6 = block_Cl_5+bredde_hedder_char_row   #E
block_Cl_7 = block_Cl_6+bredde_hedder_char_row   #D
block_Cl_8 = block_Cl_7+bredde_hedder_char_row   #C
block_Cl_9 = block_Cl_8+bredde_hedder_char_row   #B
block_Cl_10 = block_Cl_9+bredde_hedder_char_row  #A
#block_Cl_11 = block_Cl_10+bredde_text_desc
#block_Cl_12 = block_Cl_11+bredde_text_borstav #E
#block_Cl_13 = block_Cl_12+bredde_text_borstav_plass
#block_Cl_14 = block_Cl_13+bredde_text_borstav #D
#block_Cl_15 = block_Cl_14+bredde_text_borstav_plass
#block_Cl_16 = block_Cl_15+bredde_text_borstav #C
#block_Cl_17 = block_Cl_16+bredde_text_borstav_plass
#block_Cl_18 = block_Cl_17+bredde_text_borstav #B
#block_Cl_19 = block_Cl_18+bredde_text_borstav_plass
#block_Cl_20 = block_Cl_19+bredde_text_borstav #A
#block_Cl_21 = block_Cl_20+bredde_text_borstav_plass
#block_Cl_22 = block_Cl_21+bredde_text_borstav
#block_Cl_23 = block_Cl_21+bredde_text_borstav_plass
#block_Cl_24 = block_Cl_23+bredde_text_borstav
#block_Cl_25 = block_Cl_24+bredde_text_borstav
block_level_0 = 20
block_level_1 = block_level_0 + hoyde_hedder
block_level_2 = block_level_1 + hoyde_hedder
block_level_3 = block_level_2 + 0
block_level_4 = block_level_3+hoyde_v_text
block_level_5 = block_level_4+hoyde_number#1
block_level_6 = block_level_5+hoyde_number#2
block_level_7 = block_level_6+hoyde_number#3
block_level_8 = block_level_7+hoyde_number#4
block_level_9 = block_level_8+hoyde_number#5
#print(block_level_9,' ',hoyde_number,' 8', block_level_8)
#block_level_10 = block_level_9+hoyde_text_tall_plass
#block_level_11 = block_level_10+hoyde_text_tall_plass
#block_level_12 = block_level_11+hoyde_text_tall_plass
#block_level_13 = block_level_12+hoyde_text_tall_plass
#block_level_14 = block_level_13+hoyde_text_tall_plass
#block_level_15 = block_level_14+hoyde_text_tall_plass
#block_level_16 = block_level_15+hoyde_text_tall_plass
#block_level_17 = block_level_16+hoyde_text_tall_plass
#block_level_18 = block_level_17+hoyde_text_tall_plass
#block_level_19 = block_level_18+hoyde_text_tall_plass
#block_level_20 = block_level_19+hoyde_text_tall_plass
#block_level_21 = block_level_20+hoyde_text_tall_plass
#block_level_22 = block_level_21+hoyde_text_tall_plass
#block_level_23 = block_level_22+hoyde_text_tall_plass
#block_level_24 = block_level_23+hoyde_text_tall_plass
#block_level_25 = block_level_24+hoyde_text_tall_plass
#block_level_26 = block_level_25+hoyde_text_tall_plass
#block_level_27 = block_level_26+hoyde_text_tall_plass
#block_level_28 = block_level_27+hoyde_text_tall_plass
#block_level_29 = block_level_28+hoyde_text_tall_plass
hoyde_cons_v = block_level_9 - block_level_4
bredde_text_description_line_1 = block_Cl_10
bredde_text_description_line_2 = block_Cl_6
Text_level_1 = block_level_1+hoyde_text_tall_plass
Text_level_2 = block_level_2+hoyde_text_tall_plass
Text_level_3 = block_level_3+hoyde_text_tall_plass
Text_level_4 = block_level_4+hoyde_text_tall_plass
Text_level_5 = block_level_5+hoyde_text_tall_plass
Text_level_6 = block_level_6+hoyde_text_tall_plass
Text_level_7 = block_level_7+hoyde_text_tall_plass
Text_level_8 = block_level_8+hoyde_text_tall_plass
Text_level_9 = block_level_9+hoyde_text_tall_plass-10
#Text_level_10 = Text_level_9+hoyde_text_tall_plass
#Text_level_11 = Text_level_10+hoyde_text_tall_plass
#Text_level_12 = Text_level_11+hoyde_text_tall_plass
#Text_level_13 = Text_level_12+hoyde_text_tall_plass
#Text_level_14 = Text_level_13+hoyde_text_tall_plass
#Text_level_15 = Text_level_14+hoyde_text_tall_plass
#Text_level_16 = Text_level_15+hoyde_text_tall_plass
#Text_level_17 = Text_level_16+hoyde_text_tall_plass
#Text_level_18 = Text_level_17+hoyde_text_tall_plass
#Text_level_19 = Text_level_18+hoyde_text_tall_plass
#Text_level_20 = Text_level_19+hoyde_text_tall_plass
#Text_level_21 = Text_level_20+hoyde_text_tall_plass
#Text_level_22 = Text_level_21+hoyde_text_tall_plass
#Text_level_23 = Text_level_22+hoyde_text_tall_plass
#Text_level_24 = Text_level_23+hoyde_text_tall_plass
#Text_level_25 = Text_level_24+hoyde_text_tall_plass
#Text_level_26 = Text_level_25+hoyde_text_tall_plass
#Text_level_27 = Text_level_26+hoyde_text_tall_plass
#Text_level_28 = Text_level_27+hoyde_text_tall_plass
#3Text_level_29 = Text_level_28+hoyde_text_tall_plass
 
Text_Cl_0 = 0
Text_Cl_1 = block_Cl_1 + bredde_text_borstav_plass
Text_Cl_2 = block_Cl_2 + bredde_text_borstav_plass
Text_Cl_3 = block_Cl_3 + bredde_text_borstav_plass
Text_Cl_4 = block_Cl_4 + bredde_text_borstav_plass
Text_Cl_5 = block_Cl_5 + bredde_text_borstav_plass
Text_Cl_6 = block_Cl_6 + bredde_text_borstav_plass
Text_Cl_7 = block_Cl_7 + bredde_text_borstav_plass
Text_Cl_8 = block_Cl_8 + bredde_text_borstav_plass
Text_Cl_9 = block_Cl_9 + bredde_text_borstav_plass
Text_Cl_10 = block_Cl_10 + bredde_text_borstav_plass
Text_Cl_1_L = 50
Text_Cl_2_L = 150
Text_Cl_3_L = 250
Text_Cl_4_L = 350
Text_Cl_5_L = 450
#Text_Cl_11 = Text_Cl_10+bredde_text_desc
#Text_Cl_12 = Text_Cl_11+bredde_text_borstav #E
#Text_Cl_13 = Text_Cl_11+bredde_text_borstav_plass
#Text_Cl_14 = Text_Cl_12+bredde_text_borstav #D
#Text_Cl_15 = Text_Cl_12+bredde_text_borstav_plass
#Text_Cl_16 = Text_Cl_14+bredde_text_borstav #C
#Text_Cl_17 = Text_Cl_14+[]
#Text_Cl_18 = Text_Cl_16+bredde_text_borstav #B
#Text_Cl_19 = Text_Cl_16+bredde_text_borstav_plass
#Text_Cl_20 = Text_Cl_18+bredde_text_borstav #A
#Text_Cl_21 = Text_Cl_18+bredde_text_borstav_plass
#Text_Cl_22 = Text_Cl_21+bredde_text_borstav
#Text_Cl_23 = Text_Cl_21+bredde_text_borstav_plass
#Text_Cl_24 = Text_Cl_23+bredde_text_borstav
#Text_Cl_25 = Text_Cl_24+bredde_text_borstav
# Text_Cl_26 = Text_Cl_25
# Text_Cl_27 = Text_Cl_26
# Text_Cl_28 = Text_Cl_27
# Text_Cl_29 = Text_Cl_28
#%% plasserer text og blokker verdi
#%% henter overskrift og tid
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
hent_beskrivelse=input('Hva er overskriften på rapporten:')
Risk_Matrix_Table_hedder = 'Python for beregninger '+ hent_beskrivelse +' : '+ timestampStr
#%% henter overskrift og tid
#%% plasserer text og blokker verdi
Risk_Matrix_A = 'A'
Risk_Matrix_B = 'B'
Risk_Matrix_C = 'C'
Risk_Matrix_D = 'D'
Risk_Matrix_E = 'E'
Risk_Matrix_1 = '1'
Risk_Matrix_2 = '2'
Risk_Matrix_3 = '3'
Risk_Matrix_4 = '4'
Risk_Matrix_5 = '5'
Risk_Matrix_Function = 'Function'
Risk_Matrix_Reputation = 'Reputation'
Risk_Matrix_Economic = 'Economic'
Risk_Matrix_Extreme = 'Extreme'
Risk_Matrix_High = 'High'
Risk_Matrix_Medium = 'Medium'
Risk_Matrix_Low = 'Low'
Risk_Matrix_Probability = 'Probability'
Risk_Matrix_Consequence = 'Consequence'
Risk_Matrix_A_hedder = 'A'
Risk_Matrix_B_hedder = 'B'
Risk_Matrix_C_hedder = 'C'
Risk_Matrix_D_hedder = 'D'
Risk_Matrix_E_hedder = 'E'

Risk_Matrix_1_function_text = 'Arbeider til bedriften blir ødelagt'
Risk_Matrix_2_function_text = 'Ingen får brukt systemet'
Risk_Matrix_3_function_text = 'Få forstår systemet'
Risk_Matrix_4_function_text = 'Enkelt å gjøre feil'
Risk_Matrix_5_function_text = 'Systemet er ustabilt'
Risk_Matrix_1_reputation_text = 'International media coverage'
Risk_Matrix_2_reputation_text = 'National media coverage'
Risk_Matrix_3_reputation_text = 'Regional media coverage'
Risk_Matrix_4_reputation_text = 'Local media coverage'
Risk_Matrix_5_reputation_text = 'No media coverage'
Risk_Matrix_1_Economic_text = 'USD > 1 mill $'
Risk_Matrix_2_Economic_text = 'USD 250 k – 1 mill $'
Risk_Matrix_3_Economic_text = 'USD 50 k – 250 k $'
Risk_Matrix_4_Economic_text = 'USD 10 k – 50 k $'
Risk_Matrix_5_Economic_text = 'USD < 10 k $'


Risk_Matrix_Function_1 = Risk_Matrix_1_function_text
Risk_Matrix_Reputation_1 = Risk_Matrix_1_reputation_text
Risk_Matrix_Economic_1 = Risk_Matrix_1_Economic_text
Risk_Matrix_Function_2 = Risk_Matrix_2_function_text
Risk_Matrix_Reputation_2 = Risk_Matrix_2_reputation_text
Risk_Matrix_Economic_2 = Risk_Matrix_2_Economic_text
Risk_Matrix_Function_3 = Risk_Matrix_3_function_text
Risk_Matrix_Reputation_3 = Risk_Matrix_3_reputation_text
Risk_Matrix_Economic_3 = Risk_Matrix_3_Economic_text
Risk_Matrix_Function_4 = Risk_Matrix_4_function_text
Risk_Matrix_Reputation_4 = Risk_Matrix_4_reputation_text
Risk_Matrix_Economic_4 = Risk_Matrix_4_Economic_text
Risk_Matrix_Function_5 = Risk_Matrix_5_function_text
Risk_Matrix_Reputation_5 = Risk_Matrix_5_reputation_text
Risk_Matrix_Economic_5 = Risk_Matrix_5_Economic_text
Risk_Matrix_Probability_A_hedder = '< 3 dager'
Risk_Matrix_Probability_B_hedder = '> 3 < 10 dager'
Risk_Matrix_Probability_C_hedder = '> 10 < 30 dager'
Risk_Matrix_Probability_D_hedder = '> 30 < 60 dager'
Risk_Matrix_Probability_E_hedder = '> 60 dager'


Risk_Matrix_A1_color = BLACK
Risk_Matrix_A2_color = RED
Risk_Matrix_A3_color = YELLOW
Risk_Matrix_A4_color = YELLOW
Risk_Matrix_A5_color = GREEN
Risk_Matrix_B1_color = BLACK
Risk_Matrix_B2_color = RED
Risk_Matrix_B3_color = YELLOW
Risk_Matrix_B4_color = YELLOW
Risk_Matrix_B5_color = GREEN
Risk_Matrix_C1_color = RED
Risk_Matrix_C2_color = RED
Risk_Matrix_C3_color = YELLOW
Risk_Matrix_C4_color = GREEN
Risk_Matrix_C5_color = GREEN
Risk_Matrix_D1_color = RED
Risk_Matrix_D2_color = YELLOW
Risk_Matrix_D3_color = YELLOW
Risk_Matrix_D4_color = GREEN
Risk_Matrix_D5_color = GREEN
Risk_Matrix_E1_color = RED
Risk_Matrix_E2_color = YELLOW
Risk_Matrix_E3_color = GREEN
Risk_Matrix_E4_color = GREEN
Risk_Matrix_E5_color = GREEN
#%% plasserer text og blokker verdi
#%% setter verdier for å sikre at programmet virker hvis fil ikke leses
# føste rad bruker hash 
# neste rad = E5, D5, C5, B5, A5, E4 ....  
# bruker 
# nederste rad
Risk_Matrix_E5_text = '0'
Risk_Matrix_D5_text = '6'
Risk_Matrix_C5_text = '0'
Risk_Matrix_B5_text = '0'
Risk_Matrix_A5_text = '3'
# neste rad oppover
Risk_Matrix_E4_text = '0'
Risk_Matrix_D4_text = '0'
Risk_Matrix_C4_text = '9'
Risk_Matrix_B4_text = '0'
Risk_Matrix_A4_text = '0'
# neste rad oppover
Risk_Matrix_E3_text = '8'
Risk_Matrix_D3_text = '0'
Risk_Matrix_C3_text = '0'
Risk_Matrix_B3_text = '4'
Risk_Matrix_A3_text = '0'
# neste rad oppover
Risk_Matrix_E2_text = '0'
Risk_Matrix_D2_text = '7'
Risk_Matrix_C2_text = '0'
Risk_Matrix_B2_text = '0'
Risk_Matrix_A2_text = '0'
# neste rad oppover
Risk_Matrix_E1_text = '0'
Risk_Matrix_D1_text = '0'
Risk_Matrix_C1_text = '6'
Risk_Matrix_B1_text = '0'
Risk_Matrix_A1_text = '0'
#%% definerer lister for sum av ulike farger
RM_BLACK=[]
RM_RED=[]
RM_YELLOW=[]
RM_GREEN=[]
#%% definerer lister for sum av ulike farger
#%% les fra fil
file_name = 'Matrise_a_e_1_5.txt'

if path.isfile(file_name):
  value_tabell = np.loadtxt(file_name, delimiter= ',')
  if len(value_tabell) > 23:
    # nederste rad
    Risk_Matrix_E5_text = str(value_tabell[0]) #GREEN
    Risk_Matrix_D5_text = str(value_tabell[1]) #GREEN
    Risk_Matrix_C5_text = str(value_tabell[2]) #GREEN
    Risk_Matrix_B5_text = str(value_tabell[3]) #GREEN
    Risk_Matrix_A5_text = str(value_tabell[4]) #GREEN
    # neste rad oppover
    Risk_Matrix_E4_text = str(value_tabell[5]) #GREEN
    Risk_Matrix_D4_text = str(value_tabell[6]) #GREEN
    Risk_Matrix_C4_text = str(value_tabell[7]) #GREEN
    Risk_Matrix_B4_text = str(value_tabell[8]) #YELLOW
    Risk_Matrix_A4_text = str(value_tabell[9]) #YELLOW
    # neste rad oppover
    Risk_Matrix_E3_text = str(value_tabell[10]) #GREEN
    Risk_Matrix_D3_text = str(value_tabell[11]) #YELLOW
    Risk_Matrix_C3_text = str(value_tabell[12]) #YELLOW
    Risk_Matrix_B3_text = str(value_tabell[13]) #YELLOW
    Risk_Matrix_A3_text = str(value_tabell[14]) #YELLOW
    # neste rad oppover
    Risk_Matrix_E2_text = str(value_tabell[15]) #YELLOW
    Risk_Matrix_D2_text = str(value_tabell[16]) #YELLOW
    Risk_Matrix_C2_text = str(value_tabell[17]) #RED
    Risk_Matrix_B2_text = str(value_tabell[18]) #RED
    Risk_Matrix_A2_text = str(value_tabell[19]) #RED
    # neste rad oppover
    Risk_Matrix_E1_text = str(value_tabell[20]) #RED
    Risk_Matrix_D1_text = str(value_tabell[21]) #RED
    Risk_Matrix_C1_text = str(value_tabell[22]) #RED
    Risk_Matrix_B1_text = str(value_tabell[23]) #BLACK
    Risk_Matrix_A1_text = str(value_tabell[24]) #BLACK


#%% les fra fil    
#%% legger inn verdier for ulike farger og summerer disse
RM_BLACK.append(float(Risk_Matrix_B1_text))
RM_BLACK.append(float(Risk_Matrix_A1_text))
BLACK_sum=RM_BLACK[0]+RM_BLACK[1]
print(RM_BLACK,' Sum BLACK :',BLACK_sum)
RM_RED.append(float(Risk_Matrix_C2_text))
RM_RED.append(float(Risk_Matrix_B2_text))
RM_RED.append(float(Risk_Matrix_A2_text))
RM_RED.append(float(Risk_Matrix_E1_text))
RM_RED.append(float(Risk_Matrix_D1_text))
RM_RED.append(float(Risk_Matrix_C1_text))
RED_sum=RM_RED[0]+RM_RED[1]+RM_RED[2]+RM_RED[3]+RM_RED[4]+RM_RED[5]
print(RM_RED,' Sum RED :',RED_sum)
RM_YELLOW.append(float(Risk_Matrix_B4_text))
RM_YELLOW.append(float(Risk_Matrix_A4_text))
RM_YELLOW.append(float(Risk_Matrix_D3_text))
RM_YELLOW.append(float(Risk_Matrix_C3_text))
RM_YELLOW.append(float(Risk_Matrix_B3_text))
RM_YELLOW.append(float(Risk_Matrix_A3_text))
RM_YELLOW.append(float(Risk_Matrix_E4_text))
RM_YELLOW.append(float(Risk_Matrix_D4_text))
YELLOW_sum=RM_YELLOW[0]+RM_YELLOW[1]+RM_YELLOW[2]+RM_YELLOW[3]+RM_YELLOW[4]+RM_YELLOW[5]+RM_YELLOW[6]+RM_YELLOW[7]
print(RM_YELLOW,' Sum YELLOW :',YELLOW_sum)
RM_GREEN.append(float(Risk_Matrix_E5_text))
RM_GREEN.append(float(Risk_Matrix_D5_text))
RM_GREEN.append(float(Risk_Matrix_C5_text))
RM_GREEN.append(float(Risk_Matrix_B5_text))
RM_GREEN.append(float(Risk_Matrix_A5_text))
RM_GREEN.append(float(Risk_Matrix_E4_text))
RM_GREEN.append(float(Risk_Matrix_D4_text))
RM_GREEN.append(float(Risk_Matrix_C4_text))
RM_GREEN.append(float(Risk_Matrix_E3_text))
green_sum=RM_GREEN[0]+RM_GREEN[1]+RM_GREEN[2]+RM_GREEN[3]+RM_GREEN[4]+RM_GREEN[5]+RM_GREEN[6]+RM_GREEN[7]+RM_GREEN[8]
print(RM_GREEN,' Sum GREEN :',green_sum)
#%% legger inn verdier for ulike farger og summerer disse
#%% legger inn verdier legend
Risk_Matrix_Extreme = 'Extreme '+str(BLACK_sum)
Risk_Matrix_High = 'High '+str(RED_sum)
Risk_Matrix_Medium = 'Medium '+str(YELLOW_sum)
Risk_Matrix_Low = 'Low '+str(green_sum)
#%% legger inn verdier legend
#%% beregner total sum
Risk_Matrix_sum_graph = [BLACK_sum]
Risk_Matrix_sum_graph.append(RED_sum)
Risk_Matrix_sum_graph.append(YELLOW_sum)
Risk_Matrix_sum_graph.append(green_sum)


RM_length=Risk_Matrix_sum_graph.count
Risk_Matrix_details_graph = [RM_BLACK]
Risk_Matrix_details_graph.append(RM_RED)
Risk_Matrix_details_graph.append(RM_YELLOW)
Risk_Matrix_details_graph.append(RM_GREEN)
sum_details=BLACK_sum+RED_sum+YELLOW_sum+green_sum
#%% beregner total sum
#%% plott nr 1
Risk_Matrix_sum_graph_value=np.array(Risk_Matrix_sum_graph)
#pg.plot_details(RM_BLACK,RM_RED,RM_YELLOW,RM_GREEN,Risk_Matrix_sum_graph_value,RM_length)
pg.plot_bar_details(BLACK_sum,RED_sum,YELLOW_sum,green_sum,sum_details,4)
#%% plott nr 1
IMG_bar =  'Risk_fig_01.png'
#img_rx = Image(url=IMG,width=100, height=100)
if path.isfile(IMG_bar):
   Result_RM_bar = pygame.image.load(IMG_bar)
else :
   print('Image ikke produsert og dette kan gi error')
   
#%% start plot 2
pg_l.plot_lines_details(RM_BLACK,RM_RED,RM_YELLOW,RM_GREEN,Risk_Matrix_sum_graph_value,RM_length)
IMG_line =  'Risk_fig_line_02.png'
#img_rx = Image(url=IMG,width=100, height=100)
#%% ferdig plott 2
#%% if else sløyfe  
if path.isfile(IMG_line):
   Result_RM_line = pygame.image.load(IMG_line)
else :
   print('Image ikke produsert og dette kan gi error')
   
#%% skriv til fil med tuple
##
#skriv til fil med summer bassert på fargekoder
#husk å kunne legge inn # med forklaring først.
#now til fila
#hent input fra brukere

T_out1 = ('#'+Risk_Matrix_Table_hedder)
T_out2 = ('sum_black='+str(BLACK_sum),'sum_red='+str(RED_sum),'sum_yellow='+str(YELLOW_sum),'sum_green='+str(green_sum))
T_out_b = ('black:'+ str(RM_BLACK),'red:'+ str(RM_RED),'yellow:'+ str(RM_YELLOW),'green:'+str(RM_GREEN))

#T_out_r = ()
#T_out_y = ()
#T_out_g = ()
#caption=hent_beskrivelse
#Risk_Matrix_Table_hedder
#np.savetxt('Risiko_matrise_summert.txt',T_out,delimiter=',')
#a = (“first”,”second”,”third”) #tuple.
#%% skriver til fil

file_text_write = open('Risiko_matrise_summert.txt','w') 
#open a file in write mode.
file_text_write.write(' '.join(T_out1)) #write the tuple into a file.
file_text_write.write(' '.join(T_out2)) #write the tuple into a file.
file_text_write.write(' '.join(T_out_b)) #write the tuple into a file.
#file_text_write.savetofile
file_text_write.close() #close the file.

#%% skriver til fil ferdig
#%% setter verdier
Risk_Matrix_1_function_x1 = Text_Cl_6
Risk_Matrix_2_function_x1 = Text_Cl_6
Risk_Matrix_3_function_x1 = Text_Cl_6
Risk_Matrix_4_function_x1 = Text_Cl_6
Risk_Matrix_5_function_x1 = Text_Cl_6
Risk_Matrix_1_reputation_x1 = Text_Cl_8
Risk_Matrix_2_reputation_x1 = Text_Cl_8
Risk_Matrix_3_reputation_x1 = Text_Cl_8
Risk_Matrix_4_reputation_x1 = Text_Cl_8
Risk_Matrix_5_reputation_x1 = Text_Cl_8
Risk_Matrix_1_Economic_x1 = Text_Cl_10
Risk_Matrix_2_Economic_x1 = Text_Cl_10
Risk_Matrix_3_Economic_x1 = Text_Cl_10
Risk_Matrix_4_Economic_x1 = Text_Cl_10
Risk_Matrix_5_Economic_x1 = Text_Cl_10
Risk_Matrix_Probability_A_hedder_x1 = Text_Cl_9
Risk_Matrix_Probability_B_hedder_x1 = Text_Cl_8
Risk_Matrix_Probability_C_hedder_x1 = Text_Cl_7
Risk_Matrix_Probability_D_hedder_x1 = Text_Cl_6
Risk_Matrix_Probability_E_hedder_x1 = Text_Cl_5
Risk_Matrix_1_function_y1 = Text_level_5
Risk_Matrix_2_function_y1 = Text_level_6
Risk_Matrix_3_function_y1 = Text_level_7
Risk_Matrix_4_function_y1 = Text_level_8
Risk_Matrix_5_function_y1 = Text_level_9
Risk_Matrix_1_reputation_y1 = Text_level_5
Risk_Matrix_2_reputation_y1 = Text_level_6
Risk_Matrix_3_reputation_y1 = Text_level_7
Risk_Matrix_4_reputation_y1 = Text_level_8
Risk_Matrix_5_reputation_y1 = Text_level_9
Risk_Matrix_1_Economic_y1 = Text_level_5
Risk_Matrix_2_Economic_y1 = Text_level_6
Risk_Matrix_3_Economic_y1 = Text_level_7
Risk_Matrix_4_Economic_y1 = Text_level_8
Risk_Matrix_5_Economic_y1 = Text_level_9
Risk_Matrix_Probability_A_hedder_y1 = Text_level_3
Risk_Matrix_Probability_B_hedder_y1 = Text_level_3
Risk_Matrix_Probability_C_hedder_y1 = Text_level_3
Risk_Matrix_Probability_D_hedder_y1 = Text_level_3
Risk_Matrix_Probability_E_hedder_y1 = Text_level_3
Text_Cl_Extreme = 50
Text_Cl_High = 100
Text_Cl_Medium = 150
Text_Cl_Low = 200
Risk_Matrix_A1_x1 = Text_Cl_6
Risk_Matrix_A2_x1 = Text_Cl_6
Risk_Matrix_A3_x1 = Text_Cl_6
Risk_Matrix_A4_x1 = Text_Cl_6
Risk_Matrix_A5_x1 = Text_Cl_6
Risk_Matrix_B1_x1 = Text_Cl_7
Risk_Matrix_B2_x1 = Text_Cl_7
Risk_Matrix_B3_x1 = Text_Cl_7
Risk_Matrix_B4_x1 = Text_Cl_7
Risk_Matrix_B5_x1 = Text_Cl_7
Risk_Matrix_C1_x1 = Text_Cl_8
Risk_Matrix_C2_x1 = Text_Cl_8
Risk_Matrix_C3_x1 = Text_Cl_8
Risk_Matrix_C4_x1 = Text_Cl_8
Risk_Matrix_C5_x1 = Text_Cl_8
Risk_Matrix_D1_x1 = Text_Cl_9
Risk_Matrix_D2_x1 = Text_Cl_9
Risk_Matrix_D3_x1 = Text_Cl_9
Risk_Matrix_D4_x1 = Text_Cl_9
Risk_Matrix_D5_x1 = Text_Cl_9
Risk_Matrix_E1_x1 = Text_Cl_10
Risk_Matrix_E2_x1 = Text_Cl_10
Risk_Matrix_E3_x1 = Text_Cl_10
Risk_Matrix_E4_x1 = Text_Cl_10
Risk_Matrix_E5_x1 = Text_Cl_10
Risk_Matrix_Function_x1 = Text_Cl_6
Risk_Matrix_Reputation_x1 = Text_Cl_8
Risk_Matrix_Economic_x1 = Text_Cl_10
Risk_Matrix_Extreme_x1 = Text_Cl_Extreme
Risk_Matrix_High_x1 = Text_Cl_High
Risk_Matrix_Medium_x1 = Text_Cl_Medium
Risk_Matrix_Low_x1 = Text_Cl_Low
Risk_Matrix_Probability_x1 = Text_Cl_10
Risk_Matrix_Consequence_x1 = Text_Cl_10
Risk_Matrix_Probability_l2_x1 = Text_Cl_8
Risk_Matrix_table_hedder_x1 = Text_Cl_3
Risk_Matrix_Consequence_l2_x1 = 100
# neste verdi rekke
Risk_Matrix_A1_x2 = Text_Cl_10
Risk_Matrix_A2_x2 = Text_Cl_10
Risk_Matrix_A3_x2 = Text_Cl_10
Risk_Matrix_A4_x2 = Text_Cl_10
Risk_Matrix_A5_x2 = Text_Cl_10
Risk_Matrix_B1_x2 = Text_Cl_9
Risk_Matrix_B2_x2 = Text_Cl_9
Risk_Matrix_B3_x2 = Text_Cl_9
Risk_Matrix_B4_x2 = Text_Cl_9
Risk_Matrix_B5_x2 = Text_Cl_9
Risk_Matrix_C1_x2 = Text_Cl_8
Risk_Matrix_C2_x2 = Text_Cl_8
Risk_Matrix_C3_x2 = Text_Cl_8
Risk_Matrix_C4_x2 = Text_Cl_8
Risk_Matrix_C5_x2 = Text_Cl_8
Risk_Matrix_D1_x2 = Text_Cl_7
Risk_Matrix_D2_x2 = Text_Cl_7
Risk_Matrix_D3_x2 = Text_Cl_7
Risk_Matrix_D4_x2 = Text_Cl_7
Risk_Matrix_D5_x2 = Text_Cl_7
Risk_Matrix_E1_x2 = Text_Cl_6
Risk_Matrix_E2_x2 = Text_Cl_6
Risk_Matrix_E3_x2 = Text_Cl_6
Risk_Matrix_E4_x2 = Text_Cl_6
Risk_Matrix_E5_x2 = Text_Cl_6
Risk_Matrix_Function_x2 = Text_Cl_3
Risk_Matrix_Reputation_x2 = Text_Cl_4
Risk_Matrix_Economic_x2 = Text_Cl_5
Risk_Matrix_Extreme_x2 = Text_Cl_Extreme+20
Risk_Matrix_High_x2 = Text_Cl_High+20
Risk_Matrix_Medium_x2 = Text_Cl_Medium+20
Risk_Matrix_Low_x2 = Text_Cl_Low+20
Risk_Matrix_Probability_x2 = Text_Cl_2+100
Risk_Matrix_Consequence_x2 = Text_Cl_1+20
Risk_Matrix_A1_y1 = Text_level_5
Risk_Matrix_A2_y1 = Text_level_6
Risk_Matrix_A3_y1 = Text_level_7
Risk_Matrix_A4_y1 = Text_level_8
Risk_Matrix_A5_y1 = Text_level_9
Risk_Matrix_B1_y1 = Text_level_5
Risk_Matrix_B2_y1 = Text_level_6
Risk_Matrix_B3_y1 = Text_level_7
Risk_Matrix_B4_y1 = Text_level_8
Risk_Matrix_B5_y1 = Text_level_9
Risk_Matrix_C1_y1 = Text_level_5
Risk_Matrix_C2_y1 = Text_level_6
Risk_Matrix_C3_y1 = Text_level_7
Risk_Matrix_C4_y1 = Text_level_8
Risk_Matrix_C5_y1 = Text_level_9
Risk_Matrix_D1_y1 = Text_level_5
Risk_Matrix_D2_y1 = Text_level_6
Risk_Matrix_D3_y1 = Text_level_7
Risk_Matrix_D4_y1 = Text_level_8
Risk_Matrix_D5_y1 = Text_level_9
Risk_Matrix_E1_y1 = Text_level_5
Risk_Matrix_E2_y1 = Text_level_6
Risk_Matrix_E3_y1 = Text_level_7
Risk_Matrix_E4_y1 = Text_level_8
Risk_Matrix_E5_y1 = Text_level_9
Risk_Matrix_Function_y1 = Text_level_4
Risk_Matrix_Reputation_y1 = Text_level_4
Risk_Matrix_Economic_y1 = Text_level_4
Risk_Matrix_Extreme_y1 = 500
Risk_Matrix_High_y1 = 500
Risk_Matrix_Medium_y1 = 500
Risk_Matrix_Low_y1 = 500
Risk_Matrix_Probability_y1 = 10
Risk_Matrix_Consequence_y1 = 150
Risk_Matrix_Probability_l2_y1 = 20
Risk_Matrix_table_hedder_y1 = 30
Risk_Matrix_Consequence_l2_y1 = 100
Risk_Matrix_A1_y2 = Text_level_5
Risk_Matrix_A2_y2 = Text_level_6
Risk_Matrix_A3_y2 = Text_level_7
Risk_Matrix_A4_y2 = Text_level_8
Risk_Matrix_A5_y2 = Text_level_9
Risk_Matrix_B1_y2 = Text_level_5
Risk_Matrix_B2_y2 = Text_level_6
Risk_Matrix_B3_y2 = Text_level_7
Risk_Matrix_B4_y2 = Text_level_8
Risk_Matrix_B5_y2 = Text_level_9
Risk_Matrix_C1_y2 = Text_level_5
Risk_Matrix_C2_y2 = Text_level_6
Risk_Matrix_C3_y2 = Text_level_7
Risk_Matrix_C4_y2 = Text_level_8
Risk_Matrix_C5_y2 = Text_level_9
Risk_Matrix_D1_y2 = Text_level_5
Risk_Matrix_D2_y2 = Text_level_6
Risk_Matrix_D3_y2 = Text_level_7
Risk_Matrix_D4_y2 = Text_level_8
Risk_Matrix_D5_y2 = Text_level_9
Risk_Matrix_E1_y2 = Text_level_5
Risk_Matrix_E2_y2 = Text_level_6
Risk_Matrix_E3_y2 = Text_level_7
Risk_Matrix_E4_y2 = Text_level_8
Risk_Matrix_E5_y2 = Text_level_9
Risk_Matrix_Function_y2 = 13 
Risk_Matrix_Reputation_y2 = 13 
Risk_Matrix_Economic_y2 = 13
Risk_Matrix_Extreme_y2 = 520
Risk_Matrix_High_y2 = 520
Risk_Matrix_Medium_y2 = 520
Risk_Matrix_Low_y2 = 520
Risk_Matrix_Probability_y2 = 30
Risk_Matrix_Consequence_y2 = 450
# text plassering
Risk_Matrix_T_1_Function_x1 = Text_Cl_3
Risk_Matrix_T_2_Function_x1 = Text_Cl_3
Risk_Matrix_T_3_Function_x1 = Text_Cl_3
Risk_Matrix_T_4_Function_x1 = Text_Cl_3
Risk_Matrix_T_5_Function_x1 = Text_Cl_3
Risk_Matrix_T_1_Reputation_x1 = Text_Cl_4
Risk_Matrix_T_2_Reputation_x1 = Text_Cl_4
Risk_Matrix_T_3_Reputation_x1 = Text_Cl_4
Risk_Matrix_T_4_Reputation_x1 = Text_Cl_4
Risk_Matrix_T_5_Reputation_x1 = Text_Cl_4
Risk_Matrix_T_1_Economic_x1 = Text_Cl_5
Risk_Matrix_T_2_Economic_x1 = Text_Cl_5
Risk_Matrix_T_3_Economic_x1 = Text_Cl_5
Risk_Matrix_T_4_Economic_x1 = Text_Cl_5
Risk_Matrix_T_5_Economic_x1 = Text_Cl_5
Risk_Matrix_T_Probability_A_hedder_x1 = Text_Cl_10
Risk_Matrix_T_Probability_B_hedder_x1 = Text_Cl_9
Risk_Matrix_T_Probability_C_hedder_x1 = Text_Cl_8
Risk_Matrix_T_Probability_D_hedder_x1 = Text_Cl_7
Risk_Matrix_T_Probability_E_hedder_x1 = Text_Cl_6
Risk_Matrix_T_1_Function_y1 = Text_level_5
Risk_Matrix_T_2_Function_y1 = Text_level_6
Risk_Matrix_T_3_Function_y1 = Text_level_7
Risk_Matrix_T_4_Function_y1 = Text_level_8
Risk_Matrix_T_5_Function_y1 = Text_level_9
Risk_Matrix_T_1_Reputation_y1 = Text_level_5
Risk_Matrix_T_2_Reputation_y1 = Text_level_6
Risk_Matrix_T_3_Reputation_y1 = Text_level_7
Risk_Matrix_T_4_Reputation_y1 = Text_level_8
Risk_Matrix_T_5_Reputation_y1 = Text_level_9
Risk_Matrix_T_1_Economic_y1 = Text_level_5
Risk_Matrix_T_2_Economic_y1 = Text_level_6
Risk_Matrix_T_3_Economic_y1 = Text_level_7
Risk_Matrix_T_4_Economic_y1 = Text_level_8
Risk_Matrix_T_5_Economic_y1 = Text_level_9
Risk_Matrix_T_Probability_A_hedder_y1 = Text_level_3
Risk_Matrix_T_Probability_B_hedder_y1 = Text_level_3
Risk_Matrix_T_Probability_C_hedder_y1 = Text_level_3
Risk_Matrix_T_Probability_D_hedder_y1 = Text_level_3
Risk_Matrix_T_Probability_E_hedder_y1 = Text_level_3
Text_Cl_Extreme = 50
Text_Cl_High = 100
Text_Cl_Medium = 150
Text_Cl_Low = 200
Risk_Matrix_T_A1_x1 = Text_Cl_10
Risk_Matrix_T_A2_x1 = Text_Cl_10
Risk_Matrix_T_A3_x1 = Text_Cl_10
Risk_Matrix_T_A4_x1 = Text_Cl_10
Risk_Matrix_T_A5_x1 = Text_Cl_10
Risk_Matrix_T_B1_x1 = Text_Cl_9
Risk_Matrix_T_B2_x1 = Text_Cl_9
Risk_Matrix_T_B3_x1 = Text_Cl_9
Risk_Matrix_T_B4_x1 = Text_Cl_9
Risk_Matrix_T_B5_x1 = Text_Cl_9
Risk_Matrix_T_C1_x1 = Text_Cl_8
Risk_Matrix_T_C2_x1 = Text_Cl_8
Risk_Matrix_T_C3_x1 = Text_Cl_8
Risk_Matrix_T_C4_x1 = Text_Cl_8
Risk_Matrix_T_C5_x1 = Text_Cl_8
Risk_Matrix_T_D1_x1 = Text_Cl_7
Risk_Matrix_T_D2_x1 = Text_Cl_7
Risk_Matrix_T_D3_x1 = Text_Cl_7
Risk_Matrix_T_D4_x1 = Text_Cl_7
Risk_Matrix_T_D5_x1 = Text_Cl_7
Risk_Matrix_T_E1_x1 = Text_Cl_6
Risk_Matrix_T_E2_x1 = Text_Cl_6
Risk_Matrix_T_E3_x1 = Text_Cl_6
Risk_Matrix_T_E4_x1 = Text_Cl_6
Risk_Matrix_T_E5_x1 = Text_Cl_6
Risk_Matrix_T_Function_x1 = Text_Cl_6
Risk_Matrix_T_Reputation_x1 = Text_Cl_8
Risk_Matrix_T_Economic_x1 = Text_Cl_10
Risk_Matrix_T_Extreme_x1 = Text_Cl_Extreme
Risk_Matrix_T_High_x1 = Text_Cl_High
Risk_Matrix_T_Medium_x1 = Text_Cl_Medium
Risk_Matrix_T_Low_x1 = Text_Cl_Low
Risk_Matrix_T_Probability_x1 = Text_Cl_10
Risk_Matrix_T_Consequence_x1 = Text_Cl_10
Risk_Matrix_T_Probability_l2_x1 = Text_Cl_8
Risk_Matrix_T_table_hedder_x1 = Text_Cl_3
Risk_Matrix_T_Consequence_l2_x1 = 100
Risk_Matrix_T_1_x1 = Text_Cl_2
Risk_Matrix_T_2_x1 = Text_Cl_2
Risk_Matrix_T_3_x1 = Text_Cl_2
Risk_Matrix_T_4_x1 = Text_Cl_2
Risk_Matrix_T_5_x1 = Text_Cl_2
Risk_Matrix_T_Label_x1 = 50 
Risk_Matrix_T_1_v_x1 = 25
# neste verdi rekke
Risk_Matrix_T_A1_x2 = Text_Cl_10
Risk_Matrix_T_A2_x2 = Text_Cl_10
Risk_Matrix_T_A3_x2 = Text_Cl_10
Risk_Matrix_T_A4_x2 = Text_Cl_10
Risk_Matrix_T_A5_x2 = Text_Cl_10
Risk_Matrix_T_B1_x2 = Text_Cl_9
Risk_Matrix_T_B2_x2 = Text_Cl_9
Risk_Matrix_T_B3_x2 = Text_Cl_9
Risk_Matrix_T_B4_x2 = Text_Cl_9
Risk_Matrix_T_B5_x2 = Text_Cl_9
Risk_Matrix_T_C1_x2 = Text_Cl_8
Risk_Matrix_T_C2_x2 = Text_Cl_8
Risk_Matrix_T_C3_x2 = Text_Cl_8
Risk_Matrix_T_C4_x2 = Text_Cl_8
Risk_Matrix_T_C5_x2 = Text_Cl_8
Risk_Matrix_T_D1_x2 = Text_Cl_7
Risk_Matrix_T_D2_x2 = Text_Cl_7
Risk_Matrix_T_D3_x2 = Text_Cl_7
Risk_Matrix_T_D4_x2 = Text_Cl_7
Risk_Matrix_T_D5_x2 = Text_Cl_7
Risk_Matrix_T_E1_x2 = Text_Cl_6
Risk_Matrix_T_E2_x2 = Text_Cl_6
Risk_Matrix_T_E3_x2 = Text_Cl_6
Risk_Matrix_T_E4_x2 = Text_Cl_6
Risk_Matrix_T_E5_x2 = Text_Cl_6
Risk_Matrix_T_Function_x2 = Text_Cl_3
Risk_Matrix_T_Reputation_x2 = Text_Cl_4
Risk_Matrix_T_Economic_x2 = Text_Cl_5
Risk_Matrix_T_Extreme_x2 = Text_Cl_Extreme+20
Risk_Matrix_T_High_x2 = Text_Cl_High+20
Risk_Matrix_T_Medium_x2 = Text_Cl_Medium+20
Risk_Matrix_T_Low_x2 = Text_Cl_Low+20
Risk_Matrix_T_Probability_x2 = Text_Cl_5+100
Risk_Matrix_T_Consequence_x2 = Text_Cl_1+20
Risk_Matrix_T_A1_y1 = Text_level_5
Risk_Matrix_T_A2_y1 = Text_level_6
Risk_Matrix_T_A3_y1 = Text_level_7
Risk_Matrix_T_A4_y1 = Text_level_8
Risk_Matrix_T_A5_y1 = Text_level_9
Risk_Matrix_T_B1_y1 = Text_level_5
Risk_Matrix_T_B2_y1 = Text_level_6
Risk_Matrix_T_B3_y1 = Text_level_7
Risk_Matrix_T_B4_y1 = Text_level_8
Risk_Matrix_T_B5_y1 = Text_level_9
Risk_Matrix_T_C1_y1 = Text_level_5
Risk_Matrix_T_C2_y1 = Text_level_6
Risk_Matrix_T_C3_y1 = Text_level_7
Risk_Matrix_T_C4_y1 = Text_level_8
Risk_Matrix_T_C5_y1 = Text_level_9
Risk_Matrix_T_D1_y1 = Text_level_5
Risk_Matrix_T_D2_y1 = Text_level_6
Risk_Matrix_T_D3_y1 = Text_level_7
Risk_Matrix_T_D4_y1 = Text_level_8
Risk_Matrix_T_D5_y1 = Text_level_9
Risk_Matrix_T_E1_y1 = Text_level_5
Risk_Matrix_T_E2_y1 = Text_level_6
Risk_Matrix_T_E3_y1 = Text_level_7
Risk_Matrix_T_E4_y1 = Text_level_8
Risk_Matrix_T_E5_y1 = Text_level_9
Risk_Matrix_T_Function_y1 = Text_level_4
Risk_Matrix_T_Reputation_y1 = Text_level_4
Risk_Matrix_T_Economic_y1 = Text_level_4
Risk_Matrix_T_Extreme_y1 = 500
Risk_Matrix_T_High_y1 = 500
Risk_Matrix_T_Medium_y1 = 500
Risk_Matrix_T_Low_y1 = 500
Risk_Matrix_T_Probability_y1 = 10
Risk_Matrix_T_Consequence_y1 = 150
Risk_Matrix_T_Probability_l2_y1 = 20
Risk_Matrix_T_table_hedder_y1 = 30
Risk_Matrix_T_Consequence_l2_y1 = 100
Risk_Matrix_T_1_v_y1 = 10
Risk_Matrix_T_1_y1 = Text_level_5
Risk_Matrix_T_2_y1 = Text_level_6
Risk_Matrix_T_3_y1 = Text_level_7
Risk_Matrix_T_4_y1 = Text_level_8
Risk_Matrix_T_5_y1 = Text_level_9
Risk_Matrix_T_Label_y1 = 500 
Risk_Matrix_T_1_v_y1 = 200
Risk_Matrix_T_A1_y2 = Text_level_5
Risk_Matrix_T_A2_y2 = Text_level_6
Risk_Matrix_T_A3_y2 = Text_level_7
Risk_Matrix_T_A4_y2 = Text_level_8
Risk_Matrix_T_A5_y2 = Text_level_9
Risk_Matrix_T_B1_y2 = Text_level_5
Risk_Matrix_T_B2_y2 = Text_level_6
Risk_Matrix_T_B3_y2 = Text_level_7
Risk_Matrix_T_B4_y2 = Text_level_8
Risk_Matrix_T_B5_y2 = Text_level_9
Risk_Matrix_T_C1_y2 = Text_level_5
Risk_Matrix_T_C2_y2 = Text_level_6
Risk_Matrix_T_C3_y2 = Text_level_7
Risk_Matrix_T_C4_y2 = Text_level_8
Risk_Matrix_T_C5_y2 = Text_level_9
Risk_Matrix_T_D1_y2 = Text_level_5
Risk_Matrix_T_D2_y2 = Text_level_6
Risk_Matrix_T_D3_y2 = Text_level_7
Risk_Matrix_T_D4_y2 = Text_level_8
Risk_Matrix_T_D5_y2 = Text_level_9
Risk_Matrix_T_E1_y2 = Text_level_5
Risk_Matrix_T_E2_y2 = Text_level_6
Risk_Matrix_T_E3_y2 = Text_level_7
Risk_Matrix_T_E4_y2 = Text_level_8
Risk_Matrix_T_E5_y2 = Text_level_9
Risk_Matrix_T_Function_y2 = 13 
Risk_Matrix_T_Reputation_y2 = 13 
Risk_Matrix_T_Economic_y2 = 13
Risk_Matrix_T_Extreme_y2 = 520
Risk_Matrix_T_High_y2 = 520
Risk_Matrix_T_Medium_y2 = 520
Risk_Matrix_T_Low_y2 = 520
Risk_Matrix_T_Probability_y2 = 30
Risk_Matrix_T_Consequence_y2 = 450
#%% fonet i pygame defineres og verdier settes
fonts = pygame.font.get_fonts()
font_H = pygame.font.SysFont('chalkduster.ttf', 20)
font_V = pygame.font.SysFont('chalkduster.ttf', 20)
#font_tmp = pygame.font.SysFont('chalkduster.ttf', 20)

## roterer 90 grader fungerer ok
#img1 = font_H.render('Odd er Kul i dag', True, MAGENTA)
#img1 = pygame.transform.rotate(img1, 90)
# xxxx rotasjon stop

# fungerer ikke
#font_V = pygame.transform.flip(img1, True, False)  # Flip the text vertically.
# fungerer ikke
#%% fonet i pygame defineres og verdier settes
#%% verdier settes for benyttelse av text i tabell
img_propability_hedder = font_H.render(Risk_Matrix_Probability, True, MAGENTA)
img_propability_underline = font_H.render('rate in company', True, BLUE)
img_table_hedder = font_H.render(Risk_Matrix_Table_hedder, True, BLUE)
img_T_E = font_V.render(Risk_Matrix_E, True, MAGENTA)
img_T_E = pygame.transform.rotate(img_T_E, 90)
img_T_D = font_V.render(Risk_Matrix_D, True, BLUE)
img_T_D = pygame.transform.rotate(img_T_D, 90)
img_T_C = font_V.render(Risk_Matrix_C, True, BLUE)
img_T_C = pygame.transform.rotate(img_T_C, 90)
img_T_B = font_V.render(Risk_Matrix_B, True, BLUE)
img_T_B = pygame.transform.rotate(img_T_B, 90)
img_T_A = font_V.render(Risk_Matrix_A, True, BLUE)
img_T_A = pygame.transform.rotate(img_T_A, 90)
img_T_Consequence = font_H.render(Risk_Matrix_Consequence, True, BLUE)
img_T_Consequence = pygame.transform.rotate(img_T_Consequence, 90)
img_T_Consequence_l2 = font_H.render(Risk_Matrix_Consequence_l2, True, BLUE)
img_T_Function = font_H.render(Risk_Matrix_Function, True, BLUE)
img_T_Reputation = font_H.render(Risk_Matrix_Reputation, True, BLUE)
img_T_Economic = font_H.render(Risk_Matrix_Economic, True, BLUE)
img_T_propability_E = font_V.render(Risk_Matrix_Probability_E_hedder, True, BLUE)
img_T_propability_E = pygame.transform.rotate(img_T_propability_E, 90)
img_T_propability_D = font_V.render(Risk_Matrix_Probability_D_hedder, True, BLUE)
img_T_propability_D = pygame.transform.rotate(img_T_propability_D, 90)
img_T_propability_C = font_V.render(Risk_Matrix_Probability_C_hedder, True, BLUE)
img_T_propability_C = pygame.transform.rotate(img_T_propability_C, 90)
img_T_propability_B = font_V.render(Risk_Matrix_Probability_B_hedder, True, BLUE)
img_T_propability_B = pygame.transform.rotate(img_T_propability_B, 90)
img_T_propability_A = font_V.render(Risk_Matrix_Probability_A_hedder, True, BLUE)
img_T_propability_A = pygame.transform.rotate(img_T_propability_A, 90)
img_T_propability_1_v = font_V.render(Risk_Matrix_Probability, True, BLUE)
img_T_Consequence_1 = font_H.render(Risk_Matrix_Consequence_1, True, BLUE)
img_T_Consequence_Function_1 = font_H.render(Risk_Matrix_Function_1, True, BLUE)
img_T_Consequence_Reputation_1 = font_H.render(Risk_Matrix_Reputation_1, True, BLUE)
img_T_Consequence_Economic_1 = font_H.render(Risk_Matrix_Economic_1, True, BLUE)
img_T_Consequence_E_1 = font_H.render(Risk_Matrix_E1_text, True, BLUE)
img_T_Consequence_D_1 = font_H.render(Risk_Matrix_D1_text, True, BLUE)
img_T_Consequence_C_1 = font_H.render(Risk_Matrix_C1_text, True, BLUE)
img_T_Consequence_B_1 = font_H.render(Risk_Matrix_B1_text, True, WHITE)
img_T_Consequence_A_1 = font_H.render(Risk_Matrix_A1_text, True, WHITE)
img_T_Consequence_2 = font_H.render(Risk_Matrix_Consequence_2, True, BLUE)
img_T_Consequence_Function_2 = font_H.render(Risk_Matrix_Function_2, True, BLUE)
img_T_Consequence_Reputation_2 = font_H.render(Risk_Matrix_Reputation_2, True, BLUE)
img_T_Consequence_Economic_2 = font_H.render(Risk_Matrix_Economic_2, True, BLUE)
img_T_Consequence_E_2 = font_H.render(Risk_Matrix_E2_text, True, BLUE)
img_T_Consequence_D_2 = font_H.render(Risk_Matrix_D2_text, True, BLUE)
img_T_Consequence_C_2 = font_H.render(Risk_Matrix_C2_text, True, BLUE)
img_T_Consequence_B_2 = font_H.render(Risk_Matrix_B2_text, True, BLUE)
img_T_Consequence_A_2 = font_H.render(Risk_Matrix_A2_text, True, BLUE)
img_T_Consequence_3 = font_H.render(Risk_Matrix_Consequence_3, True, BLUE)
img_T_Consequence_Function_3 = font_H.render(Risk_Matrix_Function_3, True, BLUE)
img_T_Consequence_Reputation_3 = font_H.render(Risk_Matrix_Reputation_3, True, BLUE)
img_T_Consequence_Economic_3 = font_H.render(Risk_Matrix_Economic_3, True, BLUE)
img_T_Consequence_E_3 = font_H.render(Risk_Matrix_E3_text, True, BLUE)
img_T_Consequence_D_3 = font_H.render(Risk_Matrix_D3_text, True, BLUE)
img_T_Consequence_C_3 = font_H.render(Risk_Matrix_C3_text, True, BLUE)
img_T_Consequence_B_3 = font_H.render(Risk_Matrix_B3_text, True, BLUE)
img_T_Consequence_A_3 = font_H.render(Risk_Matrix_A3_text, True, BLUE)
img_T_Consequence_4 = font_H.render(Risk_Matrix_Consequence_4, True, BLUE)
img_T_Consequence_Function_4 = font_H.render(Risk_Matrix_Function_4, True, BLUE)
img_T_Consequence_Reputation_4 = font_H.render(Risk_Matrix_Reputation_4, True, BLUE)
img_T_Consequence_Economic_4 = font_H.render(Risk_Matrix_Economic_4, True, BLUE)
img_T_Consequence_E_4 = font_H.render(Risk_Matrix_E4_text, True, BLUE)
img_T_Consequence_D_4 = font_H.render(Risk_Matrix_D4_text, True, BLUE)
img_T_Consequence_C_4 = font_H.render(Risk_Matrix_C4_text, True, BLUE)
img_T_Consequence_B_4 = font_H.render(Risk_Matrix_B4_text, True, BLUE)
img_T_Consequence_A_4 = font_H.render(Risk_Matrix_A4_text, True, BLUE)
img_T_Consequence_5 = font_H.render(Risk_Matrix_Consequence_1, True, BLUE)    
img_T_Consequence_Function_5 = font_H.render(Risk_Matrix_Function_5, True, BLUE)
img_T_Consequence_Reputation_5 = font_H.render(Risk_Matrix_Reputation_5, True, BLUE)
img_T_Consequence_Economic_5 = font_H.render(Risk_Matrix_Economic_5, True, BLUE)
img_T_Consequence_E_5 = font_H.render(Risk_Matrix_E5_text, True, BLUE)
img_T_Consequence_D_5 = font_H.render(Risk_Matrix_D5_text, True, BLUE)
img_T_Consequence_C_5 = font_H.render(Risk_Matrix_C5_text, True, BLUE)
img_T_Consequence_B_5 = font_H.render(Risk_Matrix_B5_text, True, BLUE)
img_T_Consequence_A_5 = font_H.render(Risk_Matrix_A5_text, True, BLUE)
img_T_Label = font_H.render('Label:', True, BLUE)
img_T_Extreme = font_H.render(Risk_Matrix_Extreme, True, BLUE)
img_T_High = font_H.render(Risk_Matrix_High, True, BLUE)
img_T_Medium = font_H.render(Risk_Matrix_Medium, True, BLUE)
img_T_Low = font_H.render(Risk_Matrix_Low, True, BLUE)
#%% verdier settes for benyttelse av text i tabell
#%% verdier settes for benyttelse av text i tabell
K_k = BLACK
K_r = RED
K_g = GREEN
K_b = BLUE
K_y = YELLOW
K_c = CYAN
K_m = MAGENTA
K_w = WHITE
#%% pygame start info
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, 
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

pygame.init()
screen = pygame.display.set_mode((1024, 750))

running = True
background = GRAY
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                
                caption = 'background color = ' + str(background)
                pygame.display.set_caption(caption)

    screen.fill(background)
    #screen.fill(background)
    # plassering av tabell farger
    # row_1 
    run_RED(screen,block_Cl_5, block_level_4, bredde_text_borstav, hoyde_text_tall)
    run_RED(screen,block_Cl_6, block_level_4, bredde_text_borstav, hoyde_text_tall)
    run_RED(screen,block_Cl_7, block_level_4, bredde_text_borstav, hoyde_text_tall)
    run_BLACK(screen,block_Cl_8, block_level_4, bredde_text_borstav, hoyde_text_tall)
    run_BLACK(screen,block_Cl_9, block_level_4, bredde_text_borstav, hoyde_text_tall)
    #row_2
    run_YELLOW(screen,block_Cl_5, block_level_5, bredde_text_borstav, hoyde_text_tall)
    run_YELLOW(screen,block_Cl_6, block_level_5, bredde_text_borstav, hoyde_text_tall)
    run_RED(screen,block_Cl_7, block_level_5, bredde_text_borstav, hoyde_text_tall)
    run_RED(screen,block_Cl_8, block_level_5, bredde_text_borstav, hoyde_text_tall)
    run_RED(screen,block_Cl_9, block_level_5, bredde_text_borstav, hoyde_text_tall)
    #row_3 
    #    pygame.draw.rect(screen, RED, (50, 20, 160, 100),5)
    run_GREEN(screen,block_Cl_5, block_level_6, bredde_text_borstav, hoyde_text_tall)
    run_YELLOW(screen,block_Cl_6, block_level_6, bredde_text_borstav, hoyde_text_tall)
    run_YELLOW(screen,block_Cl_7, block_level_6, bredde_text_borstav, hoyde_text_tall)
    run_YELLOW(screen,block_Cl_8, block_level_6, bredde_text_borstav, hoyde_text_tall)
    run_YELLOW(screen,block_Cl_9, block_level_6, bredde_text_borstav, hoyde_text_tall)
    #row_4
    run_GREEN(screen,block_Cl_5, block_level_7, bredde_text_borstav, hoyde_text_tall)
    run_GREEN(screen,block_Cl_6, block_level_7, bredde_text_borstav, hoyde_text_tall)
    run_GREEN(screen,block_Cl_7, block_level_7, bredde_text_borstav, hoyde_text_tall)
    run_YELLOW(screen,block_Cl_8, block_level_7, bredde_text_borstav, hoyde_text_tall)
    run_YELLOW(screen,block_Cl_9, block_level_7, bredde_text_borstav, hoyde_text_tall)
    #row_5
    run_GREEN(screen,block_Cl_5, block_level_8, bredde_text_borstav, hoyde_text_tall)
    run_GREEN(screen,block_Cl_6, block_level_8, bredde_text_borstav, hoyde_text_tall)
    run_GREEN(screen,block_Cl_7, block_level_8, bredde_text_borstav, hoyde_text_tall)
    run_GREEN(screen,block_Cl_8, block_level_8, bredde_text_borstav, hoyde_text_tall)
    run_GREEN(screen,block_Cl_9, block_level_8, bredde_text_borstav, hoyde_text_tall)
    #print(block_level_9)
    #print(block_Cl_10)
    #labels
    #run_BLACK(screen,400, 60, 160, 100)
    #run_RED(screen,150, 120, 260, 200)
    #run_YELLOW(screen,350, 20, 160, 100)
    #run_GREEN(screen,100, 60, 160, 100)
    # used ?
    #run_BLUE(screen,150, 100, 160, 100)
    # used ?    
    #run_WHITE(screen,450, 100, 160, 100)
    #pygame.font
    #screen.draw.text(Risk_Matrix_Consequence, (5, 5), angle=0)
    #pygame.display.update()
    #plassering av bokser med text
    run_BLACK_line(screen,block_Cl_0, block_level_0,bredde_text_description_line_1 ,hoyde_hedder,Strek_width)
    run_BLACK_line(screen,block_Cl_0, block_level_1, bredde_text_description_line_2,hoyde_hedder ,Strek_width)
    #   labels E-A 
    run_BLACK_line(screen,block_Cl_5, block_level_1, bredde_text_borstav,hoyde_hedder ,Strek_width)
    run_BLACK_line(screen,block_Cl_6, block_level_1, bredde_text_borstav,hoyde_hedder ,Strek_width)
    run_BLACK_line(screen,block_Cl_7, block_level_1, bredde_text_borstav,hoyde_hedder ,Strek_width)
    run_BLACK_line(screen,block_Cl_8, block_level_1, bredde_text_borstav,hoyde_hedder ,Strek_width)
    run_BLACK_line(screen,block_Cl_9, block_level_1, bredde_text_borstav,hoyde_hedder ,Strek_width)
    #run_BLACK_line(screen,block_Cl_10, block_level_1, bredde_text_borstav,hoyde_bokstaver,Strek_width)
    #Hole 
    run_BLACK_line(screen,block_Cl_2, block_level_2, bredde_function_row ,hoyde_v_text,Strek_width)
    run_BLACK_line(screen,block_Cl_3, block_level_2, bredde_reputation_row,hoyde_v_text,Strek_width)
    run_BLACK_line(screen,block_Cl_4, block_level_2, bredde_Economic_row,hoyde_v_text,Strek_width)
    #char E-A
    run_BLACK_line(screen,block_Cl_5, block_level_2, bredde_text_borstav,hoyde_v_text,Strek_width)
    run_BLACK_line(screen,block_Cl_6, block_level_2, bredde_text_borstav,hoyde_v_text,Strek_width)
    run_BLACK_line(screen,block_Cl_7, block_level_2, bredde_text_borstav,hoyde_v_text,Strek_width)
    run_BLACK_line(screen,block_Cl_8, block_level_2, bredde_text_borstav,hoyde_v_text,Strek_width)
    run_BLACK_line(screen,block_Cl_9, block_level_2, bredde_text_borstav,hoyde_v_text,Strek_width)
    #Vertical text
    run_BLACK_line(screen,block_Cl_0, block_level_4, bredde_start_boktav,hoyde_cons_v,Strek_width)
    #Numbers 1
    run_BLACK_line(screen,block_Cl_1, block_level_4, text_label_nr_bredder,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_1, block_level_5, text_label_nr_bredder,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_1, block_level_6, text_label_nr_bredder,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_1, block_level_7, text_label_nr_bredder,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_1, block_level_8, text_label_nr_bredder,hoyde_text_tall,Strek_width)
    #Function
    run_BLACK_line(screen,block_Cl_2, block_level_4, bredde_function_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_2, block_level_5, bredde_function_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_2, block_level_6, bredde_function_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_2, block_level_7, bredde_function_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_2, block_level_8, bredde_function_row,hoyde_text_tall,Strek_width)
    #Reputation
    run_BLACK_line(screen,block_Cl_3, block_level_4, bredde_reputation_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_3, block_level_5, bredde_reputation_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_3, block_level_6, bredde_reputation_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_3, block_level_7, bredde_reputation_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_3, block_level_8, bredde_reputation_row,hoyde_text_tall,Strek_width)
    #Echonomic
    run_BLACK_line(screen,block_Cl_4, block_level_4, bredde_Economic_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_4, block_level_5, bredde_Economic_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_4, block_level_6, bredde_Economic_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_4, block_level_7, bredde_Economic_row,hoyde_text_tall,Strek_width)
    run_BLACK_line(screen,block_Cl_4, block_level_8, bredde_Economic_row,hoyde_text_tall,Strek_width)
    #run_BLACK_line(screen,Text_Cl_3, Text_level_10, Text_Cl_4,Text_level_12,Strek_width)
    #run_BLACK_line(screen,Text_Cl_3, Text_level_12, Text_Cl_4,Text_level_14,Strek_width)
    #run_BLACK_line(screen,Text_Cl_3, Text_level_14, Text_Cl_4,Text_level_16,Strek_width)
    #run_BLACK_line(screen,Text_Cl_3, Text_level_16, Text_Cl_4,Text_level_18,Strek_width)
    #run_BLACK_line(screen,Text_Cl_4, Text_level_6, Text_Cl_5,Text_level_8,Strek_width)
    #run_BLACK_line(screen,Text_Cl_4, Text_level_8, Text_Cl_5,Text_level_10,Strek_width)
    #run_BLACK_line(screen,Text_Cl_4, Text_level_10, Text_Cl_5,Text_level_12,Strek_width)
    #run_BLACK_line(screen,Text_Cl_4, Text_level_12, Text_Cl_5,Text_level_14,Strek_width)
    #run_BLACK_line(screen,Text_Cl_4, Text_level_14, Text_Cl_5,Text_level_16,Strek_width)
    #run_BLACK_line(screen,Text_Cl_4, Text_level_16, Text_Cl_5,Text_level_18,Strek_width)
    # plassering av text til skjerm
    screen.blit(img_table_hedder, (Text_Cl_1, Text_level_1))
    screen.blit(img_propability_underline, (Text_Cl_6, Text_level_1-60))
    screen.blit(img_propability_hedder, (Text_Cl_6, Text_level_1-40))
    screen.blit(img_T_E, (Text_Cl_5, Text_level_1))
    screen.blit(img_T_D, (Text_Cl_6, Text_level_1))
    screen.blit(img_T_C, (Text_Cl_7, Text_level_1))
    screen.blit(img_T_B, (Text_Cl_8, Text_level_1)) 
    screen.blit(img_T_A, (Text_Cl_9, Text_level_1))
    screen.blit(img_T_Consequence, (Text_Cl_0+25, Text_level_6))
    screen.blit(img_T_Consequence_l2, (Text_Cl_1, Text_level_1-60))
    screen.blit(img_T_Function, (Text_Cl_2, Text_level_2))
    screen.blit(img_T_Reputation, (Text_Cl_3, Text_level_2))
    screen.blit(img_T_Economic, (Text_Cl_4, Text_level_2))
    screen.blit(img_T_propability_E, (Text_Cl_5, Text_level_2))
    screen.blit(img_T_propability_D, (Text_Cl_6, Text_level_2))
    screen.blit(img_T_propability_C, (Text_Cl_7, Text_level_2))
    screen.blit(img_T_propability_B, (Text_Cl_8, Text_level_2))
    screen.blit(img_T_propability_A, (Text_Cl_9, Text_level_2))
    #screen.blit(img_T_propability_1_v, (Risk_Matrix_T_1_v_x1, Risk_Matrix_T_1_v_y1))
    screen.blit(img_T_Consequence_1, (Text_Cl_1-15, Text_level_4))
    screen.blit(img_T_Consequence_Function_1, (Text_Cl_2, Text_level_4))
    screen.blit(img_T_Consequence_Reputation_1, (Text_Cl_3, Text_level_4))
    screen.blit(img_T_Consequence_Economic_1, (Text_Cl_4, Text_level_4))
    screen.blit(img_T_Consequence_E_1, (Text_Cl_5, Text_level_4))
    screen.blit(img_T_Consequence_D_1, (Text_Cl_6, Text_level_4))
    screen.blit(img_T_Consequence_C_1, (Text_Cl_7, Text_level_4))
    screen.blit(img_T_Consequence_B_1, (Text_Cl_8, Text_level_4))
    screen.blit(img_T_Consequence_A_1, (Text_Cl_9, Text_level_4))
    screen.blit(img_T_Consequence_2, (Text_Cl_1-15, Text_level_5))
    screen.blit(img_T_Consequence_Function_2, (Text_Cl_2, Text_level_5))
    screen.blit(img_T_Consequence_Reputation_2, (Text_Cl_3, Text_level_5))
    screen.blit(img_T_Consequence_Economic_2, (Text_Cl_4, Text_level_5))
    screen.blit(img_T_Consequence_E_2, (Text_Cl_5, Text_level_5))
    screen.blit(img_T_Consequence_D_2, (Text_Cl_6, Text_level_5))
    screen.blit(img_T_Consequence_C_2, (Text_Cl_7, Text_level_5))
    screen.blit(img_T_Consequence_B_2, (Text_Cl_8, Text_level_5))
    screen.blit(img_T_Consequence_A_2, (Text_Cl_9, Text_level_5))
    screen.blit(img_T_Consequence_3, (Text_Cl_1-15, Text_level_6))
    screen.blit(img_T_Consequence_Function_3, (Text_Cl_2, Text_level_6))
    screen.blit(img_T_Consequence_Reputation_3, (Text_Cl_3, Text_level_6))
    screen.blit(img_T_Consequence_Economic_3, (Text_Cl_4, Text_level_6))
    screen.blit(img_T_Consequence_E_3, (Text_Cl_5, Text_level_6))
    screen.blit(img_T_Consequence_D_3, (Text_Cl_6, Text_level_6))
    screen.blit(img_T_Consequence_C_3, (Text_Cl_7, Text_level_6))
    screen.blit(img_T_Consequence_B_3, (Text_Cl_8, Text_level_6))
    screen.blit(img_T_Consequence_A_3, (Text_Cl_9, Text_level_6))
    screen.blit(img_T_Consequence_4, (Text_Cl_1-15, Text_level_7))
    screen.blit(img_T_Consequence_Function_4, (Text_Cl_2, Text_level_7))
    screen.blit(img_T_Consequence_Reputation_4, (Text_Cl_3, Text_level_7))
    screen.blit(img_T_Consequence_Economic_4, (Text_Cl_4, Text_level_7))
    screen.blit(img_T_Consequence_E_4, (Text_Cl_5, Text_level_7))
    screen.blit(img_T_Consequence_D_4, (Text_Cl_6, Text_level_7))
    screen.blit(img_T_Consequence_C_4, (Text_Cl_7, Text_level_7))
    screen.blit(img_T_Consequence_B_4, (Text_Cl_8, Text_level_7))
    screen.blit(img_T_Consequence_A_4, (Text_Cl_9, Text_level_7))
    screen.blit(img_T_Consequence_5, (Text_Cl_1-15, Text_level_8))    
    screen.blit(img_T_Consequence_Function_5, (Text_Cl_2, Text_level_8))
    screen.blit(img_T_Consequence_Reputation_5, (Text_Cl_3, Text_level_8))
    screen.blit(img_T_Consequence_Economic_5, (Text_Cl_4, Text_level_8))
    screen.blit(img_T_Consequence_E_5, (Text_Cl_5, Text_level_8))
    screen.blit(img_T_Consequence_D_5, (Text_Cl_6, Text_level_8))
    screen.blit(img_T_Consequence_C_5, (Text_Cl_7, Text_level_8))
    screen.blit(img_T_Consequence_B_5, (Text_Cl_8, Text_level_8))
    screen.blit(img_T_Consequence_A_5, (Text_Cl_9, Text_level_8))
    #legend
    screen.blit(img_T_Label, (Text_Cl_1_L, Text_level_9))
    screen.blit(img_T_Extreme, (Text_Cl_2_L, Text_level_9))
    screen.blit(img_T_High, (Text_Cl_3_L, Text_level_9))
    screen.blit(img_T_Medium, (Text_Cl_4_L+10, Text_level_9))
    screen.blit(img_T_Low, (Text_Cl_5_L+15, Text_level_9))
    # LINJER FOR HVER FARGE
    screen.blit(Result_RM_bar,(100,500))
    # SAMT BEREGNE GJENNOMSNITT
    screen.blit(Result_RM_line,(450,500))
    #screen.blit(img1, (200, 500))
    #plassering av legend
    run_BLACK(screen,Text_Cl_2_L-20,Text_level_9,15,15) #SUM SVARTE
    run_RED(screen,Text_Cl_3_L-20,Text_level_9,15,15)   #SUM RED 
    run_YELLOW(screen,Text_Cl_4_L-10,Text_level_9,15,15)#SUM YELLOW
    run_GREEN(screen,Text_Cl_5_L-5,Text_level_9,15,15) #SUM GREEN
    #run_RED(screen,1,1,1,1)
    #run_RED(screen,1,1,1,1)
    #refresh skjermbilde
    pygame.display.update()
   
# lagrer ferdig skjermbilde
fname = "Risiko_Matrise_skjermbilde_ferdig.png"
pygame.image.save(screen, fname)
print("file {} has been saved".format(fname))
   # pygame.savetofile('test_grid.pdf')
#avslutter benyttelse av Pygame
pygame.quit()
#Programmet avsluttes med å lukke vindu