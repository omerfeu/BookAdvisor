import pandas as pd


def save_database(df: pd.DataFrame):
    path = input("Enter path: ")  # todo: check errors
    df.to_csv(path, index=False)
    return df


def add_book(df: pd.DataFrame):
    title = input("Enter book title: ")
    num = input("Pages number: ")
    genre = input("Genre: ")
    df.loc[len(df.index)] = [title, num, genre]
    return df


def load_database(df: pd.DataFrame):
    path = input("Enter path: ")
    return pd.read_csv(path)


def add_from_database(df: pd.DataFrame):
    path = input("Enter path: ")
    new_df = pd.read_csv(path)
    return pd.concat([df, new_df]).reset_index(drop=True)


def print_database(df: pd.DataFrame):
    print(df)
    return df


if __name__ == '__main__':
    df = pd.DataFrame(columns=['Title', 'Pages', 'Genre'])
    instructions = {
        'add book': add_book,
        'load new database': load_database,
        'add from database': add_from_database,
        'save': save_database,
        'print': print_database
    }

    while (True):
        inp = input('What to do next? ')
        if inp == 'exit':
            exit(0)
        elif inp == 'help':
            print("Available commands:")
            print(list(instructions.keys()))
            continue

        elif inp not in instructions.keys():
            print("No such thing...")
            continue
        else:
            df = instructions[inp](df)

        print("Done!")
