def add(x):
    if x == '':
        return 0
    delimiter = ','
    if x.startswith('//'):
        delimiter = x[2]
        x = x.replace('//{}\n'.format(delimiter), '')
    x = x.replace('\n', delimiter)
    x = x.replace(delimiter, ',')
    x_split = x.split(',')
    negatives = [n for n in x_split if int(n) < 0]
    if negatives:
        raise Exception('negatives not allowed: {}'.format(','.join(negatives)))
    total = 0
    for num in x_split:
        total += int(num)
    return total
