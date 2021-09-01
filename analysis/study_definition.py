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

# --STUDY POPULATION AND STUDY VARIABLES--
# Defines the study population of interest and variables to extract

    # --DEFINES DATA BEHAVIOUR--
study = StudyDefinition(
    default_expectations={
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
            return_expectations={
                "rate": "universal",
                "int": {"distribution":"population_ages"},
        }
    ),

    agepostcovid = patients.age_as_of(
        "2021-03-01",
        return_expectations={
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

)
