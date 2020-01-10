import pandas as pd
import os


class DataGather:
    def __init__(self, csv_files_path="C:/Users/Boaretto/Documents/BookRecSystem/Data"):
        self._csv_files_paths = csv_files_path
        self._books = None
        self._ratings = None
        self._load_books()
        self._load_ratings()

    def _load_books(self):
        csv_path = os.path.join(self._csv_files_paths, "books.csv")
        print(csv_path)
        self._books = pd.read_csv(csv_path, sep=',')

    def _load_ratings(self):
        csv_path = os.path.join(self._csv_files_paths, "ratings.csv")
        self._ratings = pd.read_csv(csv_path, sep=',')

    @property
    def books(self):
        return self._books

    @property
    def ratings(self):
        return self._ratings


if __name__ == "__main__":
    dg = DataGather("C:/Users/Boaretto/Documents/BookRecSystem/Data")
    books = dg.books
    print("There are {} books in dataset.".format(len(books)))
    print(books.head(5))












