import numpy as np
import pandas as pd


def generate_data(df: pd.DataFrame, books: pd.DataFrame) -> pd.DataFrame:  # todo: not very efficient
    """
    Generates the data.

    :param df: a dataframe where each sample is a list of books (a user's reading list)
    :param books: a dataframe that represents the books list
    :return: dummy values for df. dataframe with shape (number of samples, number of books) where each column represents a book and each row represents a sample. has 1 if the sample contains the book, 0 otherwise
    """
    result = pd.DataFrame(0, index=df.index, columns=books.index)

    for index in df.index:
        for book in df.iloc[index]:
            if pd.isna(book):
                continue
            result.loc[index, book] = 1

    return pd.DataFrame(result)


def cross_by_book(id, df: pd.DataFrame):
    """
    Gets a book and the data.
    For all the lists (samples) containing the book, counts the number of
    times each of the rest of the books appear in those lists.
    Normalize and returns a probability vector which represents each book probability to appear in a
    list containing the given book.

    :param id: an ID of a book to check
    :param df: the data
    :return: probability vector
    """
    books_advice = df.groupby(id).sum()
    if books_advice.shape[0] <= 1:
        books_advice.iloc[:, :] = 0
        return books_advice.loc[0]
    books_advice = books_advice.loc[1]
    s = books_advice.sum()
    books_advice /= s
    return books_advice


def cross_by_reading_list(lst, data: pd.DataFrame) -> (np.ndarray, np.ndarray):
    """
    Gets a reading list and the data.
    For each book in the list gets the probability vector for the rest of the books (meaning how probable
    it is for a book to appear in a list containing the current book).
    Adds them up and sorts the list in descending order.
    We get a list of book's IDs where the first element is the book which appeared in the most reading lists
    that contains one of the books in the given reading list.

    :param lst: a book's list (book's indexes)
    :param data: the data
    :return: an array of books IDs, sorted from the most probable to the least, and the corresponding probability vector

    """
    p = pd.Series(index=data.columns)
    for book in lst:
        p = p.add(cross_by_book(book, data), fill_value=0)
    indices = pd.Series.argsort(-p)
    p = p.iloc[indices].drop(labels=lst).to_numpy()

    return data.columns[indices].drop(labels=lst).to_numpy(), p / p.sum()
