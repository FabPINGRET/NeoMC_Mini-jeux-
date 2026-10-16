# Fin de la campagne : honneurs, titre de héros, générique
scoreboard players add @s mg.tvc 1000
function mg:terra/rpg/xp {n:1500}
function mg:terra/rpg/ch {n:100}
function mg:terra/rpg/cs/finale
title @s times 20 100 30
title @s title {"text":"HÉROS DE TERRA NOVA","color":"gold","bold":true}
title @s subtitle {"text":"La colonie te doit sa survie","color":"yellow"}
tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a terminé la campagne de Terra Nova !","color":"gold"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @a ~ ~ ~ 1 0.8
execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;16766720,16777215],has_trail:true}]}}}}
tellraw @s [{"text":"\n— Terra Nova —\n","color":"green","bold":true},{"text":"Une campagne NeoMC. Merci d'avoir joué !\n","color":"gray"},{"text":"Le bestiaire, les œufs d'ambre et les boss t'attendent toujours.","color":"aqua"}]
