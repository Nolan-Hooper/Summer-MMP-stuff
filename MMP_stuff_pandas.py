# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:48:49 2020

@author: hoopd
"""

import pandas
assignment_list=["People dying or getting sick","People recovering","My personal risk of becoming infected","My support of government recommendations and regulations","Me feeling contempt, outrage, anger","Me feeling worry, fear, helplessness","Me feeling sympathy, sadness, regret","People breathing, sneezing, or coughing", "People touching things", "People gathering","Returning home or to work from infected areas","Infected people don't know they are spreading virus","Young people not feeling at risk","People don't understand situation","Social Distancing/ Shelter in Place / Closure of non-essential businesses","Curbside carryout (restaurants, stores)","COVID-19 testing","Practicing hygiene/handwashing","Wearing Masks","Developing a vaccine","Herd Immunity (virus cannot spread because many people are immune)","Media coverage","Timely and reliable information","Poverty","Homelessness","Access to free healthcare for COVID-19 patients","Coordinated, national-level response", "Economic Downturn / Recession","People losing jobs", "Government financial support for businesses", "Government financial support for families"]
DF=pandas.read_csv("Master Table all on one sheet.csv")
DF["From assignment (1=yes, 0=no)"]=DF["Node Text"].apply(lambda x: 1 if x in assignment_list else 0)
DF.write_csv("Panda Table for MMP FIles.csv")