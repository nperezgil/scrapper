import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import io
import matplotlib.pyplot as plt
import csv
import os


dd = pd.read_csv("population_spain_dataset.csv")
# pirámide poblacional 2020
mujeres = dd.loc[(dd['Sexo'] == 'Mujeres') & (dd['Edad'] != 'Todas las edades') & (dd['Periodo'] == 2020) & (dd['Lugar'] == 'Total Nacional') & (dd['Nacimiento'] == 'Total'), 'Total'].values
hombres = dd.loc[(dd['Sexo'] == 'Hombres') & (dd['Edad'] != 'Todas las edades') & (dd['Periodo'] == 2020) & (dd['Lugar'] == 'Total Nacional') & (dd['Nacimiento'] == 'Total'), 'Total'].values
total = dd.loc[(dd['Sexo'] == 'Total') & (dd['Edad'] != 'Todas las edades') & (dd['Periodo'] == 2020) & (dd['Lugar'] == 'Total Nacional') & (dd['Nacimiento'] == 'Total'), 'Total'].values


y = range(0, len(mujeres))
x_male = hombres
x_female = mujeres

#define plot parameters
fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))

#specify background color and plot title
fig.patch.set_facecolor('xkcd:light grey')
plt.figtext(.5,.9,"Piramide poblacional 2020 ", fontsize=15, ha='center')

#define male and female bars
axes[0].barh(y, x_male, align='center', color='blue')
axes[0].set(title='Hombres')
axes[1].barh(y, x_female, align='center', color='green')
axes[1].set(title='Mujeres')

#adjust grid parameters and specify labels for y-axis
axes[1].grid()
axes[0].set(yticks=y, yticklabels=dd['Edad'].unique().tolist()[1:])
axes[0].invert_xaxis()
axes[0].grid()

#display plot
plt.show()
