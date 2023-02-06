# load libraries
library(dplyr)
library(ggcorrplot)
library(plotly)

install.packages('dplyr')
install.packages('ggcorrplot')
install.packages('plotly')

tr = read.csv(file ="C:\\Users\\bhavi\\OneDrive\\Desktop\\Documents\\INFS 580\\Crash_Incidents.csv")
summary(tr)
head(tr)

df <- data.frame(tr)



