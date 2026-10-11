# @s : gagnant de l'événement
scoreboard players add @s mg.evw 1
item replace entity @s armor.head with minecraft:golden_helmet[minecraft:item_name={"text":"👑 Couronne de champion","color":"gold","bold":true},minecraft:enchantment_glint_override=true,minecraft:unbreakable={},minecraft:custom_data={mg_ev:1b}]
tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" remporte l'événement ! (","color":"gold"},{"score":{"name":"@s","objective":"mg.evw"},"color":"yellow"},{"text":" victoire(s) d'événement)","color":"gold"}]
title @s title {"text":"🏆 Champion !","color":"gold","bold":true}
execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;16766720,16777215],has_twinkle:true}]}}}}
execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:30,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:2,explosions:[{shape:"large_ball",colors:[I;16711680,65535],has_trail:true}]}}}}
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
