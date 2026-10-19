"""Patinoire de Noël (importée par gen_themes.py, jamais lancée seule) : une piste de glace derrière le buffet, à l'est, sous le décor de Noël seulement.

Blocs : les remplacements passent par CH (change) comme le reste du décor, donc « on » ne pose que si le bloc d'origine est encore là et « off » remet
l'original (herbe, fleurs, arbres) ; rien de neuf côté restauration. RINK = (x1, x2, z1, z2), sol y 63 (pieds y 64) : packed_ice, bordure blue_ice sur
l'anneau extérieur, coins chanfreinés de CHAMFER. check() arrête le générateur si une case de glace n'est plus du sol, passe à un rayon >= 60 (la promenade
circulaire commence là), est refusée par free() ou n'a pas 3 blocs de hauteur libre (hors arbres de CLEAR et plantes, retirées), ou si un bloc non-plante
d'une boîte de CLEAR touche un arbre retiré (lanterne, liane, cacao : il tomberait en objet).
Arbres dégagés : CLEAR = [((x, z), rayon Chebyshev)] ; carve() retire de chaque boîte (y 64..72) toutes les cellules *_log / *_leaves, et les remplacements
du décor (neige, guirlande, cadeau) qui s'y trouvaient, qui les couvraient (neige sur les feuilles) ou qui couvraient la piste (y 64..74) ; les plantes de la
piste partent, la glace remplace le sol. Le reste de la boîte garde son décor ; le sol découvert hors glace (plus rien au-dessus) reçoit une couche de neige.
pre_lines() : lignes de vidage en y décroissant, émises avant « on » par place (l'ordre trié de « on » poserait la glace avant d'ôter les fleurs, qui tomberaient).
reskin() : le titre « Patinoire » (tag mg.thx, retiré par lobby/theme/clear ; jamais mg.thm : Tron l'utilise).

Glisse : mêmes valeurs que le patin du ragoût (theme_stew.SKATE), modificateur mg:thrink (celui du ragoût : mg:thstew). Chaque tick, lobby/theme/tick
(branchements de write()) : le joueur du spawn qui entre dans la piste (volume dx/dy/dz, dy = 1 : la grotte PvP est dessous, y 41..52), glace posée (la case
centrale est de la packed_ice), ni créatif ni spectateur, reçoit le tag mg.thrk (rink_on) ; rink_set ajoute les modificateurs (tag mg.thrkm) ; il sort de la
piste, joue, est en survie ou occupé (BUSY de sit_item) ou le thème change : rink_off ; le volume ne teste pas la dimension : une ligne dédiée (unless
dimension overworld) lui retire la glisse. Le ragoût patin prime : tag mg.thsk (posé par stew_skate, retiré par stew_clear), les modificateurs de la piste sont retirés
(rink_unset) pendant l'effet et remis à sa fin, jamais de cumul (vitesse -120 % : bloqué). Nettoyages : off du thème (off_lines), core/attr_reset, desinstaller.
Tout reste sous lobby/theme/ (cf. theme_world.load) ; aucun objectif, équipe ni bossbar.
"""
import math

import common as C
import sit_item as SI
import theme_stew as TS
from theme_mobs import THEME_TAG
from theme_world import CH, G, GROUND, PLANTS, SNOWABLE, W, bid, change, free

RINK = (32, 48, 7, 35)                   # (x1, x2, z1, z2) : cases de la piste, 17 x 29
CHAMFER = 2                              # coins coupés : cases à moins de CHAMFER (somme des distances aux deux bords) retirées
CLEAR = [((42, 24), 3), ((34, 21), 2), ((43, 12), 3), ((49, 31), 3), ((33, 30), 2)]   # arbres retirés : (centre x, z), rayon Chebyshev
RADIUS = 60                              # rayon du spawn à partir duquel commence la promenade circulaire : la glace reste en dessous
HEAD = 3                                 # hauteur libre exigée au-dessus de la glace (y 64..66)
TREE_TOP = G + 9                         # dernier y des arbres retirés (72)
TOP = G + 11                             # dernier y des remplacements du décor retirés (74 : neige sur les feuilles)
ICE, EDGE, AIR = 'minecraft:packed_ice', 'minecraft:blue_ice', 'minecraft:air'
SNOW = 'minecraft:snow[layers=1]'        # neige du sol découvert sous les arbres retirés (comme theme_noel)
MOD = 'mg:thrink'
F = 'lobby/theme'
TITLE_POS = '41.5 67 20.5'               # milieu de la piste, 3 blocs au-dessus de la glace


def shape():
    """Cases (x, z) de la glace : le rectangle RINK, coins chanfreinés."""
    x1, x2, z1, z2 = RINK
    return {(x, z) for x in range(x1, x2 + 1) for z in range(z1, z2 + 1)
            if min(x - x1, x2 - x) + min(z - z1, z2 - z) >= CHAMFER}


def blocks():
    """Glace de chaque case : blue_ice sur l'anneau extérieur (une case voisine hors de la piste), packed_ice dedans."""
    ice = shape()
    return {(x, z): EDGE if any(n not in ice for n in ((x + 1, z), (x - 1, z), (x, z + 1), (x, z - 1))) else ICE for x, z in ice}


def tree_cells():
    """Cellules des arbres retirés (troncs et feuilles des boîtes de CLEAR, y 64..72) ; une entrée de CLEAR sans arbre arrête le générateur."""
    out = set()
    for (cx, cz), r in CLEAR:
        found = {(x, y, z) for x in range(cx - r, cx + r + 1) for z in range(cz - r, cz + r + 1) for y in range(G + 1, TREE_TOP + 1)
                 if bid(W.get((x, y, z))).endswith(('_log', '_leaves'))}
        if not found:
            raise SystemExit(f'theme_rink : aucun arbre dans la boîte CLEAR {((cx, cz), r)} : entrée à retirer ou à déplacer')
        out |= found
    return out


def neighbours(k):
    x, y, z = k
    return ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1))


def check():
    """Le générateur s'arrête si la piste n'a plus sa place : appelé après theme_world/theme_water.load() et TN.prepare()."""
    gone = tree_cells()
    bad = []
    for x, z in sorted(shape()):
        ground = bid(W.get((x, G, z)))
        if ground not in GROUND:
            bad.append(f'({x}, {z}) : sol {ground} (pas du sol du spawn)')
        if math.hypot(x, z) >= RADIUS:
            bad.append(f'({x}, {z}) : rayon {math.hypot(x, z):.1f} >= {RADIUS} (promenade)')
        if not all(free(x, y, z) for y in range(G, G + HEAD + 1)):
            bad.append(f'({x}, {z}) : refusée par free() (plot, zone modifiée ou réservée)')
        for y in range(G + 1, G + HEAD + 1):
            b = W.get((x, y, z))
            if b and (x, y, z) not in gone and bid(b) not in PLANTS:
                bad.append(f'({x}, {y}, {z}) : {bid(b)} gêne (hauteur libre de {HEAD} blocs hors CLEAR)')
    for (cx, cz), r in CLEAR:            # lanterne suspendue, liane, cacao... : un support retiré les ferait tomber en objet
        for x in range(cx - r, cx + r + 1):
            for z in range(cz - r, cz + r + 1):
                for y in range(G + 1, TREE_TOP + 1):
                    k = (x, y, z)
                    if k in W and k not in gone and bid(W[k]) not in PLANTS and any(n in gone for n in neighbours(k)):
                        bad.append(f'{k} : {bid(W[k])} touche un arbre retiré (CLEAR {((cx, cz), r)}) : il tomberait en objet')
    if bad:
        raise SystemExit('theme_rink : la patinoire RINK n\'a plus sa place :\n  ' + '\n  '.join(bad[:15]) + (f'\n  ... ({len(bad)} au total)' if len(bad) > 15 else ''))


def snow_after(x, z, gone):
    """Colonne (x, z) hors glace, dans une boîte de CLEAR : la neige que le décor y aurait posée si les arbres n'avaient pas été retirés ? Vrai si le sol
    tient la neige et que plus rien de W ne couvre la colonne une fois les arbres partis (déterministe : pas de tirage rnd)."""
    return bid(W.get((x, G, z))) in SNOWABLE and not any((x, y, z) in W and (x, y, z) not in gone for y in range(G + 2, G + 40))


def carve():
    """Dans le thème Noël, EN DERNIER (après cadeaux et bougies : le tirage rnd ne bouge pas) : arbres retirés, plantes de la piste retirées, glace posée.
    Les remplacements du décor ne sont retirés que sur la glace, sur les cellules d'arbre retirées et juste au-dessus d'elles (neige sur les feuilles) ;
    sous les arbres retirés, hors glace, le sol découvert reçoit une couche de neige (comme theme_noel : fleurs et touffes y passent en neige)."""
    ice, gone = blocks(), tree_cells()
    flat = {(x, y, z) for x, z in ice for y in range(G + 1, G + HEAD + 1) if (x, y, z) in W}       # plantes (check() : rien d'autre)
    def gift_by_log(k):                  # cadeau (shulker box) au pied d'un tronc retiré : il passe par snow_after avec le sol découvert
        return k[1] == G + 1 and bid(CH[k][1]).endswith('_shulker_box') and any((k[0] + dx, k[1], k[2] + dz) in gone for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    for k in [k for k in CH if G < k[1] <= TOP and ((k[0], k[2]) in ice or k in gone or (k[0], k[1] - 1, k[2]) in gone or gift_by_log(k))]:
        CH.pop(k)                        # neige, guirlande ou cadeau orphelin
    snow = set()                         # cases du sol découvert (y G + 1) : neige au lieu de l'air
    for x, z in sorted({(x, z) for (cx, cz), r in CLEAR for x in range(cx - r, cx + r + 1) for z in range(cz - r, cz + r + 1)} - set(ice)):
        k = (x, G + 1, z)
        if snow_after(x, z, gone) and k not in CH and (k in gone or bid(W.get(k)) in PLANTS or k not in W):
            snow.add(k)
    for k in sorted(gone | flat):
        change(k, SNOW if k in snow else AIR)
    for k in sorted(snow - gone):
        change(k, SNOW)
    for (x, z), b in sorted(ice.items()):
        change((x, G, z), b)
    assert all(k in CH and CH[k][1] == (SNOW if k in snow else AIR) for k in gone | flat), 'theme_rink : cellule à retirer refusée par change() (free())'
    assert all(CH.get((x, G, z), (None, None))[1] == b for (x, z), b in ice.items()), 'theme_rink : case de glace refusée par change() (free())'


def pre_lines():
    """Vidage (bloc d'origine -> air) en y décroissant, pour « place » avant « on » : la glace ne se pose jamais sous une fleur encore là."""
    return ['# patinoire : plantes et arbres retirés d\'abord, de haut en bas (sinon la glace serait posée sous des fleurs qui tomberaient en objets)'] + \
           [f'execute if block {x} {y} {z} {bid(o)} run setblock {x} {y} {z} {AIR}'
            for (x, y, z), (o, n) in sorted(CH.items(), key=lambda t: (-t[0][1], t[0])) if n == AIR]


def off_lines():
    """Ajouté au off du thème : lobby/theme/tick ne tourne plus sans thème, plus personne ne retirerait la glisse."""
    return [f'execute as @a[tag=mg.thrk] run function mg:{F}/rink_off']


def reskin():
    """Titre au-dessus de la piste (modèle : title() de gen_themes), à rappeler par le reskin de Noël."""
    text = C.js([{'text': '⛸ Patinoire', 'color': 'aqua', 'bold': True}, {'text': '\nÇa glisse !', 'color': 'white', 'italic': True}])
    return ['summon minecraft:text_display ' + TITLE_POS + ' {Tags:["mg.lby","' + THEME_TAG + '"],billboard:"center",background:1426063360,'
            'shadow:1b,text:' + text + ',transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],'
            'right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}']


def selector():
    """Arguments de sélecteur (sans @a) : joueurs du spawn dans la piste, pas en survie, ni créatifs ni spectateurs, ni occupés : BUSY de sit_item.py
    (partie, élytra, plot, parcours, Mini Party, duel...) et le parkour. Le volume ne teste pas la dimension : voir le branchement de tick."""
    x1, x2, z1, z2 = RINK
    return (f'x={x1},y={G + 1},z={z1},dx={x2 - x1},dy=1,dz={z2 - z1},gamemode=!spectator,gamemode=!creative' +
            ''.join(f',tag=!{t}' for t in dict.fromkeys(['mg.surv', *TS.stew_busy(SI.BUSY)])))


def centre():
    """Case centrale de la piste (packed_ice) : « if block » de l'entrée, on ne glisse que si la glace est posée (restore au redémarrage, pose refusée)."""
    x1, x2, z1, z2 = RINK
    x, z = (x1 + x2) // 2, (z1 + z2) // 2
    assert blocks()[(x, z)] == ICE, 'theme_rink : la case centrale de RINK n\'est pas de la packed_ice'
    return f'{x} {G} {z} {ICE}'


def mods(verb):
    return [f'attribute @s minecraft:{a} modifier ' + (f'add {MOD} {v} {TS.OP}' if verb == 'add' else f'remove {MOD}') for a, v in TS.SKATE]


def write():
    """Écrit rink_on/set/unset/off et les branchements (lobby/theme/tick, core/attr_reset, desinstaller), après TB.write : les ancres sont posées."""
    w = C.w
    sel = selector()
    w(f'{F}/rink_on', ['# ⛸ Patinoire de Noël : @s entre dans la piste (appelé chaque tick par lobby/theme/tick) ; rink_set pose ensuite la glisse',
                       'tag @s add mg.thrk', 'title @s actionbar {"text":"⛸ Patinoire : ça glisse !","color":"aqua"}'])
    w(f'{F}/rink_set', ['# ⛸ Patinoire : glisse du patin du ragoût (mg:thrink, mêmes valeurs que theme_stew.SKATE) pour @s ; pas pendant le ragoût patin (mg.thsk)'] +
      mods('add') + ['tag @s add mg.thrkm'])
    w(f'{F}/rink_unset', ['# ⛸ Patinoire : glisse retirée de @s (sorti de la piste, ou le ragoût patin prend le relais) ; jamais les valeurs de base'] +
      mods('remove') + ['tag @s remove mg.thrkm'])
    w(f'{F}/rink_off', ['# ⛸ Patinoire : @s n\'est plus dans la piste (sortie, partie, thème retiré, reconnexion, désinstallation) : glisse et tags retirés',
                        f'function mg:{F}/rink_unset', 'tag @s remove mg.thrk'])
    C.patch(f'{F}/tick', 'scoreboard players add $tht mg.st 1', [
        '# patinoire de Noël : entrée dans la piste (dy = 1 : la grotte PvP est dessous), sortie, glisse (le ragoût patin prime : tag mg.thsk)',
        f'execute if score $theme mg.st matches 2 in minecraft:overworld if block {centre()} as @a[{sel},tag=!mg.thrk] run function mg:{F}/rink_on',
        f'execute unless score $theme mg.st matches 2 as @a[tag=mg.thrk] run function mg:{F}/rink_off',
        f'execute in minecraft:overworld unless block {centre()} as @a[tag=mg.thrk] run function mg:{F}/rink_off',
        f'execute as @a[tag=mg.thrk] at @s unless dimension minecraft:overworld run function mg:{F}/rink_off',
        f'execute in minecraft:overworld as @a[tag=mg.thrk] unless entity @s[{sel}] run function mg:{F}/rink_off',
        f'execute as @a[tag=mg.thrk,tag=mg.thsk,tag=mg.thrkm] run function mg:{F}/rink_unset',
        f'execute as @a[tag=mg.thrk,tag=!mg.thsk,tag=!mg.thrkm] run function mg:{F}/rink_set'], where='before')
    C.patch('core/attr_reset', f'function mg:{F}/stew_clear', [f'function mg:{F}/rink_off'])
    C.patch('desinstaller', f'execute as @a run function mg:{F}/stew_clear', [f'execute as @a run function mg:{F}/rink_off'])
