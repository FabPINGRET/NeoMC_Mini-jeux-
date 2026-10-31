"""Taille de chaque carte dans les infobulles des menus (mg.go set <id> et votes mg.vote set 1000+<id>).

Jamais lancé seul : gen_variants.py appelle run() en dernier (après var_votemaps, qui écrit les fenêtres vote_m*).
Les variantes ✦ (ids 100..196) ont leur taille dans var_data (desc des arènes et des sols).
Tailles mesurées sur les fonctions de construction (boîte des blocs posés, murs de barrière exclus) ; quand une carte
était déjà décrite avec une taille (README, infobulle), c'est cette valeur qui est gardée.
Règle d'écriture, pour chaque bouton de carte dont l'infobulle n'a pas encore de taille (« 31×31 ») :
- infobulle vide : description reprise d'un autre menu pour la même carte, sinon « Carte » ; puis la taille ;
- sinon : « (taille) » ajouté à la fin du texte.
Idempotent : une infobulle qui contient déjà une taille n'est pas touchée.
"""
import json
import os
import re

import var_common as VC

# id de lancement -> taille (lue entre parenthèses, ou après « Carte » si l'infobulle est vide)
SIZES = {
    # sols
    1: '29×29', 2: '29×29', 244: '29×29', 245: '35×35 → 27×27', 20: '37×37', 21: '61×61 → 45×45',
    22: 'disque de 15×15 à 23×23 selon le nombre de joueurs', 24: '31×31', 29: '21×21', 42: '21×21',
    28: '24×24', 91: '24×24', 92: '24×24', 251: '24×24',
    # combat
    3: '27×27', 13: '27×27', 44: '41×41', 45: '41×41', 47: '41×41', 48: '41×41', 50: '49×35', 51: '49×35',
    26: '25×25', 52: '41×41', 53: '71×71',
    31: '31×31', 32: '61×61', 33: '61×61', 34: '31×31', 35: '19×19', 43: '41×41', 46: '41×41', 49: '49×35',
    79: '41×121', 80: '101×101',
    67: '31×31', 68: '51×51', 69: '51×51', 70: '51×51', 252: '51×51', 253: '51×51',
    # équipes
    71: '75×75', 72: '87×86', 73: '84×83', 74: '91×89',
    5: '71×43', 7: '83×43', 14: '59×33', 15: '63×20', 16: '77×29', 17: '81×29', 18: '101×41', 19: '81×31',
    254: '33×13', 255: '37×9',
    36: '49×61', 54: '31×41', 55: '81×101', 30: '31×25', 88: '81×19', 89: '145×29', 90: '145×29', 246: 'arènes de 41×141',
    93: '85×45', 242: '85×45', 243: '85×45',
    # PvE et arcade
    6: '31×31', 8: '31×31', 9: '31×31', 10: '31×31', 11: '31×31', 12: '31×31',
    37: '29×53', 38: '39×39', 39: '53×53', 40: '61×61', 41: '45×45',
    97: '53×53', 210: '53×53', 212: '53×53', 229: '75×77', 231: '101×70', 235: '95×45', 237: '89×71', 247: '53×63', 249: '51×59',
    98: '53×53', 211: '53×53', 213: '53×53', 230: '75×77', 232: '101×70', 236: '95×45', 238: '89×71', 248: '53×63', 250: '51×59',
    217: '53×53', 218: '53×53', 219: '53×53',
    86: '51×51', 87: '51×51', 206: '51×51', 207: '51×51', 208: '51×51', 209: '51×51',
    94: '85×81', 202: '83×81', 204: '84×81', 95: '101×101', 203: '101×101', 205: '101×101',
    84: '101×101', 85: '101×101', 200: '201×201', 201: '201×201',
    96: '3 cartes, de 41×31 à 49×33', 227: 'cartes de 41×31 à 49×33', 99: 'ville de 178×179', 198: '57×41', 220: '43×99',
    224: 'parcours de 12×150', 225: '18×18', 226: '21×21', 239: '23×21', 240: '23×21', 241: '100×100',
    221: '47×47', 222: '47×47', 223: '47×47',
    # courses
    56: '94×54', 61: '280×222', 62: '497×365', 63: '201×201',
    23: 'puits de 5×5, 66 blocs de chute', 25: 'tube de 11×11', 64: 'puits de 37×37', 65: 'puits de 37×37', 228: 'puits de 37×37',
    75: 'zone de 376×743', 76: 'zone de 376×743', 77: 'arène de 185×185',
    # fête
    57: 'parcelle de 25×25 par joueur', 58: 'parcelle de 25×25 par joueur', 59: 'île de 181×181', 60: 'île de 181×181',
    214: '8 pistes, 68×55', 215: '199×199', 216: '4 courts, 160×51',
}
HAS_SIZE = re.compile(r'\d{2,}\s?×\s?\d+')
GO = re.compile(r'trigger mg\.go set (\d+)$')
VOTE = re.compile(r'trigger mg\.vote set (1\d{3})$')


def text(t):
    if isinstance(t, str):
        return t
    if isinstance(t, list):
        return ''.join(text(x) for x in t)
    if isinstance(t, dict):
        return t.get('text', '') + text(t.get('extra', []))
    return ''


def map_id(a):
    cmd = a.get('action', {}).get('command', '')
    m = GO.match(cmd)
    if m:
        return int(m.group(1))
    m = VOTE.match(cmd)
    return int(m.group(1)) - 1000 if m else None


def run():
    ddir = os.path.join(VC.D, 'dialog')
    files = sorted(f for f in os.listdir(ddir) if f.endswith('.json'))
    dialogs = {f: json.load(open(os.path.join(ddir, f), encoding='utf-8')) for f in files}
    desc = {}                                   # id -> description (sans taille) trouvée dans un menu
    for d in dialogs.values():
        for a in d.get('actions', []) or []:
            i, t = map_id(a), text(a.get('tooltip', '')).strip()
            if i in SIZES and t and '\n' not in t and i not in desc:
                desc[i] = re.sub(r'\s*\([^()]*×[^()]*\)$', '', t)
    n = 0
    for f, d in dialogs.items():
        changed = False
        for a in d.get('actions', []) or []:
            i = map_id(a)
            if i not in SIZES:
                continue
            t = text(a.get('tooltip', '')).strip()
            if HAS_SIZE.search(t) or SIZES[i] in t:
                continue
            if not t:
                d0 = desc.get(i)
                new = d0 if d0 and HAS_SIZE.search(d0) else f'{d0} ({SIZES[i]})' if d0 else f'Carte : {SIZES[i]}'
                a['tooltip'] = [{'text': new, 'color': 'gray'}]
            else:
                tip = a['tooltip']
                if isinstance(tip, str):
                    tip = [{'text': tip, 'color': 'gray'}]
                elif isinstance(tip, dict):
                    tip = [tip]
                a['tooltip'] = tip + [{'text': f' ({SIZES[i]})', 'color': 'gray'}]
            changed = True
            n += 1
        if changed:
            VC.save_dialog(f[:-5], d)
    print(f'Tailles des cartes : {n} infobulles complétées')
