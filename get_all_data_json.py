from convert_json import convert_json

# mengambil semua data dari csv dan mengubah ke format json
def get_all_data_json(dataframe):
    return convert_json(dataframe)