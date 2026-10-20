"""TDM sniper : fonctions de combat (tick, lunette, tir, rayon, touches, frags), écrites par gen_tdm.py.

Deux équipes du cœur (mg_red / mg_blue), tous les participants (tag mg.play, mode aventure) dans une arène du duel
($tma = arène réservée, 1..3). mg.tmhp = PV (2 ; tête = 2 dégâts, corps = 1) ; mg.tmk = frags (joueur, et Rouge / Bleu pour
l'équipe) ; mg.tmcd = recharge du tir ; mg.tmx = décompte de protection (réapparition : 3 s intouchable, ne tire pas).
Tags temporaires : mg.tmsh tireur, mg.tmen équipe adverse du tireur (seule visée : le rayon traverse les coéquipiers),
mg.tmvc victime touchée, mg.tmp protégé, mg.tmsc lunette, mg.tmcr accroupi.
Sniper : clic gauche = tir, clic droit = lunette (mg.gads, boîte de clic de tools/arcade/gen_gunclick.py).
Couteau (stone_sword, clic gauche) : l'advancement mg:tdm_melee appelle tdm/melee_adv ; 1 dégât, recharge 1 s (mg.tmkc), même
filtre d'équipe adverse que le tir ; sur la boîte de clic d'un adversaire armé du sniper : tdm/box_knife (via gun/cl_foreign). Packs de soin : tdm_packs.py. La réapparition (tdm/spawn, tdm/respawn) et le kit : gen_tdm.py.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'duel'))
from duel_play import SNEAK, SCOPE, SHOT_CD

P = 'tag=mg.play,gamemode=adventure'
TEAMS = (('red', 'Rouge', 'red', 'blue'), ('blue', 'Bleu', 'blue', 'red'))     # équipe, score d'équipe, couleur, couleur adverse


def item_kill(zs):
    """Supprime les snipers au sol, dans la boîte des arènes seulement (même forme que desinstaller : pas de nbt global)."""
    z0, z1 = min(zs) - 72, max(zs) + 73
    return (f'execute as @e[type=minecraft:item,x=-22,y=60,z={z0},dx=44,dy=500,dz={z1 - z0}] '
            'if items entity @s contents *[custom_data~{mg_tm:1b}] run kill @s')


def build(w, js, zs, win, limit):
    """w(rel, lignes) écrit une fonction ; js = sérialiseur de texte JSON ; zs = z du centre des 3 arènes ; win = frags ; limit = ticks."""
    def tx(text, color='gray', **kw):
        return {'text': text, 'color': color, **kw}

    def sel(s, color='yellow', **kw):
        return {'selector': s, 'color': color, **kw}

    # ------------------------------------------------------------------ tick
    w('tdm/tick', [
        '# TDM sniper — tick (état 2)',
        'scoreboard players add $tmt mg.st 1',
        '# morts hors tir (commande, vide) : réapparition sans frag ; lunette avant les tirs',
        f'execute as @a[{P},scores={{mg.deaths=1..}}] run function mg:tdm/respawn',
        f'execute as @a[{P}] at @s run function mg:tdm/scope',
        'execute as @a[tag=mg.tmp,tag=mg.play] run function mg:tdm/prot_tick',
        f'execute as @a[{P},tag=!mg.tmp,scores={{mg.tmcd=1}}] run title @s actionbar ' + js([tx('🎯 Sniper prêt', 'aqua')]),
        f'execute as @a[{P},scores={{mg.tmcd=1}}] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 2',
        f'scoreboard players remove @a[{P},scores={{mg.tmcd=1..}}] mg.tmcd 1',
        f'scoreboard players remove @a[{P},scores={{mg.tmkc=1..}}] mg.tmkc 1',
        f'execute as @a[{P},scores={{mg.qs=1..}}] run function mg:tdm/shoot',
        '# le kit (sniper et couteau) est rendu si un effacement ou un jet l\'a retiré',
        f'execute as @a[{P}] unless items entity @s container.* minecraft:warped_fungus_on_a_stick[custom_data~{{mg_tm:1b}}] run function mg:tdm/kit',
        f'execute as @a[{P}] unless items entity @s container.* *[custom_data~{{mg_tm:1b,mg_kn:1b}}] run function mg:tdm/kit',
        '# sniper et couteau jetés ou ramassés par un autre : retirés',
        item_kill(zs),
        'clear @a[tag=!mg.play] *[custom_data~{mg_tm:1b}]',
        '# packs de soin',
        'function mg:tdm/pack_tick',
        '# hors de l\'arène (chute...) : réapparition sans frag',
    ] + [f'execute if score $tma mg.st matches {i} as @a[{P}] unless entity @s[x=-22,dx=44,y=60,dy=500,z={z - 72},dz=145] '
         'run function mg:tdm/respawn' for i, z in enumerate(zs, 1)] + [
        f'execute if score $tmt mg.st matches {limit - 1200} run tellraw @a[tag=mg.play] ' + js([tx('🎯 Plus qu\'une minute !', 'gold')]),
        f'execute if score $state mg.st matches 2 if score $tmt mg.st matches {limit}.. run function mg:tdm/timeout',
        '# équipe vide (déconnexions) : l\'autre gagne ; plus personne : égalité (seul : entraînement, pas de victoire)',
        'execute store result score $tmn mg.st if entity @a[tag=mg.play,team=mg_red]',
        'execute store result score $tmm mg.st if entity @a[tag=mg.play,team=mg_blue]',
        'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $tmn mg.st matches 0 if score $tmm mg.st matches 1.. '
        'run return run function mg:core/win_blue',
        'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $tmm mg.st matches 0 if score $tmn mg.st matches 1.. '
        'run return run function mg:core/win_red',
        'execute if score $state mg.st matches 2 if score $tmn mg.st matches 0 if score $tmm mg.st matches 0 run function mg:core/draw',
    ])

    w('tdm/prot_tick', [
        '# Réapparition protégée (@s = joueur mg.tmp ; mg.tmx = décompte en ticks)',
        'scoreboard players remove @s mg.tmx 1',
        'execute if score @s mg.tmx matches 40 run title @s actionbar ' + js([tx('2', 'yellow', bold=True)]),
        'execute if score @s mg.tmx matches 20 run title @s actionbar ' + js([tx('1', 'yellow', bold=True)]),
        'execute if score @s mg.tmx matches ..0 run title @s actionbar ' + js([tx('🎯 FEU !', 'red', bold=True)]),
        'execute if score @s mg.tmx matches ..0 at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 0.6 1.4',
        'execute if score @s mg.tmx matches ..0 run tag @s remove mg.tmp',
        'execute if score @s mg.tmx matches ..0 run scoreboard players reset @s mg.tmx',
    ])

    # ------------------------------------------------------------------ lunette
    w('tdm/scope', [
        '# Lunette (@s = joueur, position exécutée) : clic droit = zoom (lenteur) + cache, de nouveau clic droit = retirée (mg.gads, gun/cl_right)',
        '# mg.tmcr = accroupi (hauteur de tête pour le rayon : la lunette se pose debout aussi)',
        f'execute if predicate {SNEAK} run tag @s add mg.tmcr',
        f'execute unless predicate {SNEAK} run tag @s remove mg.tmcr',
        'execute if entity @s[tag=mg.gads] run return run function mg:tdm/scope_on',
        'execute if entity @s[tag=mg.tmsc] run function mg:tdm/unscope',
    ])
    w('tdm/scope_on', [
        '# Lunette en place (renouvelée à chaque tick tant que mg.gads est posé)',
        'tag @s add mg.tmsc',
        'effect give @s minecraft:slowness 1 6 true',
        'title @s times 0 5 2',
        'execute if score $rp mg.st matches 1 run title @s title ' + js({'text': SCOPE, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0}),
        'execute unless score $rp mg.st matches 1 run title @s title ' + js(tx('+', 'white')),
    ])
    w('tdm/unscope', [
        '# Fin de lunette (@s = joueur)',
        'tag @s remove mg.tmsc',
        'effect clear @s minecraft:slowness',
        'title @s clear',
    ])

    # ------------------------------------------------------------------ tir
    w('tdm/shoot', [
        '# Tir du sniper (@s = joueur qui a fait un clic gauche, gun/cl_left) : rayon de 150 blocs, recharge 2 s',
        'scoreboard players reset @s mg.qs',
        '# le sniper en main droite seulement (le couteau porte aussi mg_tm ; un clic droit vanilla avec lui ne doit pas tirer)',
        'execute unless items entity @s weapon.mainhand minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run return 0',
        'execute if entity @s[tag=mg.tmp] run return 0',
        'execute if score @s mg.tmcd matches 1.. run return 0',
        f'scoreboard players set @s mg.tmcd {SHOT_CD}',
        'tag @s add mg.tmsh',
        '# le rayon ne vise que l\'équipe adverse : il traverse les coéquipiers (pas de tir ami)',
        f'execute if entity @s[team=mg_red] run tag @a[{P},team=mg_blue] add mg.tmen',
        f'execute if entity @s[team=mg_blue] run tag @a[{P},team=mg_red] add mg.tmen',
        'scoreboard players set $rs mg.st 300',
        'execute at @s run playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 1 1.8',
        '# marqueur de fin de rayon : mg.tmend (propre au TDM) + mg.rend (le repère de core/shot_trail)',
        'execute at @s anchored eyes run summon minecraft:marker ^ ^ ^0.5 {Tags:["mg.tmend","mg.rend"]}',
        'execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:tdm/ray',
        '# traînée : part de l\'arme et rejoint le point d\'impact',
        'scoreboard players set $trp mg.st 0',
        'scoreboard players set $trs mg.st 320',
        'execute at @s anchored eyes positioned ^-0.3 ^-0.2 ^0.7 facing entity @e[type=minecraft:marker,tag=mg.tmend,limit=1] feet run function mg:core/shot_trail',
        'kill @e[type=minecraft:marker,tag=mg.tmend]',
        '# frag APRÈS la traînée (la réapparition déplacerait la victime)',
        'execute as @a[tag=mg.tmvc,scores={mg.tmhp=..0}] run function mg:tdm/frag',
        'tag @a remove mg.tmvc',
        'tag @a remove mg.tmen',
        'tag @s remove mg.tmsh',
    ])

    base = 'tag=mg.tmen,tag=!mg.tmp'
    chk = 'limit=1,sort=nearest] run return run function mg:tdm/'
    w('tdm/ray', [
        '# Un pas du rayon (0,5 bloc) : bloc plein = fin ; adversaire touché = tête puis corps ; air = on avance',
        'execute unless loaded ~ ~ ~ run return 0',
        'tp @e[type=minecraft:marker,tag=mg.tmend,distance=..1,limit=1] ~ ~ ~',
        'execute unless block ~ ~ ~ #mg:ray_pass run return run particle minecraft:electric_spark ~ ~ ~ 0.1 0.1 0.1 0.1 4',
        '# tête : 0,4 autour des yeux (1,62 debout, 1,27 accroupi : mg.tmcr), testée AVANT le corps',
        f'execute positioned ~ ~-1.62 ~ as @a[{base},tag=!mg.tmcr,distance=..0.4,{chk}hit_head',
        f'execute positioned ~ ~-1.27 ~ as @a[{base},tag=mg.tmcr,distance=..0.4,{chk}hit_head',
        '# corps (zone resserrée sous la tête : un tir à la tête ne devient pas un tir au corps)',
        f'execute positioned ~ ~-0.7 ~ as @a[{base},tag=!mg.tmcr,distance=..0.8,{chk}hit_body',
        f'execute positioned ~ ~-0.5 ~ as @a[{base},tag=mg.tmcr,distance=..0.75,{chk}hit_body',
        'scoreboard players remove $rs mg.st 1',
        'execute if score $rs mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:tdm/ray',
    ])

    w('tdm/hit_head', [
        '# Tir à la tête (@s = victime) : 2 dégâts = frag',
        'scoreboard players set $tmd mg.st 2',
        'function mg:tdm/hit',
    ])
    w('tdm/hit_body', [
        '# Tir au corps (@s = victime) : 1 dégât (2 touches pour un frag)',
        'scoreboard players set $tmd mg.st 1',
        'function mg:tdm/hit',
    ])
    w('tdm/hit', [
        '# Adversaire touché (@s = victime ; le tireur porte mg.tmsh ; $tmd = dégâts). Le frag est traité par tdm/shoot',
        'scoreboard players operation @s mg.tmhp -= $tmd mg.st',
        'tag @s add mg.tmvc',
        'execute at @s run particle minecraft:crit ~ ~1.2 ~ 0.3 0.4 0.3 0.2 25',
        'execute at @s run playsound minecraft:entity.player.hurt master @a ~ ~ ~ 1 1',
        'execute as @a[tag=mg.tmsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1.5',
        'execute if score $tmd mg.st matches 2.. as @a[tag=mg.tmsh,limit=1] run title @s actionbar ' + js([tx('🎯 TÊTE !', 'gold', bold=True)]),
        'execute if score $tmd mg.st matches ..1 if score @s mg.tmhp matches 1.. as @a[tag=mg.tmsh,limit=1] run title @s actionbar '
        + js([tx('🎯 Touché au corps : encore une touche !', 'aqua')]),
        'execute if score $tmd mg.st matches ..1 if score @s mg.tmhp matches 1.. run title @s actionbar '
        + js([tx('💥 Touché ! Encore une touche et tu perds une vie.', 'red')]),
    ])

    # ------------------------------------------------------------------ couteau (clic gauche)
    w('tdm/melee_adv', [
        '# Récompense de mg:tdm_melee (@s = attaquant) : coup de couteau = 1 dégât à l\'équipe adverse (partie TDM en cours seulement)',
        'advancement revoke @s only mg:tdm_melee',
        'execute unless score $game mg.st matches 246 run return 0',
        'execute unless score $state mg.st matches 2 run return 0',
        'execute unless entity @s[tag=mg.play,tag=!mg.tmp] run return 0',
        'execute unless items entity @s weapon.mainhand *[custom_data~{mg_kn:1b}] run return 0',
        'execute if score @s mg.tmkc matches 1.. run return 0',
        '# recharge posée AVANT le coup (un coup balayé déclenche l\'advancement plusieurs fois dans le même tick)',
        'scoreboard players set @s mg.tmkc 20',
        'tag @s add mg.tmsh',
        f'execute if entity @s[team=mg_red] run tag @a[{P},team=mg_blue] add mg.tmen',
        f'execute if entity @s[team=mg_blue] run tag @a[{P},team=mg_red] add mg.tmen',
        '# victime = adversaire non protégé touché ce tick ET dont le dernier attaquant est @s (pas un autre adversaire à portée)',
        'execute as @a[tag=mg.tmen,tag=!mg.tmp,distance=..5] if data entity @s {HurtTime:10s} if function mg:tdm/melee_att run tag @s add mg.tmvc',
        'execute as @p[tag=mg.tmvc] run function mg:tdm/melee_hit',
        'tag @a remove mg.tmvc',
        'tag @a remove mg.tmen',
        'tag @s remove mg.tmsh',
    ])
    w('tdm/melee_att', [
        '# (@s = victime, appelée par `if function`) : 1 si son dernier attaquant est le porteur de mg.tmsh, sinon 0',
        'execute on attacker if entity @s[tag=mg.tmsh] run return 1',
        'return 0',
    ])
    w('tdm/melee_hit', [
        '# Coup de couteau (@s = victime ; l\'attaquant porte mg.tmsh) : 1 dégât, frag si les PV sont épuisés',
        'scoreboard players set $tmd mg.st 1',
        'function mg:tdm/hit',
        'execute if score @s mg.tmhp matches ..0 run function mg:tdm/frag',
    ])
    w('tdm/box_knife', [
        '# Coup de couteau sur la boîte de clic d\'un adversaire (gun/cl_foreign : @s = attaquant, victime = @a[tag=mg.gcme]) :',
        '# la boîte de 2,6 blocs autour de ses yeux intercepte le coup, mg:tdm_melee ne se déclenche donc pas ; mêmes règles que melee_adv',
        'execute unless score $game mg.st matches 246 run return 0',
        'execute unless score $state mg.st matches 2 run return 0',
        'execute unless entity @s[tag=mg.play,tag=!mg.tmp] run return 0',
        'execute unless items entity @s weapon.mainhand *[custom_data~{mg_kn:1b}] run return 0',
        'execute if score @s mg.tmkc matches 1.. run return 0',
        f'execute if entity @s[team=mg_red] run tag @a[{P},team=mg_blue] add mg.tmen',
        f'execute if entity @s[team=mg_blue] run tag @a[{P},team=mg_red] add mg.tmen',
        '# victime = adversaire non protégé propriétaire de la boîte frappée, à portée du couteau (pas de coup ami)',
        'execute at @s as @a[tag=mg.gcme,tag=mg.tmen,tag=!mg.tmp,distance=..4.5] run tag @s add mg.tmvc',
        'execute unless entity @a[tag=mg.tmvc] run return run tag @a remove mg.tmen',
        '# recharge posée AVANT le coup (comme melee_adv), puis le coup existant (melee_hit)',
        'scoreboard players set @s mg.tmkc 20',
        'tag @s add mg.tmsh',
        'execute as @a[tag=mg.tmvc,limit=1] run function mg:tdm/melee_hit',
        'tag @a remove mg.tmvc',
        'tag @a remove mg.tmen',
        'tag @s remove mg.tmsh',
    ])

    # ------------------------------------------------------------------ frags
    frag = ['# Frag (@s = victime, PV épuisés ; le tireur porte mg.tmsh ; $tmd = dégâts du dernier tir) : +1 au tireur et à son équipe, '
            'kill-feed, réapparition immédiate',
            'scoreboard players add @a[tag=mg.tmsh,limit=1] mg.tmk 1']
    for t, nm, col, ocol in TEAMS:
        frag.append(f'execute if entity @a[tag=mg.tmsh,team=mg_{t}] run scoreboard players add {nm} mg.tmk 1')
    for t, nm, col, ocol in TEAMS:
        for cond, suffix in (('2..', ' (tête)'), ('..1', '')):
            frag.append(f'execute if entity @a[tag=mg.tmsh,team=mg_{t}] if score $tmd mg.st matches {cond} run tellraw @a[tag=mg.play] '
                        + js([sel('@a[tag=mg.tmsh,limit=1]', col), tx(' 🎯 ', 'gold'), sel('@s', ocol), tx(suffix, 'gray')]))
    frag += ['execute as @a[tag=mg.tmsh,limit=1] run title @s actionbar ' + js([tx('🎯 Frag ! ', 'green', bold=True),
                                                                                  {'score': {'name': '@s', 'objective': 'mg.tmk'}, 'color': 'gold'}]),
             'execute as @a[tag=mg.tmsh,limit=1] at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2',
             'execute at @s run particle minecraft:firework ~ ~1 ~ 0.3 0.5 0.3 0.15 40',
             'function mg:tdm/spawn']
    for t, nm, col, ocol in TEAMS:
        frag.append(f'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score {nm} mg.tmk matches {win}.. '
                    f'run function mg:core/win_{t}')
    w('tdm/frag', frag)
