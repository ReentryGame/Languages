import glob, json, re

lang_stats = {}

for fn in glob.glob('**', recursive=True):
    if len(re.findall(r'[a-z]{2,}-[a-z]{2,}\.json$', fn)) == 0:
        continue
    lang = fn.split('.')[-2]
    if lang not in lang_stats.keys():
        lang_stats[lang] = 0
    with open(fn) as f:
        j = json.load(f)
        for elem in j:
            if elem['Text'].strip().lower().startswith(lang.lower()):
                continue
            lang_stats[lang] += 1

og_lang_ids = lang_stats['en-us']

for lang in lang_stats.keys():
    if lang == 'en-us':
        continue
    print(lang, lang_stats[lang], og_lang_ids, 100.0 * lang_stats[lang] / og_lang_ids)
