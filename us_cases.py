import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Lelikoth/Wizualizacja/main/us_states.csv')
df = df.dropna()


fig  = px.scatter_geo(df,
                      locations="state_code",
                      size="cases",
                      locationmode="USA-states",
                      hover_data=["state", "cases"],
                      labels={"cases": "Cases", "state": "State", "state_code": "State code", "Date": "Quarter"},
                      animation_frame="date",
                      )


fig.update_layout(
    title="Covid-19 Cases in the USA",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    geo=dict(
        scope='usa',
        projection_type='albers usa'
    ),
    template="ggplot2",
)

fig.show()