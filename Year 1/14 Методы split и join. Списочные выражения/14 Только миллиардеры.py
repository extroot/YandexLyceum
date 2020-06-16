print('\n'.join([','.join(' '.join([n if int(n) >= 1000000000 else ''
                                    for n in i.split(',')]).split())
                 for i in input().split(';')]))
