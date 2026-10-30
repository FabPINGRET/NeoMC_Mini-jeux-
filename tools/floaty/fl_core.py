"""Patchs des fichiers SUIVIS du pack mg pour brancher la carte « Scourge of the Floaty Isles » (idempotents : relancer ne duplique rien).

    fl_core.check(racine_du_depot)     # SystemExit si une ancre manque (rien n'est modifié)
    fl_core.apply(racine_du_depot)

Même câblage que tools/arcade/gen_filon.py, ancré sur les lignes de Filon (donc à lancer après gen_ombrelune / gen_filon) :
core/tick (pre_tick + lobby_tick), survie/leave (renvoi), survie/cmd (mg.sv 10), core/pull_all + optout + request (mg.pullw : rappel
d'un admin), core/reconnect (rattrapage avant le « return 0 » des joueurs de survie), survie/tick (exclusions), core/load (état),
desinstaller (départ des joueurs en haut du fichier, avec ceux du Filon, avant la suppression de mg.st / mg.svid ; objectif, chunk forcé,
tags, storage), dialog/main_menu.json (bouton : après patch_menu, relancer `python tools/rating/gen_rating.py .` qui régénère
rate/d/main_menu*.mcfunction depuis ce menu).
Les générateurs tools/lobby/gen_sidebar.py (sb/auto : exclusion mg.flw, à relancer après : `python tools/lobby/gen_sidebar.py .`) et
tools/admin/gen_tp_general.py (tpg/survie : même ligne que le patch ci-dessous) portent leur propre ligne Floaty ; gen_tp_general
n'est PAS relancé (il réécrirait tpg/lobby sans la ligne du duel, que gen_duel y ajoute).
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'lib'))
import mcfn  # noqa: E402
from fl_wire import FORCE  # noqa: E402                   # chunk forcé de la carte : une seule définition

P = 'floaty'
BUTTON = 'trigger mg.sv set 10'
AFTER_BUTTON = 'trigger mg.sv set 9'                       # le bouton Floaty vient après celui du Filon
FN_LOAD = ['# Floaty : pas de session au chargement (le point de contrôle et les drapeaux du groupe, eux, sont gardés) ; le chunk forcé est persisté dans le monde :',
           '# après un arrêt en pleine session il resterait forcé à vie, session_start le recharge au besoin',
           'scoreboard players set $flw mg.st 0', f'execute in mg:floaty run forceload remove {FORCE}', 'scoreboard objectives add mg.fla dummy']
# LEAVE : tout en haut de desinstaller (avec ceux du Filon), AVANT la suppression de mg.st / mg.svid / mg.svvx : vault_save lit mg.svid et mg.svvx
LEAVE_ANCHOR = 'execute as @a[tag=mg.fnw] in minecraft:overworld run function mg:filon/leave'
FN_LEAVE = [f'execute as @a[tag=mg.flw] in minecraft:overworld run function mg:{P}/leave']
FN_UNINST = [f'execute in mg:floaty run forceload remove {FORCE}', 'tag @a remove mg.flw', 'tag @a remove mg.pullw',
             'data remove storage mg:floaty v', 'data remove storage mg:floaty cu']
# ('patch', fichier, ancre (ligne exacte), lignes, 'after' | 'before') ou ('replace', fichier, ancien texte, nouveau texte)
PATCHES = [
    ('patch', 'core/tick', 'function mg:ombre/pre_tick', [f'function mg:{P}/pre_tick'], 'after'),
    ('patch', 'core/tick', 'function mg:filon/lobby_tick', [f'function mg:{P}/lobby_tick'], 'after'),
    ('patch', 'survie/leave', 'execute if entity @s[tag=mg.fnw] run return run function mg:filon/leave',
     [f'execute if entity @s[tag=mg.flw] run return run function mg:{P}/leave'], 'after'),
    ('patch', 'survie/cmd', 'execute if score @s mg.sv matches 9 run function mg:filon/menu_go',
     [f'execute if score @s mg.sv matches 10 run function mg:{P}/menu_go'], 'after'),
    ('replace', 'survie/cmd', '9 = Filon,', '9 = Filon, 10 = Floaty,'),
    # rappel d'un admin (pull_all) : mg.pullw ; un joueur de la carte n'est pas un joueur de survie ordinaire
    ('replace', 'core/pull_all', 'tag=!mg.olw,tag=!mg.fnw] add mg.pulls', 'tag=!mg.olw,tag=!mg.fnw,tag=!mg.flw] add mg.pulls'),
    ('patch', 'core/pull_all', 'tag @a[tag=mg.fnw] add mg.pullf', ['tag @a[tag=mg.flw] add mg.pullw'], 'after'),
    ('patch', 'core/pull_all', 'tag @a[tag=mg.spectate] remove mg.pullf', ['tag @a[tag=mg.spectate] remove mg.pullw'], 'after'),
    ('patch', 'core/pull_all', 'execute as @a[tag=mg.pullf] in minecraft:overworld run function mg:filon/leave',
     [f'execute as @a[tag=mg.pullw] in minecraft:overworld run function mg:{P}/leave'], 'after'),
    ('patch', 'core/optout', 'execute if entity @s[tag=mg.pullf] in minecraft:overworld run function mg:filon/enter',
     [f'execute if entity @s[tag=mg.pullw] in minecraft:overworld run function mg:{P}/enter'], 'after'),
    ('patch', 'core/optout', 'tag @s remove mg.pullf', ['tag @s remove mg.pullw'], 'after'),
    ('patch', 'core/request', 'tag @a remove mg.pullf', ['tag @a remove mg.pullw'], 'after'),
    # TP général → survie : les joueurs de la carte en sortent d'abord (tpg/lobby, gta, terra, ombre, filon passent par survie/leave, qui les renvoie)
    ('patch', 'tpg/survie', 'execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.fnw] run function mg:filon/leave',
     [f'execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.mpp,tag=mg.flw] run function mg:{P}/leave'], 'after'),
    # survie/tick : un joueur de la carte est dans mg:floaty sans être un joueur de survie égaré (pre_tick le ramène s'il en sort)
    ('replace', 'survie/tick', 'tag=mg.surv,tag=!mg.fnw] at @s if dimension minecraft:overworld run function mg:survie/from_overworld',
     'tag=mg.surv,tag=!mg.fnw,tag=!mg.flw] at @s if dimension minecraft:overworld run function mg:survie/from_overworld'),
    ('replace', 'survie/tick', 'tag=!mg.fnw,tag=!mg.svg2,', 'tag=!mg.fnw,tag=!mg.flw,tag=!mg.svg2,'),
    # reconnexion : le rattrapage passe AVANT le « return 0 » des joueurs de survie (mg.surv est posé aussi pour la carte)
    ('patch', 'core/reconnect', 'execute if entity @s[tag=mg.surv] run return 0',
     ['# Dans la carte Floaty : la partie commune a avancé pendant son absence (cœurs, point de contrôle, avancements)',
      f'execute if entity @s[tag=mg.flw] run function mg:{P}/cu/run'], 'before'),
    ('patch', 'core/load', 'scoreboard objectives add mg.bw trigger', FN_LOAD, 'after'),
    ('patch', 'desinstaller', LEAVE_ANCHOR, FN_LEAVE, 'after'),
    ('patch', 'desinstaller', 'scoreboard objectives remove mg.bw', ['scoreboard objectives remove mg.fla'], 'after'),
    # AVANT floaty:uninstall : chunk forcé, tags et storages (les joueurs, eux, sont partis en haut du fichier : voir LEAVE_ANCHOR)
    ('patch', 'desinstaller', 'function floaty:uninstall', FN_UNINST, 'before'),
]


def _fn(root):
    return mcfn.Fn(str(Path(root) / 'data' / 'mg' / 'function'))


def check(root):
    """SystemExit (rien n'est modifié) si une ancre n'est pas trouvée exactement une fois (sauf patch déjà appliqué) ou si le menu n'a pas le bouton du Filon."""
    fn = _fn(root)
    for kind, rel, a, b, *w in PATCHES:
        if not os.path.exists(fn.path(rel)):
            raise SystemExit(f'abandon (rien n\'a été modifié) : {rel}.mcfunction introuvable')
        lines = fn.lines_of(rel)
        done = all(l in lines for l in b) if kind == 'patch' else b in '\n'.join(lines)
        n = lines.count(a) if kind == 'patch' else '\n'.join(lines).count(a)
        if rel == 'desinstaller' and a == 'function floaty:uninstall' and 'function mg:elyrace/uninstall' in lines:
            continue                    # l'appel de floaty:uninstall est posé par gen_floaty (check_desinstaller a validé son ancre)
        if not done and n != 1:
            raise SystemExit(f'abandon (rien n\'a été modifié) : {rel} : {a!r} trouvé {n} fois (une seule attendue)')
    menu = _menu(root)
    if BUTTON not in menu[1] and AFTER_BUTTON not in menu[1]:
        raise SystemExit(f'abandon (rien n\'a été modifié) : dialog/main_menu.json : bouton « {AFTER_BUTTON} » (Filon) introuvable')


def _menu(root):
    path = str(Path(root) / 'data' / 'mg' / 'dialog' / 'main_menu.json')
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    return path, [a['action'].get('command') for a in d['actions']], d


def patch_menu(root):
    """Bouton « Floaty » après celui du Filon (rien ne change s'il y est déjà)."""
    path, cmds, d = _menu(root)
    if BUTTON in cmds:
        return False
    d['actions'].insert(cmds.index(AFTER_BUTTON) + 1, {
        'label': [{'text': '🏝 Aller à Scourge of the Floaty Isles', 'color': 'aqua', 'bold': True}],
        'tooltip': [{'text': 'Une aventure en îles flottantes, une seule partie commune à tout le serveur : rejoins-la à tout moment (ton inventaire de la carte est gardé)', 'color': 'gray'}],
        'action': {'type': 'minecraft:run_command', 'command': BUTTON}})
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return True


def apply(root):
    """Applique PATCHES et le bouton du menu à data/mg de root (appeler check avant)."""
    fn = _fn(root)
    for kind, rel, a, b, *w in PATCHES:
        if kind == 'patch':
            fn.patch(rel, a, b, w[0])
        else:
            fn.replace(rel, a, b)
    patch_menu(root)
