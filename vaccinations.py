import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/covid-cases.csv')
df['total_vaccinations'] = df['total_vaccinations'].fillna(0)
df['vaccinations_rate'] = round((df['total_vaccinations'] / df['population']) * 100, 2)
locations = df['location'].unique()

for x in locations:
    records = df[df['location'] == x]
    temp = 0
    for index, row in records.iterrows():
        if((row['vaccinations_rate'] != 0) & (temp < row['vaccinations_rate'])):
            temp = row['vaccinations_rate']
            df.at[index,'vaccinations_rate'] = row['vaccinations_rate']
        if(row['vaccinations_rate'] < temp):
            row['vaccinations_rate'] = temp
            df.at[index,'vaccinations_rate'] = temp
        #print(row['case_rate'])
df['head'] = df['location']


fig = px.choropleth(df, locations= 'location', locationmode='country names',
                    color='vaccinations_rate', color_continuous_scale="greens",
                    scope="world", 
                    animation_frame='date', range_color=[0, 200])
fig.update_layout(
    title="Covid-19 Vaccinations in the World",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    geo=dict(
        scope='world',
        projection_type='natural earth'
    ),
    template="ggplot2",
)
fig.show()


