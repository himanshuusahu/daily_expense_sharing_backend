# Calculate splits based on split type
def calculate_splits(data):
    split_type = data['split_type']
    splits = data['splits']
    amount = data['amount']
    
    # Equal split
    if split_type == 'equal':
        split_amount = amount / len(splits)
        for split in splits:
            split['amount'] = split_amount
    
    # Exact split
    elif split_type == 'exact':
        for split in splits:
            if 'amount' not in split:
                raise ValueError('Exact split requires amount for each participant')
    
    # Percentage split
    elif split_type == 'percentage':
        for split in splits:
            if 'percentage' not in split:
                raise ValueError('Percentage split requires percentage for each participant')
            split['amount'] = (split['percentage'] / 100) * amount
    
    return data
