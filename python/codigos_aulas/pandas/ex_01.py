import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

data = "21-01-2023"

pd.to_datetime(data, dayfirst=True)