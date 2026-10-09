"""Outils communs aux générateurs de mini-jeux (écriture idempotente + câblage dans core/).

Cartes supplémentaires (« clones ») : tools/arcade/gen_maps.py relance un générateur avec la variable d'environnement
NEOMC_MAP (JSON) : {"sfx": "2", "keys": ["koth"], "ids": {"86": 206, "87": 207}, "entry": "koth", "label": "Pyramide", "p": {...}}.
Le générateur lit ses réglages avec param() ; ici, tout ce qu'il écrit est renommé (dossier koth → koth2, appels
mg:koth/ → mg:koth2/, ids de jeu 86 → 206) et la zone n'est chargée (forceload) que pendant la partie :
<entry>/prepare charge la zone puis lance <entry>/prepare_b 3 s plus tard (la préparation d'origine), <entry>/cleanup la libère.
"""
import atexit
import json
import os
import re

MAP = json.loads(os.environ.get('NEOMC_MAP') or 'null')
_FL = []          # zones de la carte clonée (forceload pendant la partie)
_ENTRY = {}       # textes de prepare / cleanup du point d'entrée (réécrits à la fin)


def param(name, default):
    """Réglage de la carte : valeur du clone, sinon valeur d'origine."""
    return MAP['p'].get(name, default) if MAP else default


def _id(n):
    return int(MAP['ids'].get(str(n), n)) if MAP else int(n)


def _tx(s):
    """Texte d'une commande → version clone (appels de fonctions et ids de jeu)."""
    if not MAP:
        return s
    keys = '|'.join(sorted(map(re.escape, MAP['keys']), key=len, reverse=True))
    s = re.sub(r'((?:function|clear) mg:)(' + keys + r')/', lambda m: m.group(1) + m.group(2) + MAP['sfx'] + '/', s)
    s = re.sub(r'(\$game mg\.st matches )(\d+)(?:\.\.(\d+))?',
               lambda m: m.group(1) + (str(_id(m.group(2))) if not m.group(3) else f'{_id(m.group(2))}..{_id(m.group(3))}'), s)
    return s


def _rel(rel):
    if not MAP:
        return rel
    head, _, rest = rel.partition('/')
    return (head + MAP['sfx'] if head in MAP['keys'] else head) + '/' + rest

R = '.'
D = F = None


def init(root):
    global R, D, F
    R = root
    D = os.path.join(R, 'data/mg')
    F = os.path.join(D, 'function')


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def w(rel, lines):
    if MAP:
        if rel.partition('/')[0] not in MAP['keys']:      # fichier commun (ex. gun/) : réécrit tel quel
            return _write(rel, lines)
        rel, lines = _rel(rel), [_tx(l) for l in lines]
        e = MAP['entry'] + MAP['sfx']
        if rel in (e + '/prepare', e + '/cleanup'):
            _ENTRY[rel] = lines
            return
    _write(rel, lines)


def _write(rel, lines):
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def lines_of(rel):
    return open(os.path.join(F, rel + '.mcfunction'), encoding='utf-8').read().split('\n')


def patch(rel, anchor, new_lines, where='after'):
    new_lines = [_tx(l) for l in new_lines]
    p = os.path.join(F, rel + '.mcfunction')
    lines = open(p, encoding='utf-8').read().split('\n')
    if all(l in lines for l in new_lines):
        return
    idx = [i for i, l in enumerate(lines) if l == anchor]
    if len(idx) != 1:
        raise SystemExit(f'{rel} : ancre {anchor!r} trouvée {len(idx)} fois')
    i = idx[0] + (1 if where == 'after' else 0)
    lines[i:i] = new_lines
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))


def go_range(gid):
    """Élargit la plage d'ids acceptés par core/go (1..N) si besoin."""
    p = os.path.join(F, 'core/go.mcfunction')
    t = open(p, encoding='utf-8').read()
    m = re.search(r'unless score @s mg\.go matches 1\.\.(\d+) unless', t)
    if m and int(m.group(1)) < gid:
        t = t.replace(m.group(0), f'unless score @s mg.go matches 1..{gid} unless')
        open(p, 'w', encoding='utf-8', newline='\n').write(t)


def register(gids, key, announce_lines, prepare=True, go=True, tick=True, cleanup=True):
    """Câble un jeu (ids gids, dossier key) : annonce, prepare, go, tick, cleanup, plage d'ids."""
    gids = [_id(g) for g in gids]
    if MAP:
        key = key + MAP['sfx'] if key in MAP['keys'] else key
    lo, hi = min(gids), max(gids)
    m = f'{lo}' if lo == hi else f'{lo}..{hi}'
    if not MAP:
        go_range(hi)
    anchor_ann = next(l for l in lines_of('core/request') if l.startswith('execute if score $game mg.st matches 57 run tellraw'))
    patch('core/request', anchor_ann, announce_lines, where='before')
    if prepare:
        patch('core/request', 'execute if score $game mg.st matches 57..58 run function mg:bb/prepare', [f'execute if score $game mg.st matches {m} run function mg:{key}/prepare'])
    if go:
        patch('core/begin', 'execute if score $game mg.st matches 57..58 run function mg:bb/go', [f'execute if score $game mg.st matches {m} run function mg:{key}/go'])
    if tick:
        patch('core/game_tick', 'execute if score $game mg.st matches 57..58 run function mg:bb/tick', [f'execute if score $game mg.st matches {m} run function mg:{key}/tick'])
    if cleanup:
        patch('core/return_lobby', 'execute if score $game mg.st matches 57..58 run function mg:bb/cleanup', [f'execute if score $game mg.st matches {m} run function mg:{key}/cleanup'])


def objectives(names):
    """names : [(objectif, critère)] → core/load + desinstaller."""
    patch('core/load', 'scoreboard objectives add mg.bw trigger', [f'scoreboard objectives add {n} {c}' for n, c in names])
    patch('desinstaller', 'scoreboard objectives remove mg.bw', [f'scoreboard objectives remove {n}' for n, c in names])


def forceload(lines):
    if MAP:     # carte clonée : zone chargée seulement pendant la partie
        _FL.extend(l for l in lines if l.startswith('forceload add '))
        return
    patch('core/forceloads', 'function mg:tnttag/map/fl', lines, where='before')


def announce(gid, cond, icon_name, col, desc):
    if MAP:
        icon_name = f'{icon_name} — {MAP.get("labels", {}).get(str(gid), MAP["label"])}'
        gid = _id(gid)
    return (f'execute if score $game mg.st matches {gid}{cond} run tellraw @a ' + js([
        {'selector': '@s', 'color': 'yellow'}, {'text': ' lance ', 'color': 'gray'}, {'text': icon_name, 'color': col, 'bold': True},
        {'text': f' : {desc}', 'color': 'gray'}]))


@atexit.register
def _finish():
    """Clone : prepare = charger la zone puis préparer 3 s plus tard ; cleanup = libérer la zone."""
    if not MAP or not F:
        return
    e = MAP['entry'] + MAP['sfx']
    prep = _ENTRY.get(e + '/prepare')
    if prep is not None:
        wait = []
        for l in _FL:      # zone pas encore chargée : on réessaie 1 s plus tard
            x1, z1, x2, z2 = map(int, l.split()[2:6])
            for x, z in ((x1, z1), (x2, z2), ((x1 + x2) // 2, (z1 + z2) // 2)):
                wait.append(f'execute unless loaded {x} 80 {z} run return run schedule function mg:{e}/prepare_b 20t')
        _write(e + '/prepare_b', [f'# {MAP.get("label") or e} : préparation (zone chargée par {e}/prepare)',
                                  'execute unless score $state mg.st matches 1 run return 0'] + wait + prep)
        _write(e + '/prepare', [f'# {MAP.get("label") or e} : la zone n\'est chargée que pendant la partie'] + _FL +
               [f'schedule function mg:{e}/prepare_b 60t'])
        patch('desinstaller', 'scoreboard objectives remove mg.bw', [f'schedule clear mg:{e}/prepare_b'] +
              [l.replace('forceload add ', 'forceload remove ') for l in _FL])
    clean = _ENTRY.get(e + '/cleanup')
    if clean is not None:
        _write(e + '/cleanup', clean + [l.replace('forceload add ', 'forceload remove ') for l in _FL] +
               [f'schedule clear mg:{e}/prepare_b'])
