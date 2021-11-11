######################################

# This script:
# - Produces counts of patients prescribed antidepressant by various demographic characteristics pre and post COVID.
# - Saves descriptive data summary table

######################################

#---------------------------------------------------------------------------------------------

## Create output directory
dir.create(here::here("output", "tables"), showWarnings = FALSE, recursive=TRUE)
#setwd("//ims.gov.uk/data/Users/GBBULVD/BULHOME23/NRajendran/Data/Desktop/DESKTOP FILES/R")
 
## Read in input data
addata<- read.csv (here::here ("output/data", "input.csv"))
#addata <- read.csv (file = "opensafelyinput2.csv")

#---------------------------------------------------------------------------------------------

## Exploring data

# Looking at variables
#names(addata)

# Other details regarding number of rows variables and variable type
#str(addata)

# Looking at variable distinct values
#unique(addata$ethnicity)
#unique(addata$imd)

#---------------------------------------------------------------------------------------------

#class(addataethimd$ethnicity)

# Reshaping data so IMD and ethnicity are renamed as categories than numbers
addataethimd <- addata
        addataethimd$ethnicity[addataethimd$ethnicity=="1"]<-"White"
        addataethimd$ethnicity[addataethimd$ethnicity=="2"]<-"Mixed"
        addataethimd$ethnicity[addataethimd$ethnicity=="3"]<-"Asian or Asian British"
        addataethimd$ethnicity[addataethimd$ethnicity=="4"]<-"Black or Black British"
        addataethimd$ethnicity[addataethimd$ethnicity=="5"]<-"Other ethnic groups"
        addataethimd$imd[addataethimd$imd=="0"]<-"NA"
        addataethimd$imd[addataethimd$imd=="1"]<-"1 most deprived"
        addataethimd$imd[addataethimd$imd=="2"]<-"2"
        addataethimd$imd[addataethimd$imd=="3"]<-"3"
        addataethimd$imd[addataethimd$imd=="4"]<-"4"
        addataethimd$imd[addataethimd$imd=="5"]<-"5 least deprived"
 

# Looking at the new distinct values of ethnicity upon reshaping
#unique(addataethimd$imd)
#unique(addataethimd$ethnicity)        

# Filter on patients on antidepressants data pre COVID
addataethimdprecov <- addataethimd %>%
        filter(ADprecovid == "1")

# Filter on patients on antidepressants data post COVID
addataethimdpostcov <- addataethimd %>%
        filter(ADpostcovid == "1")

#---------------------------------------------------------------------------------------------

# Data table should summarise count of patients on AD post COVID grouped by ethnicity

#addataethimdprecov %>% group_by(ethnicity) %>% summarise(n = n())


#Has AD prescribing by ethnic group changed pre and post covid?
addataprecovidsummaryeth <- addataethimdprecov %>%
        count(ethnicity, sort = FALSE, name = "precovpatnum")    

addatapostcovidsummaryeth <- addataethimdpostcov %>%
        count(ethnicity, sort = FALSE, name = "postcovpatnum")   

addatatotalsummaryeth <- addataethimd %>%
        count(ethnicity, sort = FALSE, name = "totalethpatnum")


#Has AD prescribing by sex and ethnic group changed pre and post covid?
addataprecovidsummaryethsex <- addataethimdprecov %>%
        count(ethnicity, sex, sort = FALSE, name = "precovpatnum")    

addatapostcovidsummaryethsex <- addataethimdpostcov %>%
        count(ethnicity, sex, sort = FALSE, name = "postcovpatnum")    

#Has AD prescribing by sex changed pre and post covid?
addataprecovidsummarysex <- addataethimdprecov %>%
        count(sex, sort = FALSE, name = "precovpatnum")    

addatapostcovidsummarysex <- addataethimdpostcov %>%
        count(sex, sort = FALSE, name = "postcovpatnum")    

#Has AD prescribing by age changed pre and post covid?
addataprecovidsummaryage <- addataethimdprecov %>%
        count(ageprecovid, sort = FALSE, name = "precovpatnum")    

addatapostcovidsummaryage <- addataethimdpostcov %>%
        count(agepostcovid, sort = FALSE, name = "postcovpatnum")  

#Has AD prescribing by IMD changed pre and post covid?
addataprecovidsummaryIMD <- addataethimdprecov %>%
        count(imd, sort = FALSE, name = "precovpatnum")    

addatapostcovidsummaryIMD <- addataethimdpostcov %>%
        count(imd, sort = FALSE, name = "postcovpatnum")   

#---------------------------------------------------------------------------------------------

# Creating graphs to show pre and post covid summaries

# Need to join the pre and post covid summary datasets to have both graph input data in single table
# Join on ethnicity

#names(addataprecovidsummary)
#names(addatapostcovidsummary)

addatatoplot <- addataprecovidsummaryeth %>%
        left_join(., addatapostcovidsummaryeth, by = "ethnicity") %>%
        left_join(., addatatotalsummaryeth, by = "ethnicity")

# Bar Plots

addatatoplot %>% 
ggplot (aes(x=ethnicity, y=precovpatnum)) + 
        geom_bar(stat = "identity", fill = "#581845") + 
        coord_flip()+
        theme_bw()+
        ggtitle("Impact of COVID-19 on ethnicity and antidepressant prescribing: pre-covid prescribing") +
        labs(y="Patient numbers", x = "Ethnicity") 
#        scale_fill_brewer(palette = "Pastel1")

addatatoplot %>% 
        ggplot (aes(x=ethnicity, y=postcovpatnum)) + 
        geom_bar(stat = "identity", fill = "#69B6B3") + 
        coord_flip()+
        theme_bw()+
        ggtitle("Impact of COVID-19 on ethnicity and antidepressant prescribing: post-covid prescribing") +
        labs(y="Patient numbers", x = "Ethnicity") 
#        scale_fill_brewer(palette = "Pastel1")

write.csv (addatatoplot,file=here::here("output","tables","tables.csv"))
        





