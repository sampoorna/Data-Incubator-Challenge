#import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

directory = "ML-10M/"
delim = "::"
filename = "ratings.dat"

print "Reading file.............."
data = pd.read_csv(directory+filename, delimiter=delim, header=None, names = ['userid', 'movieid', 'rating', 'timestamp'], engine = 'python')
#movies = pd.read_csv(directory+ "movies.dat", delimiter = delim, header=None, names = ['movieid', 'name', 'genres'], engine = 'python')
print "...............File reading complete!"

#uniqMovies = np.unique(movies['movieid'])
#ratingsPerItem = {key: 0 for key in uniqMovies}

meanRating = np.mean(data['rating'])
print meanRating
#print "Movies in dataset ...", len(uniqMovies), " movies rated...", len(np.unique(data['movieid']))

#li = data.groupby(['movieid']).agg(['count'])
uniqMovies = np.unique(data['movieid'])
rats = []
for mov in uniqMovies:
	rows = data[data['movieid'] == mov] # Rows corresponding to each movieid
	rats.append(np.count_nonzero(rows[['rating']]))
#print rats

grouped = data.groupby(['movieid'])
li = grouped['rating'].agg(['count', 'sum'])
print li.filter(lambda x: x.count > 2000)

	
plt.hist(rats, bins = 100)
plt.title("Histogram of Movie Rating Frequency")
plt.xlabel("Movies")
plt.ylabel("Frequency of Ratings")
plt.savefig("HistogramRatings_100bins.png")