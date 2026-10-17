"""Arbre des menus : sous-menus des modes (cartes d'origine puis variantes ★), catégories, menu principal, retours.

Jamais lancé seul : gen_variants.py appelle run() après var_common.init() et les crochets (var_hooks).
"""
import os
import re

import var_common as VC
from var_cats import OPEN, build
from var_common import act, drop_lines, js, load_dialog, patch, save_dialog, w
from var_data import MODES, SET


# ============================================================ menus
def label_for(v):
    st = v['dif']
    return [{'text': f'✦ {v["map"]["name"]} ', 'color': v['map']['col']},
            {'text': '★' * st, 'color': 'gold'}, {'text': '☆' * (4 - st), 'color': 'dark_gray'}]


def tip_for(v):
    return [{'text': f'Carte {v["map"]["src"]} : {v["map"]["desc"]}\n', 'color': 'gray'},
            {'text': 'Réglages : ' + SET[v['mode']['key']][v['dif'] - 1], 'color': 'gold'}]


# ============================================================ arbre des menus
# Menu principal = catégories ; catégorie = jeux ; jeu = cartes natives puis variantes (★ → ★★★★).
def is_generated(a):
    cmd = a.get('action', {}).get('command', '')
    m = re.match(r'trigger mg\.(go|opt) set (\d+)$', cmd)
    return bool(m) and ((m.group(1) == 'go' and 100 <= int(m.group(2)) <= 196) or (m.group(1) == 'opt' and 32 <= int(m.group(2)) <= 39))


def is_back(a):
    lab = a['label'][0]['text'] if isinstance(a['label'], list) else a['label']
    return lab.startswith('«')


# actions existantes (pour garder leurs infobulles), lues dans tous les menus
KNOWN = {}


def known(cmd, label, col, tip=None):
    return KNOWN.get(cmd) or act(label, col, cmd, tip)


BODY_NOTE = [{'text': '\nCartes d’origine, puis ✦ variantes (ce jeu sur la carte d’un autre jeu, réglages adaptés). ', 'color': 'gray'},
             {'text': '★', 'color': 'gold'}, {'text': ' facile → ', 'color': 'gray'}, {'text': '★★★★', 'color': 'gold'},
             {'text': ' difficile.', 'color': 'gray'}]
OPT_CAT = {'sols': 40, 'equipes': 41, 'courses': 42, 'fete': 43, 'votes': 44, 'joueur': 45, 'kart': 46, 'arcade': 47, 'combat': 14,
           # choix de la carte des jeux d'arcade (cartes supplémentaires : tools/arcade/gen_maps.py)
           'tron': 50, 'koth': 51, 'uhc': 52, 'hg': 53, 'zombies': 54, 'infection': 55, 'wii': 56, 'autotamp': 57, 'ctf': 58}
SUB = {'pvp': ('sub_pvparena', 'combat'), 'oitc': ('sub_oitc', 'combat'), 'quake': ('quakemaps', 'combat'),
       'tnttag': ('sub_tnttag', 'combat'), 'spleef': ('sub_spleef', 'sols'), 'tntrun': ('sub_tntrun', 'sols'),
       'splegg': ('sub_splegg', 'sols')}
NEW_SUB = {'spleef': ('❄ Spleef', 'aqua', [act('❄ Spleef (tour de neige)', 'aqua', 'trigger mg.go set 1', 'Carte d’origine : 4 étages de neige')]),
           'tntrun': ('✷ TNT Run', 'red', [act('✷ TNT Run (3 étages de laine)', 'red', 'trigger mg.go set 2', 'Carte d’origine')])}


def back(cat):
    if cat == 'menu':
        return act('« Retour au menu', 'yellow', 'trigger mg.menu')
    return act('« Retour', 'yellow', f'trigger mg.opt set {OPT_CAT[cat]}')


def run():
    KNOWN.clear()
    for f in sorted(os.listdir(os.path.join(VC.D, 'dialog'))):
        if f.endswith('.json') and (f in ('menu.json', 'pvp.json') or f.startswith('cat_')):
            for a in load_dialog(f[:-5]).get('actions', []):
                KNOWN.setdefault(a.get('action', {}).get('command'), a)

    for m in MODES:
        name, parent = SUB[m['key']]
        d = load_dialog(name)
        if d is None:
            t, col, natives = NEW_SUB[m['key']]
            d = {'type': 'minecraft:multi_action', 'title': {'text': t, 'color': col, 'bold': True}, 'pause': False,
                 'can_close_with_escape': True, 'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Choisis la carte.', 'color': 'gray'}]}],
                 'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]}, 'actions': natives}
        natives = [a for a in d['actions'] if not is_generated(a) and not is_back(a)]
        vacts = [act(f'🎲 Variante au hasard', 'gold', f'trigger mg.go set {m["rnd"]}', f'Une des {len(m["vars"])} variantes ★, tirée au sort')]
        for v in sorted(m['vars'], key=lambda v: (v['dif'], v['id'])):
            vacts.append({'label': label_for(v), 'tooltip': tip_for(v),
                          'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.go set {v["id"]}'}})
        d['actions'] = natives + vacts + [back(parent)]
        body = d['body'][0]['contents']
        cut = next((i for i, c in enumerate(body) if isinstance(c, dict) and c.get('text', '').startswith('\n') and ('variante' in c.get('text', ''))), None)
        if cut is not None:
            del body[cut:]
        body += BODY_NOTE
        save_dialog(name, d)
        L = [f'# {m["name"]} : cartes + variantes (@s = admin) — fenêtre, sinon menu texte. Généré.',
             'scoreboard players set $dlg mg.st 0',
             f'execute store success score $dlg mg.st run dialog show @s mg:{name}',
             'execute if score $dlg mg.st matches 1 run return 0',
             'tellraw @s ' + js([{'text': f'\n{m["icon"]} {m["name"]} — variantes ', 'color': m['col'], 'bold': True},
                                 {'text': '(★ facile → ★★★★ difficile)', 'color': 'gray'}]),
             'tellraw @s ' + js(['', {'text': ' [🎲 Au hasard]', 'color': 'gold',
                                      'click_event': {'action': 'run_command', 'command': f'trigger mg.go set {m["rnd"]}'}}])]
        for v in sorted(m['vars'], key=lambda v: (v['dif'], v['id'])):
            L.append('tellraw @s ' + js(['', {'text': ' [' + v['map']['name'] + ' ', 'color': v['map']['col'],
                                             'click_event': {'action': 'run_command', 'command': f'trigger mg.go set {v["id"]}'},
                                             'hover_event': {'action': 'show_text', 'value': tip_for(v)}},
                                            {'text': '★' * v['dif'], 'color': 'gold'}, {'text': '☆' * (4 - v['dif']) + ']', 'color': 'dark_gray'}]))
        w(f'var/menu/{m["key"]}', L)

    for f in os.listdir(os.path.join(VC.D, 'dialog')):      # anciens menus séparés des variantes
        if f.startswith('var_') and f.endswith('.json'):
            os.remove(os.path.join(VC.D, 'dialog', f))

    CATS = build(known)
    for key, (title, col, body, acts, parent) in CATS.items():
        save_dialog(f'cat_{key}', {'type': 'minecraft:multi_action', 'title': {'text': title, 'color': col, 'bold': True},
                                   'pause': False, 'can_close_with_escape': True,
                                   'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': body, 'color': 'gray'}]}],
                                   'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]},
                                   'actions': acts + [back(parent)]})
        w(f'var/menu/cat_{key}', [f'# Catégorie « {title} » (@s = joueur) — fenêtre, sinon menu texte complet. Généré.',
                                  'scoreboard players set $dlg mg.st 0',
                                  f'execute store success score $dlg mg.st run dialog show @s mg:cat_{key}',
                                  'execute unless score $dlg mg.st matches 1 run function mg:core/menu_chat'])

    # Combat : le sous-menu PvP existant devient la catégorie (Bedwars et Sheep War passent dans Équipes)
    d = load_dialog('pvp')
    d['title'] = {'text': '⚔ Combat', 'color': 'red', 'bold': True}
    d['actions'] = [known(OPEN(23), '⚔ Arène PvP ▸', 'yellow'), known(OPEN(24), '➶ One in the Chamber ▸', 'gold'),
                    known(OPEN(10), '⚡ Quakecraft ▸', 'aqua'), act('✹ TNT Tag ▸', 'red', OPEN(29), 'La patate chaude'), back('menu')]
    save_dialog('pvp', d)

    # Menu principal : les catégories
    d = load_dialog('menu')
    keep = {a['action']['command']: a for a in d['actions']}
    d['body'] = [{'type': 'minecraft:plain_message', 'contents': [
        {'text': 'Choisis une catégorie, puis un jeu, puis sa carte. ', 'color': 'gray'},
        {'text': '★', 'color': 'gold'}, {'text': ' = variantes sur les cartes des autres jeux.', 'color': 'gray'}]}]
    d['actions'] = [
        act('❄ Jeux de sol ▸', 'aqua', OPEN(40), 'Spleef, TNT Run, Splegg, Sumo, Block Party, Enclumes', True),
        act('⚔ Combat ▸', 'red', OPEN(14), 'Arène PvP, One in the Chamber, Quakecraft, TNT Tag', True),
        act('⚑ Équipes ▸', 'light_purple', OPEN(41), 'Bedwars, Sheep War, Paintball, Turf Wars', True),
        act('🏁 Courses et vol ▸', 'gold', OPEN(42), 'Kart, bateaux, élytres, Dropper', True),
        known(OPEN(7), '☠ PvE ▸', 'dark_green'),
        act('🕹 Arcade ▸', 'light_purple', OPEN(47), 'Tron, King of the Hill, UHC, Hunger Games…', True),
        act('🎉 Fête et création ▸', 'green', OPEN(43), 'Mini Party, Build Battle, Téléphone', True),
        act('☑ Votes ▸', 'green', OPEN(44), 'Voter pour le prochain jeu'),
        act('👤 Joueur et plots ▸', 'aqua', OPEN(45), 'Spectateur, classement, plots'),
        keep.get('trigger mg.sv set 1') or act('🌲 Survie (monde libre)', 'green', 'trigger mg.sv set 1'),
        keep.get(OPEN(9)) or act('⛔ Arrêter la partie en cours', 'dark_red', OPEN(9)),
        act('🌍 TP général (admin) ▸', 'gold', OPEN(62), 'Tout le monde au lobby (sortie survie, GTA, plots…), en survie ou à Neo GTA'),
        act('🎉 Événements du lobby ▸', 'light_purple', OPEN(67), 'Lancer ou arrêter un événement surprise au spawn'),
        act('👁 Voir le menu joueur', 'aqua', OPEN(66), 'Ouvre le menu tel qu’un joueur le voit (votes)'),
        act('ℹ Version du datapack', 'gray', OPEN(48), 'Version en place / reçue de GitHub : savoir si une mise à jour a planté'),
        act('🚫 Exclure Zinedine', 'red', OPEN(49), 'Exclut Zinedine du serveur (définitivement, cette fois)')]
    save_dialog('menu', d)

    # Boutons retour des sous-menus : vers leur catégorie
    for name, cat in [('sub_sumo', 'sols'), ('sub_anvil', 'sols'), ('sub_bedwars', 'equipes'), ('sub_paint', 'equipes'), ('sheepmaps', 'equipes'),
                      ('sub_dropper', 'courses'), ('sub_elyrace', 'courses'), ('sub_elytra', 'courses'), ('sub_party', 'fete'), ('sub_bb', 'fete')]:
        d = load_dialog(name)
        d['actions'] = [a for a in d['actions'] if not is_back(a)] + [back(cat)]
        save_dialog(name, d)

    w('var/menu/main', ['# Ancien menu des variantes (opt 32) → menu principal. Généré.', 'function mg:core/menu_use'])
    w('var/menu/open', ['# mg.opt 32..46 → menus (catégories, jeux + variantes). Généré.',
                        'execute if score @s mg.opt matches 32 run function mg:var/menu/main'] +
      [f'execute if score @s mg.opt matches {m["opt"]} run function mg:var/menu/{m["key"]}' for m in MODES] +
      [f'execute if score @s mg.opt matches {o} run function mg:var/menu/cat_{k}' for k, o in OPT_CAT.items() if k != 'combat'])

    drop_lines('core/opt', ['execute if score @s mg.opt matches 32..39 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins.","color":"red"}',
                            'execute if score @s mg.opt matches 32..39 if entity @s[tag=mg.admin] run function mg:var/menu/open',
                            'execute if score @s mg.opt matches 46 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}',
                            'execute if score @s mg.opt matches 44..46 if entity @s[tag=mg.admin] run function mg:var/menu/open'])
    patch('core/opt', 'execute if score @s mg.opt matches 1 run function mg:core/opt_spec', [
        'execute if score @s mg.opt matches 32..43 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}',
        'execute if score @s mg.opt matches 46..47 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}',
        'execute if score @s mg.opt matches 32..43 if entity @s[tag=mg.admin] run function mg:var/menu/open',
        'execute if score @s mg.opt matches 44..47 if entity @s[tag=mg.admin] run function mg:var/menu/open',
        'execute if score @s mg.opt matches 44..45 unless entity @s[tag=mg.admin] run function mg:var/menu/open'], where='before')
