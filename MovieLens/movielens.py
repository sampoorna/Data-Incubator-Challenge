#import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

directory = "ML-10M/"
delim = "::"
filename = "ratings.dat"

print "Reading file.............."
data = pd.read_csv(directory+filename, delimiter=delim, header=None, names = ['userid', 'movieid', 'rating', 'timestamp'], engine = 'python')
movies = pd.read_csv(directory+ "movies.dat", delimiter = delim, header=None, names = ['movieid', 'name', 'genres'], engine = 'python')
print "...............File reading complete!"

#uniqMovies = np.unique(movies['movieid'])
#ratingsPerItem = {key: 0 for key in uniqMovies}

meanRating = np.mean(data['rating'])
print meanRating
#print "Movies in dataset ...", len(uniqMovies), " movies rated...", len(np.unique(data['movieid']))

#li = data.groupby(['movieid']).agg(['count'])
'''
uniqMovies = np.unique(data['movieid'])
rats = []
for mov in uniqMovies:
	rows = data[data['movieid'] == mov] # Rows corresponding to each movieid
	rats.append(np.count_nonzero(rows[['rating']]))
#print rats
'''

#data = data.join(movies, on='movieid', lsuffix="_x")

grouped = data.groupby(['movieid'])
li = grouped['rating'].agg({'count':np.count_nonzero, 'mean':np.mean, 'std':np.std})
countlist = grouped['rating'].agg(['count', 'mean', 'std'])
sortedcountlist = countlist.sort_values(by='count', ascending = False)
print sortedcountlist.head(10)#.join(movies, on='movieid', lsuffix="_x")
print sortedcountlist['count'].tail(10)
mns = sortedcountlist['mean'].tolist()
count = sortedcountlist['count'].tolist()
#print np.mean(mns) # 3.74888393907
#mns[:] = [x - meanRating for x in mns]
#rows = li['mean'].sort()
#print rows

### Plot of mean ratings of 100 most rated movies
#plt.figure();
#x = [i for i in range(100)]
plt.plot(mns[0:99])
plt.axhline(y=meanRating, color='r', linestyle='-')
plt.title('Mean Ratings of 100 Most-Rated Movies')
#plt.title('Mean Ratings Grouped By Movie')
plt.xlabel('Movies')
plt.ylabel('Mean Rating')
plt.savefig("100popmovies.png")
#plt.savefig("popmovies.png")

plt.clf()
plt.cla()
plt.close()
### Scatter plot of mean ratings versus number of ratings received
plt.plot(count, mns, 'o')
plt.title('Correlation between mean and frequency of ratings')
#plt.title('Mean Ratings Grouped By Movie')
plt.xlabel('Number of ratings received')
plt.ylabel('Mean Rating')
plt.savefig("corr100popmovies.png")

plt.clf()
plt.cla()
plt.close()


plt.plot(count, 'o')
plt.title("Movie Rating Frequency Distribution")
plt.xlabel("Movie")
plt.ylabel("Number of Ratings")
plt.savefig("freqdist.png")


'''
print max(rats)

plt.hist(rats, bins = 1000)
plt.title("Histogram of Movie Rating Frequency")
plt.xlabel("Number of Ratings Received")
plt.ylabel("Number of Movies")
plt.savefig("HistogramRatings_1000bins.png")
'''