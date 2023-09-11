import random, pandas

student_dict = {"student": ["caroline", "rudolf", "domiNika"], "score": [56, 78, 90]}


new_dataframe = pandas.DataFrame(student_dict)
for key, value in new_dataframe.items():
    print(value)
