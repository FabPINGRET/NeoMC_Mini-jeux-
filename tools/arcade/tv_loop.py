# Terra Nova : mort, interface, tick de la session, SEC ; exécuté par gen_terranova.py (exec), à la place exacte de ce bloc.
# Tranche contiguë de l'ancien gen_terranova.py : mêmes globals que la façade, aucun import, aucune copie de w/js/patch.
# Utilise : COLONY_BOX, DEF_SECOND, EXITA, say, w

# ================================================================ mort, entrées et sorties de la colonie, interface
w('terra/died', ['# @s est mort à Terra Nova (inventaire gardé) : -10 % de crédits, caisse lâchée', 'scoreboard players set @s mg.deaths 0', 'scoreboard players set #10 mg.st 10',
                 'execute if entity @s[tag=mg.tvcar] run function mg:terra/crate_drop',
                 'scoreboard players operation $tvl mg.st = @s mg.tvc', 'scoreboard players operation $tvl mg.st /= #10 mg.st',
                 'scoreboard players operation @s mg.tvc -= $tvl mg.st', 'scoreboard players set @s mg.tvhm 0', 'scoreboard players set @s mg.tvh 0',
                 'tag @s remove mg.tvoh', 'title @s times 5 40 15', 'title @s title {"text":"☠ DÉVORÉ","color":"dark_red","bold":true}',
                 'title @s subtitle [{"text":"Frais d\'infirmerie : -","color":"gray"},{"score":{"name":"$tvl","objective":"mg.st"},"color":"red"},{"text":" ₵","color":"red"}]'])
w('terra/gate', ['# Chaque seconde : qui est dans la colonie (tag mg.tvout = dehors), messages aux portes',
                 'tag @a[tag=mg.tvin2] remove mg.tvin2', f'tag @a[tag=mg.tvw,{COLONY_BOX}] add mg.tvin2',
                 'execute as @a[tag=mg.tvw,tag=mg.tvin2,tag=mg.tvout] run function mg:terra/gate_in',
                 'execute as @a[tag=mg.tvw,tag=!mg.tvin2,tag=!mg.tvout] run function mg:terra/gate_out'])
w('terra/gate_in', ['tag @s remove mg.tvout'] + say('🏠 De retour dans la colonie : tu es en sécurité', 'green') +
  ['execute at @s run playsound minecraft:block.note_block.chime player @s ~ ~ ~ 0.5 1.4'])
w('terra/gate_out', ['tag @s add mg.tvout'] + say('🌿 Tu quittes le périmètre : prudence, colon !', 'gold') +
  ['execute at @s run playsound minecraft:block.bell.use player @s ~ ~ ~ 0.5 0.8'])
HM = ['# @s : barre d\'action (crédits + mission)']
CRED = ('{"text":"⭐","color":"gold"},{"score":{"name":"@s","objective":"mg.trlv"},"color":"gold","bold":true},{"text":"  ","color":"gray"},'
        '{"score":{"name":"@s","objective":"mg.tvc"},"color":"yellow","bold":true},{"text":" ₵","color":"yellow"},{"text":"   ","color":"gray"}')
HM.append('execute if entity @s[scores={mg.tvm=0}] run return run function mg:terra/rpg/hud')
for cond, txt, col in [('scores={mg.tvm=1},tag=!mg.tvcar', '📦 Trouve la caisse (📡)', 'yellow'),
                       ('scores={mg.tvm=1},tag=mg.tvcar', '📦 Rapporte la caisse à la colonie !', 'gold'), ('scores={mg.tvm=2}', '🛡 Rejoins l\'outpost et défends-le (📡)', 'aqua'),
                       ('scores={mg.tvm=4}', '🦖 Traque le carnotaure (📡)', 'red')]:
    DST = ',{"text":"  📍 ","color":"gold"},{"score":{"name":"@s","objective":"mg.trod"},"color":"yellow","bold":true},{"text":" m","color":"gold"}'
    HM.append(f'execute if entity @s[{cond}] run return run title @s actionbar [{CRED},{{"text":"{txt}","color":"{col}"}}{DST}]')
HM.append(f'execute if entity @s[scores={{mg.tvm=3}}] run return run title @s actionbar [{CRED},{{"text":"🦖 Slashers : ","color":"green"}},{{"score":{{"name":"@s","objective":"mg.tvmp"}},"color":"white","bold":true}},{{"text":" / 5","color":"white"}}]')
w('terra/hud_main', HM)
HH = ['# @s tient un fusil à impulsions : jauge de chaleur',
      'execute if entity @s[tag=mg.tvoh] run return run title @s actionbar [{"text":"⚠ SURCHAUFFE ","color":"red","bold":true},{"text":"refroidissement…","color":"gray"}]']
for i in range(11):
    lo_, hi_ = i * 100, i * 100 + 99
    col = 'green' if i < 6 else ('gold' if i < 9 else 'red')
    HH.append(f'execute if score @s mg.tvh matches {lo_}..{hi_} run title @s actionbar [{{"text":"🔫 Chaleur ","color":"aqua"}},{{"text":"{"▮" * i}","color":"{col}"}},{{"text":"{"▮" * (10 - i)}","color":"dark_gray"}}]')
w('terra/hud_heat', HH)
w('terra/hud_one', ['# @s : barre d\'action selon l\'objet en main',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:2}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:3}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:7}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] if score @s mg.trcd matches 1.. run return run title @s actionbar {"text":"🎖 Capacité : recharge…","color":"gray"}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] run return run title @s actionbar {"text":"🎖 Capacité PRÊTE (clic droit)","color":"gold","bold":true}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:8}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] if score @s mg.tvsc matches 1.. run return run title @s actionbar {"text":"📢 Canon sonique : recharge…","color":"gray"}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] run return run title @s actionbar {"text":"📢 Canon sonique : PRÊT (clic droit)","color":"aqua","bold":true}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:5}] run return run title @s actionbar [{"text":"🕸 Filets : ","color":"white"},{"score":{"name":"@s","objective":"mg.tvnet"},"color":"yellow","bold":true}]',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:6}] run return run title @s actionbar [{"text":"⚙ Pièges : ","color":"gray"},{"score":{"name":"@s","objective":"mg.tvtr"},"color":"yellow","bold":true},{"text":"  (clic droit : poser à tes pieds)","color":"gray"}]',
                    'execute if score @s mg.tvhm matches 1.. run return 0',
                    'function mg:terra/hud_main'])

# ================================================================ tick de la session (dans la dimension)
w('terra/tick', ['# 🦖 Terra Nova : chaque tick tant qu\'un joueur y est (contexte : dimension mg:terranova)', 'scoreboard players add $tvt mg.st 1',
                 'scoreboard players operation $tvq mg.st = $tvt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $tvq mg.st %= #20 mg.st',
                 # objets
                 'execute as @a[tag=mg.tvw,scores={mg.tvq=1..}] at @s run function mg:terra/use',
                 'scoreboard players reset @a[scores={mg.tvq=1..}] mg.tvq',
                 'execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:1}] at @s run function mg:terra/prod_hit',
                 'execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:12}] at @s run function mg:terra/prod_hit',
                 'execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:13}] at @s run function mg:terra/prod_hit',
                 'scoreboard players reset @a[scores={mg.tvdd=1..}] mg.tvdd',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tvh=1..}] mg.tvh 15',
                 'scoreboard players set @a[tag=mg.tvw,scores={mg.tvh=..-1}] mg.tvh 0',
                 'execute as @a[tag=mg.tvoh,scores={mg.tvh=0}] run function mg:terra/cooled',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tvcd=1..}] mg.tvcd 1',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tvsc=1..}] mg.tvsc 1',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tval=1..}] mg.tval 1',
                 'execute as @a[tag=mg.tvw,scores={mg.tvhm=1..}] run function mg:terra/home_tick',
                 'execute as @a[tag=mg.tvw,scores={mg.tvms=1..}] run function mg:terra/mission_cmd',
                 'execute as @e[type=minecraft:interaction,tag=mg.tvbuy] if data entity @s interaction run function mg:terra/buy_int',
                 'execute as @e[type=minecraft:interaction,tag=mg.tvboard] if data entity @s interaction run function mg:terra/board_int',
                 'execute as @e[type=minecraft:item_display,tag=mg.tvpdi] at @s run tp @s ~ ~ ~ ~4 ~',
                 # dinosaures : modèles, filets, pièges
                 'scoreboard players operation $tvq3b mg.st = $tvt mg.st', 'scoreboard players set #3 mg.st 3', 'scoreboard players operation $tvq3b mg.st %= #3 mg.st',
                 'execute as @e[tag=mg.tvd] at @s if entity @a[tag=mg.tvw,distance=..32] run function mg:terra/dsync',
                 'execute as @e[tag=mg.tvd] if score @s mg.tvph = $tvq3b mg.st at @s unless entity @a[tag=mg.tvw,distance=..32] if entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync',
                 'execute if score $tvq mg.st matches 0 as @e[tag=mg.tvd] at @s unless entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync',
                 'execute if score $tvq mg.st matches 10 as @e[tag=mg.tvd] at @s unless entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync',
                 'scoreboard players remove @e[tag=mg.tvd,scores={mg.tvst=1..}] mg.tvst 1',
                 'execute as @e[tag=mg.tvnetted,scores={mg.tvst=..0}] run function mg:terra/unnet',
                 'execute as @e[type=minecraft:marker,tag=mg.tvtrap] at @s if entity @e[tag=mg.tvhos,tag=!mg.tvnetted,distance=..1.4] run function mg:terra/trap_fire',
                 # caisse : ramassage (toutes les 5 ticks)
                 'scoreboard players operation $tvq5 mg.st = $tvt mg.st', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $tvq5 mg.st %= #5 mg.st',
                 'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.tvm=1},tag=!mg.tvcar] at @s if predicate mg:sneak run function mg:terra/crate_try',
                 'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.tvm=1,mg.tvmp=1..},tag=!mg.tvcar] unless predicate mg:sneak run scoreboard players set @s mg.tvmp 0',
                 # morts, sortie
                 'execute as @a[tag=mg.tvcar] at @s run function mg:terra/carry_tick',
                 'execute as @a[tag=mg.tvw,scores={mg.deaths=1..}] run function mg:terra/died',
                 f'particle minecraft:reverse_portal {EXITA[0] + 0.5} 67 {EXITA[1] + 0.5} 0.05 1.3 1.0 0.02 4',
                 'execute as @a[tag=mg.tvw] at @s if entity @e[type=minecraft:marker,tag=mg.tvexit,distance=..1.4] in minecraft:overworld run function mg:terra/leave',
                 'execute if score $tvq mg.st matches 0 run function mg:terra/second',
                 'execute if score $tvq mg.st matches 5 as @a[tag=mg.tvw,scores={mg.tval=..0}] run function mg:terra/hud_one',
                 'execute if score $tvq mg.st matches 15 as @a[tag=mg.tvw,scores={mg.tval=..0}] run function mg:terra/hud_one',
                 'function mg:terra/rpg/tick'])
SEC = ['# Chaque seconde (dans la dimension) : colonie, soins, primes, missions, population de dinosaures, carnotaure',
       'execute unless score $tvsu mg.st matches 1.. run return 0',
       'execute if score $tvsu mg.st matches 2 run kill @e[type=#mg:tv_part,tag=mg.tvp,tag=!mg.tvok]',
       'tag @e[tag=mg.tvok] remove mg.tvok', 'scoreboard players set $tvsu mg.st 2',
       'scoreboard players set #4 mg.st 4', 'scoreboard players set #10 mg.st 10', 'scoreboard players set #12 mg.st 12',
       'function mg:terra/gate',
       'scoreboard players enable @a[tag=mg.tvw] mg.tvms', 'effect give @a[tag=mg.tvw] minecraft:saturation infinite 0 true',
       'effect give @a[tag=mg.tvw,x=9,y=64,z=11,dx=14,dy=5,dz=12] minecraft:regeneration 3 2 true',
       # primes et missions
       'execute as @a[tag=mg.tvw,scores={mg.tvkr=1..}] run function mg:terra/k_raptor',
       'execute as @a[tag=mg.tvw,scores={mg.tvkc=1..}] run function mg:terra/k_carno',
       'execute as @a[tag=mg.tvw,scores={mg.tvkb=1..}] run function mg:terra/k_herb',
       'execute as @a[tag=mg.tvw,scores={mg.tvkg=1..}] run function mg:terra/k_herb',
       'execute as @a[tag=mg.tvcar] run function mg:terra/save_pos',
       'execute as @a[tag=mg.tvcar,tag=!mg.tvout] run function mg:terra/m1_done'] + DEF_SECOND + [
       'scoreboard players operation $tvq2 mg.st = $tvt mg.st', 'scoreboard players set #40 mg.st 40', 'scoreboard players operation $tvq2 mg.st %= #40 mg.st',
       'execute if score $tvq2 mg.st matches 0 if entity @a[tag=mg.tvw,scores={mg.tvm=4}] run function mg:terra/hunt_loc',
       'execute unless entity @a[tag=mg.tvw,scores={mg.tvm=4}] run tag @e[tag=mg.tvhunt] remove mg.tvhunt',
       'execute unless entity @e[tag=mg.tvhunt] if entity @a[tag=mg.tvw,scores={mg.tvm=4}] as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] at @s run function mg:terra/hunt_spawn',
       # population
       'execute store result score $tvno mg.st if entity @a[tag=mg.tvout,gamemode=adventure]',
       'execute store result score $tvnr mg.st if entity @e[tag=mg.tvraptor,tag=!mg.trr]',
       '# slashers de la vallée : 3 par colon dehors + 6 (20 au plus)',
       'scoreboard players operation $tvwr mg.st = $tvno mg.st', 'scoreboard players set #3 mg.st 3', 'scoreboard players operation $tvwr mg.st *= #3 mg.st',
       'scoreboard players add $tvwr mg.st 6', 'execute if score $tvwr mg.st matches 21.. run scoreboard players set $tvwr mg.st 20',
       'scoreboard players remove $tvpk mg.st 1', 'scoreboard players remove $tvcc mg.st 1',
       'execute if score $tvno mg.st matches 1.. if score $tvpk mg.st matches ..0 if score $tvnr mg.st < $tvwr mg.st run function mg:terra/pack_try',
       'execute if score $tvno mg.st matches 1.. if score $tvcc mg.st matches ..0 unless entity @e[tag=mg.tvcarno] run function mg:terra/carno_try',
       'scoreboard players operation $tvq3 mg.st = $tvt mg.st', 'scoreboard players set #60 mg.st 60', 'scoreboard players operation $tvq3 mg.st %= #60 mg.st',
       # traque : toutes les 3 s, un slasher sans proie proche « flaire » un colon dehors à moins de 56 blocs
       'execute if score $tvq3 mg.st matches 0 as @e[tag=mg.tvraptor,tag=!mg.tvnetted] at @s unless entity @a[tag=mg.tvout,distance=..14] if entity @a[tag=mg.tvout,gamemode=adventure,distance=..56] run damage @s 0.01 minecraft:generic by @p[tag=mg.tvout,gamemode=adventure,distance=..56]',
       'scoreboard players operation $tvq4 mg.st = $tvt mg.st', 'scoreboard players set #400 mg.st 400', 'scoreboard players operation $tvq4 mg.st %= #400 mg.st',
       'execute if score $tvq4 mg.st matches 0 run function mg:terra/herb_fill',
       'execute if score $tvq4 mg.st matches 200 as @e[tag=mg.tvhos,tag=!mg.tvhunt] at @s unless entity @a[tag=mg.tvw,distance=..80] run tp @s ~ -400 ~',
       # défenses du périmètre, herbivores égarés
       f'execute as @e[tag=mg.tvhos,{COLONY_BOX}] at @s run function mg:terra/zap',
       f'execute as @e[tag=mg.tvherb,{COLONY_BOX}] unless predicate mg:has_passenger run tp @s @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1]',
       # brachiosaure monté sans selle (impossible à diriger) : sellé d'office
       'execute as @e[tag=mg.tvbrach] if predicate mg:has_passenger unless items entity @s saddle minecraft:saddle run function mg:terra/brach_saddle',
       # carnotaure
       f'execute as @e[tag=mg.tvcarno,tag=!mg.tvnetted] at @s unless entity @s[{COLONY_BOX}] run function mg:terra/carno_smash',
       'execute unless entity @e[tag=mg.tvcarno] run bossbar set mg:tvcarno players',
       'execute as @e[tag=mg.tvhunt,limit=1] at @s run function mg:terra/carno_bar',
       'execute unless entity @e[tag=mg.tvhunt] as @e[tag=mg.tvcarno,limit=1] at @s run function mg:terra/carno_bar',
       # ambiance
       'execute store result score $tvr mg.st run random value 0..29',
       'execute if score $tvr mg.st matches 0..9 as @e[tag=mg.tvraptor,sort=random,limit=1] at @s run playsound minecraft:entity.fox.screech hostile @a ~ ~ ~ 1.2 0.75',
       'execute if score $tvr mg.st matches 10..12 as @e[tag=mg.tvcarno,sort=random,limit=1] at @s run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 0.6',
       'execute if score $tvr mg.st matches 13..15 as @e[tag=mg.tvbrach,sort=random,limit=1] at @s run playsound minecraft:entity.camel.ambient neutral @a ~ ~ ~ 2.5 0.45',
       'execute if score $tvr mg.st matches 16..17 as @e[tag=mg.tvpachy,sort=random,limit=1] at @s run playsound minecraft:entity.goat.ambient neutral @a ~ ~ ~ 1.2 0.6',
       'execute if score $tvr mg.st matches 18 as @a[tag=mg.tvout,sort=random,limit=1] at @s run playsound minecraft:entity.parrot.ambient ambient @s ~ ~8 ~ 0.6 0.8',
       '# RPG (régions, campagne, boss) ; dinosaures d\'une session précédente restés dans une zone non chargée : retirés',
       'function mg:terra/rpg/second',
       'execute as @e[tag=mg.tvd,tag=!mg.trmount] unless score @s mg.tvses = $tvses mg.st run tp @s ~ -400 ~']
w('terra/second', SEC)
