import pandas as pd
from random import choice

# vytvorí pandas data_frame
data = pd.read_csv("31.Flash_card_app/data/french_words.csv")
# data_dict = list of dicts
data_dict = data.to_dict(orient="records")
# vytiahne random dict z listu a vytlačí ho

rand_dict = choice(data_dict)
random_french = rand_dict["French"]
random_englich = rand_dict["English"]
print(random_french, random_englich)
