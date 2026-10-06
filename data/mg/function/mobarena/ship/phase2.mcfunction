# Phase 2 : la cage de verre se brise, le Wither est libéré
fill -3 65 10697 3 73 10703 minecraft:air
data modify entity @e[tag=mg.boss,limit=1] NoAI set value 0b
tag @e[tag=mg.boss] add mg.ph2
effect clear @a[tag=mg.play] minecraft:levitation
effect give @a[tag=mg.play] minecraft:slow_falling 6 0 true
scoreboard players set $bpc mg.st 0
bossbar set mg:boss color purple
title @a title [{"text":"PHASE II","color":"dark_purple","bold":true}]
title @a subtitle [{"text":"Le verre se brise !","color":"light_purple"}]
tellraw @a [{"text":"  ☠ ","color":"dark_red"},{"text":"La cage vole en éclats : le Cœur I.A. est libre !","color":"light_purple","bold":true}]
execute as @a at @s run playsound minecraft:block.glass.break master @s ~ ~ ~ 1 0.5
execute as @a at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.6 1.2
function mg:mobarena/ship/endermen
