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
        #find_last_date_in_period = True,  # to obtain latest date on AD preCOVID
        returning = "binary_flag"
            
    ),

    ADpostcovid = patients.with_these_medications(
        antidepressantsall_codes,
        between = ["2020-03-23", "2021-03-31"],
        #find_last_date_in_period = True, # to obtain latest date on AD preCOVID
        returning = "binary_flag"

    ),

     # ETHNICITY IN 6 CATEGORIES
    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,
        returning="category",
        find_last_match_in_period=True,
        include_date_of_match=True,
        return_expectations={
            "category": {"ratios": {"1": 0.2, "2":0.2, "3":0.2, "4":0.2, "5": 0.2}},
            "incidence": 0.75,
        },
    ),

    # ethnicity_by_16_grouping = patients.with_ethnicity_from_sus(
    #    returning = "group_16",
    #    use_most_frequent_code = True,
    #),

    imd=patients.address_as_of(
        "2020-02-29",
        returning = "index_of_multiple_deprivation",
        round_to_nearest = 100,
        return_expectations = {
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
    },
    ),

    region = patients.registered_practice_as_of (
        "2020-02-01",
        returning = "nuts1_region_name",
        return_expectations = {
            "rate": "universal",
            "category": {
            "ratios": {
                "North East": 0.1,
                "North West": 0.1,
                "Yorkshire and the Humber": 0.1,
                "East Midlands": 0.1,
                "West Midlands": 0.1,
                "East of England": 0.1,
                "London": 0.2,
                "South East": 0.2,
            },
        },
    },
    ),

)
