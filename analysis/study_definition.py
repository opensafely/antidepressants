######################
# Antidepressants - health inequalities
######################

# --IMPORT STATEMENTS--
# Import/clone code building blocks from cohort extractor package

from cohortextractor import (
    StudyDefinition, 
    patients, 
    codelist,
    codelist_from_csv
    # combine_codelists, #not needed as not combining multiple code lists
    # filter_codes_by_category
)

# --DEFINE CODE LIST--
# Codelists are help within the codelist/ folder. 
# This section will import the lists from the codelists.py file

from codelists import *

# --STUDY POPULATION AND STUDY VARIABLES--
# Defines the study population of interest and variables to extract

    # --DEFINES DATA BEHAVIOUR--
study = StudyDefinition(
    default_expectations = {
        "date": {"earliest": "2000-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    # --DEFINES STUDY POPULATION--
    population = patients.registered_with_one_practice_between(
        "2019-03-01", "today"
    ),

    # --DEFINES STUDY VARIABLES--
    ageprecovid = patients.age_as_of(
        "2020-03-01",
        return_expectations = {
            "rate": "universal",
            "int": {"distribution":"population_ages"},
        }
    ),

    agepostcovid = patients.age_as_of(
        "2021-03-01",
        return_expectations = {
            "rate": "universal",
            "int": {"distribution":"population_ages"},
        }
    ),

    sex = patients.sex(
        return_expectations = {
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),

    ADprecovid = patients.with_these_medications(
        antidepressantsall_codes,
        between = ["2019-03-01", "2020-03-22"],
        return_last_date_in_period = True,  # to obtain latest date on AD preCOVID
        returning = "binary_flag"
            
    ),

    ADpostcovid = patients.with_these_medications(
        antidepressantsall_codes,
        between = ["2020-03-23", "2021-03-31"],
        return_last_date_in_period = True, # to obtain latest date on AD preCOVID
        returning = "binary_flag"

    ),

    ethnicity_by_16_grouping=patients.with_ethnicity_from_sus(
        returning="group_16",
        use_most_frequent_code = True,
    ),


)
