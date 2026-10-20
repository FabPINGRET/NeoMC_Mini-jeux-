# ================================================================ donjons : salles à vagues, alphas, barres de vie, récompenses
# Exécuté par tv_classes.py (même espace de noms). Chaque donjon = 3 salles à vagues puis l'alpha, qui ne se réveille que
# si la 3e salle est nettoyée. Aucune structure nouvelle (les régions ne se construisent qu'une fois) : les salles sont des
# sous-zones des 4 donjons de tv_world.py, leurs points d'apparition sont vérifiés dans les voxels (assert de génération).
# Machine à états $trds<i> (mg.st) : 0 libre ; 2n+1 vague de la salle n en cours ; 2n+2 salle n nettoyée ; 6 = alpha libre.
# Les mobs d'une vague portent mg.trdw<i> (nettoyage, reset) et mg.trr (balayage des dinosaures loin des joueurs).
TROPH = {'dilo': ('mg.trvn', 3, 'glandes à venin'), 'ptera': ('mg.trai', 3, 'ailes'), 'raptor': ('mg.trgr', 6, 'griffes'), 'carno': ('mg.trdn', 3, 'dents')}
ALPHA_HP = {'dilo': 120, 'ptera': 90, 'raptor': 120, 'carno': 450}
WAVE_MAX = 6                                                      # effectif maximal d'une vague (charge en entités)
WAVE_XP = (100, 200, 300)                                         # XP de la salle nettoyée (salles 1/2/3), rayon 48 autour de la salle
WAVE_SP = {'dilo', 'compy', 'raptor', 'ptera'}                    # espèces hostiles des régions (ni herbivores, ni carnotaure : 160 PV x3 en zone s)

# ---------------------------------------------------------------- les 12 salles (points dérivés des ancres de tv_world.py)
_m_x, _m_z = TVW['MOTHER']
_tg = TVW['ground'](_m_x, _m_z) - 1                              # g de TS.tree_heart (Arbre-Mère)
_p_x, _p_z = TVW['NEST']
_pg = TVW['ground'](_p_x, _p_z) - 1                              # g de TS.spire_nest (Pic du Nid)
_n_x, _n_z = TVW['MINE']
_ny = DUNGEONS[2][5][1]                                           # pieds dans la mine : y de la porte (TS.mine : g + 1)
_v_x, _v_z = TVW['VOLC']
_ty = TVW['TUBE_Y']
_tex = DUNGEONS[3][5][0] + 3                                      # entrée du tube : la porte est en ex - 3 (TS.lava_tube)
_tez = DUNGEONS[3][5][2]                                          # axe du tube à l'entrée : z de la porte


def _tcz(x):                                                      # axe du tube en x (même formule que TS.lava_tube)
    return _v_z + round(4 * _m.sin((x - (_v_x - 22)) / (_tex - (_v_x - 22)) * 5))


assert _tcz(_tex) == _tez, 'tv_dungeons.py : formule de l\'axe du tube (_tcz) en désaccord avec TS.lava_tube'


def _room(c, r, sp, pts, fly=False):
    """c : centre du déclencheur, r : rayon (sphère), sp : espèces (tirées dans l'ordre, en boucle), pts : points d'apparition
    (pieds, bloc entier), fly : apparition en l'air (ptéranodons, pas de sol exigé)."""
    return {'c': c, 'r': r, 'sp': sp, 'pts': pts, 'fly': fly}


ROOMS = {
    # Arbre : base du tronc, palier g+12, palier g+24 (les points sont sur les restes des paliers, hors volée)
    'arbre': [_room((_m_x, _tg + 3, _m_z), 7, ['compy', 'dilo'], [(_m_x - 2, _tg + 1, _m_z - 2), (_m_x + 2, _tg + 1, _m_z - 2), (_m_x - 2, _tg + 1, _m_z + 2)]),
              _room((_m_x - 1, _tg + 14, _m_z), 7, ['dilo', 'raptor'], [(_m_x - 2, _tg + 13, _m_z), (_m_x - 1, _tg + 13, _m_z + 2), (_m_x - 1, _tg + 13, _m_z - 1)]),
              _room((_m_x - 1, _tg + 26, _m_z), 7, ['raptor', 'dilo'], [(_m_x - 2, _tg + 25, _m_z - 2), (_m_x - 1, _tg + 25, _m_z), (_m_x - 2, _tg + 25, _m_z + 2)])],
    # Pic : pied (intérieur, côté entrée), mi-tour (dans le puits : les meurtrières sont en verre, l'extérieur est inaccessible),
    # abords du nid (plateau du sommet, à l'air libre)
    'pic': [_room((_p_x, _pg + 3, _p_z), 9, ['raptor'], [(_p_x - 3, _pg + 1, _p_z - 3), (_p_x - 3, _pg + 1, _p_z + 3), (_p_x, _pg + 1, _p_z + 5)]),
            _room((_p_x, _pg + 24, _p_z), 8, ['ptera'], [(_p_x - 2, _pg + 24, _p_z - 3), (_p_x + 2, _pg + 24, _p_z + 3), (_p_x - 2, _pg + 24, _p_z + 3)], fly=True),
            _room((_p_x, _pg + 46, _p_z), 9, ['ptera', 'raptor'], [(_p_x - 4, _pg + 47, _p_z), (_p_x + 4, _pg + 47, _p_z), (_p_x, _pg + 47, _p_z + 4)])],
    # Mine : galerie (croisement mx+8), dépôt (mz-15), dortoir (mz+15)
    'mine': [_room((_n_x + 8, _ny + 1, _n_z), 8, ['raptor', 'dilo'], [(_n_x + 4, _ny, _n_z - 1), (_n_x + 12, _ny, _n_z + 1), (_n_x + 6, _ny, _n_z + 1)]),
             _room((_n_x + 8, _ny + 1, _n_z - 15), 7, ['raptor'], [(_n_x + 5, _ny, _n_z - 13), (_n_x + 11, _ny, _n_z - 13), (_n_x + 9, _ny, _n_z - 16)]),
             _room((_n_x + 8, _ny + 1, _n_z + 15), 7, ['dilo', 'raptor'], [(_n_x + 5, _ny, _n_z + 14), (_n_x + 11, _ny, _n_z + 15), (_n_x + 8, _ny, _n_z + 13)])],
    # Tube : parvis d'entrée, milieu du tube (sol naturel y-1), seuil de la crypte
    'tube': [_room((_tex - 4, _ty, _tez), 5, ['compy', 'raptor'], [(_tex - 4, _ty, _tez - 1), (_tex - 4, _ty, _tez + 1), (_tex - 3, _ty, _tez)]),
             _room((_tex + 4, _ty, _tcz(_tex + 4)), 5, ['raptor', 'compy'], [(x_, _ty - 1, _tcz(x_)) for x_ in (_tex + 2, _tex + 4, _tex + 6)]),
             _room((_v_x - 36, _ty, _v_z), 6, ['raptor'], [(_v_x - 34, _ty, _v_z - 2), (_v_x - 34, _ty, _v_z + 2), (_v_x - 33, _ty, _v_z - 4)])],
}
# (Vox, alpha, porte) reconstruits comme dans tv_world.py ; mine() ignore son 4e argument (86, repris tel quel : il est positionnel)
_VOX = {'arbre': lambda: TVW['TS'].tree_heart(_m_x, _m_z, _tg), 'pic': lambda: TVW['TS'].spire_nest(_p_x, _p_z, _pg),
        'mine': lambda: TVW['TS'].mine(_n_x, _n_z, _ny - 1, 86), 'tube': lambda: TVW['TS'].lava_tube(_v_x, _v_z, _tex, _ty)}
_NOSTAND = ('carpet', 'cobweb', 'vine', 'rail', 'bush', 'skull', 'lantern', 'egg', 'bars', 'fence', 'chain', 'trapdoor', 'bed', 'barrel', 'chest',
            'slab[type=bottom]', 'slab[type=double]', 'tnt', 'crafting', 'lamp', 'lava', 'magma', 'fire')   # ne portent pas un mob (ou le brûlent)


def _cell(v, x, y, z):
    """'air' / 'solid' / 'dec' (décor sans sol) / '?' : bloc des voxels, sinon terrain naturel (colonne COL : solide jusqu'à h)."""
    b = v.get(x, y, z)
    if b is not None:
        return 'air' if b == 'air' else ('dec' if any(s in b for s in _NOSTAND) else 'solid')
    c = TVW['COL'].get((x, z))
    return '?' if c is None else ('solid' if y <= c[0] else 'air')


def _check_rooms():
    """Assert de génération : chaque point d'apparition a l'air aux pieds et à la tête et un sol solide dessous (sauf salle volante),
    n'est pas sur un œuf d'ambre. Vérifie d'abord que les structures reconstruites ont bien l'alpha et la porte de DUNGEONS."""
    for key, rooms in ROOMS.items():
        v, *ap = _VOX[key]()
        ref = next(list(d[4:6]) for d in DUNGEONS if d[1] == key)
        if ap != ref:
            raise RuntimeError(f'Donjon {key} : structure reconstruite (alpha, porte) = {ap} et DUNGEONS = {ref} : ancres de tv_dungeons.py à revoir')
        for n, R in enumerate(rooms):
            if not 2 <= len(R['pts']) <= 3 or not set(R['sp']) <= WAVE_SP:
                raise RuntimeError(f'Donjon {key} salle {n + 1} : 2 ou 3 points et espèces hostiles de la région exigés')
            for (x, y, z) in R['pts']:
                bad = [(lab, c) for lab, c in (('pieds', _cell(v, x, y, z)), ('tête', _cell(v, x, y + 1, z))) if c != 'air']
                if not R['fly'] and _cell(v, x, y - 1, z) != 'solid':
                    bad.append(('sol', _cell(v, x, y - 1, z)))
                if (x, y, z) in TVW['EGGS']:
                    bad.append(('œuf d\'ambre', 'ici'))
                if bad:
                    raise RuntimeError(f'Donjon {key} salle {n + 1} : point d\'apparition ({x}, {y}, {z}) invalide ({bad}) : '
                                       'revoir ROOMS dans tv_dungeons.py (géométrie de la structure dans tv_structs.py)')


_check_rooms()


def _reach(key, alpha, door):
    """Rayon de présence du donjon : tout point utile (porte, centres, apparitions) à portée de l'alpha, 44 au moins (le Pic fait 47 de haut)."""
    pts = [door] + [R['c'] for R in ROOMS[key]] + [p for R in ROOMS[key] for p in R['pts']]
    return max(44, _m.ceil(max(_m.dist(alpha, p) for p in pts)) + 6)


# ---------------------------------------------------------------- fonctions des donjons
DG = ['# Chaque seconde : donjons (salles à vagues, déclenchement de l\'alpha à l\'approche, suivi, victoire, reset si plus personne)']
for i, (k, key, name, sp, (ax, ay, az), door) in enumerate(DUNGEONS):
    hp = ALPHA_HP[sp]
    RR = _reach(key, (ax, ay, az), door)
    AT = f'positioned {ax} {ay} {az}'
    PL = f'@a[tag=mg.tvw,gamemode=adventure,distance=..{RR}]'
    w(f'{P}/dg/{key}_start', [f'# {name} : l\'alpha se réveille', f'execute positioned {ax} {ay} {az} run function mg:terra/dino/{sp}',
                              f'tag @e[tag=mg.tvlast] add mg.trboss', f'tag @e[tag=mg.tvlast] add mg.trdg_{key}',
                              f'execute as @e[tag=mg.tvlast] run attribute @s minecraft:max_health base set {hp}',
                              f'execute as @e[tag=mg.tvlast] run attribute @s minecraft:attack_damage modifier add mg:tralpha 0.5 add_multiplied_base',
                              f'execute as @e[tag=mg.tvlast] run data merge entity @s {{Health:{hp}f,CustomName:{js(TEXT("Alpha : " + name, "dark_red", bold=True))}}}',
                              'scoreboard players operation $tvi mg.st = @e[tag=mg.tvlast,limit=1] mg.tvid',
                              'execute as @e[tag=mg.tvp] if score @s mg.tvid = $tvi mg.st run data merge entity @s {Glowing:1b,glow_color_override:16729156}'] +
      ([f'execute positioned {ax} {ay} {az} run function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.trr',
        f'execute positioned {ax} {ay} {az} run function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.trr'] if sp == 'raptor' else []) +
      [f'scoreboard players set $trda{i} mg.st 1', f'scoreboard players set $trdr{i} mg.st 0', f'bossbar set mg:trdg{i} max {hp}',
       f'execute positioned {ax} {ay} {az} run title @a[tag=mg.tvw,distance=..30] title {js(TEXT("ALPHA", "dark_red", bold=True))}',
       f'execute positioned {ax} {ay} {az} run title @a[tag=mg.tvw,distance=..30] subtitle {js(TEXT(name, "gray"))}',
       f'execute positioned {ax} {ay} {az} as @a[tag=mg.tvw,distance=..30] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 1 0.8'])
    w(f'{P}/dg/{key}', [f'# {name} : chaque seconde pendant le combat',
                        f'execute positioned {ax} {ay} {az} run bossbar set mg:trdg{i} players @a[tag=mg.tvw,distance=..40]',
                        f'execute store result bossbar mg:trdg{i} value run data get entity @e[tag=mg.trdg_{key},limit=1] Health'])
    # reset (plus personne en aventure à portée pendant 20 s) : vagues et alpha, états remis à 0, mobs renvoyés dans le vide
    # si au moins une salle avait été nettoyée (état >= 2), cooldown de 60 s : sinon quitter puis revenir rejouerait la salle pour son XP
    # cooldown 10 s inconditionnel (lot A, alpha tué puis purgé) posé AVANT le 60 conditionnel, qui le remplace si une salle était nettoyée
    w(f'{P}/dg/{key}_reset', [f'# {name} : remis à zéro (plus personne)', f'scoreboard players set $trda{i} mg.st 0',
                              f'scoreboard players set $trdc{i} mg.st 10',
                              f'execute if score $trds{i} mg.st matches 2.. run scoreboard players set $trdc{i} mg.st 60', f'scoreboard players set $trds{i} mg.st 0',
                              f'scoreboard players set $trdr{i} mg.st 0', f'execute as @e[tag=mg.trdg_{key}] at @s run tp @s ~ -400 ~', f'kill @e[tag=mg.trdg_{key}]',
                              f'execute as @e[tag=mg.trdw{i}] at @s run tp @s ~ -400 ~', f'kill @e[tag=mg.trdw{i}]', f'bossbar set mg:trdg{i} players'])
    o, q, lab = TROPH[sp]
    w(f'{P}/dg/{key}_win', [f'# {name} : alpha vaincu', f'scoreboard players set $trda{i} mg.st 0', f'scoreboard players set $trds{i} mg.st 0',
                            f'scoreboard players set $trdc{i} mg.st 180',
                            f'bossbar set mg:trdg{i} players', f'execute positioned {ax} {ay} {az} as @a[tag=mg.tvw,gamemode=adventure,distance=..48] run function mg:{P}/dg/{key}_rw'])
    w(f'{P}/dg/{key}_rw', [f'# @s a vaincu l\'alpha : {name}', f'scoreboard players add @s {o} {q}', 'scoreboard players add @s mg.tvc 150', f'function mg:{P}/xp {{n:300}}',
                           'tellraw @s ' + js(TEXT(f'  +{q} {lab}, +150 ₵', 'gold')), 'title @s title {"text":"ALPHA VAINCU","color":"gold","bold":true}'] +
      bit_test('mg.trdg', i) + [f'execute if score $b mg.st matches 0 run function mg:{P}/dg/{key}_first'])
    w(f'{P}/dg/{key}_first', [f'# Premier passage : {name}', f'scoreboard players operation @s mg.trdg += #p{i} mg.st', f'function mg:{P}/xp {{n:500}}',
                              f'title @s subtitle {js(TEXT("Donjon terminé : " + name + " (+500 XP)", "yellow"))}',
                              'tellraw @a[tag=mg.tvw] ' + js([TEXT('🏆 ', 'gold'), {'selector': '@s', 'color': 'yellow'}, TEXT(' a terminé le donjon « ' + name + ' » !', 'gold')])])
    # l'alpha dort tant que les 3 salles ne sont pas nettoyées (pas de porte : rappel sur la barre d'action)
    w(f'{P}/dg/{key}_lock', [f'# {name} : l\'alpha dort encore (salles nettoyées = état / 2)', f'scoreboard players operation $trwn mg.st = $trds{i} mg.st',
                             'scoreboard players operation $trwn mg.st /= #2 mg.st',
                             f'execute {AT} as @a[tag=mg.tvw,gamemode=adventure,distance=..12] run title @s actionbar ' +
                             js([TEXT('🔒 L\'alpha dort encore : salles nettoyées ', 'gray'), {'score': {'name': '$trwn', 'objective': 'mg.st'}, 'color': 'yellow', 'bold': True},
                                 TEXT(' / 3', 'gray')]),
                             f'execute {AT} run scoreboard players set @a[tag=mg.tvw,gamemode=adventure,distance=..12] mg.tval 30'])
    for n, R in enumerate(ROOMS[key]):
        cx, cy, cz = R['c']
        W = [f'# {name} : vague de la salle {n + 1} / 3 ({", ".join(R["sp"])})', f'scoreboard players set $trds{i} mg.st {2 * n + 1}', f'scoreboard players set $trdr{i} mg.st 0',
             f'execute {AT} store result score $trwn mg.st if entity {PL}', f'scoreboard players add $trwn mg.st {2 + n}',
             f'execute if score $trwn mg.st matches {WAVE_MAX + 1}.. run scoreboard players set $trwn mg.st {WAVE_MAX}', 'tag @e[tag=mg.tvlast] remove mg.tvlast']
        for j in range(WAVE_MAX):                               # j-ième mob : espèce et point en boucle, seulement si l'effectif le demande
            px_, py_, pz_ = R['pts'][j % len(R['pts'])]
            W += [f'execute if score $trwn mg.st matches {j + 1}.. positioned {px_ + 0.5} {py_} {pz_ + 0.5} run function mg:terra/dino/{R["sp"][j % len(R["sp"])]}',
                  'tag @e[tag=mg.tvlast] add mg.trnew']
        W += ['tag @e[tag=mg.trnew] add mg.trr', f'tag @e[tag=mg.trnew] add mg.trdw{i}'] + [
            f'execute as @e[tag=mg.trnew,tag={TAGS[s_]}] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]'
            for s_ in ('raptor', 'compy') if s_ in R['sp']] + [
            f'function mg:{P}/zone/{k}', 'tag @e[tag=mg.trnew] remove mg.trnew',
            f'execute {AT} run title @a[tag=mg.tvw,distance=..{RR}] actionbar {js(TEXT("⚔ " + name + f" : salle {n + 1} / 3", "red", bold=True))}',
            f'execute {AT} run scoreboard players set @a[tag=mg.tvw,distance=..{RR}] mg.tval 30',
            f'execute positioned {cx} {cy} {cz} run playsound minecraft:event.raid.horn hostile @a[tag=mg.tvw,distance=..{RR}] ~ ~ ~ 0.6 1.4']
        w(f'{P}/dg/{key}_w{n}', W)
        w(f'{P}/dg/{key}_c{n}', [f'# {name} : salle {n + 1} / 3 nettoyée', f'scoreboard players set $trds{i} mg.st {2 * n + 2}',
                                 f'execute positioned {cx} {cy} {cz} as @a[tag=mg.tvw,gamemode=adventure,distance=..48] run function mg:{P}/xp {{n:{WAVE_XP[n]}}}',
                                 f'execute positioned {cx} {cy} {cz} run title @a[tag=mg.tvw,distance=..48] times 5 40 10',
                                 f'execute positioned {cx} {cy} {cz} run title @a[tag=mg.tvw,distance=..48] title {js(TEXT(f"Salle nettoyée {n + 1}/3", "gold", bold=True))}',
                                 f'execute positioned {cx} {cy} {cz} run title @a[tag=mg.tvw,distance=..48] subtitle ' +
                                 js(TEXT(f'+{WAVE_XP[n]} XP' + (' : l\'alpha t\'attend' if n == 2 else ''), 'yellow')),
                                 f'execute positioned {cx} {cy} {cz} run playsound minecraft:entity.player.levelup player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.8 1.2'])
    DG += [f'scoreboard players remove $trdc{i} mg.st 1',
           f'execute unless score $trds{i} mg.st matches 0 {AT} unless entity {PL} run scoreboard players add $trdr{i} mg.st 1',
           f'execute unless score $trds{i} mg.st matches 0 {AT} if entity {PL} run scoreboard players set $trdr{i} mg.st 0',
           f'execute unless score $trds{i} mg.st matches 0 if score $trdr{i} mg.st matches 20.. run function mg:{P}/dg/{key}_reset',
           f'execute if score $trda{i} mg.st matches 1 unless entity @e[tag=mg.trdg_{key}] run function mg:{P}/dg/{key}_win']
    for n, R in enumerate(ROOMS[key]):                          # salle n : déclenchée si l'état vaut 2n, le cooldown est écoulé et qu'un joueur est dans le rayon ; nettoyée quand ses mobs sont tous morts
        cx, cy, cz = R['c']
        px_, py_, pz_ = R['pts'][0]                             # filet : le centre peut être dans un bloc plein (pilier de l'Arbre), on renvoie sur un point d'apparition validé
        DG += [f'execute if score $trds{i} mg.st matches {2 * n} if score $trdc{i} mg.st matches ..0 positioned {cx} {cy} {cz} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..{R["r"]}] run function mg:{P}/dg/{key}_w{n}',
               f'execute if score $trds{i} mg.st matches {2 * n + 1} positioned {cx} {cy} {cz} if loaded ~ ~ ~ unless entity @e[tag=mg.trdw{i}] run function mg:{P}/dg/{key}_c{n}',
               f'execute if score $trds{i} mg.st matches {2 * n + 1} as @e[tag=mg.trdw{i}] {AT} unless entity @s[distance=..{RR}] run tp @s {px_ + 0.5} {py_} {pz_ + 0.5}']
    DG += [f'execute unless score $trda{i} mg.st matches 1 if score $trdc{i} mg.st matches ..0 if score $trds{i} mg.st matches 6 {AT} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:{P}/dg/{key}_start',
           f'execute unless score $trds{i} mg.st matches 6 if score $trdc{i} mg.st matches ..0 unless entity @e[tag=mg.trdw{i}] {AT} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:{P}/dg/{key}_lock',
           f'execute if score $trda{i} mg.st matches 1 run function mg:{P}/dg/{key}']
w(f'{P}/dungeons', DG)
DG_SETUP = ['# Session : barres des alphas des donjons']
DG_CLEAR = ['# Fin de session : barres des alphas']
for i, (k, key, name, sp, pos, door) in enumerate(DUNGEONS):
    DG_SETUP += [f'bossbar add mg:trdg{i} {js(TEXT("👑 Alpha : " + name, "dark_red"))}', f'bossbar set mg:trdg{i} color red', f'bossbar set mg:trdg{i} style notched_10',
                 f'bossbar set mg:trdg{i} players', f'scoreboard players set $trda{i} mg.st 0', f'scoreboard players set $trdc{i} mg.st 0',
                 f'scoreboard players set $trds{i} mg.st 0']
    DG_CLEAR += [f'bossbar remove mg:trdg{i}', f'scoreboard players set $trda{i} mg.st 0']
w(f'{P}/dg_setup', DG_SETUP)
w(f'{P}/dg_clear', DG_CLEAR)
