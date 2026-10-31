"""Variantes : les modes de jeu sur les cartes des autres jeux, avec une difficulté ★ à ★★★★.

    python tools/variantes/gen_variants.py .        (depuis la racine du dépôt ; idempotent)

Génère :
  data/mg/function/var/**          remap des ids, annonce, préparation par mode, arènes, sols, réglages
  data/mg/dialog/var_*.json        menus (★ Variantes ▸ dans le menu principal et les sous-menus)
  data/mg/tags/block/ray_pass.json blocs traversés par le rayon du Quake (herbes, fleurs…)
et applique de petits crochets (marqués « [variantes] ») dans les fichiers des jeux concernés.

Principe : un id de variante (100..196) fixe $ar (arène ou sol, 0 = carte native), $dif (1..4)
et $vmode (jeu). Les jeux gardent leur comportement natif tant que $ar = 0 (et $dif = 2 = réglages actuels).

Familles :
  combat  : PvP (3), One in the Chamber (26), Quakecraft (31), TNT Tag (27) sur 18 arènes
            (cartes PvP, OITC, Quake, TNT Tag, Paintball). Exclus : l'arène PvP classique (sol y 63),
            le Paintball comme mode (il lui faut du béton blanc et deux bases).
  sols    : Spleef (1), TNT Run (2), Splegg (20) sur 6 formes de sol construites au même endroit
            (centre 0 ~ 24300) : 4 reprises des jeux + Pyramide + Anneaux.
            Exclus : Pluie d'enclumes et Block Party (mécaniques liées à leur sol).

Modules (jamais lancés seuls, chargés ici après VC.init) : var_common.py (écriture des fonctions et des menus, crochets
idempotents patch / replace), var_data.py (arènes, sols, modes, réglages, liste des variantes), var_combat.py,
var_floors.py (préparation par mode), var_hooks.py (crochets dans les jeux), var_menus.py + var_cats.py (arbre des
menus), var_stars.py (noms courts et étoiles), var_votemaps.py (votes par carte), var_voteauto.py (majorité de votes),
var_sizes.py (taille de chaque carte dans les infobulles).
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')   # sortie console en UTF-8 (Windows : cp1252 sinon)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import var_common as VC                                          # noqa: E402
VC.init(sys.argv[1] if len(sys.argv) > 1 else '.')
import var_combat                                                # noqa: E402
import var_data                                                  # noqa: E402
import var_floors                                                # noqa: E402
import var_hooks                                                 # noqa: E402
import var_menus                                                 # noqa: E402
import var_stars                                                 # noqa: E402
import var_voteauto                                              # noqa: E402
import var_votemaps                                              # noqa: E402
import var_sizes                                                 # noqa: E402
from var_common import js, stars, w                              # noqa: E402
from var_data import MODES, SET, VARIANTS                        # noqa: E402


def write_remap_start():
    # ============================================================ remap + annonce
    lines = ['# Variantes (généré par tools/variantes/gen_variants.py) : id → $vmode (jeu), $ar (arène/sol), $dif (1..4)',
             '# Appelé par core/request quand $game = 100..196 ; ne change pas $game (pour ne pas déclencher les annonces natives)']
    for m in MODES:
        n = len(m['vars'])
        lines.append(f'execute if score $game mg.st matches {m["rnd"]} store result score $vr mg.st run random value 0..{n - 1}')
        for i, v in enumerate(m['vars']):
            lines.append(f'execute if score $game mg.st matches {m["rnd"]} if score $vr mg.st matches {i} run scoreboard players set $game mg.st {v["id"]}')
    for v in VARIANTS:
        lines += [f'execute if score $game mg.st matches {v["id"]} run scoreboard players set $vmode mg.st {v["mode"]["game"]}',
                  f'execute if score $game mg.st matches {v["id"]} run scoreboard players set $ar mg.st {v["ar"]}',
                  f'execute if score $game mg.st matches {v["id"]} run scoreboard players set $dif mg.st {v["dif"]}']
    lines.append('scoreboard players operation $vid mg.st = $game mg.st')
    w('var/remap', lines)

    lines = ['# Variante : annonce puis $game = jeu réel (@s = demandeur). Généré.']
    for v in VARIANTS:
        m, a = v['mode'], v['map']
        st = v['dif']
        lines.append(f'execute if score $vid mg.st matches {v["id"]} run tellraw @a ' + js([
            {'selector': '@s', 'color': 'yellow'}, {'text': ' lance ', 'color': 'gray'},
            {'text': f'{m["icon"]} {m["short"]} — {a["name"].upper()} ', 'color': m['col'], 'bold': True},
            {'text': '★' * st, 'color': 'gold'}, {'text': '☆' * (4 - st), 'color': 'dark_gray'}, {'text': ' !', 'color': 'gray'}]))
        lines.append(f'execute if score $vid mg.st matches {v["id"]} run tellraw @a ' + js([
            {'text': 'Variante : ', 'color': 'gray'}, {'text': f'carte {a["src"]} ({a["desc"]})', 'color': 'white'},
            {'text': ' · réglages : ', 'color': 'gray'}, {'text': SET[m['key']][st - 1], 'color': 'gold'}]))
    lines.append('scoreboard players operation $game mg.st = $vmode mg.st')
    w('var/start', lines)


# Ordre imposé : chaque étape relit ce que les précédentes ont écrit (voir les docstrings des modules)
write_remap_start()
var_combat.run()
var_floors.run()
var_hooks.run()
var_menus.run()
var_stars.run()
var_votemaps.run()
var_voteauto.run()
var_sizes.run()

# ============================================================ récapitulatif (docs)
md = ['# Variantes (générées par `tools/variantes/gen_variants.py`)', '',
      'Chaque mode sur les cartes des autres jeux. La difficulté (★ à ★★★★) dépend de la carte et change les réglages.',
      'Menu : ≡ → catégorie (❄ Jeux de sol / ⚔ Combat) → jeu → cartes d’origine puis variantes ★.', '',
      '| Réglages | ★ | ★★ | ★★★ | ★★★★ |', '|---|---|---|---|---|']
for m in MODES:
    md.append(f'| {m["name"]} | ' + ' | '.join(SET[m['key']]) + ' |')
md += ['', '| Id | Mode | Carte (origine) | Difficulté |', '|---|---|---|---|']
for m in MODES:
    md.append(f'| {m["rnd"]} | {m["name"]} | variante au hasard | |')
    for v in m['vars']:
        md.append(f'| {v["id"]} | {m["name"]} | {v["map"]["name"]} ({v["map"]["src"]}) | {stars(v["dif"])} |')
os.makedirs(os.path.join(VC.R, 'docs'), exist_ok=True)
with open(os.path.join(VC.R, 'docs/VARIANTES.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(md) + '\n')

print(f'{len(VARIANTS)} variantes (ids 100..{var_data.LAST_ID - 1}, hasard 190..196), {len(VC.written)} fichiers générés')
for m in MODES:
    print(f'  {m["name"]:<20} {len(m["vars"]):>2}  opt {m["opt"]}  ' + ' '.join(f'{v["id"]}{stars(v["dif"])}' for v in m['vars']))

# Les notes des joueurs remplacent les étoiles dans les menus : à refaire après chaque régénération des menus
import runpy
runpy.run_path(os.path.join(HERE, '..', 'rating', 'gen_rating.py'), run_name='__main__')
