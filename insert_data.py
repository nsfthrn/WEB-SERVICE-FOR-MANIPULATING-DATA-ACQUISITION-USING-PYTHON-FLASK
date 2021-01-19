from get_row_count import get_row_count

# menambahkan data
def insert_data(dataframe, newdata):
    index = get_row_count(dataframe) + 1
    dataframe.at[index] = newdata