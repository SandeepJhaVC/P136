import pandas as pd

data = pd.read_csv("final_data_with_gravity.csv")
star_name = list(data["Star_name"])

final_list = []

temp_dict = {
    "star_name" : list(data["Star_name"]),
    "distance" : list(data["Distance"]),
    "mass" : list(data["Mass"]),
    "radius" : list(data["Radius"]),
    "gravity" : list(data["Gravity"])
}

final_list.append(temp_dict)
print(final_list)