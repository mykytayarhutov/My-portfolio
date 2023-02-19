import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [11,7]

office_df = pd.read_csv('the_office_series.csv')
office_df.head()
office_df. rename(columns = {'Unnamed: 0':'episode_number'}, inplace = True)
office_df.head()
scaled_ratings = (office_df['Ratings']-min(office_df['Ratings']))/(max(office_df['Ratings'])-min(office_df['Ratings']))
office_df.insert(loc=12, column="scaled_ratings", value=scaled_ratings)
office_df.info()
cols = []

for ind, row in office_df.iterrows():
    if row['scaled_ratings'] < 0.25:
        cols.append('red')
    elif row['scaled_ratings'] < 0.50:
        cols.append('orange')
    elif row['scaled_ratings'] < 0.75:
        cols.append('lightgreen')
    else:
        cols.append('darkgreen')
plt.scatter(x=office_df['episode_number'], y=office_df['Viewership'], c=cols)
plt.xlabel("Episode Number")
plt.ylabel("Viewership in Millions")
plt.show()
print("Colour represents the Rating of the episodes")
has_guest= []
for i in office_df['GuestStars']:
    if pd.isnull(i):
        has_guest.append(False)
    else:
        has_guest.append(True)
office_df.insert(loc=13, column="has_guest", value=has_guest)
office_df.info()
sizes = []

for ind, row in office_df.iterrows():
    if row['has_guest'] == False:
        sizes.append(25)
    else:
        sizes.append(250)
plt.scatter(x=office_df['episode_number'], y=office_df['Viewership'], c=cols, s=sizes)
plt.xlabel("Episode Number")
plt.ylabel("Viewership in Millions")
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.show()
print()
print("Colour represents the Rating of the episodes")
print("Size represents the Appearances of Guest in the episodes")