#Write a pandas dataframe to csv file.
import pandas as pd
import numpy as np

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

frame = pd.DataFrame(data)
frame.to_csv("out.csv", index=False)
print("Dataframe successfully written to out.csv")