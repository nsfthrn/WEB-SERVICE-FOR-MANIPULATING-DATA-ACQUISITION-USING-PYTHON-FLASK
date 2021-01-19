# mengambil data dari column tertentu
def get_column(dataframe, fieldname):
    return dataframe.loc[:, [fieldname]]