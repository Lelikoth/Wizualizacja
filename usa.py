
import pandas as pd
import plotly.express as px


path = 'https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/us_states.csv'
df = pd.read_csv(path)


fig = px.choropleth(df, locations='state_code', locationmode='USA-states', color='deaths', scope='usa',
                    hover_name=df['state'], hover_data=['deaths'],
                    animation_frame='date', color_continuous_scale='reds', range_color=[0, df['deaths'].max()],
                    labels={'state_code': 'State', 'total_deaths': 'Deaths', 'date': 'Quarter', 'deaths': 'Deaths'}
                    )

fig.update_layout(
    title="Deaths in the United States",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"),
    template="ggplot2")


fig.show()
