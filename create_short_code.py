def get_short_code(name):
    if not name:
        return

    name_list = name.split()
    res = ''
    if len(name_list) == 1:
        res = name_list[0][:3]
    elif len(name_list) == 2:
        res = res + name_list[0][:2]
        res = res + name_list[1][0]
    elif len(name_list) > 2:
        res = res + name_list[0][0]
        res = res + name_list[1][0]
        res = res + name_list[2][0]
    return res.upper()


name = 'korim'
name = 'Abdul Korim'
name = 'MOhammad Abdul korim'

print(get_short_code(name))