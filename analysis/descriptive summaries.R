######################################

# This script:
# - Produces counts of patients prescribed antidepressant by various demographic characteristics pre and post COVID.
# - Saves descriptive data summary table

######################################

#Only need to run this code if packages not already installed
install.packages("dplyr") #useful for manipulating data, makes code easier to write
install.packages("reshape")
install.packages("varhandle") # converting factors to numeric variables?
install.packages("tidyverse")

#Need to run this each time to bring in R packages
library(dplyr)
library(reshape)
library(varhandle)
library(tidyverse)
