import os

files = os.listdir('files')
ext = [val.split('.')[-1] for val in files]
key_dict = {val:list() for val in set(ext)}
for val in files:
    if val.split('.')[-1] in key_dict.keys():
        key_dict[val.split('.')[-1]].append(val)

print(key_dict)
