# Phase 2 : le Comte devient invisible 10 s et invoque des nuées de vexes
tag @e[tag=mg.boss] add mg.ph2
effect give @e[tag=mg.boss] minecraft:invisibility 10 0 true
scoreboard players set $bpc mg.st 0
bossbar set mg:boss color purple
title @a title [{"text":"PHASE II","color":"dark_purple","bold":true}]
title @a subtitle [{"text":"Le Comte s'évanouit dans les ombres...","color":"gray"}]
tellraw @a [{"text":"  ☠ ","color":"dark_red"},{"text":"Le Comte de Sang disparaît et lâche ses vexes !","color":"dark_purple","bold":true}]
execute as @a at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.6 0.5
function mg:mobarena/cathedral/vexes
