import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/covid-cases.csv')
df['total_cases'] = df['total_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['total_vaccinations'] = df['total_vaccinations'].fillna(0)
df['percent_cases'] = (df['total_cases'] / df['population']).round(2)
df = df.dropna()

minimum = 0
maximum = df['percent_cases'].max()

fig = px.choropleth(df, locations="location", 
                        locationmode="country names",
                        color="percent_cases",
                        hover_data=['total_cases', 'percent_cases'],
                        color_continuous_scale="Blues",
                        range_color=[minimum, maximum],
                        animation_group="location",
                        animation_frame="date",
                        labels= {"percent_cases": "Rate", "location": "Location", "date": "Quarter", "total_cases": "Total cases"})

fig.update_layout(
    title="Covid-19 Cases in the World",
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
