def reload_data(filename, dataframe):
    dataframe.to_csv(filename, index=False, sep=':')