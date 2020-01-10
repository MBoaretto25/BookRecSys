import os
import matplotlib.pyplot as plt
import pandas as pd

from .data_gather import DataGather


pd.options.display.float_format = '{:.2f}'.format


class DataVisualization:

    def __init__(self):
        self._dg = DataGather()
        self._books = self._dg.books
        self._ratings = self._dg.ratingss

    def get_ratings_describe(self):
        print("Ratings Statistics")
        self._ratings.describe()['rating']

    def get_10_highest_ratings(self):
        avg_ratings = self._books.sort_values(by=["average_rating"])
        best_ratings = avg_ratings.iloc[-10:]
        print("10 Highest Rated Books!")
        print(" Avg. Rating  |  Title")
        fmt = "       {:.2f}     | {}"
        for i in range(len(best_ratings)-1, -1, -1):
            print(fmt.format(best_ratings.iloc[i]['average_rating'], best_ratings.iloc[i]['title']))

    def get_10_lowest_ratings(self):
        avg_ratings = self._books.sort_values(by=["average_rating"], ascending=False)
        best_ratings = avg_ratings.iloc[-10:]
        print("10 Lowest Rated Books!")
        print(" Avg. Rating  |  Title")
        fmt = "       {:.1f}     | {}"
        for i in range(len(best_ratings)):
            print(fmt.format(best_ratings.iloc[i]['average_rating'], best_ratings.iloc[i]['title']))

    def get_10_highest_ratings_count(self):
        avg_ratings = self._books['average_rating']
        pass

    def get_10_lowest_ratings_count(self):
        pass

    def get_ratings_distribution(self):
        pass

    def get_avg_user_rating_count(self):
        pass

    def get_most_user_rating_count(self):
        pass

    def get_lowest_user_rating_count(self):
        pass


if __name__ == "__main__":
    pass
