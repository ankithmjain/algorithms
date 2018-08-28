def match(pattern, text):
    if len(pattern) ==0 and len(text)==0:
        return True
    if pattern[0] == text[0] or pattern[0] == '.':
        print pattern[0]
        return match(pattern[1:], text[1:])
    elif pattern[0] == '*':
        return match(pattern[2:], text[1:]) or match(pattern[2:], text)
    else:
        return False

pattern = 'abcd.f'
text = 'abcdef'
print match(pattern, text)

