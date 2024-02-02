# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:49:50 2023

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.getcwd()
os.chdir("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project")
os.getcwd()

Covid_Data = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project\\COVID-19_Cases.csv")
Covid_Data_CountyCases = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project\\United_States_COVID-19_Community_Levels_by_County.csv")
County_PopulationDensity = pd.read_csv("C:/Users/DELL/Downloads/AIT Project Files/Population_Densities_County.csv")
County_PopulationDensity

Covid_Data_CountyCases.head(10)
Dataframe1 = Covid_Data_CountyCases[["health_service_area", "covid_cases_per_100k","county","state","county_population","health_service_area_population"]]
Dataframe1.head(5)


#County Vs County Population
Dataframe1_grouped_county = Dataframe1.groupby("county")['covid_cases_per_100k'].mean()
Dataframe1_grouped_county.head(5)
Dataframe1_grouped_county.index
Dataframe1_grouped_county =Dataframe1_grouped_county.reset_index()
Dataframe1_grouped_county.columns

Dataframe1_grouped_county = Dataframe1_grouped_county.sort_values(by='covid_cases_per_100k', ascending=False)


County_top20 = Dataframe1_grouped_county.head(20)
County_top20
County_bottom20 = Dataframe1_grouped_county.tail(20)



County_top20 = pd.merge(County_top20, Covid_Data_CountyCases[["county", "county_population"]], on="county")
County_bottom20 = pd.merge(County_bottom20, Covid_Data_CountyCases[["county", "county_population"]], on="county")

#plots
fig, ax = plt.subplots()
ax.bar(County_top20.county, County_top20['covid_cases_per_100k'], color='red')
ax.set_xlabel("County")
ax.set_ylabel("Average COVID Cases per 100k", color='red')
ax.tick_params(axis='y', labelcolor='red')
ax.set_title("Top 20 Counties \n with the Highest Average COVID Cases per 100k")
plt.xticks(rotation=90)
plt.show()

fig, ax = plt.subplots()
ax.bar(County_top20.county, County_top20['county_population'], color='blue', alpha=0.5)
ax.set_xlabel("County")
ax.set_ylabel("County Population", color='blue')
ax.tick_params(axis='y', labelcolor='blue')
ax.set_title("Population of Top 20 Counties \n with the Highest Average COVID Cases per 100k")
plt.xticks(rotation=90)
plt.show()

fig, ax = plt.subplots()
ax.bar(County_bottom20.county, County_bottom20['covid_cases_per_100k'], color='red')
ax.set_xlabel("County")
ax.set_ylabel("Average COVID Cases per 100k", color='red')
ax.tick_params(axis='y', labelcolor='red')
ax.set_title("20 Counties \n with the Lowest Average COVID Cases per 100k")
plt.xticks(rotation=90)
plt.show()

fig, ax = plt.subplots()
ax.bar(County_bottom20.county,County_bottom20['county_population'], color='blue', alpha=0.5)
ax.set_xlabel("County")
ax.set_ylabel("County Population", color='blue')
ax.tick_params(axis='y', labelcolor='blue')
ax.set_title("Population of Top 20 Counties \n with the Lowest Average COVID Cases per 100k")
plt.xticks(rotation=90)
plt.show()

#Population_Density
County_PopulationDensity = County_PopulationDensity.sort_values(by='Pop_sq_mi',ascending=False)
County_PopulationDensity_top20=County_PopulationDensity.head(20)
County_PopulationDensity_Bottom20=County_PopulationDensity.tail(20)


County_PopulationDensity_top20.plot.bar(x='County_name',y='Pop_sq_mi')
plt.title("Top 20 Counties \n with the Highest Population Density")
plt.xlabel("County")
plt.ylabel("Population Density")
plt.show()

County_PopulationDensity_Bottom20.plot.bar(x='County_name',y='Pop_sq_mi')
plt.title("Bottom 20 Counties \n with the Highest Population Density")
plt.xlabel("County")
plt.ylabel("Population Density")
plt.show()

Dataframe2 = Covid_Data_CountyCases[["covid_19_community_level", "covid_cases_per_100k"]]
Dataframe2_grouped = Dataframe2.groupby("covid_19_community_level").mean()
Dataframe2_grouped

Dataframe2_grouped.plot(kind="bar")
plt.title("covid_19_community_level VS Average covid_cases_per_100k")
plt.xlabel("County")
plt.ylabel("Average COVID Cases per 100k")
plt.show()

Covid_Data_CountyCases.boxplot(column='covid_cases_per_100k', by='state', figsize=(10,5))
plt.xlabel('State')
plt.xticks(rotation=90)
plt.ylabel('COVID-19 Cases per 100k')
plt.title('COVID-19 Cases by State')
plt.show()


Q1 = Covid_Data_CountyCases['covid_cases_per_100k'].quantile(0.25)
Q3 = Covid_Data_CountyCases['covid_cases_per_100k'].quantile(0.75)
IQR = Q3 - Q1
IQR

# Determine the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Removing data points that are below lower bound or above the upper bound
Dataframe_box = Covid_Data_CountyCases[(Covid_Data_CountyCases['covid_cases_per_100k'] > lower_bound) & (Covid_Data_CountyCases['covid_cases_per_100k'] < upper_bound)]
Dataframe_box

# Boxplot of COVID-19 cases per 100k by state by removing outliers
Dataframe_box.boxplot(column='covid_cases_per_100k', by='state', figsize=(10,5))
plt.xlabel('State')
plt.xticks(rotation=90)
plt.ylabel('COVID-19 Cases per 100k')
plt.title('COVID-19 Cases by State')
plt.show()

Covid_Data = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project\\COVID-19_Cases.csv")


Demographic_Data = Covid_Data[['current_status', 'res_county']]

Demographic_Data = Demographic_Data.groupby(['res_county', 'current_status']).size().reset_index(name='count')
Demographic_Data.head(10)

Demographic_Data = Demographic_Data.pivot(index='res_county', columns='current_status', values='count')
Demographic_Data.head(10)


Top_20_counties = Demographic_Data.sum(axis=1).nlargest(20).index
Demographic_Data_filtered = Demographic_Data.loc[Top_20_counties]


Demographic_Data_filtered.plot(kind='bar', stacked=True)
plt.title('Number of Laboratory-confirmed cases and Probable cases by county (Top 20 counties)')
plt.xlabel('County')
plt.ylabel('Number of cases')
plt.legend(title='Case Status')
plt.show()


#age

Demographic_Data_age = Covid_Data[['current_status', 'age_group']]


Demographic_Data_age = Demographic_Data_age.groupby(['age_group', 'current_status']).size().reset_index(name='count')
Demographic_Data_age.head(10)

Demographic_Data_age = Demographic_Data_age.pivot(index='age_group', columns='current_status', values='count')
Demographic_Data_age.head(10)


Demographic_Data_age.plot(kind='bar', stacked=True)
plt.title('Number of Laboratory-confirmed cases and Probable cases by age')
plt.xlabel('Age_Group')
plt.ylabel('Number of cases')
plt.legend(title='Case Status')
plt.show()

#sex
Demographic_Data_sex = Covid_Data[['current_status', 'sex']]
Demographic_Data_sex
Demographic_Data_sex = Demographic_Data_sex.drop(Demographic_Data_sex[(Demographic_Data_sex['sex'] == 'Missing') | (Demographic_Data_sex['sex'] == 'Unknown')].index)
Demographic_Data_sex.head(20)

Demographic_Data_sex = Demographic_Data_sex.groupby(['sex', 'current_status']).size().reset_index(name='count')
Demographic_Data_sex.head(10)

Demographic_Data_sex = Demographic_Data_sex.pivot(index='sex', columns='current_status', values='count')
Demographic_Data_sex.head(10)


Demographic_Data_sex.plot(kind='bar', stacked=True)
plt.title('Number of Laboratory-confirmed cases and Probable cases by sex')
plt.xlabel('SEX')
plt.ylabel('Number of cases')
plt.legend(title='Case Status')
plt.show()

#race

Demographic_Data_race = Covid_Data[['current_status', 'race']]
Demographic_Data_race
Demographic_Data_race = Demographic_Data_race.drop(Demographic_Data_race[(Demographic_Data_race['race'] == 'Missing') | (Demographic_Data_race['race'] == 'Unknown')].index)
Demographic_Data_race.head(20)

Demographic_Data_race = Demographic_Data_race.groupby(['race', 'current_status']).size().reset_index(name='count')
Demographic_Data_race.head(10)

Demographic_Data_race = Demographic_Data_race.pivot(index='race', columns='current_status', values='count')
Demographic_Data_race.head(10)

Demographic_Data_race.plot(kind='bar', stacked=True)
plt.title('Number of Laboratory-confirmed cases and Probable cases by Race')
plt.xlabel('RACE')
plt.ylabel('Number of cases')
plt.legend(title='Case Status')
plt.show()

#ethnicity
Demographic_Data_ethnicity = Covid_Data[['current_status', 'ethnicity']]
Demographic_Data_ethnicity
Demographic_Data_ethnicity = Demographic_Data_ethnicity.drop(Demographic_Data_ethnicity[(Demographic_Data_ethnicity['ethnicity'] == 'Missing') | (Demographic_Data_ethnicity['ethnicity'] == 'Unknown')].index)
Demographic_Data_ethnicity.head(20)

Demographic_Data_ethnicity = Demographic_Data_ethnicity.groupby(['ethnicity', 'current_status']).size().reset_index(name='count')
Demographic_Data_ethnicity.head(10)

Demographic_Data_ethnicity = Demographic_Data_ethnicity.pivot(index='ethnicity', columns='current_status', values='count')
Demographic_Data_ethnicity.head(10)


Demographic_Data_ethnicity.plot(kind='bar', stacked=True)
plt.title('Number of Laboratory-confirmed cases and Probable cases by ethnicity')
plt.xlabel('Ethnicity')
plt.ylabel('Number of cases')
plt.legend(title='Case Status')
plt.show()


import pandas as pd
import seaborn as sns
Covid_Data_Vaccinations = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project\\COVID-19_Vaccinations_in_the_United_States_County.csv")
data = Covid_Data_Vaccinations[['Recip_County', 'Series_Complete_Pop_Pct', 'Administered_Dose1_Pop_Pct']]
county_data = data.groupby(['Recip_County']).mean()

color_palette = sns.color_palette('bright', len(county_data))

plt.scatter(county_data['Administered_Dose1_Pop_Pct'], county_data['Series_Complete_Pop_Pct'], c=color_palette)
plt.xlabel('Percent with at least one dose')
plt.ylabel('Percent fully vaccinated')
plt.title('COVID-19 Vaccination Rates by County')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Covid_Data_Vaccinations = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project\\COVID-19_Vaccinations_in_the_United_States_County.csv")
county_data = Covid_Data_Vaccinations.groupby(['Recip_County']).mean()
top_20_counties = county_data.sort_values(by='Series_Complete_Pop_Pct', ascending=False).head(20).index.tolist()
top_20_data = Covid_Data_Vaccinations[Covid_Data_Vaccinations['Recip_County'].isin(top_20_counties)]


sns.set_style("whitegrid")
g = sns.FacetGrid(top_20_data, col="Recip_County", col_wrap=4, height=2.5, aspect=2)
g.map(sns.lineplot, "Date", "Series_Complete_Pop_Pct")
g.set_axis_labels("Date", "")
g.set_titles("{col_name}")
g.fig.suptitle("Trend of Vaccination Rates for Top 20 Counties", y=1.05)
g.set_xticklabels(rotation=90)
g.set_ylabels("Fully Vaccinated %")
plt.show()


county_data = Covid_Data_Vaccinations.groupby(['Recip_County']).mean()
bottom_20_counties = county_data.sort_values(by='Series_Complete_Pop_Pct').head(20).index.tolist()
bottom_20_data = Covid_Data_Vaccinations[Covid_Data_Vaccinations['Recip_County'].isin(bottom_20_counties)]


sns.set_style("whitegrid")
g = sns.FacetGrid(bottom_20_data, col="Recip_County", col_wrap=4, height=2.5, aspect=2)
g.map(sns.lineplot, "Date", "Series_Complete_Pop_Pct")
g.set_axis_labels("Date", "")
g.set_titles("{col_name}")
g.fig.suptitle("Trend of Vaccination Rates for Bottom 20 Counties", y=1.05)
g.set_xticklabels(rotation=90)
g.set_ylabels("Fully Vaccinated %")
plt.show()
