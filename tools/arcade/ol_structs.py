"""🏰 Ombrelune : constructions (cité de Havreclair, villages, repaires des boss, donjons). Module importé par gen_ombrelune.py.

Chaque bâtisseur remplit un Vox (tv_build) en coordonnées absolues. Les lieux utiles au jeu (PNJ, balises, coffres, leviers,
arènes, salles des donjons) sont notés dans SPOTS / DUNGEONS / ARENAS.

Façade : le code est réparti dans ol_skit (état + outils), ol_city / ol_city_b, ol_hamlets, ol_dungeons et ol_region_*;
les consommateurs continuent à faire `import ol_structs as S` (mêmes noms, mêmes objets d'état).
"""
import ol_world as W

from ol_skit import (  # noqa: F401 (réexport)
    SPOTS, DUNGEONS, ARENAS, LORE, CHESTS, G, spot, dir_vec, opp, cone_roof, round_tower, crenels,
    brace_ladders, stone_mix, HOUSE_STYLES, house, struct_cmds
)
from ol_city import city  # noqa: F401 (réexport)
from ol_city_b import castle, temple, mage_tower, guild, tavern, forge_b, market, stables, alchemist  # noqa: F401 (réexport)
from ol_hamlets import village, brumecombe, windmill, bandit_fort  # noqa: F401 (réexport)
from ol_dungeons import DUN_THEMES, dungeon  # noqa: F401 (réexport)
from ol_region_nord import (  # noqa: F401 (réexport)
    giant_tree, rope_bridge, aelindor, spider_lair, shrine, longhouse, hrafnheim, giant_hold
)
from ol_region_est import stilt_village, witch_isle, oasis_town, pyramid, obelisks, bastion, caldera  # noqa: F401 (réexport)
from ol_region_sud import dwarf_camp, dwarf_gate, rebel_camp, citadel, soul_well_entry, chapel  # noqa: F401 (réexport)


def all_structures():
    """Liste (nom, région, Vox) de toutes les constructions, avec les donjons."""
    S = []
    S.append(('city', 'hub', city()))
    S += [('brumecombe', 'w', brumecombe()), ('windmill', 'w', windmill()), ('bandit_fort', 'w', bandit_fort()), ('chapel', 'w', chapel())]
    S += [('aelindor', 'nw', aelindor()), ('spider_lair', 'nw', spider_lair()), ('shrine', 'nw', shrine())]
    S += [('hrafnheim', 'n', hrafnheim()), ('giant_hold', 'n', giant_hold())]
    S += [('stilts', 'ne', stilt_village()), ('witch_isle', 'ne', witch_isle())]
    S += [('oasis', 'e', oasis_town()), ('pyramid', 'e', pyramid()), ('obelisks', 'e', obelisks())]
    S += [('bastion', 'se', bastion()), ('caldera', 'se', caldera())]
    S += [('dwarf_camp', 's', dwarf_camp()), ('dwarf_gate', 's', dwarf_gate())]
    S += [('rebels', 'sw', rebel_camp()), ('citadel', 'sw', citadel()), ('soul_well', 'sw', soul_well_entry())]
    # donjons : (clé, région, entrée x z y, sol, thème, direction, nom, alpha)
    cx, cz = W.P['crypt']
    S.append(('dg_crypt', 'w', dungeon('crypt', 'w', (cx, cz - 4, 67), 50, 'crypt', 'south', 'Cryptes de Valdor', 'Seigneur des cryptes')))
    x, z = W.P['spider_nest']
    S.append(('dg_nest', 'nw', dungeon('nest', 'nw', (x, z, 71), 54, 'nest', 'north', 'Nid des tisseuses', 'Tisseuse alpha')))
    x, z = W.P['ice_cave']
    S.append(('dg_ice', 'n', dungeon('ice', 'n', (x, z, 87), 66, 'ice', 'east', 'Grotte de givre', 'Wendigo des glaces')))
    x, z = W.P['sunken']
    S.append(('dg_sunken', 'ne', dungeon('sunken', 'ne', (x, z, 64), 48, 'sunken', 'east', 'Temple englouti', 'Gardien noyé')))
    x, z = W.P['tombs']
    S.append(('dg_tomb', 'e', dungeon('tomb', 'e', (x, z, 65), 48, 'tomb', 'west', 'Tombeaux d\'Azhar', 'Momie royale')))
    x, z = W.P['forge_r']
    S.append(('dg_forge', 'se', dungeon('forge', 'se', (x, z, 71), 52, 'forge', 'south', 'Forge écarlate', 'Forgeron calciné')))
    x, z = W.P['mines']
    mx, mz = x, 126
    S.append(('dg_mine', 's', dungeon('mine', 's', (mx, mz, 67), 48, 'mine', 'south', 'Mines profondes', 'Contremaître maudit')))
    x, z = W.P['soul_well']
    S.append(('dg_souls', 'sw', dungeon('souls', 'sw', (x, z + 6, 65), 46, 'souls', 'south', 'Puits des âmes', 'Gardien des âmes')))
    return S
