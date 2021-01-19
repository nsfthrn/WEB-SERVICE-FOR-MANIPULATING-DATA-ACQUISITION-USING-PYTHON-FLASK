# menghapus satu data dari index id
def delete_data(dataframe, id):
    id = int(id) if type(id) != int else id
    dataframe.drop([id], axis=0, inplace=True)
    return dataframe