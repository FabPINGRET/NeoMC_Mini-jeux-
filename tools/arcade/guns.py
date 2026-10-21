"""Armes « réelles » (pistolet, mitraillette, fusil à pompe, fusil, sniper, Ray Gun) — partagées par Zombies et Infection.

Objet : warped_fungus_on_a_stick avec custom_data {gun:N, mg_gun:1b} ; clic droit = tir (objectif mg.qs déjà existant).
Chargeur par type (mg.g1..mg.g6), rechargement auto quand vide ou en s'accroupissant (mg.gsn), recharge mg.grl/mg.grt,
cadence mg.gcd. Rayon par pas de 0,4 bloc ; cibles = entités taguées mg.gtg (zombies, joueurs infectés).
Dégâts sur les mobs : on retire directement de la vie (pas d'invulnérabilité entre deux balles), coup fatal via
`damage … by <tireur>` pour que le kill soit crédité. Sur les joueurs : `damage … by <tireur>`.
Overlay de recharge dans la hotbar : composant use_cooldown (groupes mg:gun<n>) posé avant le clic qui vide le chargeur, variante
marquée par custom_data gcr (voir gun/cd_*) ; cadence du Sniper aussi. Limites : recharge par accroupi / Q sans overlay ;
fenêtre d'1 tick après un achat (Speed Cola, munitions : zm/tick passe après gun/tick), où l'overlay peut être celui de l'état précédent.
Lobby et Neo GTA : pas d'use_cooldown (tir au clic gauche, gcd partagé) mais une barre de durabilité (gun/bar, appelée par lobby/guns_tick
et gta/tick) : recharge de l'arme en main et cadence du Sniper seule ; en Neo GTA, gcd étant partagé, un Sniper en main montre aussi (sur 30 ticks) le gcd laissé par une autre arme ou le bazooka.
Une arme qui n'est plus l'objet en main (autre case, main gauche) est remise à zéro par gun/bar_clear (hotbar.0..8 et main gauche, garde unbreakable).
Limite : une arme jetée (Q) pendant la recharge n'est plus dans l'inventaire et garde sa barre au sol.
La barre change le damage de l'objet à chaque tick : les définitions mg/items/gun_*.json portent hand_animation_on_swap:false (sinon l'animation de
changement d'objet se rejouerait) ; le repli minecraft:crossbow ($rp ≠ 1, sans pack) n'a pas ce réglage et continue de s'animer.
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
    7: ('Mitrailleuse RPK', 'rifle', 6, 2, 60, 80, 60, [(0, 0)], 'red'),
    8: ('Revolver Python', 'pistol', 14, 10, 6, 40, 60, [(0, 0)], 'dark_aqua'),
}
STEP = 0.4
SOUND = {1: ('entity.firework_rocket.blast', 1.6), 2: ('entity.firework_rocket.blast', 2.0), 3: ('entity.generic.explode', 1.8),
         4: ('entity.firework_rocket.large_blast', 1.4), 5: ('entity.firework_rocket.large_blast', 0.7), 6: ('block.beacon.power_select', 2.0),
         7: ('entity.firework_rocket.blast', 1.2), 8: ('entity.firework_rocket.large_blast', 1.0)}
# Zombies : arme améliorée (Pack-a-Punch, custom_data pap:1b) = dégâts ×3, chargeur ×2 ; fusil à pompe à bout portant (5 blocs) = dégâts ×4


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
             f'execute unless score @s mg.g{n} = @s mg.g{n} run scoreboard players set @s mg.g{n} {mag}',   # arme ramassée au sol
             f'execute if score @s mg.g{n} matches ..0 run return run function mg:gun/reload_{n}',
             f'scoreboard players remove @s mg.g{n} 1', f'scoreboard players set @s mg.gcd {cd}',
             f'execute if entity @s[tag=mg.zdbl] run scoreboard players set @s mg.gcd {max(1, cd * 2 // 3)}',
             'execute if items entity @s weapon.mainhand *[custom_data~{pap:1b}] run tag @s add mg.gpap',
             'tag @s add mg.gsh', f'scoreboard players set $gdn mg.st {n}']
        for (a, b) in pel:
            F += [f'scoreboard players set $grs mg.st {int(rng / STEP)}', 'scoreboard players set $gstop mg.st 0',
                  f'execute anchored eyes rotated ~{a} ~{b} positioned ^ ^ ^0.6 run function mg:gun/ray']
        snd, pt = SOUND[n]
        F += ['tag @s remove mg.gsh', 'tag @s remove mg.gpap', 'tag @e[tag=mg.ghd] remove mg.ghd',
              f'playsound minecraft:{snd} player @a ~ ~ ~ {0.5 if n == 2 else 0.9} {pt}',
              'execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3' if n != 6 else
              'execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:happy_villager ~ ~ ~ 0.05 0.05 0.05 0 4',
              f'execute if score @s mg.g{n} matches 0 run function mg:gun/reload_{n}']
        w(f'gun/fire_{n}', F)
        w(f'gun/reload_{n}', [f'# Recharge {name}', f'execute if score @s mg.g{n} matches {2 * mag}.. run return 0',
                              f'execute if score @s mg.g{n} matches {mag}.. unless items entity @s container.* *[custom_data~{{gun:{n},pap:1b}}] unless entity @s[tag=mg.gtw] run return 0',
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
      ['# Modes zombies (Zombies, Infection) : dégâts doublés ; Neo GTA (tireur mg.gtw) : dégâts normaux',
       'scoreboard players set #2 mg.st 2',
       'execute unless entity @a[tag=mg.gsh,tag=mg.gtw] run scoreboard players operation $gdm mg.st *= #2 mg.st',
       'execute if entity @a[tag=mg.gsh,tag=mg.zdbl] run scoreboard players operation $gdm mg.st *= #2 mg.st',
       'scoreboard players set #3 mg.st 3', 'scoreboard players set #4 mg.st 4',
       'execute if entity @a[tag=mg.gsh,tag=mg.gpap] run scoreboard players operation $gdm mg.st *= #3 mg.st',
       f'execute if score $gdn mg.st matches 3 if score $grs mg.st matches {int(16 / STEP) - int(5 / STEP)}.. unless entity @a[tag=mg.gsh,tag=mg.gtw] run scoreboard players operation $gdm mg.st *= #4 mg.st',
       'execute if entity @s[type=minecraft:player] run function mg:gun/hit_player',
       'execute unless entity @s[type=minecraft:player] run function mg:gun/hit_mob',
       'execute if score $zpts mg.st matches 1 run scoreboard players add @a[tag=mg.gsh,limit=1] mg.zpt 10',   # Zombies (toutes les cartes) : $zpts = 1
       'execute if score $zpts mg.st matches 1 if score $zdp mg.st matches 1.. run scoreboard players add @a[tag=mg.gsh,limit=1] mg.zpt 10',   # points doubles
       'particle minecraft:damage_indicator ~ ~1.2 ~ 0.2 0.3 0.2 0 2',
       'execute as @a[tag=mg.gsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player player @s ~ ~ ~ 0.5 1.6'])
    w('gun/hit_mob', ['# Mob : on retire la vie directement (pas d\'invulnérabilité), coup fatal crédité au tireur ; Zombies : mort instantanée, bonus lâché au hasard',
                      'execute if score $zpts mg.st matches 1 if score $zik mg.st matches 1.. run scoreboard players set $gdm mg.st 1000000',
                      'execute store result score $gh mg.st run data get entity @s Health 10',
                      'scoreboard players operation $gh mg.st -= $gdm mg.st',
                      'execute if score $gh mg.st matches 1.. store result entity @s Health float 0.1 run scoreboard players get $gh mg.st',
                      'execute if score $gh mg.st matches 1.. at @s run playsound minecraft:entity.zombie.hurt hostile @a ~ ~ ~ 0.5 1',
                      'execute if score $gh mg.st matches ..0 if score $zpts mg.st matches 1 if entity @s[tag=mg.zz] at @s run function mg:zx/drop_roll',
                      'execute if score $gh mg.st matches ..0 run damage @s 1000 minecraft:player_attack by @a[tag=mg.gsh,limit=1]'])
    w('gun/hit_player', ['# Joueur : Infection (zombie touché) = dégâts doublés ; Neo GTA (tireur mg.gtw) = dégâts normaux ; lobby (tireur mg.lsh) = un demi-cœur',
                         'execute if entity @a[tag=mg.gsh,tag=mg.lsh] run return run damage @s 1 minecraft:player_attack by @a[tag=mg.gsh,limit=1]'] +
      [f'execute if entity @a[tag=mg.gsh,tag=mg.gtw] if score $gdn mg.st matches {n} run return run damage @s {g[2]} minecraft:player_attack by @a[tag=mg.gsh,limit=1]' for n, g in GUNS.items()] +
      [f'execute if score $gdn mg.st matches {n} run return run damage @s {2 * g[2]} minecraft:player_attack by @a[tag=mg.gsh,limit=1]' for n, g in GUNS.items()])
    w('gun/reload_tick', ['# @s recharge', 'scoreboard players remove @s mg.grl 1',
                          'execute if score @s mg.grl matches 1.. run return 0'] +
      [l for n, g in GUNS.items() for l in (f'execute if score @s mg.grt matches {n} run scoreboard players set @s mg.g{n} {g[4]}',
                                             f'execute if entity @s[tag=mg.gtw] if score @s mg.grt matches {n} run scoreboard players set @s mg.g{n} {2 * g[4]}',
                                             f'execute if score @s mg.grt matches {n} if items entity @s container.* *[custom_data~{{gun:{n},pap:1b}}] run scoreboard players set @s mg.g{n} {2 * g[4]}')] +   # Neo GTA, arme améliorée : chargeurs doublés

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
    # Overlay de recharge (hotbar) : le composant use_cooldown ne s'applique qu'au clic, donc il est posé AVANT le clic qui vide
    # le chargeur (variante « dernière balle », gcr 1b / 2b Speed Cola) puis ramené à 0,05 s pendant la recharge (gcr 0b).
    # Le groupe mg:gun<n> ne change jamais entre variantes. Sniper (SNP) : variante normale = cadence (gcr 0b, 3b Double Tap) ;
    # gcr 4b = Sniper neutralisé (0,05 s) pendant une recharge sans overlay (accroupi, Q, autre arme) : un clic refusé ne verrouille rien.
    SNP = 5
    w('gun/cd_set', ['# Pose use_cooldown (n = arme, s = secondes) et le marqueur de variante gcr (m) sur l\'objet en main',
                     '$item modify entity @s weapon.mainhand {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:$(s)f,cooldown_group:"mg:gun$(n)"}}}',
                     '$item modify entity @s weapon.mainhand {function:"minecraft:set_custom_data",tag:{gcr:$(m)b}}'])
    cdn = ['# Variante normale (hors dernière balle) : retire l\'overlay de recharge ; Sniper : overlay de cadence',
           f'execute unless items entity @s weapon.mainhand *[custom_data~{{gun:{SNP}}}] unless items entity @s weapon.mainhand *[custom_data~{{gcr:1b}}] unless items entity @s weapon.mainhand *[custom_data~{{gcr:2b}}] run return 0']
    for n, g in GUNS.items():
        if n == SNP:
            s, s2 = f'{g[3] / 20:g}', f'{max(1, g[3] * 2 // 3) / 20:g}'
            cdn += [f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] unless entity @s[tag=mg.zdbl] unless items entity @s weapon.mainhand *[custom_data~{{gcr:0b}}] run return run function mg:gun/cd_set {{n:{n},s:{s},m:0}}',
                    f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] if entity @s[tag=mg.zdbl] unless items entity @s weapon.mainhand *[custom_data~{{gcr:3b}}] run return run function mg:gun/cd_set {{n:{n},s:{s2},m:3}}']
        else:
            cdn += [f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n},gcr:{m}b}}] run return run function mg:gun/cd_set {{n:{n},s:0.05,m:0}}' for m in (1, 2)]
    w('gun/cd_n', cdn)
    w('gun/cd_r', ['# Variante « dernière balle » (macro n, s = recharge, h = recharge Speed Cola) : l\'overlay couvre la recharge',
                   '$execute if entity @s[tag=mg.zsc] unless items entity @s weapon.mainhand *[custom_data~{gcr:2b}] run function mg:gun/cd_set {n:$(n),s:$(h),m:2}',
                   '$execute unless entity @s[tag=mg.zsc] unless items entity @s weapon.mainhand *[custom_data~{gcr:1b}] run function mg:gun/cd_set {n:$(n),s:$(s),m:1}'])
    w('gun/cd_hand', ['# @s tient une arme mg_gun : choisit la variante use_cooldown (limites : accroupi, Q, Neo GTA, lobby)',
                      f'execute if score @s mg.grl matches 1.. if items entity @s weapon.mainhand *[custom_data~{{gun:{SNP},gcr:4b}}] run return 0',
                      f'execute if score @s mg.grl matches 1.. if items entity @s weapon.mainhand *[custom_data~{{gun:{SNP}}}] run return run function mg:gun/cd_set {{n:{SNP},s:0.05,m:4}}',
                      'execute if score @s mg.grl matches 1.. run return run function mg:gun/cd_n',
                      'execute if score @s mg.gcd matches 1.. run return run function mg:gun/cd_n'] +
      [f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] if score @s mg.g{n} matches ..1 run return run function mg:gun/cd_r {{n:{n},s:{g[5] / 20:g},h:{g[5] // 2 / 20:g}}}' for n, g in GUNS.items()] +
      ['function mg:gun/cd_n'])
    # Barre de durabilité (lobby, Neo GTA) : le tir au clic gauche / le gcd partagé ne passent pas par use_cooldown (réservé à Zombies et
    # Infection). La barre se REMPLIT au fil de la recharge (ou de la cadence du Sniper) : set_damage prend la fraction de durabilité
    # restante (1 = barre pleine), donc damage = (total - reste) / total, soit la progression. Les faux joueurs $gbt (durée totale),
    # $gbr (ticks restants) et $gbar (millièmes) sont sur mg.st. L'objet est posé « unbreakable » : on retire le composant pour
    # afficher la barre (dans le même item modify, avant set_damage qui ignore un objet incassable) puis on le remet à la fin.
    w('gun/bar_set', ['# @s tient une arme : barre de durabilité = progression ($gbt = durée totale, $gbr = ticks restants)',
                      'execute unless score $gbt mg.st matches 1.. run return 0',
                      'scoreboard players operation $gbar mg.st = $gbt mg.st', 'scoreboard players operation $gbar mg.st -= $gbr mg.st',
                      'scoreboard players set #1000 mg.st 1000', 'scoreboard players operation $gbar mg.st *= #1000 mg.st',
                      'scoreboard players operation $gbar mg.st /= $gbt mg.st',
                      'execute if score $gbar mg.st matches ..0 run scoreboard players set $gbar mg.st 1',   # set_damage 0 = objet « cassé »
                      'execute if score $gbar mg.st matches 1000.. run scoreboard players set $gbar mg.st 999',
                      'item modify entity @s weapon.mainhand [{function:"minecraft:set_components",components:{"!minecraft:unbreakable":{}}},'
                      '{function:"minecraft:set_damage",damage:{type:"minecraft:score",target:{type:"minecraft:fixed",name:"$gbar"},score:"mg.st",scale:0.001}}]'])
    bar = ['# @s tient une arme mg_gun (lobby, Neo GTA) : barre de durabilité pendant la recharge, puis pendant la cadence du Sniper',
           '# La recharge est celle de l\'arme en main seulement (mg.grt) ; gcd est partagé en Neo GTA : la cadence du Sniper n\'est montrée que s\'il n\'y a pas de recharge',
           'scoreboard players set $gbt mg.st 0',
           'execute if score @s mg.grl matches 1.. run scoreboard players operation $gbr mg.st = @s mg.grl',
           'execute unless score @s mg.grl matches 1.. if score @s mg.gcd matches 1.. run scoreboard players operation $gbr mg.st = @s mg.gcd']
    bar += [f'execute if score @s mg.grl matches 1.. if score @s mg.grt matches {n} if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] run scoreboard players set $gbt mg.st {g[5]}'
            for n, g in GUNS.items()]
    bar += [f'execute unless score @s mg.grl matches 1.. if score @s mg.gcd matches 1.. if items entity @s weapon.mainhand *[custom_data~{{gun:{SNP}}}] run scoreboard players set $gbt mg.st {GUNS[SNP][3]}',
            'execute if score $gbt mg.st matches 1.. run return run function mg:gun/bar_set',
            '# Rien à montrer : on remet à zéro toute arme restée avec une barre (celle qui vient de finir sa recharge comprise)',
            'function mg:gun/bar_clear']
    w('gun/bar', bar)
    # Remise à zéro (incassable, intact) de chaque arme mg_gun qui n'est plus incassable : hotbar.0..8 et main gauche. Les objets déjà incassables
    # (tout l'inventaire hors recharge, bazooka du lobby compris : lrpg porte mg_gun + unbreakable) ne sont pas touchés. Garde en tête : un seul
    # test (hotbar.* puis main gauche) tant qu'aucune barre ne traîne, donc coût minime les ticks sans recharge. Le bazooka GTA (rpg:1b seul)
    # n'a pas mg_gun. Appelée par gun/bar (rien à montrer) et par lobby/guns_tick, gta/tick quand l'objet en main n'est pas l'arme à barre.
    bar_off = '*[custom_data~{mg_gun:1b},!minecraft:unbreakable]'
    reset = '{function:"minecraft:set_components",components:{"minecraft:unbreakable":{},"minecraft:damage":0}}'
    w('gun/bar_clear', ['# @s : toute arme mg_gun sans unbreakable (barre de durabilité figée) redevient incassable et intacte (hotbar.0..8, main gauche)',
                        f'execute unless items entity @s hotbar.* {bar_off} unless items entity @s weapon.offhand {bar_off} run return 0'] +
      [f'execute if items entity @s {s} {bar_off} run item modify entity @s {s} {reset}' for s in [f'hotbar.{i}' for i in range(9)] + ['weapon.offhand']])
    w('gun/tick', ['# Armes : à appeler chaque tick par le jeu',
                   'execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:gun/use',
                   'scoreboard players reset @a[scores={mg.qs=1..}] mg.qs',
                   'scoreboard players remove @a[scores={mg.gcd=1..}] mg.gcd 1',
                   'execute as @a[scores={mg.grl=1..}] at @s run function mg:gun/reload_tick',
                   'execute as @a[tag=mg.play,scores={mg.gsn=1..}] at @s run function mg:gun/sneak',
                   'scoreboard players reset @a[scores={mg.gsn=1..}] mg.gsn',
                   'execute as @a[tag=mg.play,tag=!mg.gtw] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/cd_hand',
                   'execute as @a[tag=mg.play] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/hud'])
    w('gun/reset', ['# @s : munitions et recharge remises à zéro', 'scoreboard players reset @s mg.grl', 'scoreboard players reset @s mg.grt',
                    'scoreboard players reset @s mg.gcd'] + [f'scoreboard players reset @s mg.g{n}' for n in GUNS])
    C.objectives([('mg.gcd', 'dummy'), ('mg.grl', 'dummy'), ('mg.grt', 'dummy'), ('mg.gsn', 'minecraft.custom:minecraft.sneak_time')] +
                 [(f'mg.g{n}', 'dummy') for n in GUNS])


def give(n, slot):
    """Ligne mcfunction : donne l'arme n à @s dans slot."""
    return f'function mg:gun/put_{n} {{slot:"{slot}"}}'
