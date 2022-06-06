import pandas as pd 
import plotly.express as px


df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/covid-cases.csv')
df['total_cases'] = df['total_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['total_vaccinations'] = df['total_vaccinations'].fillna(0)

df_eu = df[df['location'] == 'Europe']
df_na = df[df['location'] == 'North America']
df_sa = df[df['location'] == 'South America']
df_as = df[df['location'] == 'Asia']
df_af = df[df['location'] == 'Africa']
df_oc = df[df['location'] == 'Oceania']
df_au = df[df['location'] == 'Australia']

df_merge = pd.concat([df_eu, df_na, df_sa, df_as, df_af, df_oc, df_au])

fig = px.pie(df_merge, values='total_vaccinations', names='location', labels={'total_vaccinations': 'Vaccinations', 'location': 'Continent'},)

fig.update_layout(
    title="Vaccinations in the World by Continent",
    legend_title="Continent",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    template="ggplot2",
)

fig.show()