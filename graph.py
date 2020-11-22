import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
from itertools import chain

matplotlib.rcParams['axes.formatter.useoffset'] = False

df = pd.read_excel('dataset.xlsx', sheet_name="Model")
df2 = pd.read_excel('dataset.xlsx', sheet_name="Basel")

fig = plt.figure()

plt.subplots_adjust(left=0.15, right=0.80, top=0.9, bottom=0.1)
plt.style.use('seaborn')

ax1 = fig.add_subplot(111)

ax2 = ax1.twiny()
ax3 = ax2.twinx()

plot1 = ax1.step(df["ticks"], df["riding"]*100, 'C1', label='Model')
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

plot2 = ax3.step(df2["Startdatum Woche"], df2["Fahrgäste (Einsteiger)"], 'C2', label='Basel')
xFormatter = mtick.StrMethodFormatter('{x:,.0f}')
ax3.yaxis.set_major_formatter(xFormatter)
ax2.set_ylabel('Ridership in Basel per week')

ax1.set_xlabel('Ticks (Model)')
ax1.set_ylabel('Ridership (Model)')
ax3.set_ylabel('Public Transport Entries (Basel)')
ax2.set_xlabel('Dates (Basel)')
ax2.xaxis.set_label_position('top')

formatter = mdates.DateFormatter("%m/%d")
ax2.xaxis.set_major_formatter(formatter)
ax2.grid(True)

lns = plot1+plot2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

plt.savefig("plot.pdf")
plt.savefig("plot.png")