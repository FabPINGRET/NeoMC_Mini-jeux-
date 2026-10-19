# 🌙 Ombrelune : chaque tick tant qu'un joueur y est (contexte : dimension)
scoreboard players add $olt mg.st 1
scoreboard players operation $olq mg.st = $olt mg.st
scoreboard players operation $olq mg.st %= #20 mg.st
scoreboard players operation $olq2 mg.st = $olt mg.st
scoreboard players operation $olq2 mg.st %= #2 mg.st
scoreboard players operation $olq4 mg.st = $olt mg.st
scoreboard players operation $olq4 mg.st %= #4 mg.st
scoreboard players operation $olq5 mg.st = $olt mg.st
scoreboard players operation $olq5 mg.st %= #5 mg.st
scoreboard players operation $olq60 mg.st = $olt mg.st
scoreboard players operation $olq60 mg.st %= #60 mg.st
scoreboard players operation $olq100 mg.st = $olt mg.st
scoreboard players operation $olq100 mg.st %= #100 mg.st
scoreboard players set #8 mg.st 8
# objets, potions, choix, interactions
execute as @a[tag=mg.olw,scores={mg.olq=1..}] at @s run function mg:ombre/use
scoreboard players reset @a[scores={mg.olq=1..}] mg.olq
execute as @a[tag=mg.olw,scores={mg.olhb=1..}] run function mg:ombre/mana_pot
execute as @a[tag=mg.olw,scores={mg.oltk=1..}] run function mg:ombre/tk
execute as @a[tag=mg.olw,scores={mg.oldt=1..}] run function mg:ombre/m/hurt
execute as @e[type=minecraft:interaction,tag=mg.olnpc] if data entity @s interaction run function mg:ombre/npc/int
execute as @e[type=minecraft:interaction,tag=mg.olway] if data entity @s interaction run function mg:ombre/way_int
execute as @e[type=minecraft:interaction,tag=mg.olint] if data entity @s interaction run function mg:ombre/q/int
execute as @e[type=minecraft:interaction,tag=mg.olint] if data entity @s attack run function mg:ombre/q/int
execute as @e[type=minecraft:interaction,tag=mg.oljar] if data entity @s interaction run function mg:ombre/boss/jar_int
execute as @e[type=minecraft:interaction,tag=mg.oljar] if data entity @s attack run function mg:ombre/boss/jar_int
execute as @e[type=minecraft:interaction,tag=mg.olpill] if data entity @s interaction run function mg:ombre/boss/pill_int
execute as @e[type=minecraft:item_display,tag=mg.olspin] at @s run tp @s ~ ~ ~ ~4 ~
# créatures articulées : chaque tick près d'un joueur, sinon 2 fois par seconde
execute as @e[tag=mg.olbd] at @s if entity @a[tag=mg.olw,distance=..48] run function mg:ombre/bsync
execute if score $olq mg.st matches 0 as @e[tag=mg.olbd] at @s unless entity @a[tag=mg.olw,distance=..48] run function mg:ombre/bsync
execute if score $olq mg.st matches 10 as @e[tag=mg.olbd] at @s unless entity @a[tag=mg.olw,distance=..48] run function mg:ombre/bsync
function mg:ombre/cl/tick
function mg:ombre/m/web_tick
execute if score $olq5 mg.st matches 0 run function mg:ombre/q/coltick
execute if score $olq5 mg.st matches 0 run function mg:ombre/pg_tick
execute if score $olq5 mg.st matches 0 run function mg:ombre/tc_tick
execute if score $olq5 mg.st matches 0 as @a[tag=mg.olw,scores={mg.olpk=1..}] unless predicate mg:sneak run scoreboard players set @s mg.olpk 0
execute as @a[tag=mg.olcine] run function mg:ombre/cs/run
execute if score $olq mg.st matches 0 as @a[tag=mg.olw,tag=!mg.olcine,scores={mg.olon=1}] at @s run function mg:ombre/ind
execute if score $olq mg.st matches 10 as @a[tag=mg.olw,tag=!mg.olcine,scores={mg.olon=1}] at @s run function mg:ombre/ind
execute as @a[tag=mg.olw,scores={mg.deaths=1..}] run function mg:ombre/died
scoreboard players remove @a[tag=mg.olw,scores={mg.olal=1..}] mg.olal 1
execute if score $olq mg.st matches 0 run function mg:ombre/second
execute if score $olq mg.st matches 5 as @a[tag=mg.olw,tag=!mg.olcine,scores={mg.olal=..0}] run function mg:ombre/hud
execute if score $olq mg.st matches 15 as @a[tag=mg.olw,tag=!mg.olcine,scores={mg.olal=..0}] run function mg:ombre/hud
