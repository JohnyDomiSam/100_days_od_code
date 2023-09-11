import csv, pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_list = data["Primary Fur Color"].to_list()
gray_squirels = fur_color_list.count("Gray")
red_squirels = fur_color_list.count("Cinnamon")
black_squirels = fur_color_list.count("Black")
print(gray_squirels)
print(red_squirels)
print(black_squirels)
squirel_dict = {"Fur color": ["Gray", "Red", "black"], "Count": [2473, 392, 103]}
squirel_data = pandas.DataFrame(squirel_dict)
squirel_data.to_csv("squirel_data.csv")
