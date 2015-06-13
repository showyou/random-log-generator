def load_csv(filename):
    results = []
    with open(filename, 'r') as fp:
        line = fp.read().split('\n')[:-1]
        for l in line:
            data = l.split('\t')
            results.append(data)
        #print line
    return results
 
if __name__ == '__main__':
    stations = load_csv('stations.tsv')
    for st in stations:
        print st[0], st[1:]
