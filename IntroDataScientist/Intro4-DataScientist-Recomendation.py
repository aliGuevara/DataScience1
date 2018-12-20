import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# fetch data and format it
data = fetch_movielens(min_rating=4.0)

# print training and testing data
# data containe information about movies and rating for each one
# data split its information in train ans test data
# train is data for train algorithm
# test is data to know the accuracy grade of the algorithm
# print(data) to show all data
print(repr(data['train']))
print(repr(data['test']))

#its possible use other loss functions like warp,logistic,bpr and warp-kos
#create model
model=LightFM(loss='warp')
#train model
model.fit(data['train'],epochs=30,num_threads=2)

def sample_recommendation(model,data,user_ids):
    #number of users and movies in training data
    n_users, n_items = data['train'].shape
    #generate recomendation for each user we input
    for user_id in user_ids:

        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)

sample_recommendation(model, data, [3, 25, 450])