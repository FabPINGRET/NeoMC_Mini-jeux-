"""Logique de jeu de la Course d'elytres (mg:elyrace/*), independante du parcours : objectifs, depart, tick, regles
communes (choc contre un mur, arrivee, fin, temps ecoule, nettoyage). Le tick de chaque joueur, les tables qui dependent
des coordonnees (anneaux, reprises, places) et la construction sont propres a chaque parcours (course_fns.py, rings.py,
build_chain.py) ; la preparation et les repartiteurs par parcours sont dans dispatch.py ; le contre-la-montre solo est a part, par
joueur (tag mg.xso : lancement dans solo.py, tick et fin dans solo_run.py) ; les records sont dans records.py. Seules finish et wall_adv
connaissent le solo (premiere ligne : renvoi vers solo/finish, ou garde de wall_adv) ; le parcours d'un joueur est mg.xcr, le temps
d'une arrivee est #xrt ($xt en groupe, mg.xst en solo).
Python stdlib uniquement (compatible 3.8).
"""
import course_common as CC
import glide as GL
import reasons as RS
import records as RC
import wind as W

GAME_ID = 66
HEARTS = 3
GRACE = 40               # ticks sans regles apres une reapparition
COOLDOWN = 12            # ticks entre deux murs comptes (avancement et chute de vitesse partagent ce delai)
STALL = 10               # ticks sans planer (apres avoir plane) avant renvoi au point de reprise
DROP_SQ = 8000           # verification de secours du choc : chute du carre de la vitesse horizontale (centiemes de bloc/tick, au carre) d'au moins ceci ;
                         # 8000 (4000 avant la gravite 0,104) : les vols de reference vont a ~3 b/tick, leur chute max par tick atteint 2574 (Canyon) et la marge x3 de
                         # verify_speed l'exige sous le seuil (7722), ce qui rend ~8000 la plus petite valeur ronde
DROP_REL = 30            # ET d'au moins ce pourcentage du carre precedent (a grande vitesse, seul ce seuil relatif protege d'un cabre brutal)
TIME_LIMIT = 3600        # 3 minutes
END_WAIT = 400           # 20 s entre le premier arrive et la fin
EDGE_X = 32              # bord de la plateforme de depart : commun a tous les parcours (verifie par checks.py)
GATE_X = 27              # portillon de depart : commun aussi
LEFT_X = EDGE_X + 1      # au-dela, le joueur n'est plus sur la plateforme de depart : les regles s'appliquent

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
    ('xq1', 'origine du balayage des anneaux : x (centiemes, position du tick precedent)', None),
    ('xq2', 'origine du balayage des anneaux : y (centiemes)', None),
    ('xq3', 'origine du balayage des anneaux : z (centiemes)', None),
    ('xu', 'ticks de turbo restants (anneau d\'or)', None),
] + W.objectives()                 # + mg.xv (anneaux de vent pris) si WIND
# objectifs HORS de OBJECTIVES (prepare remet ceux-la a zero a chaque depart de groupe) : (nom, role). xcr est pose par prepare (groupe) ou
# par solo/start ; xse, xsl et xph/xst ne servent qu'au solo (voir solo_run.py)
EXTRA_OBJECTIVES = [
    ('xcr', 'parcours du joueur (NUM : groupe et solo)'),
    ('xph', 'solo : phase (1 decompte, 2 course, 3 arrivee)'),
    ('xst', 'solo : chrono du joueur (ticks) : decompte, course ou arrivee selon la phase'),
    ('xse', 'solo : tick de la fin du dernier solo du joueur (delai de 30 s)'),
    ('xsl', 'solo : dernier tick ou le joueur etait en ligne (detecte la reconnexion)'),
]
TAGS = ['mg.xw1', 'mg.xtp'] + W.tags()    # etiquettes temporaires de la fin de course (pas des objectifs) + charges de vent si WIND
SOLO_TAGS = ['mg.xso', 'mg.xsp0']         # solo en cours ; pause d'avant le solo (hors TAGS : prepare ne doit pas les effacer)
ELYTRA = ('minecraft:elytra[minecraft:custom_data={mg_elyr:1b},minecraft:unbreakable={},'
          'minecraft:enchantments={"minecraft:binding_curse":1},'
          'minecraft:custom_name={"text":"Élytres de course","color":"aqua","italic":false}]')
SB = '"score":{"name":"@s","objective":"%s"}'


def grav_line(g):
    return 'attribute @s minecraft:gravity base set %s' % g


# gravite : la gravite de base du parcours (GRAVITY de la spec, c<N>/grav) est posee au GO, a chaque reapparition ; le turbo d'un anneau d'or la
# renforce TURBO_TICKS ticks (mg.xu) ; core/attr_reset_g la remet a la normale (fin de solo, desinstallation ; le lobby : core/attr_reset)
GRAV_ON = 'function mg:elyrace/grav_on'
GRAV_ON_ALL = 'execute as @a[tag=mg.play] run ' + GRAV_ON
GRAV_RESET = 'function mg:core/attr_reset_g'
GRAV_RESET_ALL = 'execute as @a[scores={mg.xcr=1..}] run ' + GRAV_RESET       # pas de tag=mg.play : desinstaller l'a deja retire
GRAV_TURBO = grav_line(GL.TURBO_G)
XU_SET = 'scoreboard players set @s mg.xu %d' % GL.TURBO_TICKS
XU_ZERO = 'scoreboard players set @s mg.xu 0'


def objectives_lines(specs):
    out = ['# Objectifs de la Course d\'élytres (généré par tools/elyrace/gen_elyrace.py ; appelé par mg:core/load)']
    for n, _, disp in OBJECTIVES:
        out.append('scoreboard objectives add mg.%s dummy%s' % (n, ' ' + disp if disp else ''))
    out += ['# hors de OBJECTIVES (prepare les remet à zéro à chaque départ) : parcours du joueur et état du solo (par joueur), trigger du solo, records par parcours']
    out += ['scoreboard objectives add mg.%s dummy' % n for n, _ in EXTRA_OBJECTIVES]
    out += ['scoreboard objectives add mg.xs trigger']
    out += RC.objective_lines(specs)
    out += ['# constantes de elyrace/time, de speed et du HUD du solo (plus posées par prepare : le solo n\'y passe pas)',
            'scoreboard players set #k5 mg.st 5', 'scoreboard players set #k10 mg.st 10', 'scoreboard players set #k20 mg.st 20',
            'scoreboard players set #k100 mg.st 100', 'scoreboard players set #krel mg.st %d' % DROP_REL,
            '# purge des anciens drapeaux du solo de la 2c (le solo ne passe plus par $state : $xs et $xse n\'existent plus)',
            'scoreboard players reset $xs mg.st', 'scoreboard players reset $xse mg.st']
    return out


def go_lines(specs):
    out = ['# Course d\'élytres : départ',
           'function mg:elyrace/gate_off',
           'effect give @a[tag=mg.play] minecraft:resistance infinite 4 true',
           'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true']
    out += ['# texte du départ : go_text parle à @s (le solo l\'appelle pour son seul joueur)']
    out += ['execute if score $xc mg.st matches %d as @a[tag=mg.play] run function %s' % (s.NUM, CC.fn(s, 'go_text')) for s in specs]
    out += ['# gravité de course de chaque participant (selon son parcours, mg.xcr) ; le solo l\'appelle pour son seul joueur', GRAV_ON_ALL]
    return out


def tick_lines(specs):
    """Un seul repartiteur par tick : le parcours est $xc. @e[type=player] (et non @a) ignore un joueur mort pendant les
    1 a 3 ticks de la reapparition immediate (@a le voit) : sinon respawn le replacerait, puis la reapparition vanilla le renverrait au depart."""
    sel = '@e[type=player,tag=mg.play,scores={mg.xf=0}]'
    out = ['# Course d\'élytres : tick de jeu', 'scoreboard players add $xt mg.st 1'] + W.cleanup_lines()
    for s in specs:
        cond = 'if score $xc mg.st matches %d' % s.NUM if s.NUM > 1 else 'unless score $xc mg.st matches 2..'
        out.append('execute %s as %s run function %s' % (cond, sel, CC.fn(s, 'player')))
    out += ['scoreboard players operation $xm mg.st = $xt mg.st',
            'scoreboard players operation $xm mg.st %= #k10 mg.st',
            'execute if score $xm mg.st matches 0 as @a[tag=mg.play,scores={mg.xf=0}] run function mg:elyrace/hud',
            '# Après le premier arrivé : les autres ont 20 s ; tous arrivés ou partis : fin immédiate',
            'execute if score $xw mg.st matches 1 run scoreboard players remove $xe mg.st 1',
            'execute if score $xw mg.st matches 1 if score $xe mg.st matches ..0 run return run function mg:elyrace/end',
            'execute if score $xw mg.st matches 1 unless entity @a[tag=mg.play,scores={mg.xf=0}] run return run function mg:elyrace/end',
            'execute if score $xt mg.st matches %d run tellraw @a[tag=mg.play] [{"text":"🪽 Plus que 30 secondes !","color":"gold"}]' % (TIME_LIMIT - 600),
            'execute if score $xt mg.st matches %d.. run return run function mg:elyrace/timeout' % TIME_LIMIT,
            '# plus aucun participant (déconnexion) : fin sans vainqueur',
            'execute unless entity @a[tag=mg.play] run function mg:core/draw']
    return out


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
    return ['# @s = joueur qui vient de heurter un mur (avancement mg:elyrace_wall ou chute de vitesse) : -1 coeur ; plus de coeur : reprise (why/ko)',
            'execute if score @s mg.xk matches 1.. run return 0',
            'execute if score @s mg.xg matches 1.. run return 0',
            'execute if score @s mg.xf matches 1.. run return 0',
            'execute if score @s mg.xx matches ..%d run return 0' % (LEFT_X - 1),
            'scoreboard players set @s mg.xk %d' % COOLDOWN,
            'scoreboard players remove @s mg.xh 1',
            'execute at @s run playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8',
            'execute if score @s mg.xh matches ..0 run return run ' + RS.call('ko'),
            '# encore en vie : sous-titre du choc, puis le HUD'] + RS.subtitle(*RS.HIT) + ['function mg:elyrace/hud']


def wall_adv_lines():
    return ['# Avancement mg:elyrace_wall : le joueur (@s) vient de subir des dégâts de collision en vol',
            'advancement revoke @s only mg:elyrace_wall',
            '# solo : le joueur est dans sa phase de course (le solo ne passe pas par $game ni $state)',
            'execute if entity @s[tag=mg.xso,scores={mg.xph=2}] run return run function mg:elyrace/wall',
            'execute if entity @s[tag=mg.xso] run return 0',
            'execute unless score $game mg.st matches %d run return 0' % GAME_ID,
            'execute unless score $state mg.st matches 2 run return 0',
            'execute unless entity @s[tag=mg.play,scores={mg.xf=0}] run return 0',
            'function mg:elyrace/wall']


def finish_lines(specs):
    jf = '{"selector":"@s","color":"yellow"}'
    out = ['# @s = joueur qui franchit l\'anneau d\'arrivée (course de groupe ; le solo a sa propre arrivée, qui fixe sa phase 3)',
            'execute if entity @s[tag=mg.xso] run return run function mg:elyrace/solo/finish',
            'scoreboard players add $xf mg.st 1',
            'scoreboard players operation @s mg.xf = $xf mg.st',
            'scoreboard players operation #s mg.st = $xt mg.st', 'scoreboard players operation #s mg.st /= #k20 mg.st',
            'tellraw @a[tag=mg.play] [{"text":"🏁 ","color":"gold"},%s,{"text":" passe la ligne d\'arrivée en position ","color":"gray"},{%s,"color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"#s","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]' % (jf, SB % 'mg.xf'),
            'title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]',
            'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1',
            'execute at @s run particle minecraft:firework ~ ~1 ~ 1 1 1 0.2 60',
            '# records : le temps est lu dans #xrt (chrono $xt ici), personnel puis serveur, selon le parcours du joueur (mg.xcr)',
            'scoreboard players operation #xrt mg.st = $xt mg.st']
    out += CC.per_course(specs, 'record')
    out += ['# premier arrivé : la course s\'arrête dans 20 s au plus, le temps que les autres terminent',
            'execute if score $xf mg.st matches 1 run scoreboard players set $xw mg.st 1',
            'execute if score $xf mg.st matches 1 run scoreboard players set $xe mg.st %d' % END_WAIT,
            'execute if score $xf mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🪽 Les autres ont 20 secondes pour terminer et se classer.","color":"gold"}]',
            '# arrivé : mis en sécurité au perchoir de départ (la zone construite s\'arrête après l\'arrivée), en spectateur',
            'execute store result storage mg:c x int 1 run scoreboard players get $px mg.st',
            'execute store result storage mg:c y int 1 run scoreboard players get $py mg.st',
            'execute store result storage mg:c z int 1 run scoreboard players get $pz mg.st',
            'function mg:core/tp_perch with storage mg:c',
            'gamemode spectator @s']
    return out


def small_lines():
    """Petites fonctions : points de reprise, anneau d'or, equipement, fin, temps ecoule, nettoyage, place."""
    return {
        'cp_reached': ['# @s = joueur qui valide un anneau qui est aussi un point de reprise',
                       'scoreboard players operation @s mg.xc = @s mg.xa',
                       'title @s actionbar [{"text":"⚑ Point de reprise enregistré","color":"green","bold":true}]',
                       'execute at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 1.5'],
        'gold_hit': ['# @s = joueur qui traverse un anneau d\'or : turbo de 3 s (gravité renforcée pendant %d ticks ; un 2e or le relance à pleine durée ;' % GL.TURBO_TICKS,
                     '# c<N>/player le termine, c<N>/respawn le coupe)',
                     XU_SET, GRAV_TURBO,
                     'execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.4',
                     'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.4 0.4 0.3 25',
                     'tellraw @s [{"text":"★ Anneau d\'or ! ","color":"gold","bold":true},{"text":"Turbo de 3 s : tu piques plus vite.","color":"gray"}]'],
        'equip': ['# @s = joueur : élytres verrouillées (pas de fusée : les anneaux d\'or donnent un turbo)',
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
                    'tag @a remove mg.xw1', 'tag @a remove mg.xtp'] + W.cleanup_lines() + [
                    'function mg:elyrace/fl_remove', 'scoreboard objectives setdisplay sidebar'],
        'place_one': ['# @s = joueur : prend la place suivante sur la plateforme de départ',
                      'scoreboard players add $ri mg.st 1', 'scoreboard players operation @s mg.ri = $ri mg.st',
                      'function mg:elyrace/place_tp'],
    }


def functions(specs):
    out = {'go': go_lines(specs), 'tick': tick_lines(specs), 'speed': speed_lines(), 'wall': wall_lines(),
           'wall_adv': wall_adv_lines(), 'finish': finish_lines(specs), 'objectives': objectives_lines(specs)}
    out.update(small_lines())
    out.update(W.functions())
    out.update(RS.functions())
    return out
