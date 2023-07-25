# Recommender-System
This repository aims to make available some codes that are used in prediction algorithms that I used in my scientific research.
------------------------------------------------------------------------------------------------------------------------------
# Motivation

Currently, data permeates all areas, thus increasing the need to recommend products to the user.
Using streaming as a basis for recommending movies, we have an obstacle to solve, the amount of missing data. In this way, the aim is to answer the following question:

**How can we recommend a movie to a user?**
# Theoric Model
The methodology used is the collaborative filtering of similar k-tops.
Applying two models:
* Users
* Items
Such an application uses the similarity of users and items to support its recommendation.
# Methodology
Two data sources:
* Amazon Movie Ratings
* Movilens-100k-dataset
Language used:
* python
Artificially created data - test functions
## Similarity
Using Pearson's Correlation and Cosine Correlation
The correlation between users based on the scores assigned to each film was computed.
Thus, using the correlation function offered by the package, the user correlation matrix was generated.
## Separating similar users
Using the criterion of k similar neighbors, indicated by the correlation, it was grouped into groups of k neighbors for each user.
## Separating the ratings
It is extremely important to take into account the bias of each user when evaluating a film, considering that there is no scale, the value of that film was subtracted by the average of the ratings values for all films of that user.
## Ratings before bias adjustment
The calculation used for the evaluation of any user u and a movie v is given by the formula below, which represents the weighted average of the ratings of the movie v for all neighbors of u.
## Post-bias adjustment rating
Finally, to obtain the rating value, it is necessary to add to the previously found value, the average of the ratings for that user.
## Observations
For didactic purposes, it was decided to reduce the database using an evaluation criterion for each user of at least 30 films.
It was separated into test and training, using the test to better understand the application of the methodology.
The second database was initially used.
## Conclusion
For the understanding and application of the algorithm, there was a necessary computational knowledge involved, in addition to the investigation and treatment of missing data.
As k=5 was used, it was noticed that all films were able to be predicted so that there was an attempt to use the RMSE, but this statistic did not prove to be robust for the current database.
Therefore, in the future it is intended to study the RMSE and MAE for the data. Furthermore, it is intended to scale the functions for a larger volume of data.
