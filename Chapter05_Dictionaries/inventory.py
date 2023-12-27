""""Display inventory of fantasy game character."""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    """Display player's inventory"""
    print("Inventory:")
    item_count = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_count += v
    print(f'Total number of items: {item_count}')

def add_to_inventroy(inventory, added_items):
    """Update inventory to add item if missing and increase quantity."""
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

def main():
    """Main function."""
    display_inventory(stuff)
    add_to_inventroy(stuff, dragon_loot)
    print('\nUpdated inventory:')
    display_inventory(stuff)

if __name__ == '__main__':
    main()
