tag @e[tag=mg.boss] add mg.ph2
bossbar set mg:boss color purple
title @a title [{"text":"PHASE II","color":"dark_red","bold":true}]
title @a subtitle [{"text":"Des météorites s'abattent sur l'arène !","color":"gold"}]
tellraw @a [{"text":"  ☠ ","color":"dark_red"},{"text":"Le Golem de Basalte fait pleuvoir des météorites !","color":"gold","bold":true}]
execute as @a at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 1 0.6
