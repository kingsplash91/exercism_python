"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    inventory = {}
    keys = dict.fromkeys(items)
    for key in keys:
        inventory[key] = items.count(key)
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    if inventory == {}:
        return create_inventory(items)
        
    keys = dict.fromkeys(items)
    for key in keys:
        if key not in inventory:
            inventory[key] = items.count(key)
        else:
            inventory[key] += items.count(key)
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    keys = dict.fromkeys(items)
    for key in keys:
        if key not in inventory:
            continue
        else: 
            inventory[key] -= items.count(key)
            if inventory[key] < 0:
                inventory[key] = 0
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    keys = dict.fromkeys(inventory)

    if item not in keys:
        return inventory

    new_inv = {}
    for key in keys:
        if key != item:
            new_inv[key] = inventory[key]
    
    return new_inv


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    for key in inventory:
        if inventory[key] == 0:
            inventory = remove_item(inventory, key)
            
    return list(inventory.items())
