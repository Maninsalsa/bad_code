# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+

import pandas as pd

# .head() version

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(n=3)

# How to call this function:
employees = pd.DataFrame(...)
selectFirstRows(employees)

# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.iloc(n=3)

