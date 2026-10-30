"""Fonctions de branchement de la carte « Scourge of the Floaty Isles » dans le pack mg (fonctions pures) : data/mg/function/floaty/*.

    fns = fl_wire.functions(install, spawn, reg, vault)     # {chemin sous mg/function : lignes}

Modèle : tools/arcade/gen_filon.py (tags mg.surv + mg.flw, enter / leave / menu_go / lobby_tick, session). Les patchs des fichiers suivis
du coeur (core/tick, survie/*, pull_all...) sont dans fl_core.py ; le rattrapage (floaty/cu/*) dans fl_catchup.py.
- Une seule partie pour tout le serveur : `$flw mg.st` = au moins un joueur dans la carte ; la boucle de la carte
  (`floaty:map/tick`, sinon NON branchée) ne tourne que dans ce cas, `in mg:floaty positioned <spawn>`.
- enter : garde $setup, floaty:install (une seule fois : garde interne), tags, coffre Floaty du joueur (même colonne que le coffre de
  survie : x = mg.svvx, y 102 / 103, z -30000) rendu, rattrapage de la partie commune (cu/*), puis téléportation au dernier point de
  contrôle du groupe ou au spawn. leave : coffre sauvegardé, tags retirés, barres de boss, attributs / objectifs de la carte remis, lobby.
- pre_tick : un joueur mg.flw hors de mg:floaty (mort sans point de réapparition, /tp...) quitte ; un joueur dans mg:floaty SANS mg.flw
  est renvoyé au lobby (sauf les admins : ils construisent le terrain à la main).
- Chunk forcé : la carte a UN chunk forcé (x -9776..-9761, z 416..431 : setblock / item replace du map/tick, coffres de test) ; le
  ticket d'origine ne suit pas une copie à la main du terrain : session_start le recharge, session_end le libère.
"""
import re

P = 'floaty'
FORCE = '-9776 416 -9761 431'
VAULT_SRC = re.compile(r'\$\(x\) 10([01]) -30000')
CRITERIA_OBJ = re.compile(r'^scoreboard objectives add (\S+) (\S+)')
BAR = re.compile(r'^bossbar add (\S+) ')
TXT = '{"text":"%s","color":"%s"}'
# attributs que la carte modifie et que core/attr_reset ne remet pas (attr_reset : scale, movement_speed, jump_strength, gravity, max_health, fall_damage)
EXTRA_ATTRS = ('sneaking_speed', 'armor', 'attack_damage', 'step_height')
# minuteurs / états par joueur (objectifs dummy) que la carte arme sans les remettre à zéro hors d'elle ; ignorés s'ils ne sont pas dans install
EXTRA_RESET = ('shrink_timer', 'grow_timer', 'sneak_speed_timer', 'HBWard', 'jump_flag_buffer', 'sneak_last')


def vault_functions(vault):
    """vault = {'save': lignes, 'load': lignes} de mg:survie/vault_save / vault_load -> les mêmes pour y 102 / 103 (SystemExit si la source a changé)."""
    out = {}
    for k in ('save', 'load'):
        lines, n = [], 0
        for l in vault[k]:
            new = VAULT_SRC.sub(lambda m: f'$(x) 10{int(m.group(1)) + 2} -30000', l)
            n += new != l
            lines.append(new)
        lines = [l for l in lines if l.strip()]
        if n != 41 or not lines[0].startswith('#'):
            raise SystemExit(f'survie/vault_{k} : {n} lignes de coffre reconnues (41 attendues : 27 + 14 emplacements) : le format a changé')
        lines[0] = f'# coffre Floaty de @s <-> son inventaire (macro x, y 102 / 103), pas celui de la survie (y 100 / 101) ; copie de survie/vault_{k}'
        out[f'{P}/vault_{k}'] = lines
    out[f'{P}/vault_make'] = ['# Coffres Floaty du joueur (macro x : colonne de survie, y 102 / 103) ; sans effet s\'ils existent',
                              '$execute unless block $(x) 102 -30000 minecraft:barrel run setblock $(x) 102 -30000 minecraft:barrel',
                              '$execute unless block $(x) 103 -30000 minecraft:barrel run setblock $(x) 103 -30000 minecraft:barrel']
    return out


def functions(install, spawn, reg_fns, vault):
    """install = lignes de floaty:install ; spawn = (x, y, z) ; reg_fns = fl_catchup.functions(...) ; vault : voir vault_functions."""
    sx, sy, sz = spawn
    bars = [m.group(1) for m in map(BAR.match, install) if m]
    objs = [m for m in map(CRITERIA_OBJ.match, install) if m]
    crit = [m.group(1) for m in objs if m.group(2) not in ('dummy', 'trigger')]
    crit += [o for o in EXTRA_RESET if o in {m.group(1) for m in objs}]
    pos = f'in mg:floaty positioned {sx} {sy} {sz}'
    fn = {}
    fn.update(reg_fns)
    fn.update(vault_functions(vault))
    fn[f'{P}/lobby_tick'] = [
        '# Chaque tick (monde des mini-jeux) : session de la carte, boucle de la carte', 'execute unless score $setup mg.st matches 1 run return 0',
        f'execute unless score $flw mg.st matches 1 if entity @a[tag=mg.flw] run function mg:{P}/session_start',
        f'execute if score $flw mg.st matches 1 unless entity @a[tag=mg.flw] run function mg:{P}/session_end',
        f'execute if score $flw mg.st matches 1.. {pos} run function floaty:map/tick']
    fn[f'{P}/pre_tick'] = [
        '# Avant survie/tick : un joueur de la carte hors de sa dimension quitte ; un joueur dans la dimension sans y être inscrit est renvoyé (admins exceptés)',
        f'execute as @a[tag=mg.flw] at @s unless dimension mg:floaty run function mg:{P}/strayed',
        f'execute as @a[tag=!mg.flw,tag=!mg.admin] at @s if dimension mg:floaty run function mg:{P}/intruder']
    fn[f'{P}/strayed'] = ['# @s (mg.flw) est sorti de mg:floaty autrement (mort sans point de réapparition, /tp...) : retour complet au lobby',
                          f'execute in minecraft:overworld run function mg:{P}/leave']
    fn[f'{P}/intruder'] = ['# @s est dans mg:floaty sans y être inscrit : lobby (sauf partie en cours : ses tags de partie priment)',
                           'execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] in minecraft:overworld run function mg:core/reset_player']
    fn[f'{P}/session_start'] = ['# Premier joueur : chunk forcé de la carte, load de la carte (message de version) une fois par session',
                                'scoreboard players set $flw mg.st 1', f'execute in mg:floaty run forceload add {FORCE}',
                                f'execute {pos} run function floaty:map/load']
    fn[f'{P}/session_end'] = ['# Plus personne : chunk forcé libéré', 'scoreboard players set $flw mg.st 0',
                              f'execute in mg:floaty run forceload remove {FORCE}']
    fn[f'{P}/attrs'] = ['# @s : attributs modifiés par la carte et non remis par core/attr_reset'] + \
                       [f'attribute @s minecraft:{a} base reset' for a in EXTRA_ATTRS]
    fn[f'{P}/reset_scores'] = ['# @s : objectifs de la carte à critère automatique (comptent partout, pas seulement dans la carte) remis à zéro'] + \
                              [f'scoreboard players reset @s {o}' for o in crit]
    fn[f'{P}/bars'] = ['# Barres de boss de la carte qui ont des joueurs : liste = joueurs mg.flw restants (appelé APRES le retrait du tag de @s)'] + \
                      [l for b in bars for l in (f'execute store result score #flb mg.st run bossbar get {b} players',
                                                 f'execute if score #flb mg.st matches 1.. run bossbar set {b} players @a[tag=mg.flw]')]
    fn[f'{P}/enter'] = [
        '# @s entre dans Scourge of the Floaty Isles (contexte : monde des mini-jeux)',
        'execute unless score $setup mg.st matches 1 run return run tellraw @s ' + TXT % ('⚠ Installation manquante : un OP doit d\'abord lancer /function mg:setup', 'red'),
        'execute if entity @s[tag=mg.flw] run return 0',
        'execute if entity @s[tag=mg.mpp] run return run tellraw @s ' + TXT % ('⚠ Tu participes à la Mini Party : la carte sera accessible après.', 'red'),
        '# emplacement du coffre Floaty : celui de la survie (numéro mg.svid / colonne mg.svvx)',
        'execute unless score @s mg.svid matches 1.. in minecraft:overworld run function mg:survie/assign',
        'execute unless score @s mg.svid matches 1.. run return run tellraw @s ' + TXT % ('⚠ Aucun emplacement de coffre libre : Floaty indisponible.', 'red'),
        'function mg:lobkart/leave', 'function mg:parkour/quit', 'tag @s remove mg.inplot', 'tag @s remove mg.plabel', 'tag @s remove mg.visit',
        '# état de la carte (objectifs, équipes, barres, scores) : créé une seule fois (garde dans floaty:install)', 'function floaty:install',
        'tag @s add mg.surv', 'tag @s add mg.flw',
        'execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc', 'execute if score $state mg.st matches 0 run function mg:vote/refresh',
        'team leave @s', 'effect clear @s', 'clear @s', 'xp set @s 0 levels', 'xp set @s 0 points', 'gamemode adventure @s',
        'function mg:core/attr_reset', f'function mg:{P}/attrs', 'attribute @s minecraft:fall_damage_multiplier base set 1', f'function mg:{P}/reset_scores',
        'execute store result storage mg:floaty v.x int 1 run scoreboard players get @s mg.svvx',
        f'execute in minecraft:overworld run function mg:{P}/vault_make with storage mg:floaty v',
        f'execute in minecraft:overworld run function mg:{P}/vault_load with storage mg:floaty v',
        f'function mg:{P}/cu/run', f'function mg:{P}/cu/tp', 'function mg:core/heal',
        'title @s times 10 60 20', 'title @s title {"text":"SCOURGE OF THE FLOATY ISLES","color":"aqua","bold":true}',
        'title @s subtitle {"text":"Une seule partie pour tout le serveur","color":"gray"}',
        'tellraw @s [{"text":"🏝 FLOATY ISLES","color":"aqua","bold":true},{"text":" : la partie est commune à tous les joueurs de la carte. Ton inventaire de la carte est gardé d\'une visite à l\'autre.","color":"yellow"}]',
        'tellraw @s [{"text":" ⌂ Sortir : menu Échap → ≡ Menu → Retour au lobby (ou /trigger mg.sv set 2).","color":"gray"}]',
        'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6']
    fn[f'{P}/leave'] = [
        '# @s retourne au lobby (contexte quelconque) : inventaire de la carte mis de côté, tout ce que la carte a modifié remis',
        'execute unless entity @s[tag=mg.flw] run return 0',
        'execute if score @s mg.svid matches 1.. store result storage mg:floaty v.x int 1 run scoreboard players get @s mg.svvx',
        f'execute if score @s mg.svid matches 1.. in minecraft:overworld run function mg:{P}/vault_make with storage mg:floaty v',
        f'execute if score @s mg.svid matches 1.. in minecraft:overworld run function mg:{P}/vault_save with storage mg:floaty v',
        'tag @s remove mg.flw', 'tag @s remove mg.surv', f'function mg:{P}/bars',
        'xp set @s 0 levels', 'xp set @s 0 points', f'function mg:{P}/attrs', f'function mg:{P}/reset_scores',
        'execute in minecraft:overworld run function mg:core/reset_player',
        'tellraw @s ' + TXT % ('⌂ Retour au lobby. Ton inventaire de la carte est mis de côté ; la partie continue pour les autres joueurs.', 'gold')]
    fn[f'{P}/menu_go'] = [
        '# @s : « Scourge of the Floaty Isles » (menu Échap, trigger mg.sv 10)',
        'execute unless score $setup mg.st matches 1 run return run tellraw @s ' + TXT % ('⚠ Installation manquante : un OP doit d\'abord lancer /function mg:setup', 'red'),
        'execute if entity @s[tag=mg.flw] run return run tellraw @s ' + TXT % ('Tu es déjà dans la carte.', 'gray'),
        'execute if entity @s[tag=mg.play] run return run tellraw @s ' + TXT % ('⚠ Tu participes à la partie en cours : la carte sera accessible après.', 'red'),
        'execute if entity @s[tag=mg.out] run return run tellraw @s ' + TXT % ('⚠ Partie en cours : la carte sera accessible après.', 'red'),
        'execute if entity @s[tag=mg.dl] run return run tellraw @s ' + TXT % ('⚔ Duel en cours : termine-le (ou abandonne-le) avant.', 'red'),
        'execute if entity @s[tag=mg.gtw] run function mg:gta/leave', 'execute if entity @s[tag=mg.tvw] run function mg:terra/leave',
        'execute if entity @s[tag=mg.surv] run function mg:survie/leave', f'execute in minecraft:overworld run function mg:{P}/enter']
    return fn
