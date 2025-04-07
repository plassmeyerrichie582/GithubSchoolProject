import pandas as pd
import numpy as np

# Example data: students and their grades
data = {
    'student_id': [101, 102, 103, 104],
    'grade': ['A+', 'B', 'C+', 'D'],
}

df_students = pd.DataFrame(data)
print(df_students)
