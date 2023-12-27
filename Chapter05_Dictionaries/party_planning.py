all_guest = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guest, item):
    num_brought = 0
    for k, v in guest.items():
        num_brought += v.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(f" - Apples           {str(total_brought(all_guest, 'apples'))}")
print(f" - Cups             {str(total_brought(all_guest, 'cups'))}")
print(f" - Cakes            {str(total_brought(all_guest, 'cakes'))}")
print(f" - Ham Sandwiches   {str(total_brought(all_guest, 'ham sandwiches'))}")
print(f" - Apple Pies       {str(total_brought(all_guest, 'apple pies'))}")