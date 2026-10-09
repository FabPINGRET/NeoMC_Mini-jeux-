# @s : TROU EN UN !
tellraw @a[tag=!mg.surv] [{"text":"⛳ TROU EN UN ! ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" réussit le coup parfait !","color":"gold"}]
title @a[tag=mg.play] title {"text":"TROU EN UN !","color":"gold","bold":true}
title @a[tag=mg.play] subtitle [{"selector":"@s","color":"yellow"}]
execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;16766720,16777215],has_trail:true}]}}}}
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
function mg:golf/score
