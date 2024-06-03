import pandas as pd
import numpy as np

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

frame = pd.DataFrame(data)
print(type(frame))

arr = frame.to_numpy()
print(type(arr))