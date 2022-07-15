import pandas as pd
import plotly.express as px


#Write a Python program to get the Chinese province wise cases of confirmed, deaths and recovered cases of Novel Coronavirus (COVID-19). (4)


cov_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
cov_data = cov_data[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
sorted_data = cov_data.sort_values(by='Province/State', ascending=True)   #zapis po abecedi od država
sorted_data = sorted_data.reset_index(drop=True)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(sorted_data)

#Write a Python program to visualize the state/province wise death cases of Novel Coronavirus (COVID-19) in USA.(11)

cov_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
usa_data = cov_data[cov_data['Country/Region']=='US'] #paramentri
usa_data = usa_data.groupby(['Province/State'])['Deaths'].sum().reset_index()
pd.set_option("display.max_rows", None, "display.max_columns", None)
fig = px.line(usa_data, x='Province/State', y='Deaths', title='Deaths  of COVID-19 in USA', text='Deaths') #izgled grafa
fig.show()