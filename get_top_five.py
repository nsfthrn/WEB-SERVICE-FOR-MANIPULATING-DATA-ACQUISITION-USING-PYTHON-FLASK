#mengambil 5 data urutan pertama atau terakhir
#dataframe.head berfungsi untuk mengembalikan awalan data dari objek yang ditentukan. n=5
#sedangkan dataframe.tail berfungsi untuk mengembalikan data akhir dari objek. n=5
def get_top_five(dataframe, order_by):
    return dataframe.head() if order_by == 'first' else dataframe.tail()