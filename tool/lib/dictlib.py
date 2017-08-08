def get_dict_value(dict_data, *keys):
    for key in keys:
        dict_data = dict_data[key]
    return dict_data


def set_dict_value(value, dict_data, *keys):
    for key in keys[:-1]:
        dict_data = dict_data[key]
    dict_data[keys[-1]] = value
    return value


def set_dict_value_at_existing_key(value, dict_data, *keys):
    for key in keys[:-1]:
        if key in dict_data:
            dict_data = dict_data[key]
        else:
            return None
    if keys[-1] in dict_data:
        dict_data[keys[-1]] = value
        return value
    else:
        return None
