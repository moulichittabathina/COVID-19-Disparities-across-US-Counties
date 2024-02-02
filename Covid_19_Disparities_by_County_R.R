library(tidyverse)
library(dplyr)
library(ggplot2)

my_data <- read.csv("C:/Users/DELL/Downloads/AIT Project Files/United_States_COVID-19_Community_Levels_by_County.csv",header = TRUE)
head(my_data)
count(my_data)
my_data_no_blanks <-  na.omit(my_data)
my_data_no_blanks
count(my_data_no_blanks)

setwd("C:/Users/DELL/OneDrive/Documents/AIT Project")
write.csv(my_data_no_blanks, "United_States_COVID-19_Community_Levels_by_County.csv", row.names = FALSE)

mydata1 <- read.csv("C:/Users/DELL/Downloads/AIT Project Files/COVID-19_Cases_Feb_Month_workbook.csv",header = TRUE)
count(mydata1)
my_data_no_blanks1 <-  na.omit(mydata1)
count(my_data_no_blanks1)
write.csv(my_data_no_blanks1, "COVID-19_Cases_Feb_Month_workbook.csv", row.names = FALSE)

mydata2 <- read.csv("C:/Users/DELL/Downloads/AIT Project Files/COVID-19_Cases_March_Month.csv",header = TRUE)
count(mydata2)
my_data_no_blanks2 <-  na.omit(mydata2)
count(my_data_no_blanks2)
write.csv(my_data_no_blanks2, "COVID-19_Cases_March_Month.csv", row.names = FALSE)

mydata3 <- read.csv("C:/Users/DELL/Downloads/AIT Project Files/COVID-19_Vaccinations_in_the_United_States_County.csv",header = TRUE)
count(mydata3)
my_data_no_blanks3 <-  na.omit(mydata3)
count(my_data_no_blanks3)
write.csv(my_data_no_blanks3, "COVID-19_Vaccinations_in_the_United_States_County.csv", row.names = FALSE)

Covid_Data = read.csv("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project\\COVID-19_Cases.csv")
Covid_Data_CountyCases = read.csv("C:\\Users\\DELL\\OneDrive\\Documents\\AIT Project\\United_States_COVID-19_Community_Levels_by_County.csv")
County_PopulationDensity = read.csv("C:/Users/DELL/Downloads/AIT Project Files/Population_Densities_County.csv")



grouped_data_Covid_Data_CountyCases <- Covid_Data_CountyCases %>%
  group_by(county) %>%
  summarise(avg_cases_per_100k = mean(covid_cases_per_100k))
summary(grouped_data_Covid_Data_CountyCases$avg_cases_per_100k)
mean(grouped_data_Covid_Data_CountyCases$avg_cases_per_100k)

grouped_data_Covid_Data_CountyCases <- Covid_Data_CountyCases %>%
  group_by(county) %>%
  summarise(county_population = mean(county_population))
summary(grouped_data_Covid_Data_CountyCases$county_population)
mean(grouped_data_Covid_Data_CountyCases$county_population)


