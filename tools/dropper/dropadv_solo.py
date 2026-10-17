# ================================================================== DROPPER : ESSAIS (id 228) — chacun pour soi, le moins d'essais gagne
# Exécuté par gen_dropper_adv.py (exec) : utilise wr, LV, N, TOP, FLOOR, R, PLAY et les constantes de dropadv_skip.py. Mêmes niveaux que l'Aventure.
# Un essai = un saut depuis le rebord : on part à 1, +1 à chaque raté et à chaque niveau réussi ou passé (sauf le dernier) ;
# total à l'arrivée = nombre de niveaux + ratés. Fini = spectateur (tag mg.ddone) ; quand tout le monde a fini
# (ou au bout de 30 minutes), le plus de niveaux réussis (mg.dok) puis le moins d'essais gagne : un niveau passé ne compte pas.
# Records : personnel (mg.dsb, gardé entre les parties) et serveur (#srv mg.dsb, nom du détenteur dans storage mg:dropadv rec),
# jamais battus par un joueur qui a passé un niveau.
import json, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C

SID = 228
STIME = 36000                 # 30 minutes
REC = '{"nbt":"rec","storage":"mg:dropadv","interpret":true}'

wr('s_prepare', ['# Dropper : Essais — préparation',
                 'function mg:dropadv/fl_add',
                 'scoreboard objectives add mg.dlv dummy', 'scoreboard objectives add mg.dfl dummy', 'scoreboard objectives add mg.dtr dummy',
                 'scoreboard objectives add mg.dtt dummy [{"text":"⬇ Dropper : essais","color":"aqua","bold":true}]',
                 'scoreboard objectives add mg.dsb dummy'] + KPREP + [
                 'tag @a remove mg.ddone',
                 'scoreboard players set @a[tag=mg.play] mg.dlv 1', 'scoreboard players set @a[tag=mg.play] mg.dfl 0',
                 'scoreboard players set @a[tag=mg.play] mg.dtt 1', 'scoreboard players set @a[tag=mg.play] mg.dtr 1'] + KRESET + [
                 'scoreboard players set $dat mg.st 0', 'scoreboard players set #k10 mg.st 10', 'scoreboard players set #k20 mg.st 20', 'scoreboard players set #k1000 mg.st 1000',
                 'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
                 'execute as @a[tag=mg.play] run function mg:dropadv/spawn',
                 'scoreboard objectives setdisplay sidebar mg.dtt',
                 f'scoreboard players set $px mg.st {LV[ORDER[0]].cx}', f'scoreboard players set $py mg.st {TOP + 3}', f'scoreboard players set $pz mg.st {CZ - 11}',
                 'function mg:dropadv/titles'])
wr('s_go', ['# Dropper : Essais — départ',
            'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true',
            'execute as @a[tag=mg.play] run function mg:dropper/attr_on',
            f'tellraw @a[tag=mg.play] [{{"text":"⬇ DROPPER : ESSAIS ! ","color":"aqua","bold":true}},{{"text":"Les {N} niveaux de l\'Aventure, chacun à son rythme. Chaque saut compte pour un essai : atterris dans l\'EAU du premier coup ! Le moins d\'essais gagne (30 minutes au plus).","color":"gray"}}]',
            KGO,
            'function mg:dropadv/s_records',
            'function mg:dropadv/show_level_all'])
wr('s_records', ['# Rappel des records (serveur pour tous, personnel pour chacun)',
                 f'execute if score #srv mg.dsb matches 1.. run tellraw @a[tag=mg.play] [{{"text":"🏆 Record du serveur : ","color":"gold"}},{{"score":{{"name":"#srv","objective":"mg.dsb"}},"color":"yellow","bold":true}},{{"text":" essais","color":"yellow"}},{{"text":" (","color":"gray"}},{REC},{{"text":")","color":"gray"}}]',
                 'execute unless score #srv mg.dsb matches 1.. run tellraw @a[tag=mg.play] [{"text":"🏆 Pas encore de record du serveur : à toi de le poser !","color":"gold"}]',
                 'execute as @a[tag=mg.play] if score @s mg.dsb matches 1.. run tellraw @s [{"text":"★ Ton record : ","color":"aqua"},{"score":{"name":"@s","objective":"mg.dsb"},"color":"white","bold":true},{"text":" essais","color":"white"}]'])
wr('s_tick', ['# Dropper : Essais — chaque tick',
              'scoreboard players add $dat mg.st 1',
              'scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1',
              f'execute as {PLAY} at @s if block ~ ~ ~ minecraft:water run function mg:dropadv/s_success',
              f'execute as {PLAY} at @s if block ~ ~ ~ minecraft:lava run function mg:dropadv/s_fail',
              f'execute as {PLAY} store result score @s mg.t run data get entity @s Pos[1]',
              f'execute as {PLAY[:-1]},scores={{mg.cd=0,mg.t=..{TOP - 2}}}] at @s if data entity @s {{OnGround:1b}} unless block ~ ~ ~ minecraft:water run function mg:dropadv/s_fail',
              f'execute as {PLAY[:-1]},scores={{mg.t=..{FLOOR - 4}}}] run function mg:dropadv/s_fail',
              'scoreboard players operation $dam mg.st = $dat mg.st', 'scoreboard players operation $dam mg.st %= #k10 mg.st',
              f'execute if score $dam mg.st matches 0 as {PLAY} run function mg:dropadv/s_hud',
              'function mg:dropadv/k_tick',
              f'execute if score $dat mg.st matches {STIME}.. run return run function mg:dropadv/s_end',
              'execute unless entity @a[tag=mg.play] run return run function mg:core/draw',
              f'execute unless entity {PLAY} run function mg:dropadv/s_end'])
wr('s_hud', KHUD + [f'scoreboard players set $dsl mg.st {STIME}', 'scoreboard players operation $dsl mg.st -= $dat mg.st', 'scoreboard players operation $dsl mg.st /= #k20 mg.st'] +
   [f'execute if score @s mg.dlv matches {L.n} run title @s actionbar [{{"text":"⬇ {L.n}/{N} : ","color":"gray"}},{{"text":"{L.name}","color":"{L.colr}","bold":true}},'
    f'{{"text":"   essai ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.dtr"}},"color":"white"}},{{"text":"   Σ ","color":"aqua"}},{{"score":{{"name":"@s","objective":"mg.dtt"}},"color":"white"}},'
    f'{{"text":"   ⏱ ","color":"gold"}},{{"score":{{"name":"$dsl","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gold"}}]'
    for L in LV])
wr('s_success', ['# @s atterrit dans l\'eau : niveau réussi (en mg.dtr essais), niveau suivant ou arrivée',
                 'execute unless score $state mg.st matches 2 run return 0',
                 'execute if score @s mg.cd matches 1.. run return 0',
                 'execute at @s run particle minecraft:splash ~ ~ ~ 0.5 0.5 0.5 0.2 60',
                 'execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.3',
                 'execute if score @s mg.dtr matches 1 run tellraw @a[tag=mg.play] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" réussit le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true},{"text":" du premier coup !","color":"green"}]',
                 'execute if score @s mg.dtr matches 2.. run tellraw @a[tag=mg.play] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" réussit le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true},{"text":" en ","color":"gray"},{"score":{"name":"@s","objective":"mg.dtr"},"color":"white"},{"text":" essais","color":"gray"}]',
                 'scoreboard players add @s mg.dok 1',
                 'scoreboard players set @s mg.dkc 0',
                 'scoreboard players add @s mg.dlv 1',
                 f'execute if score @s mg.dlv matches {N + 1}.. run return run function mg:dropadv/s_done',
                 'scoreboard players add @s mg.dtt 1', 'scoreboard players set @s mg.dtr 1',
                 'function mg:dropadv/spawn', 'function mg:dropadv/show_level'])
wr('s_fail', ['# @s a touché autre chose que l\'eau : un essai de plus, retour en haut du niveau',
              'execute if score @s mg.cd matches 1.. run return 0',
              'scoreboard players add @s mg.dfl 1', 'scoreboard players add @s mg.dtt 1', 'scoreboard players add @s mg.dtr 1',
              'execute at @s run particle minecraft:poof ~ ~0.2 ~ 0.3 0.2 0.3 0.05 15',
              'execute at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1',
              'title @s actionbar [{"text":"✖ Raté ! Essai n°","color":"red"},{"score":{"name":"@s","objective":"mg.dtr"},"color":"white"},{"text":" sur ce niveau...","color":"red"}]',
              'function mg:dropadv/spawn'])
wr('s_done', ['# @s a fini tous les niveaux : total d\'essais, records, puis spectateur en attendant les autres',
              f'scoreboard players set @s mg.dlv {N}', 'tag @s add mg.ddone', 'gamemode spectator @s',
              f'execute if score @s mg.dsk matches 0 run tellraw @a[tag=!mg.surv] [{{"text":"🏁 ","color":"gold"}},{{"selector":"@s","color":"gold","bold":true}},{{"text":" termine les {N} niveaux en ","color":"yellow"}},{{"score":{{"name":"@s","objective":"mg.dtt"}},"color":"white","bold":true}},{{"text":" essais !","color":"yellow"}}]',
              f'execute if score @s mg.dsk matches 1.. run tellraw @a[tag=!mg.surv] [{{"text":"🏁 ","color":"gold"}},{{"selector":"@s","color":"gold","bold":true}},{{"text":" arrive au bout : ","color":"yellow"}},{{"score":{{"name":"@s","objective":"mg.dok"}},"color":"white","bold":true}},{{"text":"/{N} réussis (","color":"yellow"}},{{"score":{{"name":"@s","objective":"mg.dsk"}},"color":"white"}},{{"text":" passé(s)), ","color":"yellow"}},{{"score":{{"name":"@s","objective":"mg.dtt"}},"color":"white","bold":true}},{{"text":" essais","color":"yellow"}}]',
              'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1',
              CLEAR,
              'execute if score @s mg.dsk matches 1.. run return run tellraw @s [{"text":"★ Niveau(x) passé(s) : pas de record cette fois.","color":"gray"}]',
              'scoreboard players set $dsn mg.st 0',
              'execute unless score @s mg.dsb matches 1.. run scoreboard players set $dsn mg.st 1',
              'execute if score @s mg.dsb matches 1.. if score @s mg.dtt < @s mg.dsb run scoreboard players set $dsn mg.st 1',
              'execute if score $dsn mg.st matches 1 run scoreboard players operation @s mg.dsb = @s mg.dtt',
              'execute if score $dsn mg.st matches 1 run tellraw @s [{"text":"★ Nouveau record personnel : ","color":"aqua","bold":true},{"score":{"name":"@s","objective":"mg.dsb"},"color":"white"},{"text":" essais !","color":"aqua"}]',
              'execute if score $dsn mg.st matches 0 run tellraw @s [{"text":"★ Ton record reste à ","color":"gray"},{"score":{"name":"@s","objective":"mg.dsb"},"color":"white"},{"text":" essais.","color":"gray"}]',
              'scoreboard players set $dsn mg.st 0',
              'execute unless score #srv mg.dsb matches 1.. run scoreboard players set $dsn mg.st 1',
              'execute if score #srv mg.dsb matches 1.. if score @s mg.dtt < #srv mg.dsb run scoreboard players set $dsn mg.st 1',
              'execute if score $dsn mg.st matches 1 run function mg:dropadv/s_srv'])
wr('s_srv', ['# @s bat le record du serveur',
             'scoreboard players operation #srv mg.dsb = @s mg.dtt',
             'item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents {function:"minecraft:set_name",entity:"this",target:"custom_name",name:[{selector:"@s",color:"white"}]}',
             'data modify storage mg:dropadv rec set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"',
             'tellraw @a[tag=!mg.surv] [{"text":"🏆 Nouveau record du serveur : ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" en ","color":"gold"},{"score":{"name":"#srv","objective":"mg.dsb"},"color":"white","bold":true},{"text":" essais !","color":"gold"}]',
             'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.firework_rocket.twinkle master @s ~ ~ ~ 1 1'])
wr('s_end', ['# Fin : le plus de niveaux réussis (mg.dok), puis le moins d\'essais (mg.dtt) ; personne n\'a réussi de niveau : match nul',
             'execute unless score $state mg.st matches 2 run return 0',
             f'execute if score $dat mg.st matches {STIME}.. run tellraw @a[tag=!mg.surv] [{{"text":"⏱ Temps écoulé !","color":"gold"}}]',
             f'execute as @a[tag=mg.play] run tellraw @a[tag=!mg.surv] [{{"selector":"@s","color":"yellow"}},{{"text":" : ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.dok"}},"color":"white","bold":true}},{{"text":"/{N} réussis, ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.dsk"}},"color":"white"}},{{"text":" passé(s), ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.dtt"}},"color":"white"}},{{"text":" essais","color":"gray"}}]',
             'execute unless entity @a[tag=mg.play,scores={mg.dok=1..}] run return run function mg:core/draw',
             '# score = niveaux réussis × 1 000 000 − essais (au plus 13 millions : pas de dépassement)',
             'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t = @s mg.dok',
             'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st',
             'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st',
             'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t -= @s mg.dtt',
             'scoreboard players set $dbest mg.st -999999999',
             'execute as @a[tag=mg.play] if score @s mg.t > $dbest mg.st run scoreboard players operation $dbest mg.st = @s mg.t',
             'execute as @a[tag=mg.play] if score @s mg.t = $dbest mg.st run tag @s add mg.dwin',
             'execute as @a[tag=mg.dwin,limit=1] run function mg:core/win_player',
             'tag @a remove mg.dwin'])
wr('s_cleanup', ['function mg:dropadv/cleanup'])

# ------------------------------------------------------------------ câblage dans core/ (idempotent) et menu du Dropper
C.init(R)
C.go_range(SID)
_ann = next(l for l in C.lines_of('core/request') if l.startswith('execute if score $game mg.st matches 57 run tellraw'))
C.patch('core/request', _ann, [C.announce(SID, '', '⬇ DROPPER : ESSAIS', 'aqua', f'les {N} niveaux de l\'Aventure, le moins d\'essais gagne !')], where='before')
for _rel, _anchor, _fn in (('core/request', 'prepare', 's_prepare'), ('core/begin', 'go', 's_go'),
                           ('core/game_tick', 'tick', 's_tick'), ('core/return_lobby', 'cleanup', 's_cleanup')):
    C.patch(_rel, f'execute if score $game mg.st matches 57..58 run function mg:bb/{_anchor}', [f'execute if score $game mg.st matches {SID} run function mg:dropadv/{_fn}'])
C.objectives([('mg.dsb', 'dummy')])
for _o in ('mg.dtt', 'mg.dtr'):                                     # objectifs de partie (créés par s_prepare)
    C.patch('desinstaller', 'scoreboard objectives remove mg.bw', [f'scoreboard objectives remove {_o}'])
for _k in range(2, len(parts) + 1):                                 # étapes de construction (leur nombre suit celui des niveaux)
    C.patch('desinstaller', 'schedule clear mg:dropadv/build_wait', [f'schedule clear mg:dropadv/build_{_k}'], where='before')
_p = os.path.join(C.F, 'core', 'request.mcfunction')         # annonce de l'Aventure : nombre de niveaux
_t = open(_p, encoding='utf-8').read()
open(_p, 'w', encoding='utf-8', newline='\n').write(re.sub(r'\(\d+ niveaux à thème', f'({N} niveaux à thème', _t))

_p = os.path.join(R, 'data', 'mg', 'dialog', 'sub_dropper.json')
_d = json.load(open(_p, encoding='utf-8'))
_acts = _d['actions']
for _a in _acts:
    if _a.get('action', {}).get('command') == 'trigger mg.go set 64':
        _a['tooltip'] = [{'text': f'{N} grands niveaux à thème enchaînés (spirale, mine, enfer, usine, espace, ballons... et l\'arc-en-ciel, le plus dur, pour finir) : le premier qui les finit gagne', 'color': 'gray'}]
if not any(_a.get('action', {}).get('command') == f'trigger mg.go set {SID}' for _a in _acts):
    _i = next(i for i, _a in enumerate(_acts) if _a.get('action', {}).get('command') == 'trigger mg.go set 65')
    _acts.insert(_i + 1, {'label': [{'text': 'Solo : essais ', 'color': 'aqua'}, {'text': '★★', 'color': 'gold'}, {'text': '☆☆', 'color': 'dark_gray'}],
                          'tooltip': [{'text': f'Chacun pour soi sur les {N} niveaux de l\'Aventure : chaque saut compte, le moins d\'essais gagne. Records personnel et du serveur', 'color': 'gray'}],
                          'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.go set {SID}'}})
open(_p, 'w', encoding='utf-8', newline='\n').write(json.dumps(_d, ensure_ascii=False, indent=2) + '\n')
print('mode essais (id', SID, ') câblé')
