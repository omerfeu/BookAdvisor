import pandas as pd
import numpy as np

if __name__ == '__main__':
    path = "./datasets/books_new.csv"
    books = pd.read_csv(path)

    # Generate probabilities
    p = np.random.rand(len(books))
    p = p / p.sum()

    # Draw 100 samples.
    # Each sample is a list of 3-6 books that represents a user's reading list.
    df = pd.DataFrame(columns=range(6))
    for i in range(100):
        n = np.random.choice(np.arange(3, 7))
        sample = books['Title'].sample(n=n, weights=p, replace=False, ignore_index=True)
        df.loc[i] = sample
    print(df)
