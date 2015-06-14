def load_with_separator(filename, sep):
    results = []
    with open(filename, 'r') as fp:
        line = fp.read().split('\n')[:-1]
        for l in line:
            data = l.split(sep)
            results.append(data)
        #print line
    return results

def load_csv(filename):
    return load_with_separator(filename, ',')

def load_tsv(filename):
    return load_with_separator(filename, '\t')
 
if __name__ == '__main__':
    stations = load_tsv('stations.tsv')
    for st in stations:
        print st[0], st[1:]
