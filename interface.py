import pandas as pd


def save_database(df: pd.DataFrame):
    path = input("Enter path: ")  # todo: check errors
    df.to_csv(path)


def add_book(df):
    name = input("Enter book name: ")
    num = input("Pages number: ")
    genre = input("Genre: ")
    df.loc[len(df.index)] = [name, num, genre]


def load_database(df):
    path = input("Enter path: ")
    df = pd.read_csv(path)


def add_from_database(df: pd.DataFrame):
    path = input("Enter path: ")
    new_df = pd.read_csv(path)
    df.append(new_df)


def print_database(df: pd.DataFrame):
    print(df)


if __name__ == '__main__':
    df = pd.DataFrame(columns=['Name', 'Pages', 'Genre'])
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
            instructions[inp](df)

        print("Done!")
