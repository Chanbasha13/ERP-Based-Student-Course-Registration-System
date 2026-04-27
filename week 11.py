# WEEK 11 - Pandas
# Course report
import pandas as pd

data = {
    "Course": ["Python", "DSA", "DBMS"],
    "Students": [50, 40, 35]
}

df = pd.DataFrame(data)

print(df)