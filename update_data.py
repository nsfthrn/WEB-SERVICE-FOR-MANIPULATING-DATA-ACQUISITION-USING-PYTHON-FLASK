# mengupdate data dari index id
def update_data(dataframe, id, newdata):
    dataframe.loc[id, :] = newdata
    return dataframe