"""Logique de jeu de la Course d'elytres (mg:elyrace/*), independante du parcours : objectifs, preparation, depart,
tick, regles (coeurs, sol, eau, planeur), mur, arrivee, fin, nettoyage. Les tables qui dependent des coordonnees
(anneaux, reprises, places) sont dans rings.py.
Python stdlib uniquement (compatible 3.8).
"""
import course_canyon as K

GAME_ID = 66
HEARTS = 3
GRACE = 40               # ticks sans regles apres une reapparition
COOLDOWN = 12            # ticks entre deux murs comptes (avancement et chute de vitesse partagent ce delai)
STALL = 10               # ticks sans planer (apres avoir plane) avant renvoi au point de reprise
DROP_SQ = 4000           # verification de secours du choc : chute du carre de la vitesse horizontale (centiemes de bloc/tick, au carre) d'au moins ceci
DROP_REL = 30            # ET d'au moins ce pourcentage du carre precedent (a grande vitesse, seul ce seuil relatif protege d'un cabre brutal)
TIME_LIMIT = 3600        # 3 minutes
END_WAIT = 400           # 20 s entre le premier arrive et la fin
LEFT_X = K.EDGE_X + 1    # au-dela, le joueur n'est plus sur la plateforme de depart : les regles s'appliquent
RING_N = len(K.RINGS)

# objectifs par joueur : (nom, role). Le premier sert au tableau de droite.
OBJECTIVES = [
    ('xa', 'anneaux valides', '[{"text":"🪽 COURSE D\'ÉLYTRES — anneaux","color":"aqua"}]'),
    ('xo', 'anneaux d\'or pris (ne fait qu\'augmenter)', None),
    ('xc', 'dernier point de reprise (numero d\'anneau, 0 = depart)', None),
    ('xh', 'coeurs restants', None),
    ('xp', 'progression maximale (x), departage la fin du temps', None),
    ('xx', 'x courant', None),
    ('xg', 'ticks de grace restants', None),
    ('xn', 'ticks consecutifs sans planer', None),
    ('xl', 'a plane depuis la derniere reapparition', None),
    ('xk', 'delai restant avant de compter un nouveau mur', None),
    ('xf', 'place a l\'arrivee (0 = pas arrive)', None),
    ('xb1', 'x precedent (centiemes)', None),
    ('xb2', 'z precedent (centiemes)', None),
    ('xb3', 'carre de la vitesse horizontale precedente', None),
]
ELYTRA = ('minecraft:elytra[minecraft:custom_data={mg_elyr:1b},minecraft:unbreakable={},'
          'minecraft:enchantments={"minecraft:binding_curse":1},'
          'minecraft:custom_name={"text":"Élytres de course","color":"aqua","italic":false}]')
ROCKET = ('minecraft:firework_rocket[minecraft:custom_data={mg_elyr:1b},minecraft:fireworks={flight_duration:1},'
          'minecraft:custom_name={"text":"Fusée d\'or","color":"gold","italic":false}]')
SB = '"score":{"name":"@s","objective":"%s"}'


def objectives_lines():
    out = ['# Objectifs de la Course d\'élytres (généré par tools/elyrace/gen_elyrace.py ; appelé par mg:core/load)']
    for n, _, disp in OBJECTIVES:
        out.append('scoreboard objectives add mg.%s dummy%s' % (n, ' ' + disp if disp else ''))
    return out


def uninstall_lines():
    out = ['# Désinstallation de la Course d\'élytres (appelé par mg:desinstaller)',
           '# pas de build_abort ici : il appelle core/forceloads, qui réactiverait tous les chargements forcés que desinstaller vient de retirer',
           'schedule clear mg:elyrace/build', 'schedule clear mg:elyrace/build_wait',
           'data remove storage mg:elyrace v1',
           'clear @a minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]',
           'clear @a minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]',
           'tag @a remove mg.xw1', 'tag @a remove mg.xtp',
           'advancement revoke @a only mg:elyrace_wall']
    out += ['scoreboard objectives remove mg.%s' % n for n, _, _ in OBJECTIVES]
    return out


def prepare_lines():
    out = ['# Course d\'élytres : préparation (parcours 1 : Canyon du Couchant)',
           '# parcours pas (entièrement) construit : on n\'envoie personne dedans, partie annulée',
           'execute unless data storage mg:elyrace v1 run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d\'élytres : le parcours n\'est pas (entièrement) construit, lance /function mg:elyrace/build","color":"red"}]',
           'execute unless data storage mg:elyrace v1 run tellraw @a[tag=mg.play] [{"text":"🪽 Le parcours n\'est pas encore construit : partie annulée.","color":"red"}]',
           'execute unless data storage mg:elyrace v1 run return run function mg:core/draw',
           '# restes d\'une partie précédente',
           'tag @a remove mg.xw1', 'tag @a remove mg.xtp',
           'function mg:elyrace/fl_add', 'function mg:elyrace/gate_on',
           '# perchoir des spectateurs (éliminés / reconnectés)',
           'scoreboard players set $px mg.st 24', 'scoreboard players set $py mg.st %d' % (K.MESA + 20), 'scoreboard players set $pz mg.st %d' % K.CZ,
           'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
           'scoreboard players set @a[tag=mg.play] mg.deaths 0']
    for n, _, _ in OBJECTIVES:
        out.append('scoreboard players set @a[tag=mg.play] mg.%s %d' % (n, HEARTS if n == 'xh' else 0))
    out += ['scoreboard players set $xt mg.st 0', 'scoreboard players set $xf mg.st 0',
            'scoreboard players set $xw mg.st 0', 'scoreboard players set $xe mg.st 0',
            'scoreboard players set #k10 mg.st 10', 'scoreboard players set #k20 mg.st 20',
            'scoreboard players set #k100 mg.st 100', 'scoreboard players set #krel mg.st %d' % DROP_REL,
            'scoreboard players set $ri mg.st 0',
            'execute as @a[tag=mg.play] run function mg:elyrace/equip',
            'execute as @a[tag=mg.play] run function mg:elyrace/place_one',
            'execute as @a[tag=mg.play] run spawnpoint @s 24 %d %d' % (K.MESA + 1, K.CZ),
            'scoreboard objectives setdisplay sidebar mg.xa']
    return out


def go_lines():
    return ['# Course d\'élytres : départ',
            'function mg:elyrace/gate_off',
            'effect give @a[tag=mg.play] minecraft:resistance infinite 4 true',
            'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true',
            'tellraw @a[tag=mg.play] [{"text":"🪽 COURSE D\'ÉLYTRES — CANYON DU COUCHANT : ","color":"aqua","bold":true},{"text":"saute de la falaise, ouvre tes élytres (espace en l\'air) et franchis les %d anneaux dans l\'ordre, par le trou. Le premier arrivé gagne (3 minutes au plus).","color":"gray"}]' % RING_N,
            'tellraw @a[tag=mg.play] [{"text":"♥ 3 cœurs : chaque choc contre un mur en retire un. Plus de cœur, anneau raté, sol, eau ou trop longtemps sans planer : retour en l\'air au dernier point de reprise (colonnes lumineuses).","color":"gray"}]',
            'tellraw @a[tag=mg.play] [{"text":"★ Trois anneaux d\'or en détour : chacun donne une fusée (clic droit en vol pour accélérer).","color":"gold"}]']


def tick_lines():
    return ['# Course d\'élytres : tick de jeu',
            'scoreboard players add $xt mg.st 1',
            'execute as @a[tag=mg.play,scores={mg.xf=0}] run function mg:elyrace/player',
            'scoreboard players operation $xm mg.st = $xt mg.st',
            'scoreboard players operation $xm mg.st %= #k10 mg.st',
            'execute if score $xm mg.st matches 0 as @a[tag=mg.play,scores={mg.xf=0}] run function mg:elyrace/hud',
            '# Après le premier arrivé : les autres ont 20 s ; tous arrivés ou partis : fin immédiate',
            'execute if score $xw mg.st matches 1 run scoreboard players remove $xe mg.st 1',
            'execute if score $xw mg.st matches 1 if score $xe mg.st matches ..0 run return run function mg:elyrace/end',
            'execute if score $xw mg.st matches 1 unless entity @a[tag=mg.play,scores={mg.xf=0}] run return run function mg:elyrace/end',
            'execute if score $xt mg.st matches %d run tellraw @a[tag=mg.play] [{"text":"🪽 Plus que 30 secondes !","color":"gold"}]' % (TIME_LIMIT - 600),
            'execute if score $xt mg.st matches %d.. run return run function mg:elyrace/timeout' % TIME_LIMIT,
            'execute unless entity @a[tag=mg.play] run function mg:core/draw']


def player_lines():
    return ['# @s = joueur en course (pas encore arrivé) : position, délais, règles',
            'execute store result score @s mg.xx run data get entity @s Pos[0]',
            'scoreboard players operation @s mg.xp > @s mg.xx',
            'scoreboard players remove @s[scores={mg.xg=1..}] mg.xg 1',
            'scoreboard players remove @s[scores={mg.xk=1..}] mg.xk 1',
            'execute if predicate mg:gliding run scoreboard players set @s mg.xl 1',
            'execute if predicate mg:gliding run scoreboard players set @s mg.xn 0',
            'execute unless predicate mg:gliding if score @s mg.xl matches 1 run scoreboard players add @s mg.xn 1',
            'function mg:elyrace/speed',
            '# Mort (filet) ou sorti de la zone construite (monde vide) : retour au dernier point de reprise',
            'execute if score @s mg.deaths matches 1.. run return run function mg:elyrace/respawn',
            'execute unless entity @s[x=%d,y=0,z=%d,dx=%d,dy=330,dz=%d] run return run function mg:elyrace/respawn'
            % (K.X0, K.Z0, K.X1 - K.X0, K.Z1 - K.Z0),
            '# Encore sur la plateforme de départ : aucune règle',
            'execute if score @s mg.xx matches ..%d run return 0' % (LEFT_X - 1),
            'execute if score @s mg.xg matches 0 if score @s mg.xn matches %d.. run return run function mg:elyrace/respawn' % (STALL + 1),
            'execute if score @s mg.xg matches 0 at @s if block ~ ~ ~ minecraft:water run return run function mg:elyrace/respawn',
            'execute if score @s mg.xg matches 0 at @s if data entity @s {OnGround:1b} run return run function mg:elyrace/respawn',
            'function mg:elyrace/rings']


def speed_lines():
    return ['# @s = joueur : chute de la vitesse horizontale d\'un tick à l\'autre (vérification de secours du choc contre un mur,',
            '# si l\'avancement ne se déclenche pas). La vitesse est mesurée par le carré de la norme (dx² + dz², en centièmes de bloc)',
            'execute store result score #cx mg.st run data get entity @s Pos[0] 100',
            'execute store result score #cz mg.st run data get entity @s Pos[2] 100',
            'scoreboard players operation #dx mg.st = #cx mg.st', 'scoreboard players operation #dx mg.st -= @s mg.xb1',
            'scoreboard players operation #dz mg.st = #cz mg.st', 'scoreboard players operation #dz mg.st -= @s mg.xb2',
            'scoreboard players operation #vv mg.st = #dx mg.st', 'scoreboard players operation #vv mg.st *= #dx mg.st',
            'scoreboard players operation #dz mg.st *= #dz mg.st', 'scoreboard players operation #vv mg.st += #dz mg.st',
            '# pendant le délai (réapparition, mur déjà compté) la référence de vitesse est remise à zéro',
            'execute if score @s mg.xk matches 1.. run scoreboard players set #vv mg.st 0',
            'scoreboard players operation #wv mg.st = @s mg.xb3', 'scoreboard players operation #wv mg.st -= #vv mg.st',
            '# seuil relatif : chute * 100 - précédent * %d >= 0 (la chute doit représenter au moins %d %% du carré précédent)' % (DROP_REL, DROP_REL),
            'scoreboard players operation #wq mg.st = #wv mg.st', 'scoreboard players operation #wq mg.st *= #k100 mg.st',
            'scoreboard players operation #wp mg.st = @s mg.xb3', 'scoreboard players operation #wp mg.st *= #krel mg.st',
            'scoreboard players operation #wq mg.st -= #wp mg.st',
            'scoreboard players operation @s mg.xb1 = #cx mg.st', 'scoreboard players operation @s mg.xb2 = #cz mg.st',
            'scoreboard players operation @s mg.xb3 = #vv mg.st',
            'execute unless predicate mg:gliding run return 0',
            'execute if score @s mg.xg matches 1.. run return 0',
            'execute if score #wv mg.st matches %d.. if score #wq mg.st matches 0.. run function mg:elyrace/wall' % DROP_SQ]


def wall_lines():
    return ['# @s = joueur qui vient de heurter un mur (avancement mg:elyrace_wall ou chute de vitesse) : -1 coeur',
            'execute if score @s mg.xk matches 1.. run return 0',
            'execute if score @s mg.xg matches 1.. run return 0',
            'execute if score @s mg.xf matches 1.. run return 0',
            'execute if score @s mg.xx matches ..%d run return 0' % (LEFT_X - 1),
            'scoreboard players set @s mg.xk %d' % COOLDOWN,
            'scoreboard players remove @s mg.xh 1',
            'execute at @s run playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8',
            'execute if score @s mg.xh matches ..0 run return run function mg:elyrace/respawn',
            'function mg:elyrace/hud']


def wall_adv_lines():
    return ['# Avancement mg:elyrace_wall : le joueur (@s) vient de subir des dégâts de collision en vol',
            'advancement revoke @s only mg:elyrace_wall',
            'execute unless score $game mg.st matches %d run return 0' % GAME_ID,
            'execute unless score $state mg.st matches 2 run return 0',
            'execute unless entity @s[tag=mg.play,scores={mg.xf=0}] run return 0',
            'function mg:elyrace/wall']


def hud_lines():
    tail = ('{"text":"   ◎ ","color":"aqua"},{%s,"color":"white"},{"text":" / %d","color":"gray"},'
            '{"text":"   ★ ","color":"gold"},{%s,"color":"white"},{"text":" / %d","color":"gray"}]'
            % (SB % 'mg.xa', RING_N, SB % 'mg.xo', len(K.GOLDS)))
    hearts = [('3..', '{"text":"♥♥♥","color":"red"}'),
              ('2', '{"text":"♥♥","color":"red"},{"text":"♡","color":"dark_gray"}'),
              ('1', '{"text":"♥","color":"red"},{"text":"♡♡","color":"dark_gray"}'),
              ('..0', '{"text":"♡♡♡","color":"dark_gray"}')]
    return ['# @s = joueur : barre d\'action (cœurs, anneaux, anneaux d\'or)'] + [
        'execute if score @s mg.xh matches %s run title @s actionbar [%s,%s' % (m, h, tail) for m, h in hearts]


def finish_lines():
    jf = '{"selector":"@s","color":"yellow"}'
    return ['# @s = joueur qui franchit l\'anneau d\'arrivée',
            'scoreboard players add $xf mg.st 1',
            'scoreboard players operation @s mg.xf = $xf mg.st',
            'scoreboard players operation #s mg.st = $xt mg.st', 'scoreboard players operation #s mg.st /= #k20 mg.st',
            'tellraw @a[tag=mg.play] [{"text":"🏁 ","color":"gold"},%s,{"text":" passe la ligne d\'arrivée en position ","color":"gray"},{%s,"color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"#s","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]' % (jf, SB % 'mg.xf'),
            'title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]',
            'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1',
            'execute at @s run particle minecraft:firework ~ ~1 ~ 1 1 1 0.2 60',
            '# premier arrivé : la course s\'arrête dans 20 s au plus, le temps que les autres terminent',
            'execute if score $xf mg.st matches 1 run scoreboard players set $xw mg.st 1',
            'execute if score $xf mg.st matches 1 run scoreboard players set $xe mg.st %d' % END_WAIT,
            'execute if score $xf mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🪽 Les autres ont 20 secondes pour terminer et se classer.","color":"gold"}]',
            '# arrivé : mis en sécurité au perchoir de départ (la zone construite s\'arrête après l\'arrivée), en spectateur',
            'execute store result storage mg:c x int 1 run scoreboard players get $px mg.st',
            'execute store result storage mg:c y int 1 run scoreboard players get $py mg.st',
            'execute store result storage mg:c z int 1 run scoreboard players get $pz mg.st',
            'function mg:core/tp_perch with storage mg:c',
            'gamemode spectator @s']


def small_lines():
    """Petites fonctions : points de reprise, anneau d'or, anneau rate, equipement, fin, temps ecoule, nettoyage, portillon."""
    return {
        'cp_reached': ['# @s = joueur qui valide un anneau qui est aussi un point de reprise',
                       'scoreboard players operation @s mg.xc = @s mg.xa',
                       'title @s actionbar [{"text":"⚑ Point de reprise enregistré","color":"green","bold":true}]',
                       'execute at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 1.5'],
        'gold_hit': ['# @s = joueur qui traverse un anneau d\'or : une fusée',
                     'give @s %s 1' % ROCKET,
                     'execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.4',
                     'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.4 0.4 0.3 25',
                     'tellraw @s [{"text":"★ Anneau d\'or ! ","color":"gold","bold":true},{"text":"+1 fusée (clic droit en vol pour accélérer).","color":"gray"}]'],
        'miss': ['# @s = joueur qui a raté un anneau : retour au dernier point de reprise',
                 'tellraw @s [{"text":"✖ Anneau raté ! ","color":"red","bold":true},{"text":"Retour au dernier point de reprise.","color":"gray"}]',
                 'function mg:elyrace/respawn'],
        'equip': ['# @s = joueur : élytres verrouillées (pas de fusée au départ : elles viennent des anneaux d\'or)',
                  'item replace entity @s armor.chest with ' + ELYTRA],
        'end': ['# Fin de la course : gagne le premier arrivé encore en ligne (plus petite place mg.xf) ; les autres sont classés dans le chat',
                'execute unless entity @a[tag=mg.play,scores={mg.xf=1..}] run return run function mg:core/draw',
                'scoreboard players set #mn mg.st 9999',
                'execute as @a[tag=mg.play,scores={mg.xf=1..}] run scoreboard players operation #mn mg.st < @s mg.xf',
                'tag @a remove mg.xw1',
                'execute as @a[tag=mg.play,scores={mg.xf=1..}] if score @s mg.xf = #mn mg.st run tag @s add mg.xw1',
                'execute as @a[tag=mg.xw1,limit=1] run function mg:core/win_player',
                'tag @a remove mg.xw1'],
        'timeout': ['# Temps écoulé : un arrivé en ligne gagne, sinon le plus avancé (anneaux validés, puis x maximal) ; rien parcouru : égalité',
                    'execute if entity @a[tag=mg.play,scores={mg.xf=1..}] run return run function mg:elyrace/end',
                    'tellraw @a[tag=mg.play] [{"text":"🪽 Temps écoulé : le plus avancé l\'emporte !","color":"gold"}]',
                    '# clé de classement par joueur (dans mg.xx, libre à ce stade) : anneaux * 2000 + x maximal',
                    'scoreboard players set #k2000 mg.st 2000',
                    'execute as @a[tag=mg.play] run scoreboard players operation @s mg.xx = @s mg.xa',
                    'execute as @a[tag=mg.play] run scoreboard players operation @s mg.xx *= #k2000 mg.st',
                    'execute as @a[tag=mg.play] run scoreboard players operation @s mg.xx += @s mg.xp',
                    'scoreboard players set #mx mg.st -1',
                    'execute as @a[tag=mg.play] run scoreboard players operation #mx mg.st > @s mg.xx',
                    'execute if score #mx mg.st matches ..%d run return run function mg:core/draw' % (LEFT_X - 1),
                    'tag @a remove mg.xtp',
                    'execute as @a[tag=mg.play] if score @s mg.xx = #mx mg.st run tag @s add mg.xtp',
                    'execute as @a[tag=mg.xtp,limit=1] run function mg:core/win_player',
                    'tag @a remove mg.xtp'],
        'cleanup': ['# Nettoyage de la Course d\'élytres (appelé au retour au lobby)',
                    'tag @a remove mg.xw1', 'tag @a remove mg.xtp',
                    'function mg:elyrace/fl_remove', 'scoreboard objectives setdisplay sidebar'],
        'place_one': ['# @s = joueur : prend la place suivante sur la plateforme de départ',
                      'scoreboard players add $ri mg.st 1', 'scoreboard players operation @s mg.ri = $ri mg.st',
                      'function mg:elyrace/place_tp'],
        'gate_on': ['# Portillon de départ (verre rouge)',
                    'fill %d %d %d %d %d %d minecraft:red_stained_glass' % (K.GATE_X, K.MESA + 1, K.CZ - 12, K.GATE_X, K.MESA + 5, K.CZ + 12)],
        'gate_off': ['# GO : ouvre le portillon',
                     'fill %d %d %d %d %d %d minecraft:air' % (K.GATE_X, K.MESA + 1, K.CZ - 12, K.GATE_X, K.MESA + 5, K.CZ + 12)],
        'fl_add': ['# Zone de départ chargée pendant la partie',
                   'forceload add %d %d %d %d' % (K.X0, K.CZ - 32, K.X0 + 96, K.CZ + 32)],
        'fl_remove': ['forceload remove %d %d %d %d' % (K.X0, K.CZ - 32, K.X0 + 96, K.CZ + 32), 'function mg:core/forceloads'],
    }


def functions():
    out = {'prepare': prepare_lines(), 'go': go_lines(), 'tick': tick_lines(), 'player': player_lines(),
           'speed': speed_lines(), 'wall': wall_lines(), 'wall_adv': wall_adv_lines(), 'hud': hud_lines(),
           'finish': finish_lines(), 'objectives': objectives_lines(), 'uninstall': uninstall_lines()}
    out.update(small_lines())
    return out
