# Armes de Neo GTA au lobby (chaque tick, avant lobby/armory_tick)
execute if score $lan mg.t matches 5 unless entity @e[type=minecraft:interaction,tag=mg.lgi,scores={mg.st=7}] run function mg:lobby/guns_build
execute as @e[type=minecraft:interaction,tag=mg.lgi] if data entity @s interaction run function mg:lobby/guns_take
execute as @e[type=minecraft:interaction,tag=mg.lgi] if data entity @s attack run function mg:lobby/guns_take
tag @a remove mg.lgn2
execute as @e[type=minecraft:interaction,tag=mg.lgi] at @s run function mg:lobby/guns_near
tag @a[tag=mg.lgn,tag=!mg.lgn2] remove mg.lgn
tag @a[tag=mg.lgn2] add mg.lgn
execute as @e[type=minecraft:item_display,tag=mg.lrkt] at @s run function mg:lobby/rkt_tick
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] unless items entity @s weapon.mainhand *[custom_data~{lrpg:1b}] run function mg:gun/bar
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw] unless items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/bar_clear
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw] if items entity @s weapon.mainhand *[custom_data~{lrpg:1b}] run function mg:gun/bar_clear
execute unless score $state mg.st matches 0 run return 0
scoreboard players remove @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.lrc=1..}] mg.lrc 1
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{lrpg:1b}] at @s run function mg:lobby/rpg_fire
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:lobby/gun_shot
scoreboard players reset @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.gqs=1..}] mg.gqs
scoreboard players remove @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.gcd=1..}] mg.gcd 1
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.grl=1..}] at @s run function mg:gun/reload_tick
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.gsn=1..}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gun/sneak
scoreboard players reset @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,scores={mg.gsn=1..}] mg.gsn
execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] unless items entity @s weapon.mainhand *[custom_data~{lrpg:1b}] run function mg:gun/hud
