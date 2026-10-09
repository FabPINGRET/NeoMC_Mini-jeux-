"""⭐ Notes des joueurs : fin de partie → note facultative sur 5 (mode de jeu, carte, fun), moyennes depuis toujours.

    python tools/rating/gen_rating.py .      (à relancer APRÈS tools/variantes/gen_variants.py, qui réécrit les menus)

- À la fin d'une partie (core/return_lobby), les participants (mg.play / mg.out) reçoivent une fenêtre :
  trois choix « — / ★ … ★★★★★ » et « Envoyer » → /trigger mg.rt set 1<mode><carte><fun>.
- Sommes et nombres de votes cumulés dans des scores (persistants) : carte #m<id> (mg.rts / mg.rtn),
  jeu #g<n> : mode (mg.rgs / mg.rgn) et fun (mg.rfs / mg.rfn).
- Les menus (fenêtres de lancement et de vote) deviennent des fenêtres « inline » générées par macro
  (mg:rate/d/<nom>) : chaque bouton de carte affiche la moyenne des joueurs à la place des étoiles de difficulté
  (tant qu'il n'y a pas de vote, les étoiles d'origine restent) ; chaque jeu affiche son score global ♥ (mode + fun).
  Les libellés sont dans storage mg:rate lab (r<id> pour une carte, f<jeu> pour un jeu), recalculés à chaque vote.
"""
import ast
import json
import os
import re
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.join(R, 'data/mg')
F = os.path.join(D, 'function')


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def w(rel, lines):
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def patch(rel, anchor, new, where='after'):
    p = os.path.join(F, rel + '.mcfunction')
    L = open(p, encoding='utf-8').read().split('\n')
    if all(l in L for l in new):
        return
    i = L.index(anchor) + (1 if where == 'after' else 0)
    L[i:i] = new
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


def snbt_str(s):
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"


# ------------------------------------------------------------------ familles de jeux (celles du hall des scores)
src = open(os.path.join(R, 'tools/hall/gen_hall.py'), encoding='utf-8').read()
GAMES = ast.literal_eval(re.search(r'GAMES = (\[.*?\n\])', src, re.S).group(1))
FIDX = {k: i + 1 for i, (k, *_) in enumerate(GAMES)}
FLAB = {k: (l, c) for k, l, c, _ in GAMES}
# boutons de navigation vers un jeu (mg.opt) et votes pour un jeu (mg.vote n) → famille
OPT_FAM = {37: 'spleef', 38: 'tntrun', 39: 'splegg', 17: 'splegg', 18: 'sumo', 20: 'anvil', 23: 'pvp', 24: 'oitc', 10: 'quake',
           29: 'tnttag', 30: 'bedwars', 8: 'sheepwar', 21: 'paintball', 7: 'mobarena', 19: 'dropper', 28: 'elyrace', 31: 'elytra',
           46: 'kart', 16: 'party', 22: 'bb'}
VOTE_FAM = {1: 'spleef', 2: 'tntrun', 3: 'pvp', 4: 'pvp', 5: 'bedwars', 6: 'sheepwar', 7: 'mobarena', 8: 'splegg', 9: 'sumo',
            10: 'dropper', 11: 'tnttag', 12: 'blockparty', 13: 'anvil', 14: 'turf', 15: 'quake', 16: 'paintball', 17: 'oitc',
            18: 'icerace', 19: 'bb', 20: 'bb', 21: 'elytra'}


def fam_of_game(n):
    for k, _, _, rngs in GAMES:
        if any(a <= n <= b for a, b in rngs):
            return k
    return None


# ------------------------------------------------------------------ libellés
STARS = set('★☆ ')


def plain(label):
    if isinstance(label, str):
        return label
    if isinstance(label, dict):
        return label.get('text', '') + ''.join(plain(x) for x in label.get('extra', []))
    return ''.join(plain(x) for x in label)


DEFAULT = {}     # id de carte → composant d'origine (étoiles de difficulté)
NAMES = {}       # id de carte → nom de la carte (pour la fenêtre de note)


def split_label(label, n):
    """Renvoie (composants du nom, composant des étoiles d'origine ou None)."""
    comps = [label] if isinstance(label, (str, dict)) else list(label)
    comps = [c if isinstance(c, dict) else {'text': c} for c in comps]
    stars = []
    while comps and comps[-1].get('text', '').strip() and set(comps[-1]['text']) <= STARS:
        stars.insert(0, comps.pop())
    if not stars and comps:      # « Nom ★★☆☆ » dans un seul texte
        t = comps[-1].get('text', '')
        m = re.search(r'\s([★☆]+)\s*$', t)
        if m:
            comps[-1] = {**comps[-1], 'text': t[:m.start(1)]}
            full = m.group(1)
            stars = [{'text': full.rstrip('☆'), 'color': 'gold'}, {'text': full[len(full.rstrip('☆')):], 'color': 'dark_gray'}]
    if stars:
        main = {'text': stars[0]['text'], 'color': stars[0].get('color', 'gold')}
        if len(stars) > 1 and stars[1]['text']:
            main['extra'] = [{'text': s['text'], 'color': s.get('color', 'dark_gray')} for s in stars[1:] if s['text']]
        DEFAULT.setdefault(n, main)
    NAMES.setdefault(n, plain(comps).strip())
    if comps and not comps[-1].get('text', '').endswith(' '):
        comps[-1] = {**comps[-1], 'text': comps[-1].get('text', '') + ' '}
    return comps


def to_snbt(o, holes):
    """JSON → texte SNBT (JSON est du SNBT valide) ; les marqueurs de trou deviennent $(clé)."""
    s = js(o)
    for k in holes:
        s = s.replace(f'"@@{k}@@"', f'$({k})')
    return s


CONVERTED = []
for f in sorted(os.listdir(os.path.join(D, 'dialog'))):
    if not f.endswith('.json'):
        continue
    name = f[:-5]
    d = json.load(open(os.path.join(D, 'dialog', f), encoding='utf-8'))
    acts = d.get('actions') or []
    holes = set()
    for a in acts:
        cmd = a.get('action', {}).get('command', '') if isinstance(a.get('action'), dict) else ''
        m = re.match(r'trigger mg\.(go|opt|vote) set (\d+)$', cmd)
        if not m:
            continue
        kind, n = m.group(1), int(m.group(2))
        if kind == 'go' and n <= 196:
            comps = split_label(a['label'], n)
            extra = [f'@@r{n}@@']
            holes.add(f'r{n}')
            fam = fam_of_game(n)
            if name.startswith('cat_') and fam and n < 100 and n not in (27, 4, 78, 66):
                extra.append(f'@@f{fam}@@')
                holes.add(f'f{fam}')
            a['label'] = comps + extra
        elif kind == 'vote' and 1001 <= n <= 1196:
            comps = split_label(a['label'], n - 1000)
            a['label'] = comps + [f'@@r{n - 1000}@@']
            holes.add(f'r{n - 1000}')
        elif (kind == 'opt' and n in OPT_FAM) or (kind == 'vote' and n in VOTE_FAM):
            fam = OPT_FAM[n] if kind == 'opt' else VOTE_FAM[n]
            comps = [a['label']] if isinstance(a['label'], (str, dict)) else list(a['label'])
            comps = [c if isinstance(c, dict) else {'text': c} for c in comps]
            a['label'] = comps + [f'@@f{fam}@@']
            holes.add(f'f{fam}')
    if not holes:
        continue
    CONVERTED.append(name)
    body = d.get('body') or []
    if body and body[0].get('type') == 'minecraft:plain_message':
        c = body[0]['contents']
        body[0]['contents'] = (c if isinstance(c, list) else [c]) + [
            {'text': '\n★★★★☆ 4,2', 'color': 'gold'}, {'text': ' = note moyenne des joueurs (sinon ★ de difficulté) · ', 'color': 'dark_gray'},
            {'text': '♥', 'color': 'light_purple'}, {'text': ' = score du jeu (mode + fun)', 'color': 'dark_gray'}]
    w(f'rate/d/{name}', [f'# Fenêtre « {name} » avec les notes des joueurs (macro : storage mg:rate lab). Générée depuis dialog/{name}.json.',
                         f'$return run dialog show @s {to_snbt(d, holes)}'])

# appels : « dialog show @s mg:<nom> » → fenêtre avec notes
conv = set(CONVERTED)
for root, _, files in os.walk(F):
    if os.sep + 'rate' + os.sep in root + os.sep:
        continue
    for fn in files:
        p = os.path.join(root, fn)
        t = open(p, encoding='utf-8').read()
        t2 = re.sub(r'dialog show @s mg:([a-z0-9_]+)', lambda m: f'function mg:rate/d/{m.group(1)} with storage mg:rate lab' if m.group(1) in conv else m.group(0), t)
        t2 = t2.replace('dialog show @s mg:$(d)', 'function mg:rate/d/$(d) with storage mg:rate lab')
        if t2 != t:
            open(p, 'w', encoding='utf-8', newline='\n').write(t2)

# ------------------------------------------------------------------ tables de libellés (index = moyenne × 10)
def tab_entry(i, fam=False):
    if i < 10:
        return '""'
    if fam:
        return js({'text': f'♥{i // 10},{i % 10}', 'color': 'light_purple'})
    s = max(1, min(5, (i + 5) // 10))
    return js({'text': '★' * s, 'color': 'gold', 'extra': [{'text': '☆' * (5 - s), 'color': 'dark_gray'},
                                                           {'text': f' {i // 10},{i % 10}', 'color': 'yellow'}]})


IDS = sorted(set(list(NAMES) + list(range(1, 99))))
L = ['# Notes : tables, libellés par défaut, recalcul de tout ce qui a des votes (appelé par core/load). Généré.',
     'data modify storage mg:rate tab set value [' + ','.join(snbt_str(tab_entry(i)) for i in range(51)) + ']',
     'data modify storage mg:rate ftab set value [' + ','.join(snbt_str(tab_entry(i, True)) for i in range(51)) + ']',
     'scoreboard players set #20 mg.st 20', 'scoreboard players set #2 mg.st 2', 'scoreboard players set #10 mg.st 10',
     'scoreboard players set #100 mg.st 100']
for n in sorted(set(IDS) | set(range(100, 197))):
    L.append(f'data modify storage mg:rate lab.r{n} set value {snbt_str(js(DEFAULT[n]) if n in DEFAULT else chr(34) * 2)}')
    L.append(f'execute if score #m{n} mg.rtn matches 1.. run function mg:rate/lab_map {{m:{n}}}')
for k, i in FIDX.items():
    L.append(f'data modify storage mg:rate lab.f{k} set value \'""\'')
    L.append(f'function mg:rate/lab_fam {{f:"{k}",g:{i}}}')
w('rate/init', L)
w('rate/lab_map', ['# Macro {m} : libellé de la carte m = moyenne des votes « carte »',
                   '$scoreboard players operation $rs mg.st = #m$(m) mg.rts', '$scoreboard players operation $rn mg.st = #m$(m) mg.rtn',
                   'function mg:rate/avg',
                   'execute store result storage mg:rate tmp.i int 1 run scoreboard players get $ra mg.st',
                   '$data modify storage mg:rate tmp.k set value "r$(m)"',
                   'function mg:rate/set with storage mg:rate tmp'])
w('rate/lab_fam', ['# Macro {f, g} : score global du jeu = moyenne des votes « mode » et « fun » réunis',
                   '$scoreboard players operation $rs mg.st = #g$(g) mg.rgs', '$scoreboard players operation $rs mg.st += #g$(g) mg.rfs',
                   '$scoreboard players operation $rn mg.st = #g$(g) mg.rgn', '$scoreboard players operation $rn mg.st += #g$(g) mg.rfn',
                   'execute if score $rn mg.st matches ..0 run return 0',
                   'function mg:rate/avg',
                   'execute store result storage mg:rate tmp.i int 1 run scoreboard players get $ra mg.st',
                   '$data modify storage mg:rate tmp.k set value "f$(f)"',
                   'function mg:rate/fset with storage mg:rate tmp'])
w('rate/avg', ['# $ra = moyenne × 10 arrondie de $rs / $rn', 'scoreboard players operation $ra mg.st = $rs mg.st',
               'scoreboard players operation $ra mg.st *= #20 mg.st', 'scoreboard players operation $ra mg.st += $rn mg.st',
               'scoreboard players operation $rd mg.st = $rn mg.st', 'scoreboard players operation $rd mg.st *= #2 mg.st',
               'scoreboard players operation $ra mg.st /= $rd mg.st',
               'execute if score $ra mg.st matches 51.. run scoreboard players set $ra mg.st 50'])
w('rate/set', ['$data modify storage mg:rate lab.$(k) set from storage mg:rate tab[$(i)]'])
w('rate/fset', ['$data modify storage mg:rate lab.$(k) set from storage mg:rate ftab[$(i)]'])

# ------------------------------------------------------------------ début de partie : quoi noter
B = ['# Début de partie : clé de la carte ($rgid → storage mg:rate key.m) et du jeu (key.f, key.g) ; les notes en attente expirent. Généré.',
     '# (épreuves d\'une Mini Party : on garde la Mini Party elle-même)',
     'execute if score $mp mg.st matches 1 unless score $game mg.st matches 59 run return 0',
     'tag @a remove mg.rate',
     'execute if score $rgid mg.st matches 27 run function mg:rate/fix {base:67,s:"$ttm"}',
     'execute if score $rgid mg.st matches 4 run function mg:rate/fix {base:71,s:"$bwm"}',
     'execute if score $rgid mg.st matches 78 run function mg:rate/fix {base:74,s:"$elm"}',
     'execute store result storage mg:rate key.m int 1 run scoreboard players get $rgid mg.st',
     'data modify storage mg:rate key.f set value ""', 'data modify storage mg:rate key.g set value 0']
for k, l, c, rngs in GAMES:
    for a, b in rngs:
        m = f'{a}' if a == b else f'{a}..{b}'
        B.append(f'execute if score $game mg.st matches {m} run data modify storage mg:rate key merge value {{f:"{k}",g:{FIDX[k]}}}')
B += ['execute store result score $rgf mg.st run data get storage mg:rate key.g']
w('rate/begin', B)
w('rate/fix', ['# Macro {base, s} : carte au hasard → carte réellement jouée', '$scoreboard players operation $rgid mg.st = $(s) mg.st',
               '$scoreboard players add $rgid mg.st $(base)'])

# noms affichés dans la fenêtre de note
NM = ['# Noms du jeu et de la carte pour la fenêtre de note (storage mg:rate cur). Généré.',
      'data modify storage mg:rate cur set value {g:"Mini-jeu",m:""}']
for k, (l, c) in FLAB.items():
    NM.append(f'execute if data storage mg:rate key{{f:"{k}"}} run data modify storage mg:rate cur.g set value {snbt_str(l)}')
for n in sorted(NAMES):
    NAMES[n] = re.sub(r'^(\S+) \1 ', r'\1 ', NAMES[n])
    fam = fam_of_game(n) if n < 100 else None
    if fam and NAMES[n] == FLAB[fam][0]:
        NAMES[n] = ''
    if NAMES[n]:
        NM.append(f'execute if data storage mg:rate key{{m:{n}}} run data modify storage mg:rate cur.m set value {snbt_str(NAMES[n])}')
NM.append('data modify storage mg:rate cur.t set value "trigger mg.rt set 1$(a)$(b)$(c)"')
w('rate/names', NM)

# ------------------------------------------------------------------ fin de partie : fenêtre de note
w('rate/collect', ['# Retour au lobby : les participants peuvent noter (pas entre deux épreuves d\'une Mini Party). Généré.',
                   'execute unless score $rgf mg.st matches 1.. run return 0',
                   'execute if score $mp mg.st matches 1 unless score $game mg.st matches 59 run return 0',
                   'tag @a[tag=mg.play] add mg.rate', 'tag @a[tag=mg.out] add mg.rate',
                   'scoreboard players enable @a[tag=mg.rate] mg.rt',
                   'function mg:rate/names', 'schedule function mg:rate/ask 50t'])
OPT = lambda: [{'id': '0', 'display': {'text': '—', 'color': 'gray'}, 'initial': True}] + \
    [{'id': str(i), 'display': [{'text': '★' * i, 'color': 'gold'}, {'text': '☆' * (5 - i), 'color': 'dark_gray'}]} for i in range(1, 6)]
DLG = {'type': 'minecraft:multi_action', 'title': {'text': '⭐ Ton avis sur la partie', 'color': 'gold', 'bold': True},
       'pause': False, 'can_close_with_escape': True,
       'body': [{'type': 'minecraft:plain_message', 'width': 300, 'contents': [
           {'text': '@@g@@', 'color': 'yellow', 'bold': True}, {'text': '\n@@m@@', 'color': 'white'},
           {'text': '\nFacultatif. 1 = bof, 5 = génial, « — » = pas d\'avis. Les moyennes de tous les joueurs (depuis le début) s\'affichent dans les menus.', 'color': 'gray'}]}],
       'inputs': [{'type': 'minecraft:single_option', 'key': 'a', 'label': {'text': '🎮 Mode de jeu'}, 'width': 260, 'options': OPT()},
                  {'type': 'minecraft:single_option', 'key': 'b', 'label': {'text': '🗺 Carte'}, 'width': 260, 'options': OPT()},
                  {'type': 'minecraft:single_option', 'key': 'c', 'label': {'text': '🎉 Fun'}, 'width': 260, 'options': OPT()}],
       'columns': 1,
       'actions': [{'label': {'text': '✔ Envoyer', 'color': 'green', 'bold': True}, 'width': 200,
                    'action': {'type': 'minecraft:dynamic/run_command', 'template': '@@t@@'}}],
       'exit_action': {'label': {'text': 'Passer', 'color': 'gray'}, 'width': 200}}
s = js(DLG).replace('@@g@@', '$(g)').replace('@@m@@', '$(m)').replace('@@t@@', '$(t)')
w('rate/ask', ['# Fenêtre de note pour les participants encore connectés (macro via storage mg:rate cur). Généré.',
               'execute as @a[tag=mg.rate] run function mg:rate/show with storage mg:rate cur'])
w('rate/show', ['# @s : fenêtre de note', f'$return run dialog show @s {s}'])
w('rate/submit', ['# @s a envoyé sa note : mg.rt = 1 abc (a mode, b carte, c fun, 0 = pas d\'avis). Généré.',
                  'scoreboard players operation $rv mg.st = @s mg.rt', 'scoreboard players reset @s mg.rt',
                  'execute unless entity @s[tag=mg.rate] run return run tellraw @s {"text":"⭐ Plus de partie à noter.","color":"gray"}',
                  'execute unless score $rv mg.st matches 1000..1555 run return 0', 'tag @s remove mg.rate',
                  'scoreboard players remove $rv mg.st 1000',
                  'scoreboard players operation $ra1 mg.st = $rv mg.st', 'scoreboard players operation $ra1 mg.st /= #100 mg.st',
                  'scoreboard players operation $rb1 mg.st = $rv mg.st', 'scoreboard players operation $rb1 mg.st /= #10 mg.st',
                  'scoreboard players operation $rb1 mg.st %= #10 mg.st',
                  'scoreboard players operation $rc1 mg.st = $rv mg.st', 'scoreboard players operation $rc1 mg.st %= #10 mg.st',
                  'execute if score $ra1 mg.st matches 6.. run scoreboard players set $ra1 mg.st 0',
                  'execute if score $rb1 mg.st matches 6.. run scoreboard players set $rb1 mg.st 0',
                  'execute if score $rc1 mg.st matches 6.. run scoreboard players set $rc1 mg.st 0',
                  'function mg:rate/add with storage mg:rate key',
                  'function mg:rate/thanks with storage mg:rate key',
                  'execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1.2'])
w('rate/thanks', ['# Macro {f, m} : remerciement avec les moyennes à jour',
                  '$tellraw @s [{"text":"⭐ Merci ! ","color":"gold","bold":true},{"storage":"mg:rate","nbt":"cur.g","color":"yellow"},{"text":" ","color":"gray"},{"storage":"mg:rate","nbt":"lab.f$(f)","interpret":true},{"text":"  ·  ","color":"dark_gray"},{"storage":"mg:rate","nbt":"cur.m","color":"white"},{"text":" ","color":"gray"},{"storage":"mg:rate","nbt":"lab.r$(m)","interpret":true}]'])
w('rate/add', ['# Macro {m, f, g} : ajoute la note de @s ($ra1 mode, $rb1 carte, $rc1 fun) aux totaux, puis recalcule les libellés',
               '$execute if score $ra1 mg.st matches 1.. run scoreboard players operation #g$(g) mg.rgs += $ra1 mg.st',
               '$execute if score $ra1 mg.st matches 1.. run scoreboard players add #g$(g) mg.rgn 1',
               '$execute if score $rc1 mg.st matches 1.. run scoreboard players operation #g$(g) mg.rfs += $rc1 mg.st',
               '$execute if score $rc1 mg.st matches 1.. run scoreboard players add #g$(g) mg.rfn 1',
               '$execute if score $rb1 mg.st matches 1.. run scoreboard players operation #m$(m) mg.rts += $rb1 mg.st',
               '$execute if score $rb1 mg.st matches 1.. run scoreboard players add #m$(m) mg.rtn 1',
               '$execute if score #m$(m) mg.rtn matches 1.. run function mg:rate/lab_map {m:$(m)}',
               '$function mg:rate/lab_fam {f:"$(f)",g:$(g)}'])

# ------------------------------------------------------------------ câblage
patch('core/request', 'execute if score $game mg.st matches 100..196 run function mg:var/remap', ['scoreboard players operation $rgid mg.st = $game mg.st'])
patch('core/begin', 'execute if score $game mg.st matches 57..58 run function mg:bb/go', ['function mg:rate/begin'], where='before')
patch('core/return_lobby', 'execute as @a[tag=mg.win] run function mg:hall/credit', ['function mg:rate/collect'])
patch('core/tick', 'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 24 63 19 minecraft:gold_block run function mg:lobby/food_build',
      ['execute as @a[scores={mg.rt=1..}] run function mg:rate/submit'])
patch('core/load', 'scoreboard objectives add mg.bw trigger', [
    'scoreboard objectives add mg.rt trigger', 'scoreboard objectives add mg.rts dummy', 'scoreboard objectives add mg.rtn dummy',
    'scoreboard objectives add mg.rgs dummy', 'scoreboard objectives add mg.rgn dummy', 'scoreboard objectives add mg.rfs dummy',
    'scoreboard objectives add mg.rfn dummy', 'function mg:rate/init'])
patch('desinstaller', 'scoreboard objectives remove mg.bw', [
    'scoreboard objectives remove mg.rt', 'scoreboard objectives remove mg.rts', 'scoreboard objectives remove mg.rtn',
    'scoreboard objectives remove mg.rgs', 'scoreboard objectives remove mg.rgn', 'scoreboard objectives remove mg.rfs',
    'scoreboard objectives remove mg.rfn', 'schedule clear mg:rate/ask', 'data remove storage mg:rate lab'])
print('Notes :', len(CONVERTED), 'fenêtres converties,', len(DEFAULT), 'cartes avec étoiles d\'origine,', len(NAMES), 'noms de cartes')
