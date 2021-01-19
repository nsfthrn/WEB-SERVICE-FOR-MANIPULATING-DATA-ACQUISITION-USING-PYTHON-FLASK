# menghapus column tertentu
def delete_column(dataframe, column):
    return dataframe.drop(column, axis=1)