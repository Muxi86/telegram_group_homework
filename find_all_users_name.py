from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    messages = data['messages']
    users = []
    for msg in messages:
        name = msg.get('actor',False)
        if name not in users and name:
            users.append(name)

        name = msg.get('from',False)
        if name not in users and name:
            users.append(name)
    return users

data = read_data('data/result.json')
print(find_all_users_name(data))