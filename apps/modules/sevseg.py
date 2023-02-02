def getSevSegStr(number, minWidth=0):
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
        elif numeral == '_':
            rows[0] += '   '
            rows[1] += ' _ '
            rows[2] += '   '
        elif numeral == '0':
            rows[0] += ' _ '
            rows[1] += '| |'
            rows[2] += '|_|'
        elif numeral == '1':
            rows[0] += '   '
            rows[1] += '  |'
            rows[2] += '  |'
        elif numeral == '2':
            rows[0] += '  _ '
            rows[1] += '  _|'
            rows[2] += ' |_ '
        elif numeral == '3':
            rows[0] += ' _ '
            rows[1] += ' _|'
            rows[2] += ' _|'
        elif numeral == '4':
            rows[0] += '    '
            rows[1] += ' |_|'
            rows[2] += '   |'
        elif numeral == '5':
            rows[0] += '  _ '
            rows[1] += ' |_ '
            rows[2] += '  _|'
        elif numeral == '6':
            rows[0] += '  _ '
            rows[1] += ' |_ '
            rows[2] += ' |_|'
        elif numeral == '7':
            rows[0] += ' _ '
            rows[1] += '  |'
            rows[2] += '  |'
        elif numeral == '8':
            rows[0] += '  _ '
            rows[1] += ' |_|'
            rows[2] += ' |_|'
        elif numeral == '9':
            rows[0] += '  _ '
            rows[1] += ' |_|'
            rows[2] += '  _|'

    if i != len(number) - 1:
        rows[0] += ' '
        rows[1] += ' '
        rows[2] += ' '

    return '\n'.join(rows)


if __name__ == '__main__':
    result = getSevSegStr("0.123456789_", 2)
    print(result)
