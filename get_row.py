# mengambil semua data dari index id
def get_row(dataframe, id):
    return dataframe.loc[id, ['raw_value', 'data', 'sign']]