"""Noms courts et étoiles ★ sur les cartes d'origine des menus (difficulté indicative).

Jamais lancé seul : gen_variants.py appelle run() après var_menus.run() (les menus sont déjà écrits).
"""
import os
import re

import var_common as VC
from var_common import load_dialog, save_dialog


# ============================================================ noms courts + étoiles sur les cartes d'origine
# Étoiles des cartes d'origine = difficulté de la carte (indicatif : leurs réglages restent ceux d'origine).
NATIVE = {
    1: ('Tour de neige', 2), 2: ('Tour de laine', 2), 20: ('Splegg', 2), 21: ('Splegg XXL', 1),
    22: ('Disque', 2), 24: ('Arène complexe', 3), 28: ('Block Party', 2), 29: ('Classique', 2), 42: ('Sol troué', 3),
    3: ('Arène classique', 3), 13: ('Classes : classique', 3), 44: ('Poussière', 2), 45: ('Classes : Poussière', 2),
    47: ('Mirage', 2), 48: ('Classes : Mirage', 2), 50: ('Nuketown', 2), 51: ('Classes : Nuketown', 2),
    26: ('Arène', 2), 52: ('Château', 2), 53: ('Grande forêt', 3),
    31: ('Néon', 2), 32: ('Volcan XL', 3), 33: ('Jungle XL', 3), 34: ('Désert', 2), 35: ('Glacier', 3),
    43: ('Poussière', 2), 46: ('Mirage', 2), 49: ('Nuketown', 2), 79: ('🎯 Ravin (sniper)', 3), 80: ('🎯 Tours (sniper)', 3), 233: ('🌀 Spirale (vertical)', 3), 234: ('🏗 Chantier (vertical)', 3),
    67: ('Classique', 3), 68: ('Collines', 2), 69: ('Canyon', 2), 70: ('Village perché', 2),
    71: ('Classique', 2), 72: ('Caldeira', 2), 73: ('Hanami', 2), 74: ('Banquise', 3),
    5: ('Classique', 2), 7: ('Forteresses', 2), 14: ('Bastions', 2), 15: ('Cubes voxel', 2), 16: ('Pyramides inversées', 3),
    17: ('Archipel', 2), 18: ('Double canyon', 3), 19: ('Nuages voxel', 3),
    36: ('Terrain', 2), 54: ('Mini-terrain', 3), 55: ('Grand terrain', 1),
    6: ('Classique', 2), 8: ('Nether', 3), 9: ('End', 3), 10: ('Ultra hard', 4), 11: ('Volant', 3), 12: ('Araignée', 3),
    37: ('Cathédrale (20 vagues)', 4), 38: ('Laboratoire (20 vagues)', 4), 39: ('Temple (20 vagues)', 4),
    40: ('Forge (20 vagues)', 4), 41: ('Vaisseau (20 vagues)', 4),
    23: ('Dropper', 2), 25: ('Tube commun', 2), 64: ('Aventure', 3), 65: ('Défi', 3), 228: ('Solo : essais', 2),
    75: ('Course d\'anneaux', 2), 76: ('Course + combat', 3), 77: ('Survie en vol', 4),
    61: ('Circuit Champignon', 2), 62: ('Royaume Koopa', 3), 63: ('Bataille', 2), 56: ('Bateaux sur glace', 2),
    81: ('Canyon du Couchant', 3), 30: ('Turf Wars', 2),
    83: ('📞 Téléphone (5+)', 2), 84: ('⚡ Tron (à pied)', 3), 85: ('🏍 Tron moto', 4), 86: ('👑 King of the Hill', 2), 87: ('👑 KotH — équipes', 2), 88: ('🏰 The Towers', 3), 89: ('🚚 Convoi', 3), 90: ('🚚 Convoi — coop', 3), 91: ('▦ Block Party — bandes', 3), 92: ('▦ Block Party — mixte', 3), 93: ('🚩 Capture the Flag', 3), 94: ('⛏ Mini UHC Run', 3), 95: ('🏹 Mini Hunger Games', 3), 96: ('🎭 Prop Hunt', 2), 97: ('🧟 Zombies', 3), 98: ('🧪 Infection', 2), 220: ('🔴 1, 2, 3 Soleil', 2), 221: ('🚗 Autos tamponneuses', 2), 222: ('🚗 Autos tamponneuses — 3 coups', 2), 223: ('🚗 Autos tamponneuses — 8 coups', 2), 224: ('🟩 Slime Jump', 3), 225: ('🙈 Labyrinthe aveugle', 2), 226: ('👑 Master dit', 2), 227: ('🔪 Murder Mystery', 3), 242: ('🚩 CTF — Nether', 3), 243: ('🚩 CTF — Banquise', 3), 244: ('✷ TNT Run — Glacier', 3), 245: ('✷ TNT Run — Grand glacier', 3), 239: ('💣 Bomberman', 3), 240: ('💣 Bomberman — équipes', 3), 241: ('🌀 Labyrinthe géant', 3), 246: ('🎯 TDM sniper', 3),   # 81 = Canyon du Couchant (Course d'élytres : 66 = parcours au hasard, plus une carte)
}
SHORT_OPT = {   # boutons de navigation (mg.opt) : noms courts
    24: '➶ OITC ▸', 10: '⚡ Quake ▸', 20: '⚓ Enclumes ▸', 19: '⬇ Dropper ▸', 28: '🪽 Course élytres ▸', 23: '⚔ Arène PvP ▸',
    8: '☁ Sheep War ▸', 21: '▓ Paintball ▸', 29: '✹ TNT Tag ▸', 17: '❍ Splegg ▸', 18: '✊ Sumo ▸',
}
SHORT_TITLE = {'sub_oitc': '➶ OITC', 'quakemaps': '⚡ Quake', 'sub_anvil': '⚓ Enclumes', 'sub_dropper': '⬇ Dropper', 'sub_elyrace': '🪽 Course élytres'}


def star_label(name, n, col):
    return [{'text': name + ' ', 'color': col}, {'text': '★' * n, 'color': 'gold'}, {'text': '☆' * (4 - n), 'color': 'dark_gray'}]


def run():
    for f in sorted(os.listdir(os.path.join(VC.D, 'dialog'))):
        if not f.endswith('.json') or f.startswith('vote'):
            continue
        name = f[:-5]
        d = load_dialog(name)
        changed = False
        for a in d.get('actions', []) or []:
            cmd = a.get('action', {}).get('command', '')
            mg_ = re.match(r'trigger mg\.(go|opt) set (\d+)$', cmd)
            if not mg_ or not isinstance(a.get('label'), list):
                continue
            kind, n = mg_.group(1), int(mg_.group(2))
            col = a['label'][0].get('color', 'white')
            if kind == 'go' and n in NATIVE:
                nm, st = NATIVE[n]
                icon = a['label'][0].get('text', '').split(' ')[0]
                if name.startswith('cat_') and len(icon) <= 2 and not icon[:1].isalnum() and not nm.startswith(icon):   # dans une catégorie, garder l'icône du jeu
                    nm = f'{icon} {nm}'
                new = star_label(nm, st, col)
                if a['label'] != new:
                    a['label'] = new
                    changed = True
            elif kind == 'opt' and n in SHORT_OPT and a['label'][0].get('text') != SHORT_OPT[n]:
                a['label'] = [{**a['label'][0], 'text': SHORT_OPT[n]}]
                changed = True
        if name in SHORT_TITLE and d.get('title', {}).get('text') != SHORT_TITLE[name]:
            d['title']['text'] = SHORT_TITLE[name]
            changed = True
        if changed:
            save_dialog(name, d)
