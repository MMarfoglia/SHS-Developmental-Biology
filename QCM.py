from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.core.display import HTML
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
#import pandas as pd
from math import *




def choice_list(choices,descript,booleen,val):
    b = widgets.RadioButtons(
    options=[choice for choice in choices],
    value=val,
    description=descript,
    disabled=booleen)
    return b

def button(descript,booleen,icon,style):
    b = widgets.Button(
    description=descript,
    disabled=booleen,
    button_style=style, # 'success', 'info', 'warning', 'danger' or ''
    tooltip='description',
    icon=icon)
    return b

def QCM(x,q,a): 
    
    display(HTML(q))
    
    choices=[x[i] for i in x]
    correct = x['correct']
        
    buttons = choice_list(choices,'',False,choices[0])

    check=widgets.Button(
    description='Check answers',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='description',
    icon='check')
    
    check = button('Check answers',False,'check','')
    
    succes = button('Congratulation!',False,'','success')
    
    fail = button('Sorry, try again!',False,'','warning')  
    
    display(buttons)
    display(check)
    def on_button_clicked1(b):
        choice = buttons.value
        if choice == correct:
            check.close()
            buttons.close()
            display(choice_list(choices,'',True,choice))
            display(succes)
            display(HTML(a))
        else:
            check.close()
            display(fail)
            
    def on_button_clicked2(b):
        choice = buttons.value
        if choice == correct:
            fail.close()
            buttons.close()
            display(choice_list(choices,'',True,choice))
            display(succes)
            display(HTML(a))

    check.on_click(on_button_clicked1)
    fail.on_click(on_button_clicked2)

q1='Question 3: How could we impact the gradient to ensure the segmentation occurs in time?'
q2='Question 2: How could we test this hypothesis? How could we assess the bicoid mRNA distribution?'
q3='Question 3: What are the parameters that influence the gradient interpretation by the cells?'
q4='Question: What kind of active transport brings Bicoid from the nurse cells into the oocyte?'







c1={'f1':'Increase translation efficiency', 'correct':'Establish the gradient before translation occurs','f3':'Decrease protein size to improve its diffusion', 'f4':'None of above'}

c2={'correct':'Reverse mRNA tagged','f2':'Antibody labeling','f3':'Integrate a fluorescent protein in the genome' }

c3={'f1':'Distance source', 'f2':'Cell competence','f3':'Exposure duration', 'correct':'All of above'}
c4={'correct':'Microtubule dependent transport', 'f2':'Actine dependent transport','f3':'Microfilament dependent transport', 'f4':'None of above'}





 
a1='<FONT COLOR="GREEN">Correct. Increase translation efficiency is not possible as Ribosome do have a translational rate which  is fixed. Establish the gradient before translation occurs reduce the time that is necessary to estabslish the protein gradient, as it is already established using mRNA. Decrease protein size could alter the protein function so this is not possible.  </font>'

a2='<FONT COLOR="GREEN">Correct. The fluorescent probe will bind the bicoid mRNA to form a double strand mRNA which would allow us to see where this mRNA is present inside the embryo. We cannot use antibodies as they bind to proteins but not to nucleic acid. Integrate a fluorescent probe in the genome could have worked. However, this requires to modify the nurse cells DNA which is way more complex. </font>'

a3='<FONT COLOR="GREEN">Correct. By definition morphogens act differentially on cells depending on their concentration. However it became clear that differential interpretation of morphogens depends not only on the <strong>level of signaling</strong> i.e. the distance from the source but also on the signaling dynamic in particular the <strong>duration of the signal</strong>. Finally, the presence of morphogen itself is not enough to induce a response and require the <strong>specific competence of receiving cells</strong>.</font>'

a4='<FONT COLOR="GREEN">Correct. Microtubule are the cytoskeleton element involved in transport through the cell. Actin filaments are filaments... </font>'


