def parse_escaped_str(str):
    new_str = ''
    i = 0
    while i < len(str):
        if str[i:i+2] == '\\\\':
            new_str += '\\'
            i += 2
            continue
        elif str[i:i+2] == '\\n':
            new_str += '\n'
            i += 2
            continue
        new_str += str[i]
        i += 1
 
    return new_str