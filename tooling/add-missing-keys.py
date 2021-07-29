import glob, json, sys, os.path

base_lang = 'en-us'
target_lang = 'nb-no' if len(sys.argv) == 1 else sys.argv[1]

known_values = []

def handle_element(prefix, element):
    r = []
    # print(prefix)
    if type(element) is dict:
        if 'Identifier' in element.keys():
            r.append(prefix + ':' + element['Identifier'])
        else:
            for k in element.keys():
                r += handle_element(prefix + ':' + k, element[k])
    elif type(element) is list:
        for i in range(len(element)):
            r += handle_element(prefix, element[i])
    else:
        print('Type', type(element))

    return r

for fn in glob.glob('**', recursive=True):
    if not fn.endswith('.{}.json'.format(base_lang)):
        continue
    with open(fn) as f:
        base_j = json.load(f)
        known_keys = handle_element('', base_j)
        target_fn = fn.replace('.{}.json'.format(base_lang), '.{}.json'.format(target_lang))
        if not os.path.isfile(target_fn):
            print('Creating', target_fn)
            with open(target_fn, 'w') as target_f:
                print('[]', file=target_f)

        def get_index(identifier):
            i = 0
            for elem in base_j:
                if 'Identifier' not in elem.keys():
                    continue
                if elem['Identifier'] == identifier:
                    return i
                i += 1

        target_j = {}
        with open(target_fn, 'r') as target_f:
            print(target_fn)
            target_j = json.load(target_f)
            for kk in known_keys:
                if kk[1:] in [_['Identifier'] for _ in target_j if 'Identifier' in _.keys()]:
                    continue
                if len(kk[1:].strip()) == 0:
                    continue
                target_j.append(
                    {
                        'Identifier': kk[1:],
                        'Text': '{}: {}'.format(target_lang, base_j[get_index(kk[1:])]['Text'])
                    }
                )
        with open(target_fn, 'w') as target_f:
            json.dump(target_j, target_f, indent=2, ensure_ascii=False)