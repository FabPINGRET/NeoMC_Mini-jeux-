# Bombardier, le jeu : bombes, item, fonctions de la partie : exécuté par gen_bomber.py (exec), à sa place dans l'ordre d'origine.
# Utilise : HX, LIMIT, NG, NPART, NUKE_AT, TOTAL, Y0, YT, Z, js, w.

# ---------------------------------------------------------------- jeu
BOMBS = [  # type, item_model, nom, couleur, cooldown (ticks), vitesse de lancer (‰), description
    (1, 'tnt', 'Bombe', 'red', 12, 900, 'Rayon 6, recharge 0,6 s'),
    (2, 'tnt_minecart', 'Méga-bombe', 'dark_red', 140, 600, 'Rayon 12, recharge 7 s'),
    (3, 'fire_charge', 'Bombe à fragmentation', 'gold', 100, 900, '7 sous-munitions, recharge 5 s'),
]


def item(t, model, name, col, cd, desc, slot):
    cdc = f',use_cooldown={{seconds:{cd / 20}f,cooldown_group:"mg:bomb{t}"}}' if cd else ''
    comp = (f'custom_data={{bomb:{t}}},item_model="minecraft:{model}",unbreakable={{}},'
            f'custom_name={js({"text": name, "color": col, "bold": True, "italic": False})},'
            f'lore=[{js({"text": desc, "color": "gray", "italic": False})},{js({"text": "Clic droit : larguer (dans la direction du regard)", "color": "dark_gray", "italic": False})}]'
            + cdc)
    return f'item replace entity @s hotbar.{slot} with minecraft:warped_fungus_on_a_stick[{comp}]'


w('bomber/prepare', ['# 💣 Bombardier : préparation (construction en étapes pendant le compte à rebours)',
                     '# perchoir des spectateurs (reconnexion, pause) : au-dessus de la ville',
                     'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {YT + 40}', f'scoreboard players set $pz mg.st {Z}',
                     f'fill -{HX} {YT} {Z - HX} {HX} {YT} {Z + HX} minecraft:barrier',
                     'scoreboard players set $bbs mg.st 0',
                     f'execute if data storage mg:bomber v1 run scoreboard players set $bbs mg.st {NG}',
                     'function mg:bomber/build_step',
                     'kill @e[tag=mg.bomb]', 'kill @e[tag=mg.bsm]',
                     'scoreboard players set $bdes mg.st 0', 'scoreboard players set $bpct mg.st 0',
                     'scoreboard players set $bidn mg.st 0',
                     'scoreboard players reset * mg.bmb',
                     'execute as @a[tag=mg.play] run function mg:bomber/join',
                     'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
                     f'spreadplayers 0 {Z} 6 50 under {YT + 3} false @a[tag=mg.play]',
                     f'execute as @a[tag=mg.play] at @s run tp @s ~ {YT + 1} ~ ~ 60',
                     f'bossbar add mg:bomber {js({"text": "🏙 Ville détruite : 0 %", "color": "red"})}',
                     f'bossbar set mg:bomber max {TOTAL}', 'bossbar set mg:bomber value 0', 'bossbar set mg:bomber color red',
                     'bossbar set mg:bomber style notched_10', 'bossbar set mg:bomber players @a[tag=mg.play]'])
w('bomber/join', ['# @s : numéro de bombardier (attribution des dégâts)', 'scoreboard players add $bidn mg.st 1',
                  'scoreboard players operation @s mg.bid = $bidn mg.st', 'scoreboard players set @s mg.bmb 0',
                  'scoreboard players set @s mg.bc1 0', 'scoreboard players set @s mg.bc2 0', 'scoreboard players set @s mg.bc3 0',
                  'scoreboard players set @s mg.bc4 0'])
ELY = ('item replace entity @s armor.chest with minecraft:elytra[custom_data={mg_bomb:1b},unbreakable={},'
       'enchantments={"minecraft:binding_curse":1},custom_name={"text":"Élytres du bombardier","color":"red","italic":false}]')
ROCKET = ('item replace entity @s hotbar.8 with minecraft:firework_rocket[custom_data={mg_bomb:1b},fireworks={flight_duration:1},'
          'custom_name={"text":"Fusée (illimitée)","color":"gold","italic":false}] 16')
w('bomber/kit', ['# @s : les bombes, les élytres et les fusées'] + [item(t, m, n, c, cd, d, i) for i, (t, m, n, c, cd, _, d) in enumerate(BOMBS)] +
  [ELY, ROCKET, 'effect give @s minecraft:speed infinite 1 true', 'effect give @s minecraft:saturation infinite 0 true',
   'effect give @s minecraft:resistance infinite 4 true', 'effect give @s minecraft:night_vision infinite 0 true'])
w('bomber/go', ['# Départ : le plancher disparaît, tout le monde s\'envole dans la ville', 'scoreboard players set $btt mg.st 0',
                f'fill -{HX} {YT} {Z - HX} {HX} {YT} {Z + HX} minecraft:air replace minecraft:barrier',
                'effect give @a[tag=mg.play] minecraft:slow_falling 3 0 true',
                f'execute unless score $bbs mg.st matches {NG + NPART}.. run function mg:bomber/build_rest',
                'execute as @a[tag=mg.play] run function mg:bomber/kit',
                'scoreboard players reset @a mg.qs',
                'scoreboard objectives setdisplay sidebar mg.bmb',
                'tellraw @a[tag=mg.play] ' + js([{'text': '💣 BOMBARDIER : ', 'color': 'red', 'bold': True},
                                                 {'text': 'saute et ouvre tes élytres (Espace) : vole entre les gratte-ciel (fusées illimitées, case 9), vise et clic droit pour larguer. '
                                                          'Posé au sol : accroupis-toi pour repartir. Chaque bloc détruit = 1 point, '
                                                          'or et statue = 10. Bombe atomique pour la dernière minute. 2 min 30.', 'color': 'gray'}])])
w('bomber/build_rest', ['# Filet de sécurité : termine la construction d\'un coup si le départ arrive avant la fin',
                        f'execute if score $bbs mg.st matches ..{NG + NPART - 1} run function mg:bomber/build_step',
                        f'execute if score $bbs mg.st matches ..{NG + NPART - 1} run function mg:bomber/build_rest'])

nuke = item(4, 'nether_star', '☢ Bombe atomique', 'green', 0, 'Rayon 22, une seule !', 3)
w('bomber/tick', ['# 💣 Bombardier : tick', 'scoreboard players add $btt mg.st 1',
                  'execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:bomber/use',
                  'scoreboard players reset @a[scores={mg.qs=1..}] mg.qs',
                  'scoreboard players remove @a[scores={mg.bc1=1..}] mg.bc1 1', 'scoreboard players remove @a[scores={mg.bc2=1..}] mg.bc2 1',
                  'scoreboard players remove @a[scores={mg.bc3=1..}] mg.bc3 1',
                  'execute as @e[type=minecraft:tnt,tag=mg.bomb] at @s run function mg:bomber/bomb_tick',
                  'execute as @a[tag=mg.play,predicate=mg:sneak,predicate=!mg:gliding,nbt={OnGround:1b}] at @s run function mg:bomber/launch',
                  'scoreboard players add @e[type=minecraft:marker,tag=mg.bsm] mg.bc4 1',
                  'execute as @e[type=minecraft:marker,tag=mg.bsm,scores={mg.bc4=400..}] run kill @s',
                  'scoreboard players operation $bq mg.st = $btt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $bq mg.st %= #20 mg.st',
                  'execute if score $bq mg.st matches 0 run function mg:bomber/second',
                  'execute if score $bq mg.st matches 0 run execute at @e[type=minecraft:marker,tag=mg.bsm] run particle minecraft:campfire_cosy_smoke ~ ~ ~ 0.8 0.3 0.8 0.02 3 force',
                  'execute if score $bq mg.st matches 10 run execute at @e[type=minecraft:marker,tag=mg.bsm] run particle minecraft:flame ~ ~0.5 ~ 0.8 0.3 0.8 0.01 4',
                  f'execute if score $btt mg.st matches {NUKE_AT} run function mg:bomber/nuke_give',
                  f'execute if score $btt mg.st matches {LIMIT - 600} run tellraw @a[tag=mg.play] {{"text":"💣 Plus que 30 secondes !","color":"gold"}}',
                  f'execute if score $state mg.st matches 2 if score $btt mg.st matches {LIMIT}.. run function mg:bomber/finish',
                  'execute store result score $alive mg.st if entity @a[tag=mg.play]',
                  'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw'])
w('bomber/second', ['# Une seconde : barre de destruction, fusées rechargées, joueurs sous le sol ou sortis de la ville ramenés au-dessus',
                    'scoreboard players operation $bpct mg.st = $bdes mg.st', 'scoreboard players set #100 mg.st 100',
                    'scoreboard players operation $bpct mg.st *= #100 mg.st', f'scoreboard players set #btot mg.st {TOTAL}',
                    'scoreboard players operation $bpct mg.st /= #btot mg.st',
                    'execute store result bossbar mg:bomber value run scoreboard players get $bdes mg.st',
                    'bossbar set mg:bomber name [{"text":"🏙 Ville détruite : ","color":"red"},{"score":{"name":"$bpct","objective":"mg.st"},"color":"yellow","bold":true},{"text":" %","color":"red"}]',
                    f'execute as @a[tag=mg.play] at @s if entity @s[y=-64,dy={64 + Y0}] run tp @s 0 {YT + 1} {Z}',
                    f'execute as @a[tag=mg.play] unless entity @s[x=-{HX},y=-64,z={Z - HX},dx={2 * HX},dy=400,dz={2 * HX}] run tp @s 0 {YT + 1} {Z}',
                    'execute as @a[tag=mg.play] run ' + ROCKET,
                    'execute if score $state mg.st matches 2 if score $bpct mg.st matches 85.. run function mg:bomber/timeout'])
w('bomber/nuke_give', ['# Dernière minute : une bombe atomique par joueur',
                       'execute as @a[tag=mg.play] run ' + nuke,
                       'title @a[tag=mg.play] title {"text":"☢","color":"green","bold":true}',
                       'title @a[tag=mg.play] subtitle {"text":"Bombe atomique disponible (case 4) !","color":"green"}',
                       'execute as @a[tag=mg.play] at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 0.6'])

# lancer : direction du regard ×1000 dans $fx $fy $fz
w('bomber/use', ['# Clic droit (@s, à sa position) : la bombe en main',
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:1}] if score @s mg.bc1 matches ..0 run return run function mg:bomber/drop {t:1,cd:"bc1",cdv:%d,sp:0.0009}' % BOMBS[0][4],
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:2}] if score @s mg.bc2 matches ..0 run return run function mg:bomber/drop {t:2,cd:"bc2",cdv:%d,sp:0.0006}' % BOMBS[1][4],
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:3}] if score @s mg.bc3 matches ..0 run return run function mg:bomber/drop {t:3,cd:"bc3",cdv:%d,sp:0.0009}' % BOMBS[2][4],
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:4}] run return run function mg:bomber/drop_nuke',
                 'playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.6'])
w('bomber/drop_nuke', ['# Bombe atomique : une seule, l\'objet disparaît', 'item replace entity @s weapon.mainhand with minecraft:air',
                       'function mg:bomber/drop {t:5,cd:"bc4",cdv:0,sp:0.0004}',
                       'tellraw @a[tag=mg.play] [{"text":"☢ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" a largué la bombe atomique !","color":"green"}]',
                       'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.6 1.4'])
w('bomber/drop', ['# @s : largue une bombe de type $(t) sous ses pieds, lancée dans la direction du regard',
                  '$scoreboard players set @s mg.$(cd) $(cdv)',
                  'execute anchored eyes positioned ^ ^ ^1 run summon minecraft:marker ~ ~ ~ {Tags:["mg.bdm"]}',
                  'execute store result score $fx mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[0] 1000',
                  'execute store result score $fy mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[1] 1000',
                  'execute store result score $fz mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[2] 1000',
                  'kill @e[type=minecraft:marker,tag=mg.bdm]',
                  'execute store result score $px0 mg.st run data get entity @s Pos[0] 1000',
                  'execute store result score $py0 mg.st run data get entity @s Pos[1] 1000',
                  'execute store result score $pz0 mg.st run data get entity @s Pos[2] 1000',
                  'scoreboard players operation $fx mg.st -= $px0 mg.st', 'scoreboard players operation $fy mg.st -= $py0 mg.st',
                  'scoreboard players remove $fy mg.st 1620', 'scoreboard players operation $fz mg.st -= $pz0 mg.st',
                  'execute positioned ~ ~-0.6 ~ run summon minecraft:tnt ~ ~ ~ {Tags:["mg.bomb","mg.bnew"],fuse:400s,explosion_power:0.0f}',
                  '$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[0] double $(sp) run scoreboard players get $fx mg.st',
                  '$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[1] double $(sp) run scoreboard players get $fy mg.st',
                  '$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[2] double $(sp) run scoreboard players get $fz mg.st',
                  'scoreboard players operation @e[type=minecraft:tnt,tag=mg.bnew] mg.bid = @s mg.bid',
                  '$scoreboard players set @e[type=minecraft:tnt,tag=mg.bnew] mg.bty $(t)',
                  'scoreboard players set @e[type=minecraft:tnt,tag=mg.bnew] mg.bc4 0',
                  '$function mg:bomber/look_$(t)',
                  'tag @e[tag=mg.bnew] remove mg.bnew',
                  'playsound minecraft:entity.tnt.primed player @a ~ ~ ~ 0.8 1.2'])
w('bomber/launch', ['# @s : posé au sol et accroupi → catapulté vers le ciel pour rouvrir les élytres',
                    'effect give @s minecraft:levitation 1 40 true',
                    'particle minecraft:gust ~ ~0.5 ~ 0.3 0.1 0.3 0 3',
                    'playsound minecraft:entity.wind_charge.wind_burst player @a ~ ~ ~ 1 0.8',
                    'title @s actionbar {"text":"🪽 Appuie sur Espace en l\'air pour rouvrir tes élytres","color":"aqua"}'])
for t, blk in [(1, 'tnt'), (2, 'coal_block'), (3, 'redstone_block'), (4, 'tnt'), (5, 'lodestone')]:
    w(f'bomber/look_{t}', [f'# Aspect de la bombe de type {t}',
                           f'data merge entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] {{block_state:{{Name:"minecraft:{blk}"}}}}'])

w('bomber/bomb_tick', ['# @s : bombe en vol (âge mg.bc4, type mg.bty, lanceur mg.bid)',
                       'scoreboard players add @s mg.bc4 1',
                       'execute if score @s mg.bc4 matches 300.. run return run kill @s',
                       'execute if entity @s[y=-64,dy=103] run return run kill @s',
                       'execute if score @s mg.bty matches 3 if score @s mg.bc4 matches 14 run return run function mg:bomber/split',
                       'particle minecraft:smoke ~ ~0.5 ~ 0.1 0.1 0.1 0 2',
                       'execute if score @s mg.bty matches 5 run particle minecraft:end_rod ~ ~0.5 ~ 0.2 0.2 0.2 0 2 force',
                       'execute unless block ~ ~-0.2 ~ #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~0.6 ~0.4 ~ #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~-0.6 ~0.4 ~ #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~ ~0.4 ~0.6 #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~ ~0.4 ~-0.6 #mg:bomb_pass run return run function mg:bomber/impact'])
w('bomber/split', ['# @s : la bombe à fragmentation s\'ouvre en 7 sous-munitions',
                   'execute store result score $mx mg.st run data get entity @s Motion[0] 1000',
                   'execute store result score $my mg.st run data get entity @s Motion[1] 1000',
                   'execute store result score $mz mg.st run data get entity @s Motion[2] 1000',
                   'scoreboard players operation $bid mg.st = @s mg.bid'] +
  ['execute summon minecraft:tnt run function mg:bomber/bomblet'] * 7 +
  ['particle minecraft:firework ~ ~0.5 ~ 0.3 0.3 0.3 0.15 25 force', 'playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 3 0.8', 'kill @s'])
w('bomber/bomblet', ['# @s : sous-munition (même lanceur, direction écartée au hasard)',
                     'tag @s add mg.bomb', 'data merge entity @s {fuse:400s,explosion_power:0.0f}',
                     'scoreboard players operation @s mg.bid = $bid mg.st', 'scoreboard players set @s mg.bty 4', 'scoreboard players set @s mg.bc4 20',
                     'execute store result score $br mg.st run random value -280..280', 'scoreboard players operation $br mg.st += $mx mg.st',
                     'execute store result entity @s Motion[0] double 0.001 run scoreboard players get $br mg.st',
                     'execute store result score $br mg.st run random value -150..80', 'scoreboard players operation $br mg.st += $my mg.st',
                     'execute store result entity @s Motion[1] double 0.001 run scoreboard players get $br mg.st',
                     'execute store result score $br mg.st run random value -280..280', 'scoreboard players operation $br mg.st += $mz mg.st',
                     'execute store result entity @s Motion[2] double 0.001 run scoreboard players get $br mg.st'])
w('bomber/impact', ['# @s : la bombe touche (explosion selon le type, points au lanceur)',
                    'scoreboard players operation $bid mg.st = @s mg.bid',
                    'execute if score @s mg.bty matches 1 run function mg:bomber/boom/r6',
                    'execute if score @s mg.bty matches 2 run function mg:bomber/boom/r12',
                    'execute if score @s mg.bty matches 3 run function mg:bomber/boom/r6',
                    'execute if score @s mg.bty matches 4 run function mg:bomber/boom/r4',
                    'execute if score @s mg.bty matches 5 run function mg:bomber/boom/r22',
                    'execute if score @s mg.bty matches 4 run function mg:bomber/fx_small',
                    'execute if score @s mg.bty matches 1 run function mg:bomber/fx_big',
                    'execute if score @s mg.bty matches 3 run function mg:bomber/fx_big',
                    'execute if score @s mg.bty matches 2 run function mg:bomber/fx_big',
                    'execute if score @s mg.bty matches 2 run function mg:bomber/fx_nuke',
                    'execute if score @s mg.bty matches 5 run function mg:bomber/fx_nuke',
                    'execute if score $bk mg.st matches 1.. run summon minecraft:marker ~ ~ ~ {Tags:["mg.bsm"]}',
                    'scoreboard players operation $bpts mg.st = $bb mg.st', 'scoreboard players set #10 mg.st 10',
                    'scoreboard players operation $bpts mg.st *= #10 mg.st', 'scoreboard players operation $bpts mg.st += $bk mg.st',
                    'scoreboard players operation $bdes mg.st += $bk mg.st', 'scoreboard players operation $bdes mg.st += $bb mg.st',
                    'execute as @a[tag=mg.play] if score @s mg.bid = $bid mg.st run function mg:bomber/credit',
                    'kill @s'])
w('bomber/credit', ['# @s : lanceur de la bombe qui vient d\'exploser ($bpts points)',
                    'scoreboard players operation @s mg.bmb += $bpts mg.st',
                    'execute if score $bpts mg.st matches 1.. run title @s actionbar [{"text":"💥 +","color":"gold"},{"score":{"name":"$bpts","objective":"mg.st"},"color":"yellow","bold":true},{"text":" dégâts","color":"gold"}]',
                    'execute if score $bpts mg.st matches 0 run title @s actionbar {"text":"💨 Raté !","color":"gray"}',
                    'execute if score $bpts mg.st matches 400.. run tellraw @a[tag=mg.play] [{"text":"💥 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" : coup dévastateur, ","color":"red"},{"score":{"name":"$bpts","objective":"mg.st"},"color":"gold","bold":true},{"text":" points !","color":"red"}]',
                    'execute if score $bpts mg.st matches 1.. at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 0.8'])
w('bomber/fx_small', ['particle minecraft:explosion ~ ~ ~ 1.5 1.5 1.5 0 6 force', 'particle minecraft:large_smoke ~ ~ ~ 1.5 1 1.5 0.05 20 force',
                      'particle minecraft:flame ~ ~ ~ 1.2 1 1.2 0.08 25 force',
                      'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 6 1'])
w('bomber/fx_big', ['particle minecraft:explosion_emitter ~ ~ ~ 1.5 1.5 1.5 0 3 force', 'particle minecraft:large_smoke ~ ~ ~ 3 2 3 0.08 60 force',
                    'particle minecraft:lava ~ ~ ~ 3 2 3 0 30 force', 'particle minecraft:flame ~ ~ ~ 3 2 3 0.15 60 force',
                    'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 12 0.6',
                    'playsound minecraft:entity.lightning_bolt.thunder master @a ~ ~ ~ 6 1.4'])
w('bomber/fx_nuke', ['particle minecraft:explosion_emitter ~ ~ ~ 6 4 6 0 25 force', 'particle minecraft:campfire_signal_smoke ~ ~8 ~ 4 12 4 0.05 200 force',
                     'particle minecraft:large_smoke ~ ~4 ~ 8 6 8 0.2 300 force', 'particle minecraft:lava ~ ~ ~ 6 4 6 0 120 force',
                     'particle minecraft:flame ~ ~2 ~ 8 4 8 0.3 300 force',
                     'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 40 0.4',
                     'playsound minecraft:entity.lightning_bolt.thunder master @a ~ ~ ~ 40 0.5',
                     'playsound minecraft:entity.wither.death master @a ~ ~ ~ 20 0.6'])
w('bomber/timeout', ['# Fin : le plus de dégâts gagne (égalité = match nul)',
                     'scoreboard players set $bx mg.st 0', 'scoreboard players operation $bx mg.st > @a[tag=mg.play] mg.bmb',
                     'scoreboard players set $bc mg.st 0', 'execute as @a[tag=mg.play] if score @s mg.bmb = $bx mg.st run scoreboard players add $bc mg.st 1',
                     'tellraw @a[tag=mg.play] [{"text":"🏙 La ville est détruite à ","color":"gray"},{"score":{"name":"$bpct","objective":"mg.st"},"color":"red","bold":true},{"text":" %","color":"gray"}]',
                     'execute if score $bx mg.st matches 0 run return run function mg:core/draw',
                     'execute if score $bc mg.st matches 2.. run return run function mg:core/draw',
                     'execute as @a[tag=mg.play] if score @s mg.bmb = $bx mg.st run function mg:core/win_player'])
w('bomber/finish', ['# Fin : résultat, puis 20 s en spectateur au-dessus de la ville pour admirer les dégâts', 'function mg:bomber/timeout',
                    'execute unless score $state mg.st matches 3 run return 0',
                    'scoreboard players set $timer mg.st 400', 'gamemode spectator @a[tag=mg.play]', 'gamemode spectator @a[tag=mg.out]',
                    f'tp @a[tag=mg.play] 0 120 {Z - HX - 20} facing 0 64 {Z}', f'tp @a[tag=mg.out] 0 120 {Z - HX - 20} facing 0 64 {Z}',
                    'tellraw @a[tag=mg.play] {"text":"👁 20 s pour survoler la ville détruite (mode spectateur), puis retour au lobby.","color":"aqua"}'])
w('bomber/cleanup', ['schedule clear mg:bomber/build_step', 'clear @a minecraft:elytra[custom_data~{mg_bomb:1b}]',
                     'clear @a minecraft:firework_rocket[custom_data~{mg_bomb:1b}]', 'kill @e[tag=mg.bomb]', 'kill @e[tag=mg.bsm]', 'bossbar remove mg:bomber',
                     'scoreboard players reset * mg.bmb', 'scoreboard players reset * mg.bid', 'effect clear @a[tag=mg.play]'])
