import pandas as pd
import pickle

# Create a sample DataFrame
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [10, 20, 30, 40, 50],
    'Target': [0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Save the DataFrame to a .plk file
with open('sample_data.plk', 'wb') as file:
    pickle.dump(df, file)
