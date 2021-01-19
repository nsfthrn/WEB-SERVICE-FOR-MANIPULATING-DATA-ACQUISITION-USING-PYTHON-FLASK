# menghapus semua data dari csv
def delete_all_data(dataframe):
    dataframe.drop(['raw_value', 'data', 'sign'], axis=1)