"""Outils communs du générateur de variantes (écriture des fonctions et des menus, crochets idempotents).

Jamais lancé seul : gen_variants.py appelle init(racine) avant d'importer les autres modules var_*.
R, D, F sont lus à l'appel (VC.F, jamais `from var_common import F`) : ils n'existent qu'après init().
`written` est la liste des fichiers écrits (comptée dans le récapitulatif).
"""
import json
import os

R = '.'
D = F = None
written = []


def init(root):
    global R, D, F
    R = root
    D = os.path.join(R, 'data/mg')
    F = os.path.join(D, 'function')


def w(rel, lines):
    path = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    written.append(path)


def wjson(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')
    written.append(path)


def stars(n):
    return '★' * n + '☆' * (4 - n)


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def patch(rel, anchor, new_lines, where='after', count=1):
    """Insère new_lines (marquées) avant/après la ligne qui contient exactement `anchor` ; ne fait rien si déjà fait."""
    path = os.path.join(F, rel + '.mcfunction')
    txt = open(path, encoding='utf-8').read()
    if all(l in txt for l in new_lines):
        return
    lines = txt.split('\n')
    idx = [i for i, l in enumerate(lines) if l == anchor]
    if len(idx) != count:
        raise SystemExit(f'{rel} : ancre introuvable ou multiple ({len(idx)}) : {anchor!r}')
    i = idx[0] + (1 if where == 'after' else 0)
    lines[i:i] = new_lines
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))


def replace(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    txt = open(path, encoding='utf-8').read()
    if new in txt:
        return
    if txt.count(old) != 1:
        raise SystemExit(f'{rel} : texte à remplacer introuvable ou multiple : {old!r}')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt.replace(old, new))


def drop_lines(rel, lines):
    path = os.path.join(F, rel + '.mcfunction')
    txt = open(path, encoding='utf-8').read().split('\n')
    txt = [l for l in txt if l not in lines]
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(txt))


# Menus : un dialogue = data/mg/dialog/<nom>.json
def load_dialog(name):
    p = os.path.join(D, f'dialog/{name}.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None


def save_dialog(name, d):
    wjson(os.path.join(D, f'dialog/{name}.json'), d)


def act(label, col, cmd, tip=None, bold=False):
    a = {'label': [{'text': label, 'color': col, **({'bold': True} if bold else {})}]}
    if tip:
        a['tooltip'] = [{'text': tip, 'color': 'gray'}]
    a['action'] = {'type': 'minecraft:run_command', 'command': cmd}
    return a
