import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')
df


# Create Scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])



# With this linear function, we are able to predict the sea level behaviour. 
# To see if it is correct we can check the fit in to the data plotting the data and the linear regression. 
# We use the statistical data visualization package Seaborn.
y2=Lin_Reg.intercept + Lin_Reg.slope * df['Year']
sns.scatterplot(x='Year',y='CSIRO Adjusted Sea Level',data=df,label='CSIRO Sea Level')
sns.lineplot(x='Year',y= y2,data=df,color='r',label='fitted line')
plt.title('Sea Level by CSIRO')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')


# We see that the fit of the linear function is correct, but the data suffer an important growth in the last decade. 
# For this reason we consider values above the year 2000 and we compute again the linear regression for this data.

df_last = df[df['Year']>=2000]
Lin_Reg_Last = linregress(x=df_last['Year'], y=df_last['CSIRO Adjusted Sea Level'])
print(Lin_Reg_Last)



# Now we plot the new linear regression together with the data of the last decade until 2050, 
# in this way we can approximately predict the value of the sea level at this years.
x1= df_last['Year']
y1=df_last['CSIRO Adjusted Sea Level']
x2=np.arange(2000,2051)
y2=Lin_Reg_Last.intercept + Lin_Reg_Last.slope*x2
plt.scatter(x1, y1, label='CSIRO Sea Level')
plt.plot(x2, y2, label='fitted line',color='r')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Sea Level by CSIRO Until Year 2050')
plt.legend()
# Save and show the plot
plt.savefig('sea_level_plot.png')
plt.show()




val_2050 = Lin_Reg_Last.intercept + Lin_Reg_Last.slope*2050
print(val_2050)

# We expect in 2050  that the sea level will be 15.38 inches above the normalized value (Year=1880)







