import glob, json, sys

base_lang = 'en-us'
target_lang = 'nb-no' if len(sys.argv) == 1 else sys.argv[1]

known_keys = []

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
        j = json.load(f)
        known_keys += handle_element(fn.replace('.{}.'.format(base_lang), '.'), j)

target_keys = []
for fn in glob.glob('**', recursive=True):
    if not fn.endswith('.{}.json'.format(target_lang)):
        continue
    with open(fn) as f:
        j = json.load(f)
        target_keys += handle_element(fn.replace('.{}.'.format(target_lang), '.'), j)

print(len(target_keys), len(known_keys))
for kk in known_keys:
    if kk in target_keys:
        continue
    print(kk, 'MISSING in', target_lang)