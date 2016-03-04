# Mid Project Checkin

### Keenan Zucker and James Jang

I think it is safe to say that we were able to accomplish our goals. We were able to complete initial data exploration and visualizations that helped us understand the dataset that we acquired. We used Basemap to plot all of the earthquake activity on a map, as well as adjust different point's color and size based on magnitude and depth. This gave us a pretty good understanding of where most earthquakes were taking place, and basically mapped out where the fault lines were without looking them up! Our data explorations are [HERE](https://github.com/keenanzucker/DataScience16CTW/blob/master/James_Exploration.ipynb) and [HERE](https://github.com/keenanzucker/DataScience16CTW/blob/master/Data_Exploration_Keenan.ipynb)

One of the first tasks we accomplished was gathering up a big and relevant dataset. USGS site provided a querying tool that was limited to 20,000 hits per search so we had to manually download the earthquake data. We wrote a script, “download.py” to download all of the data for past 116 years and combined them to make a big csv file. We split our data set into half, one for training and one for testing. 

We first used latitude, longitude and depth as predictors with RandomForestClassifier and the model gave us a decent result of around 70 percent when we tested on our test set. Then we feature engineered magType, year, month and hour to improve our result. We were able to train a model that was able to predict the category of the magnitude of the earthquake given "latitude", "longitude", "depth", "magTypeClassified", "year", "month", "hour". When we tested our model on our test set, it was able to achieve a score of 85.5%.
Our code can be found -> [HERE](https://github.com/keenanzucker/DataScience16CTW/blob/master/Model%20Iteration%201.ipynb)

Our minimum viable product by next Friday will be an earthquake predictive tool that will predict the category of magnitude (minor, light, moderate, strong, major, great), rather than a specific magnitude value, over a period of time and location inputted. 

Moving forward, we'd like to have more visualization on our results our model generated rather than just our exploration. We also want to do some parameter tuning in order to increase our model's accuracy so we can better predict earthquakes magnitude and/or depth and/or location. Some of the features we want to add are the classification of the fault line for each pair of latitude and longitude. Since most of the earthquakes happen around the fault line, this classification could help us immensely. We also want to look into some sort of calculator based off of the magnitude+depth and the location to estimate the potential damage/deaths that could occur if the earthquake we predict were to happen. 


