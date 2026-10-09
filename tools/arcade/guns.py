"""Armes « réelles » (pistolet, mitraillette, fusil à pompe, fusil, sniper, Ray Gun) — partagées par Zombies et Infection.

Objet : warped_fungus_on_a_stick avec custom_data {gun:N, mg_gun:1b} ; clic droit = tir (objectif mg.qs déjà existant).
Chargeur par type (mg.g1..mg.g6), rechargement auto quand vide ou en s'accroupissant (mg.gsn), recharge mg.grl/mg.grt,
cadence mg.gcd. Rayon par pas de 0,4 bloc ; cibles = entités taguées mg.gtg (zombies, joueurs infectés).
Dégâts sur les mobs : on retire directement de la vie (pas d'invulnérabilité entre deux balles), coup fatal via
`damage … by <tireur>` pour que le kill soit crédité. Sur les joueurs : `damage … by <tireur>`.
"""
import common as C

w, js = C.w, C.js
# id : nom, modèle, dégâts, cadence (ticks), chargeur, recharge (ticks), portée (blocs), plombs [(lacet, tangage)], couleur
GUNS = {
    1: ('Pistolet M1911', 'pistol', 6, 5, 8, 30, 60, [(0, 0)], 'gray'),
    2: ('Mitraillette MP5', 'smg', 4, 2, 30, 40, 50, [(0, 0)], 'aqua'),
    3: ('Fusil à pompe', 'shotgun', 5, 16, 4, 50, 16, [(0, 0), (-4, 0), (4, 0), (0, -3), (0, 3), (-3, 2), (3, -2)], 'gold'),
    4: ('Fusil M14', 'rifle', 10, 7, 10, 40, 80, [(0, 0)], 'yellow'),
    5: ('Sniper', 'sniper', 35, 30, 5, 60, 120, [(0, 0)], 'light_purple'),
    6: ('Ray Gun', 'raygun', 20, 8, 20, 50, 60, [(0, 0)], 'green'),
}
STEP = 0.4
SOUND = {1: ('entity.firework_rocket.blast', 1.6), 2: ('entity.firework_rocket.blast', 2.0), 3: ('entity.generic.explode', 1.8),
         4: ('entity.firework_rocket.large_blast', 1.4), 5: ('entity.firework_rocket.large_blast', 0.7), 6: ('block.beacon.power_select', 2.0)}


def item(n, slot_expr):
    name, model, *_, col = GUNS[n]
    nm = js([{'text': '🔫 ' + name, 'color': col, 'italic': False}])
    lore = js([{'text': 'Clic droit : tirer — accroupi : recharger', 'color': 'gray', 'italic': False}])
    base = f'minecraft:warped_fungus_on_a_stick[custom_data={{gun:{n},mg_gun:1b}},custom_name={nm},lore=[{lore}],unbreakable={{}}'
    return [f'$execute if score $rp mg.st matches 1 run item replace entity @s {slot_expr} with {base},item_model="mg:gun_{model}"]',
            f'$execute unless score $rp mg.st matches 1 run item replace entity @s {slot_expr} with {base},item_model="minecraft:crossbow"]']


def build():
    for n, (name, model, dmg, cd, mag, rl, rng, pel, col) in GUNS.items():
        # donner (macro : $(slot))
        w(f'gun/put_{n}', [f'# Donne « {name} » dans l\'emplacement $(slot), chargeur plein'] + item(n, '$(slot)') +
          [f'scoreboard players set @s mg.g{n} {mag}', f'execute if entity @s[tag=mg.gtw] run scoreboard players set @s mg.g{n} {2 * mag}'])
        # tir
        F = [f'# Tir : {name} (@s = tireur, position/rotation du tireur)',
             f'execute if score @s mg.g{n} matches ..0 run return run function mg:gun/reload_{n}',
             f'scoreboard players remove @s mg.g{n} 1', f'scoreboard players set @s mg.gcd {cd}',
             'tag @s add mg.gsh', f'scoreboard players set $gdn mg.st {n}']
        for (a, b) in pel:
            F += [f'scoreboard players set $grs mg.st {int(rng / STEP)}', 'scoreboard players set $gstop mg.st 0',
                  f'execute anchored eyes rotated ~{a} ~{b} positioned ^ ^ ^0.6 run function mg:gun/ray']
        snd, pt = SOUND[n]
        F += ['tag @s remove mg.gsh', 'tag @e[tag=mg.ghd] remove mg.ghd',
              f'playsound minecraft:{snd} player @a ~ ~ ~ {0.5 if n == 2 else 0.9} {pt}',
              'execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3' if n != 6 else
              'execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:happy_villager ~ ~ ~ 0.05 0.05 0.05 0 4',
              f'execute if score @s mg.g{n} matches 0 run function mg:gun/reload_{n}']
        w(f'gun/fire_{n}', F)
        w(f'gun/reload_{n}', [f'# Recharge {name}', f'execute if score @s mg.g{n} matches {mag}.. run return 0',
                              'execute if score @s mg.grl matches 1.. run return 0',
                              f'scoreboard players set @s mg.grl {rl}', f'execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl {rl // 2}',
                              f'scoreboard players set @s mg.grt {n}',
                              'playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2'])
    w('gun/use', ['# Clic droit avec une arme (@s, à sa position)', 'scoreboard players reset @s mg.qs',
                  'execute if score @s mg.gcd matches 1.. run return 0',
                  'execute if score @s mg.grl matches 1.. run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.8'] +
      [f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] run return run function mg:gun/fire_{n}' for n in GUNS])
    w('gun/ray', ['# Un pas de rayon (0,4 bloc)',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return run function mg:gun/impact',
                  'execute positioned ~-0.99 ~-0.99 ~-0.99 as @e[tag=mg.gtg,tag=!mg.ghd,dx=0,dy=0,dz=0] positioned ~0.99 ~0.99 ~0.99 if entity @s[dx=0,dy=0,dz=0] run tag @s add mg.ghit',
                  'execute if entity @e[tag=mg.ghit] run function mg:gun/hit_here',
                  'execute if score $gstop mg.st matches 1 run return 0',
                  'execute if score $gdn mg.st matches 6 run particle minecraft:dust{color:[0.3,1.0,0.4],scale:1.2} ~ ~ ~ 0 0 0 0 1',
                  'execute unless score $gdn mg.st matches 6 run particle minecraft:crit ~ ~ ~ 0 0 0 0 1',
                  'scoreboard players remove $grs mg.st 1',
                  f'execute if score $grs mg.st matches 1.. positioned ^ ^ ^{STEP} run function mg:gun/ray'])
    w('gun/hit_here', ['# Cible touchée à cet endroit (le sniper traverse, le Ray Gun explose)',
                       'execute as @e[tag=mg.ghit,limit=1] run function mg:gun/hit',
                       'tag @e[tag=mg.ghit] remove mg.ghit',
                       'execute if score $gdn mg.st matches 6 run function mg:gun/splash',
                       'execute unless score $gdn mg.st matches 5 run scoreboard players set $gstop mg.st 1'])
    w('gun/impact', ['# Le rayon touche un bloc', 'particle minecraft:smoke ~ ~ ~ 0.05 0.05 0.05 0.01 3',
                     'execute if score $gdn mg.st matches 6 run function mg:gun/splash'])
    w('gun/splash', ['# Ray Gun : explosion (2,5 blocs)', 'scoreboard players set $gstop mg.st 1',
                     'particle minecraft:dust{color:[0.3,1.0,0.4],scale:2.5} ~ ~ ~ 0.6 0.6 0.6 0 30',
                     'playsound minecraft:entity.generic.explode player @a ~ ~ ~ 0.5 1.8',
                     'execute as @e[tag=mg.gtg,tag=!mg.ghd,distance=..2.5] run function mg:gun/hit'])
    w('gun/hit', ['# @s = cible touchée (le tireur porte mg.gsh)', 'tag @s add mg.ghd'] +
      [f'execute if score $gdn mg.st matches {n} run scoreboard players set $gdm mg.st {g[2] * 10}' for n, g in GUNS.items()] +
      ['execute if entity @a[tag=mg.gsh,tag=mg.zdbl] run scoreboard players operation $gdm mg.st *= #2 mg.st',
       'execute if entity @s[type=minecraft:player] run function mg:gun/hit_player',
       'execute unless entity @s[type=minecraft:player] run function mg:gun/hit_mob',
       'execute if score $zpts mg.st matches 1 run scoreboard players add @a[tag=mg.gsh,limit=1] mg.zpt 10',   # Zombies (toutes les cartes) : $zpts = 1
       'particle minecraft:damage_indicator ~ ~1.2 ~ 0.2 0.3 0.2 0 2',
       'execute as @a[tag=mg.gsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player player @s ~ ~ ~ 0.5 1.6'])
    w('gun/hit_mob', ['# Mob : on retire la vie directement (pas d\'invulnérabilité), coup fatal crédité au tireur',
                      'execute store result score $gh mg.st run data get entity @s Health 10',
                      'scoreboard players operation $gh mg.st -= $gdm mg.st',
                      'execute if score $gh mg.st matches 1.. store result entity @s Health float 0.1 run scoreboard players get $gh mg.st',
                      'execute if score $gh mg.st matches 1.. at @s run playsound minecraft:entity.zombie.hurt hostile @a ~ ~ ~ 0.5 1',
                      'execute if score $gh mg.st matches ..0 run damage @s 1000 minecraft:player_attack by @a[tag=mg.gsh,limit=1]'])
    w('gun/hit_player', ['# Joueur (Infection)'] +
      [f'execute if score $gdn mg.st matches {n} run return run damage @s {g[2]} minecraft:player_attack by @a[tag=mg.gsh,limit=1]' for n, g in GUNS.items()])
    w('gun/reload_tick', ['# @s recharge', 'scoreboard players remove @s mg.grl 1',
                          'execute if score @s mg.grl matches 1.. run return 0'] +
      [l for n, g in GUNS.items() for l in (f'execute if score @s mg.grt matches {n} run scoreboard players set @s mg.g{n} {g[4]}',
                                             f'execute if entity @s[tag=mg.gtw] if score @s mg.grt matches {n} run scoreboard players set @s mg.g{n} {2 * g[4]}')] +   # Neo GTA : chargeurs doublés

      ['playsound minecraft:item.crossbow.loading_end player @s ~ ~ ~ 0.8 1.4'])
    w('gun/sneak', ['# Accroupi avec une arme en main : recharge', 'scoreboard players reset @s mg.gsn'] +
      [f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] run return run function mg:gun/reload_{n}' for n in GUNS])
    H = ['# Munitions dans la barre d\'action (@s tient une arme)']
    for n, g in GUNS.items():
        H.append(f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] unless score @s mg.grl matches 1.. run return run title @s actionbar ' +
                 js([{'text': '🔫 ' + g[0] + '  ', 'color': g[8]}, {'score': {'name': '@s', 'objective': f'mg.g{n}'}, 'color': 'white', 'bold': True},
                     {'text': f' / {g[4]}', 'color': 'gray'}]))
    H.append('execute if score @s mg.grl matches 1.. run title @s actionbar {"text":"⟳ Rechargement…","color":"yellow"}')
    w('gun/hud', H)
    w('gun/tick', ['# Armes : à appeler chaque tick par le jeu',
                   'execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:gun/use',
                   'scoreboard players reset @a[scores={mg.qs=1..}] mg.qs',
                   'scoreboard players remove @a[scores={mg.gcd=1..}] mg.gcd 1',
                   'execute as @a[scores={mg.grl=1..}] at @s run function mg:gun/reload_tick',
                   'execute as @a[tag=mg.play,scores={mg.gsn=1..}] at @s run function mg:gun/sneak',
                   'scoreboard players reset @a[scores={mg.gsn=1..}] mg.gsn',
                   'execute as @a[tag=mg.play] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/hud'])
    w('gun/reset', ['# @s : munitions et recharge remises à zéro', 'scoreboard players reset @s mg.grl', 'scoreboard players reset @s mg.grt',
                    'scoreboard players reset @s mg.gcd'] + [f'scoreboard players reset @s mg.g{n}' for n in GUNS])
    C.objectives([('mg.gcd', 'dummy'), ('mg.grl', 'dummy'), ('mg.grt', 'dummy'), ('mg.gsn', 'minecraft.custom:minecraft.sneak_time')] +
                 [(f'mg.g{n}', 'dummy') for n in GUNS])


def give(n, slot):
    """Ligne mcfunction : donne l'arme n à @s dans slot."""
    return f'function mg:gun/put_{n} {{slot:"{slot}"}}'
