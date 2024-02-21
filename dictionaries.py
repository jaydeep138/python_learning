user_info = dict(
    name='jaydeep',
    age = 19,
    fav_movies = ['A','B','C'],
    fav_tunes = ['X','Y','Z']
)
popped_items = user_info.popitem()
print(popped_items)
print(type(popped_items))
popped_items2 = user_info.popitem()
print(popped_items2)
print(type(popped_items2))