import json

# merubah data ke format json
def convert_json(dataframe):
    return json.loads(dataframe.to_json(orient='index'))