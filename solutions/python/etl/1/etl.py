def transform(legacy_data):
    new_mapping = {}

    for key in legacy_data.keys():
        for letter in legacy_data[key]:
            new_mapping[letter.lower()] = key
    return new_mapping
