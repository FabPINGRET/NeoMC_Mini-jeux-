"""Outils communs aux générateurs de mini-jeux (écriture idempotente + câblage dans core/)."""
import json
import os
import re

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
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def lines_of(rel):
    return open(os.path.join(F, rel + '.mcfunction'), encoding='utf-8').read().split('\n')


def patch(rel, anchor, new_lines, where='after'):
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
    lo, hi = min(gids), max(gids)
    m = f'{lo}' if lo == hi else f'{lo}..{hi}'
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
    patch('core/forceloads', 'function mg:tnttag/map/fl', lines, where='before')


def announce(gid, cond, icon_name, col, desc):
    return (f'execute if score $game mg.st matches {gid}{cond} run tellraw @a ' + js([
        {'selector': '@s', 'color': 'yellow'}, {'text': ' lance ', 'color': 'gray'}, {'text': icon_name, 'color': col, 'bold': True},
        {'text': f' : {desc}', 'color': 'gray'}]))
