from read_data import read_data

def find_user_message_count(data: dict)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    messages = data['messages']
    count = 0
    number = []
    for msg in messages:
        id = msg['id']
        number.append(f'id:{id}')
        count += 1
    return number, count

data = read_data('data/result.json')
print(find_user_message_count(data))

