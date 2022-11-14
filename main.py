from DataFactory import *
from Advisor import *

if __name__ == '__main__':
    np.random.seed(0)
    path = "./datasets/books_new.csv"

    books = pd.read_csv(path)
    index = np.random.choice(10000, books.shape[0], replace=False)  # Create random IDs
    books.set_index(index, inplace=True)

    database = create_database(path, books, samples_num=500)
    data = generate_data(database, books)

    new_sample = create_sample(books=books)

    res, p = cross_by_reading_list(new_sample, data)
    b = books.loc[res][:5]
    b['Match %'] = p[:5] * 100
    print(b)
    print(p.sum())
