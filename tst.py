def map_to_int(ch):
    if ch >= 'a' and ch <= 'z':
        return ch - 'a' + 1
    elif ch == '.':
        return 27
    elif ch == '?':
         return 28
    else:
        return -1

print(map_to_int('g'))