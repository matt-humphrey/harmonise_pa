---
author: Matt Humphrey
date_completed: 26/08/2025
type: harmonisation
---

# Harmonising Anthropometric and Blood Pressure Variables

This is the first in a series of projects aiming to harmonise all the variables related to physical assessments.

## Project Structure

### data

Contains four sub-directories with the datasets...
- Original: as they were at the beginning of the project
- Raw: as they were prior to harmonising (some datasets may have been changed by other data officers while the project was underway)
- Interim: processed initially to rename and delete specified variables
- Processed: with all transformations completed to harmonise the variables across datasets

### docs

Contains all relevant information related to the project

### notebooks

A collection of Marimo notebooks both for experimentation, and in some cases, used for running the functions to create the interim and processed datasets.

### src/harmonise_pa

This is the where all code related to the project is stored.
The key files to be aware of are:
- `config/metadata.py`: where the metadata for each unique variable is defined
- `config/variables.py`: the variables specified for alteration/exploration, renaming, and deleting
- `harmonise.py`: contains all the logic/functions to change the raw data and harmonise the variables
- `validate.py`: specifies the expected values/ranges for each variable for testing
