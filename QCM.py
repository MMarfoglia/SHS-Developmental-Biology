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

q1='Question 1: What is the function of siRNA in a siRNA screen?'
q2='Question 2: How could we impact the gradient to ensure the segmentation occurs in time?'
q3='Question 3: How could we test this hypothesis? How could we assess the bicoid mRNA distribution?'
q4='Question 4: What do you observe when changing the Diffusion coefficient?'
q5='Question 5: What do you think k coefficient is?'

q6= 'Question 6: What do you expect if we consider the effector activation for which the transcription factor has a low affinity?'
q8= 'Question 8: Will it impact the gradient shape?'
q7= 'Question 7: Same question for high affinity?'
q9='Question 9: Do you expect that the size of the C cell identity domain (without effectors activation) necessarily increase?'
q10='Question 10: Given activation threshold, what do you expect at a duration exposure t2>t1?'
q11='Question 11: Which of the following parameters does not impact the gradient shape?'
q12='Question 12: What are the parameters that influence the gradient interpretation by the cells?'


c1={'f1':'To label mRNA' ,'correct':'To inhibit proteins by degrading their mRNA' , 'f3':'To increase different proteins mRNA' , 'f4':'To degrade DNA' }

c2={'f1':'Increase translation efficiency', 'correct':'Establish the gradient before translation occurs','f3':'Decrease the protein size to improve its diffusion'}

c3={'correct':'Use a complementary mRNA tagged', 'f2':'Antibody labeling of targeted mRNA', 'f3':'Integrate a fluorescent protein in the genome' }

c4={'f1':'The initial and final concentrations change', 'correct':'The slopes increase when D increases', 'f3':'The equilibrium is different regarding D'}

c5={'f1':'Cell Division' ,'f2':'Actin dependent transport of proteins' , 'correct':'Protein Degradation' }
c6={'f1':'Activated at low morphogen level only', 'correct':'Activated at high morphogen level only', 'f2':'Activated at low and high morphogen levels'}
c7={'f1':'Activated at low morphogen level only', 'f2':'Activated at high morphogen level only', 'correct':'Activated at low & high morphogen levels'}
c8={'f1':'Yes','correct':'No'}
c9={'f1':'Yes','correct':'No'}
c10={'correct':'Domain A will become larger.','f1':'Domain A will remain the same','f2':'Domains A will become smaller'}
c11={'f1':'Initial concentration', 'f2':'Degradation rate of the morphogen', 'correct':'Cell competence', 'f3':'Diffusion coefficient'}
c12={'f1':'Distance source', 'f2':'Cell competence','f3':'Exposure duration', 'correct':'All of above'}




a1='<FONT COLOR="GREEN">Correct. This screen relies on siRNA, which are small RNA leading to specific knock-off of gene. The siRNA is a small RNA of 21 nucleotides that binds to its targeted mRNA and leads to this mRNA degradation. This results into the absence of the protein of interest. This type of screen is widely use in Biology to discover new regulators of different genetic pathways. </font>'
a2='<FONT COLOR="GREEN">Correct. Increase translation efficiency is not possible as Ribosomes do have a translational rate which  is fixed. Establish the gradient before translation occurs would reduce the time that is necessary to estabslish the protein gradient. To do so, it is possible to establish a mRNA gradient. Decrease protein size could alter the protein function as it could remove important amino acids, so this is not possible.  </font>'

a3='<FONT COLOR="GREEN">Correct. The fluorescent probe will bind the bicoid mRNA to form a double strand mRNA which would allow us to see where this mRNA is present inside the embryo. We cannot use antibodies as they bind to proteins but not to nucleic acid. Integrate a fluorescent probe in the genome could have worked. However, this requires to modify the nurse cells DNA which is way more complex. </font>'

a4='<FONT COLOR="GREEN">Correct. Increasing the Diffusion coefficient leads to an increase of the slopes of the curven which tends to be linear the more D increases. The equilibrium is the independent of D, as it only depends on the initial concentration.  </strong>.</font>'

a5='<FONT COLOR="GREEN">Correct. This coefficient is the degradation coefficient. Proteins are transitory structures that are degraded constantly within the cell. Cell division coefficient could affect the gradient, but it does not affect the concentration, it affects the length of the diffusing area x. An active transport of proteins would be possible, however, actin are not the cell microfilaments responsible for such a transport.  </strong>.</font>'

a6='<FONT COLOR="GREEN">Correct. The transcription effector can only bind at a high concentration it means at a high concentration of morphogen.  </strong>.</font>'
a7='<FONT COLOR="GREEN">Correct. As the binding affinity of The transcription effector is high it can bind to the promoter of the effector either at high or low concentrations. It means that the effector would be activated at low and high concentrations of morphogen.  </strong>.</font>'

a8='<FONT COLOR="GREEN">Correct. As the presence or absence of the receptor only impact how the cells perceive the morphogen signal the differential competence of the cell will not impact the gradient shape.</strong>.</font>'

a9='<FONT COLOR="GREEN">Correct. The size of the C cell identity domain will increase only when the cells that are exposed to a sufficient morphogen concentration to activate effectors become "non competent cells".</strong>.</font>'

a10='<FONT COLOR="GREEN">Correct. If we suppose that all the cells are equally competent and the activation threshold for specific factors do not change, an increase in duration exposure of morphogen will increase the overall signal level which is perceived by the cells. Therefore A cell identity domain will become larger as a larger part of the tissue would be exposed to a morphogen concentration higher than A activation threshold. </strong>.</font>'

a11= '<FONT COLOR="GREEN">Correct. The cell competence has an impact on the way the cells respond to morphogen signaling not on the gradient itself.</strong>.</font>'

a12='<FONT COLOR="GREEN">Correct. By definition morphogens act differentially on cells depending on their concentration. However it became clear that differential interpretation of morphogens depends not only on the <strong>level of signaling</strong> i.e. the distance from the source but also on the signaling dynamic in particular the <strong>duration of the signal</strong>. Finally, the presence of morphogen itself is not enough to induce a response and require the <strong>specific competence of receiving cells</strong>.</font>'