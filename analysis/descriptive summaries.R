######################################

# This script:
# - Produces counts of patients prescribed antidepressant by various demographic characteristics pre and post COVID.
# - Saves descriptive data summary table

######################################

# Need to run this each time to bring in R packages
library(dplyr)
library(reshape)
library(varhandle)
library(tidyverse)

# Create output directory
dir.create(here::here("output", "tables"), showWarnings = FALSE, recursive=TRUE)

# Read in input data
addata <- read.csv ("input.csv")



