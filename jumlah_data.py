# menghitung jumlah data column dan row
def jumlah_data(dataframe, field):
    count = dict(row=dataframe.shape[0], column=dataframe.shape[1])
    if not field == 'all':
        return count['row'] if field == 'row' else count['column']
    else:
        return count