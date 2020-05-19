# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:08:13 2020

@author: hoopd
"""
import csv
filename=open("Master Table all on one sheet.csv",'r')
fp=csv.reader(filename)
Master_table=open("Final_table.csv",'w')
next(fp,None)#skips line
assignment_list=["People dying or getting sick","People recovering","My personal risk of becoming infected","My support of government recommendations and regulations","Me feeling contempt, outrage, anger","Me feeling worry, fear, helplessness","Me feeling sympathy, sadness, regret","People breathing, sneezing, or coughing", "People touching things", "People gathering","Returning home or to work from infected areas","Infected people don't know they are spreading virus","Young people not feeling at risk","People don't understand situation","Social Distancing/ Shelter in Place / Closure of non-essential businesses","Curbside carryout (restaurants, stores)","COVID-19 testing","Practicing hygiene/handwashing","Wearing Masks","Developing a vaccine","Herd Immunity (virus cannot spread because many people are immune)","Media coverage","Timely and reliable information","Poverty","Homelessness","Access to free healthcare for COVID-19 patients","Coordinated, national-level response", "Economic Downturn / Recession","People losing jobs", "Government financial support for businesses", "Government financial support for families"]
for line in fp:
    ID=line[0]
    Cluster=line[1]
    Node=line[2]
    FA=line[3]
    if Node in assignment_list:
        FA="1"
    else: 
        FA="0"
    print("{}".format(ID),"{}".format(Cluster),"{}".format(Node),"{}".format(FA),file=Master_table)
#    print(ID,file=Master_table)
#    print(Cluster, file=Master_table)
#    print(Node, file=Master_table)
#    print(FA, file=Master_table)
filename.close()
Master_table.close()