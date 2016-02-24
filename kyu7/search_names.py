def search_names(logins):
    assert isinstance(logins, list), 'Must be type list'
    return list(filter((lambda x: x[0][-1] == '_'), logins))
