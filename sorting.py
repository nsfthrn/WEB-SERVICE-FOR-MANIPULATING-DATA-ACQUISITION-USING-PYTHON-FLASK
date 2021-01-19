# mengurutkan data dari atas ke bawah atau sebaliknya
# menggunakan parameter ascending pada dataframe.sort_index
def sorting(dataframe, order_by):
    asc = True if order_by == 'ascending' else False
    return dataframe.sort_index(ascending=asc)