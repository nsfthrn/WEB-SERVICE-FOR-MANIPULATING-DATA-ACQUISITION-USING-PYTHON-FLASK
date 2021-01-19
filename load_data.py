import pandas

# membaca file csv
def load_data(filename):
    return pandas.read_csv(filename, delimiter=':')