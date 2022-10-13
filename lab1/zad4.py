# Julia Krysiak

import pandas as pd

names = ['Julia', 'Maria', 'Natalia', 'Sylwia', 'Alicja']
surnames = ['Krysiak', 'Nowak', 'Kowalska', 'Wolna', 'Miła']
ages = [21, 23, 31, 18, 41]
sexes = ['K', 'K', 'K', 'K', 'K']

df = pd.DataFrame({"name": names, "surname": surnames, "age": ages, "sex": sexes})

df.info(verbose=True)

print(df.describe(include='all'))

print(df.head(3))
