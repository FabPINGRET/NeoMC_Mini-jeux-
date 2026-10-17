"""Bandeau des décors saisonniers (importé par gen_themes.py, jamais lancé seul) : une bossbar mg:thb qui présente, à tour de rôle,
les nouveautés du thème en place (PNJ, chapeaux, événement, mobs, cartes).

Cycle (lobby/theme/banner, appelé chaque seconde par lobby/theme/tick) : $thbt compte 0..PERIOD-1 ; toutes les STEP secondes une
nouvelle ligne (la barre se remplit d'un cran par ligne), puis plus rien jusqu'à la fin de la période. Visible pour les joueurs du
spawn qui ne jouent pas, ne sont ni en survie, ni sur un plot, ni en visite, ni spectateurs ; masqué quand l'événement du lobby (mg:ev) est affiché.
Création à la volée (bossbar add si absente) ; retrait : lobby/theme/banner_hide (fin de ligne, événement), lobby/theme/off,
core/load et desinstaller. Une ligne = (couleur de la barre, texte) ; {n} = nombre de chapeaux du thème (tools/cosmetics/hats_data.py).
Ajouter un thème : une entrée dans FEATURES (mêmes clés que THEMES de gen_themes.py). Glyphes : seulement ceux déjà présents dans data/.
"""
import os
import sys

import common as C
from theme_world import LOBBY

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cosmetics'))
from hats_data import HATS                                       # noqa: E402

STEP = 8                                 # secondes par ligne
PERIOD = 180                             # secondes entre deux séries de lignes
FEATURES = {
    'halloween': ('purple', [
        '🎃 Ragoût mystère de la sorcière : un effet surprise à chaque bol… oserez-vous ?',
        '🎩 {n} chapeaux d\'Halloween, galerie sous le Hall des scores',
        '🍬 Événement : la pluie de pièces devient chasse aux bonbons',
        '👻 Fantômes, chauves-souris et eau rouge au spawn',
        '🎃 Les cartes de jeu se parent d\'Halloween en partie']),
    'noel': ('red', [
        '🎄 Le lutin du buffet offre 3 feux d\'artifice (à ciel ouvert)',
        '🎩 {n} chapeaux de Noël, galerie sous le Hall des scores',
        '🎁 Événement : la pluie de pièces devient chasse aux cadeaux',
        '🔴 Bonhommes de neige, rennes et Rudolph au spawn',
        '❄ De la neige sur les cartes de jeu en partie']),
}
SPEC = ',gamemode=!spectator]'
assert LOBBY.endswith(SPEC), 'theme_world.LOBBY a changé de forme : adapter SHOWN'
SHOWN = LOBBY[:-len(SPEC)] + ',tag=!mg.inplot,tag=!mg.visit' + SPEC     # joueurs du spawn qui ne jouent pas, hors plots


def write(THEMES):
    """THEMES = [(id, clé, libellé, mg.opt, fabrique)] : lignes par thème, banner, banner_hide, branchements (après TN.wire)."""
    w, js = C.w, C.js
    assert set(FEATURES) == {key for _, key, *_ in THEMES}, 'FEATURES : une entrée par thème de THEMES'
    top = [f'execute if score $theme mg.st matches {tid} if score $thbl mg.st matches {len(FEATURES[key][1]) + 1}.. run return run '
           'function mg:lobby/theme/banner_hide' for tid, key, *_ in THEMES]
    for _, key, label, *__ in THEMES:
        color, texts = FEATURES[key]
        assert len(texts) * STEP < PERIOD, f'{key} : {len(texts)} lignes x {STEP} s doivent tenir dans {PERIOD} s'
        n = sum(1 for h in HATS if h[3] == key)
        assert n, f'{key} : aucun chapeau de saison dans hats_data.HATS'
        w(f'lobby/theme/{key}/banner', [f'# Bandeau {key} (appelé chaque seconde par lobby/theme/banner ; $thbl = ligne à afficher, 1..{len(texts)})',
                                       f'bossbar set mg:thb color {color}', f'bossbar set mg:thb max {len(texts)}',
                                       'execute store result bossbar mg:thb value run scoreboard players get $thbl mg.st'] +
          [f'execute if score $thbl mg.st matches {k} run bossbar set mg:thb name ' +
           js([{'text': f'{label} · ', 'color': {'purple': 'dark_purple'}.get(color, color), 'bold': True}, {'text': t.format(n=n), 'color': 'white'}])
           for k, t in enumerate(texts, 1)])
    w('lobby/theme/banner', [
        f'# Bandeau du thème en place (chaque seconde, lobby/theme/tick) : une ligne toutes les {STEP} s, puis rien jusqu\'à la fin du cycle de {PERIOD} s ($thbt = seconde du cycle)',
        f'execute if score $thbt mg.st matches {PERIOD - 1}.. run scoreboard players set $thbt mg.st -1',
        '# $thbt absent (thème posé ou redémarrage) : le cycle repart à 0, la première ligne dure ses 8 s pleines',
        'execute unless score $thbt mg.st matches 0.. run scoreboard players set $thbt mg.st -1',
        'scoreboard players add $thbt mg.st 1',
        '# l\'événement du lobby a sa bossbar mg:ev (get visible : succès = existence ; mg:ev n\'est jamais masquée, elle n\'existe que pendant l\'annonce et l\'événement) : le bandeau s\'efface',
        'execute store success score $thbe mg.st run bossbar get mg:ev visible',
        'execute if score $thbe mg.st matches 1 run return run function mg:lobby/theme/banner_hide',
        f'scoreboard players set #thb{STEP} mg.st {STEP}',
        'scoreboard players operation $thbl mg.st = $thbt mg.st',
        f'scoreboard players operation $thbl mg.st /= #thb{STEP} mg.st',
        'scoreboard players add $thbl mg.st 1',
        '# passé la dernière ligne : barre retirée jusqu\'à la prochaine période'] + top + [
        '# mg:thb absente (la bossbar n\'a jamais été masquée : le succès de get visible vaut son existence)',
        'execute store success score $thbe mg.st run bossbar get mg:thb visible',
        'execute if score $thbe mg.st matches 0 run bossbar add mg:thb ""'] +
      [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/banner' for tid, key, *_ in THEMES] +
      [f'execute in minecraft:overworld run bossbar set mg:thb players {SHOWN}'])
    w('lobby/theme/banner_hide', ['# Retire la bossbar du bandeau (fin de ligne, événement du lobby, thème retiré) ; sans effet si elle est absente',
                                  'bossbar remove mg:thb'])
    # branchements : une fois par seconde, au retrait du thème, au chargement (bossbar jamais en double) et à la désinstallation
    C.patch('lobby/theme/tick', 'function mg:lobby/theme/npc_second', ['function mg:lobby/theme/banner'])
    C.patch('lobby/theme/off', 'scoreboard players set $theme mg.st 0', ['function mg:lobby/theme/banner_hide'])
    C.patch('lobby/theme/off', 'scoreboard players set $theme mg.st 0', ['scoreboard players reset $thbt mg.st'])
    C.patch('core/load', 'scoreboard objectives add mg.st dummy', ['bossbar remove mg:thb'])
    C.patch('desinstaller', 'data remove storage mg:lobby theme', ['bossbar remove mg:thb'])
