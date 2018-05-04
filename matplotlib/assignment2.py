import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
import pandas as pd
import datetime

df = pd.read_csv('921a697d63e17c1cb86364faf0d309c7fe078fabf6f3e24be2cefa47.csv', parse_dates=['Date'])
df['mm_dd']=df['Date'].dt.strftime('%m-%d')
df = df[df['mm_dd']!='02-29']   #drop leap years, since can't be compared to 
df_2008_2014=df[(df['Date']<='2014-12-31') & (df['Date']>='2008-01-01')]
df_2015=df[df['Date']>='2015-01-01']
min_vals_2008_2014=df_2008_2014[df_2008_2014['Element']=='TMIN'].groupby(['mm_dd'], sort=True)['Data_Value'].min()
max_vals_2008_2014=df_2008_2014[df_2008_2014['Element']=='TMAX'].groupby(['mm_dd'], sort=True)['Data_Value'].max()
min_vals_2015=df_2015[df_2015['Element']=='TMIN'].groupby(['mm_dd'], sort=True)['Data_Value'].min()
max_vals_2015=df_2015[df_2015['Element']=='TMAX'].groupby(['mm_dd'], sort=True)['Data_Value'].max()
minmax_df=pd.concat([min_vals_2008_2014, max_vals_2008_2014, min_vals_2015, max_vals_2015], 
            axis=1,keys=['min_2008_2014', 'max_2008_2014', 'min_2015', 'max_2015'])
minmax_df=minmax_df.transform(lambda x:x/10)
minmax_df.index='2015-'+minmax_df.index
minmax_df.index=pd.to_datetime(minmax_df.index, format='%Y-%m-%d')

plt.plot(minmax_df.index, minmax_df['min_2008_2014'], 'k', 
        minmax_df.index,minmax_df['max_2008_2014'], 'k', alpha=0.2, label='Temperature range 2008-2014')
hotter_2015=minmax_df[minmax_df['max_2015']>minmax_df['max_2008_2014']]
plt.scatter(hotter_2015.index, hotter_2015['max_2015'], c='r', 
        s=10, label='Hotter in 2015 ('+str(len(hotter_2015))+' days)')
colder_2015=minmax_df[minmax_df['min_2015']<minmax_df['min_2008_2014']]
plt.scatter(colder_2015.index, colder_2015['min_2015'], c='b', 
        s=10, label='Colder in 2015 ('+str(len(colder_2015))+' days)')
ax=plt.gca()
ax.fill_between(minmax_df.index, minmax_df['min_2008_2014'], minmax_df['max_2008_2014'], 
        alpha=0.2, color='lightslategray')
ax.set_xlim([datetime.date(2015, 1, 1), datetime.date(2015, 12, 31)])
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('%b'))
plt.ylabel('Temperature(°C)')
plt.title('Days in 2015 exceeding temperature from 2008-2014 at Falls Church, Virginia, United States')
ax.set_frame_on(False)
ax.legend()
plt.show()

