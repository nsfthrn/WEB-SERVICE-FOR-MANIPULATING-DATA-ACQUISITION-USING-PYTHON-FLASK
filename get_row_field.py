# mengambil satu data dari column tertentu
def get_row_field(dataframe, field):
    return "{}:{}".format(field, dataframe[field])