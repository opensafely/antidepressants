######################################

# Some covariates used in the study are created from codelists of clinical conditions or 
# numerical values available on a patient's records.
# This script fetches all of the codelists identified in codelists.txt from OpenCodelists.

######################################


# --IMPORT STATEMENTS--

# Import code building blocks from cohort extractor package
from cohortextractor import (codelist, codelist_from_csv, combine_codelists)


# --CODELISTS--

# Antidepressants - All
#antidepressantsall_codes = codelist_from_csv(
#  "codelists/user-nish0119-antidepressant-drugs-all-bnf-chapter-4-section-3.csv",
#  system = "snomed",
#  column = "dmd_id",
#)

# Antidepressants - SSRI
antidepressantsall_codes = codelist_from_csv(
  "codelists/opensafely-selective-serotonin-reuptake-inhibitors-dmd.csv",
  system = "snomed",
  column = "dmd_id",
)

ethnicity_codes = codelist_from_csv(
    "codelists/opensafely-ethnicity.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_6",
)