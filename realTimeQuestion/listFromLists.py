val = [1,4,2,3,[11,12,13,[21,22,23,24]]]

flat_list = []
def fltlst(val):
    for i in val:
        if type(i) is list:
            fltlst(i)
        else:
            flat_list.append(i)

fltlst(val)
print(flat_list)
