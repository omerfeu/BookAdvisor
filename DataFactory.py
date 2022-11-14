import pandas as pd
import numpy as np


def create_sample(books, p=None, length=(3, 7), col_name="index"):
    """
    Generates a single reading list.

    :param books: a df of books to draw from
    :param p: probabilites for each book
    :param length: range of the list to generate
    :param col_name: the name of the column representing the book's ID
    :return: a single sample with IDs representing the books
    """
    n = np.random.choice(np.arange(*length))
    sample = books.sample(n=n, weights=p, replace=False).reset_index()
    return sample['index']


def create_database(path, books, samples_num=100, list_range=(3, 7)):
    # Generate probabilities
    p = np.random.rand(len(books))
    p = p / p.sum()

    # Draw m samples.
    # Each sample is a list of book's IDs (its length in the range 'list_range')
    # that represents a user's reading list.
    df = pd.DataFrame(columns=range(list_range[1] - 1))
    for i in range(samples_num):
        s = create_sample(books, p, list_range)
        df.loc[i] = s
    return df
