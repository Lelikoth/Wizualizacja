import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/covid-cases.csv')
filter = df['continent']=='Europe'
df = df.where(filter)
df['total_cases'] = df['total_cases'].fillna(0)
df['total_vaccinations'] = df['total_vaccinations'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df = df.dropna()
df['case_rate'] = round((df['total_cases'] / df['population'])*100, 2)


locations = df['location'].unique()
for x in locations:
    records = df[df['location'] == x]
    temp = 0
    for index, row in records.iterrows():
        if((row['case_rate'] != 0) & (temp < row['case_rate'])):
            temp = row['case_rate']
            df.at[index,'case_rate'] = row['case_rate']
        if(row['case_rate'] < temp):
            row['case_rate'] = temp
            df.at[index,'case_rate'] = temp

fig = px.scatter_geo(df, locations='location', locationmode='country names', 
                     scope="europe", size='case_rate',
                     #color='case_rate', 
                     #range_color=[0, 50],
                     #color_continuous_scale="Blues",
                     hover_name='location', hover_data=['date', 'total_cases'],
                     animation_frame='date'
                     )

fig.update_layout(
    title="Covid-19 Cases in Europe",
    height=700,
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    geo=dict(
        scope='europe',
        #projection_type='natural earth'
    ),
    template="ggplot2",
)

fig.show()
