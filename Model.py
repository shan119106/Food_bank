# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:43:38 2022

@author: Admin
"""

from pulp import *
import pandas as pd
Food_bank = pd.read_excel("Data_Food_Bank_copy.xlsx",sheet_name ="FoodBank")
print(Food_bank["Name"])
agency = pd.read_excel("Data_Food_Bank_copy.xlsx",sheet_name ="Agency")
Demaind = pd.read_excel("Data_Food_Bank_copy.xlsx",sheet_name ="DemandPoints")
FbtoAgency = pd.read_excel("Data_Food_Bank_copy.xlsx",sheet_name ="FbtoAgency")
FBtoDPdist = pd.read_excel("Data_Food_Bank_copy.xlsx",sheet_name ="FBtoDdist")
DPtoAgencydist = pd.read_excel("Data_Food_Bank_copy.xlsx",sheet_name ="DPtoAgencydist")
problem = LpProblem("FoodBank",LpMinimize)
