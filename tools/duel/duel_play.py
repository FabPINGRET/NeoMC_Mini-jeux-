"""Duel sniper : fonctions de combat (tick, lunette, tir, rayon, touches, manches), écrites par gen_duel.py.

Un duel = 2 joueurs (tag mg.dl, mg.dli = instance 1..3 = arène) ; mg.dla marque le défieur (départ nord) ;
mg.dlhp = PV de la manche (2 ; tête = 2 dégâts, corps = 1) ; mg.dlr = manches gagnées (3 pour gagner).
Tags temporaires : mg.dlsh tireur, mg.dlvc victime touchée, mg.dlwn gagnant, mg.dlsp joueurs de l'instance en cours,
mg.dlp manche en préparation (3 s : intouchable, ne tire pas ; mg.dlx sert alors de décompte), mg.dlsc lunette.
"""

SNEAK = '{condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}}'
SCOPE = chr(0xE222)      # cache de lunette du resource pack (font mg:gta, comme le sniper de Neo City)


def sniper_kill(zs):
    """Supprime les snipers au sol, dans la boîte des arènes seulement (même forme que desinstaller : pas de nbt global)."""
    z0, z1 = min(zs) - 72, max(zs) + 73
    return (f'execute as @e[type=minecraft:item,x=-22,y=60,z={z0},dx=44,dy=500,dz={z1 - z0}] '
            'if items entity @s contents *[custom_data~{mg_dl:1b}] run kill @s')


def build(w, js, zs):
    """w(rel, lignes) écrit une fonction ; js = sérialiseur de texte JSON ; zs = z du centre des 3 arènes."""
    def tx(text, color='gray', **kw):
        return {'text': text, 'color': color, **kw}

    def sel(s, color='yellow', **kw):
        return {'selector': s, 'color': color, **kw}

    def sc(name, color='gold'):
        return {'score': {'name': name, 'objective': 'mg.dlr'}, 'color': color}

    # ------------------------------------------------------------------ tick
    w('duel/tick', [
        '# Duel sniper — tick (core/tick : au moins un duelliste, ou une invitation en attente)',
        '# invitations : décompte, expiration (30 s), invitation orpheline (défieur parti)',
        'scoreboard players remove @a[scores={mg.dlto=1..,mg.dlx=1..},tag=!mg.dl] mg.dlx 1',
        'execute as @a[scores={mg.dlto=1..,mg.dlx=0},tag=!mg.dl] run function mg:duel/expire',
        'execute as @a[tag=mg.dlrq] run function mg:duel/rq_check',
        '# duellistes : la pause reste posée (une partie lancée ne les prend pas), lunette avant les tirs',
        'tag @a[tag=mg.dl] add mg.spectate',
        'execute as @a[tag=mg.dl] at @s run function mg:duel/scope',
        'execute as @a[tag=mg.dlp] run function mg:duel/prot_tick',
        'execute as @a[tag=mg.dl,scores={mg.dlcd=1}] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 2',
        'execute as @a[tag=mg.dl,tag=!mg.dlp,scores={mg.dlcd=1}] run title @s actionbar ' + js([tx('🎯 Sniper prêt', 'aqua')]),
        'scoreboard players remove @a[tag=mg.dl,scores={mg.dlcd=1..}] mg.dlcd 1',
        'execute as @a[tag=mg.dl,scores={mg.qs=1..}] run function mg:duel/shoot',
        '# le kit est rendu si un effacement (lancement de partie) l\'a retiré',
        'execute as @a[tag=mg.dl] unless items entity @s container.* *[custom_data~{mg_dl:1b}] run function mg:duel/kit',
        '# snipers jetés ou ramassés par un autre : retirés',
        sniper_kill(zs),
        'clear @a[tag=!mg.dl] minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}]',
        '# hors de l\'arène (chute, mort et réapparition au lobby...) : forfait ; puis adversaire parti',
    ] + [f'execute as @a[tag=mg.dl,scores={{mg.dli={i}}}] unless entity @s[x=-22,dx=44,y=60,dy=500,z={z - 72},dz=145] run function mg:duel/forfeit'
         for i, z in enumerate(zs, 1)]
      + [f'execute if entity @a[tag=mg.dl,scores={{mg.dli={i}}}] run function mg:duel/inst {{i:{i}}}' for i in (1, 2, 3)])

    w('duel/inst', [
        '# Duel sniper — arène $(i) (macro) : un seul duelliste restant = victoire par forfait',
        '$execute store result score #dln mg.st if entity @a[tag=mg.dl,scores={mg.dli=$(i)}]',
        '$execute if score #dln mg.st matches 1 as @a[tag=mg.dl,scores={mg.dli=$(i)}] run function mg:duel/left',
    ])

    w('duel/prot_tick', [
        '# Manche en préparation (@s = duelliste mg.dlp ; mg.dlx = décompte en ticks)',
        'scoreboard players remove @s mg.dlx 1',
        'execute if score @s mg.dlx matches 40 run title @s actionbar ' + js([tx('2', 'yellow', bold=True)]),
        'execute if score @s mg.dlx matches 20 run title @s actionbar ' + js([tx('1', 'yellow', bold=True)]),
        'execute if score @s mg.dlx matches ..0 run title @s actionbar ' + js([tx('⚔ FEU !', 'red', bold=True)]),
        'execute if score @s mg.dlx matches ..0 at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 0.6 1.4',
        'execute if score @s mg.dlx matches ..0 run tag @s remove mg.dlp',
        'execute if score @s mg.dlx matches ..0 run scoreboard players reset @s mg.dlx',
    ])

    # ------------------------------------------------------------------ lunette
    w('duel/scope', [
        '# Lunette (@s = duelliste, position exécutée) : accroupi = zoom (lenteur) + cache ; se relever la retire',
        f'execute if predicate {SNEAK} run return run function mg:duel/scope_on',
        'execute if entity @s[tag=mg.dlsc] run function mg:duel/unscope',
    ])
    w('duel/scope_on', [
        '# Lunette en place (renouvelée à chaque tick tant qu\'il reste accroupi)',
        'tag @s add mg.dlsc',
        'effect give @s minecraft:slowness 1 6 true',
        'title @s times 0 5 2',
        'execute if score $rp mg.st matches 1 run title @s title ' + js({'text': SCOPE, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0}),
        'execute unless score $rp mg.st matches 1 run title @s title ' + js(tx('+', 'white')),
    ])
    w('duel/unscope', [
        '# Fin de lunette (@s = duelliste)',
        'tag @s remove mg.dlsc',
        'effect clear @s minecraft:slowness',
        'title @s clear',
    ])

    # ------------------------------------------------------------------ tir
    w('duel/shoot', [
        '# Tir du sniper (@s = duelliste qui a fait un clic droit) : rayon de 150 blocs, recharge 2 s',
        'scoreboard players reset @s mg.qs',
        'execute unless items entity @s weapon.* *[custom_data~{mg_dl:1b}] run return 0',
        'execute if entity @s[tag=mg.dlp] run return 0',
        'execute if score @s mg.dlcd matches 1.. run return 0',
        'scoreboard players set @s mg.dlcd 40',
        'tag @s add mg.dlsh',
        '# le rayon ne touche que l\'adversaire de la même arène (mg.dli)',
        'scoreboard players operation $dli mg.st = @s mg.dli',
        'scoreboard players set $rs mg.st 300',
        'execute at @s run playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 1 1.8',
        '# marqueur de fin de rayon : mg.dlend (propre au duel) + mg.rend (le repère de core/shot_trail)',
        'execute at @s anchored eyes run summon minecraft:marker ^ ^ ^0.5 {Tags:["mg.dlend","mg.rend"]}',
        'execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:duel/ray',
        '# traînée : part de l\'arme et rejoint le point d\'impact',
        'scoreboard players set $trp mg.st 0',
        'scoreboard players set $trs mg.st 320',
        'execute at @s anchored eyes positioned ^-0.3 ^-0.2 ^0.7 facing entity @e[type=minecraft:marker,tag=mg.dlend,limit=1] feet run function mg:core/shot_trail',
        'kill @e[type=minecraft:marker,tag=mg.dlend]',
        '# fin de manche APRÈS la traînée (le retour au départ déplacerait le tireur)',
        'execute as @a[tag=mg.dlvc,scores={mg.dlhp=..0}] run function mg:duel/round',
        'tag @a remove mg.dlvc',
        'tag @s remove mg.dlsh',
    ])

    base = 'tag=mg.dl,tag=!mg.dlsh,tag=!mg.dlp'
    chk = 'limit=1,sort=nearest] if score @s mg.dli = $dli mg.st run return run function mg:duel/'
    w('duel/ray', [
        '# Un pas du rayon (0,5 bloc) : bloc plein = fin ; joueur touché = tête puis corps ; air = on avance',
        'execute unless loaded ~ ~ ~ run return 0',
        'tp @e[type=minecraft:marker,tag=mg.dlend,distance=..1,limit=1] ~ ~ ~',
        'execute unless block ~ ~ ~ #mg:ray_pass run return run particle minecraft:electric_spark ~ ~ ~ 0.1 0.1 0.1 0.1 4',
        '# tête : 0,4 autour des yeux (1,62 debout, 1,27 accroupi), testée AVANT le corps',
        f'execute positioned ~ ~-1.62 ~ as @a[{base},tag=!mg.dlsc,distance=..0.4,{chk}hit_head',
        f'execute positioned ~ ~-1.27 ~ as @a[{base},tag=mg.dlsc,distance=..0.4,{chk}hit_head',
        '# corps (zone resserrée sous la tête : un tir à la tête ne devient pas un tir au corps)',
        f'execute positioned ~ ~-0.7 ~ as @a[{base},tag=!mg.dlsc,distance=..0.8,{chk}hit_body',
        f'execute positioned ~ ~-0.5 ~ as @a[{base},tag=mg.dlsc,distance=..0.75,{chk}hit_body',
        'scoreboard players remove $rs mg.st 1',
        'execute if score $rs mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:duel/ray',
    ])

    w('duel/hit_head', [
        '# Tir à la tête (@s = victime) : 2 dégâts = manche perdue',
        'scoreboard players set $dld mg.st 2',
        'function mg:duel/hit',
    ])
    w('duel/hit_body', [
        '# Tir au corps (@s = victime) : 1 dégât (2 touches pour éliminer)',
        'scoreboard players set $dld mg.st 1',
        'function mg:duel/hit',
    ])
    w('duel/hit', [
        '# Joueur touché (@s = victime ; le tireur porte mg.dlsh ; $dld = dégâts). La fin de manche est traitée par duel/shoot',
        'scoreboard players operation @s mg.dlhp -= $dld mg.st',
        'tag @s add mg.dlvc',
        'execute at @s run particle minecraft:crit ~ ~1.2 ~ 0.3 0.4 0.3 0.2 25',
        'execute at @s run playsound minecraft:entity.player.hurt master @a ~ ~ ~ 1 1',
        'execute as @a[tag=mg.dlsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1.5',
        'execute if score $dld mg.st matches 2.. as @a[tag=mg.dlsh,limit=1] run title @s actionbar ' + js([tx('🎯 TÊTE !', 'gold', bold=True)]),
        'execute if score $dld mg.st matches ..1 if score @s mg.dlhp matches 1.. as @a[tag=mg.dlsh,limit=1] run title @s actionbar '
        + js([tx('🎯 Touché au corps : encore une touche !', 'aqua')]),
        'execute if score $dld mg.st matches ..1 if score @s mg.dlhp matches 1.. run title @s actionbar '
        + js([tx('💥 Touché ! Encore une touche et tu perds la manche.', 'red')]),
    ])

    # ------------------------------------------------------------------ manches
    w('duel/round', [
        '# Manche perdue (@s = victime ; le tireur porte mg.dlsh) : +1 manche au tireur, match fini à 3',
        'scoreboard players operation $dli mg.st = @s mg.dli',
        'tag @a[tag=mg.dlsh,limit=1] add mg.dlwn',
        'scoreboard players add @a[tag=mg.dlsh,limit=1] mg.dlr 1',
        'execute as @a[tag=mg.dl] if score @s mg.dli = $dli mg.st run tag @s add mg.dlsp',
        'execute if entity @a[tag=mg.dlwn,scores={mg.dlr=3..}] run return run function mg:duel/win',
        'execute at @s run particle minecraft:firework ~ ~1 ~ 0.3 0.5 0.3 0.15 40',
        'tellraw @a[tag=mg.dlsp] ' + js([tx('⚔ Manche pour ', 'gold'), sel('@a[tag=mg.dlwn,limit=1]'), tx(' : ', 'gray'),
                                         sc('@a[tag=mg.dlwn,limit=1]'), tx(' - ', 'gray'), sc('@s', 'red')]),
        'tag @a remove mg.dlwn',
        'function mg:duel/next',
    ])
    w('duel/win', [
        '# Match gagné (3 manches) : le gagnant porte mg.dlwn, $dli = arène',
        'tellraw @a ' + js([tx('⚔ ', 'gold'), sel('@a[tag=mg.dlwn,limit=1]', bold=True), tx(' bat ', 'gray'),
                            sel('@a[tag=mg.dlsp,tag=!mg.dlwn,limit=1]', 'red'), tx(' en duel sniper : ', 'gray'),
                            sc('@a[tag=mg.dlwn,limit=1]'), tx(' - ', 'gray'), sc('@a[tag=mg.dlsp,tag=!mg.dlwn,limit=1]', 'red')]),
        'function mg:duel/end',
    ])
    w('duel/end', [
        '# Fin de duel de l\'arène $dli (le gagnant porte mg.dlwn) : +1 victoire, retour au lobby des deux joueurs',
        'execute as @a[tag=mg.dl] if score @s mg.dli = $dli mg.st run tag @s add mg.dlsp',
        'scoreboard players add @a[tag=mg.dlwn,limit=1] mg.dlw 1',
        'tellraw @a[tag=mg.dlwn,limit=1] ' + js([tx('⚔ Victoire ! Duels gagnés : ', 'green'),
                                               {'score': {'name': '@s', 'objective': 'mg.dlw'}, 'color': 'gold'}]),
        'execute as @a[tag=mg.dlwn,limit=1] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2',
        'execute as @a[tag=mg.dlsp] run function mg:duel/stop',
        'tag @a remove mg.dlwn',
    ])
    w('duel/left', [
        '# L\'adversaire est parti (@s = le joueur resté) : victoire par forfait',
        'scoreboard players operation $dli mg.st = @s mg.dli',
        'tellraw @s ' + js([tx('⚔ Ton adversaire a quitté le duel : victoire par forfait.', 'green')]),
        'tag @s add mg.dlwn',
        'function mg:duel/end',
    ])
    w('duel/forfeit', [
        '# Abandon ou chute hors de l\'arène (@s = le perdant) : l\'adversaire gagne',
        '# (déjà sorti du duel par un forfait plus tôt dans le même tick : rien)',
        'execute unless entity @s[tag=mg.dl] run return 0',
        'scoreboard players operation $dli mg.st = @s mg.dli',
        'tag @s add mg.dlfl',
        'execute as @a[tag=mg.dl,tag=!mg.dlfl] if score @s mg.dli = $dli mg.st run tag @s add mg.dlwn',
        'tellraw @a[tag=mg.dlwn] ' + js([sel('@s', 'red'), tx(' abandonne le duel : victoire par forfait.', 'green')]),
        'tellraw @s ' + js([tx('⚔ Tu perds le duel par forfait.', 'gray')]),
        'tag @s remove mg.dlfl',
        'function mg:duel/end',
    ])
