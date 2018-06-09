#!/usr/bin/env bash

# Code Analysis
printf "========== Coverage Report ==========\n\n"
coverage report sentimentanalyzer/tests/test_simple.py
printf "\n========== End of Coverage Report ==========\n\n\n"

printf "========== PEP8 Output ==========\n\n"
pycodestyle sentimentanalyzer
printf "\n========== End of PEP8 Output ==========\n\n\n"

printf "========== Pylint Output ==========\n\n"
pylint sentimentanalyzer
printf "\n========== End of Pylint Output ==========\n\n\n"

