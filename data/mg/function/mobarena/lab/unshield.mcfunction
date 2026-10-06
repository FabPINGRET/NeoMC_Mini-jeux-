data modify entity @e[tag=mg.boss,limit=1] Invulnerable set value 0b
tag @e[tag=mg.boss] remove mg.shield
bossbar set mg:boss color red
title @a title [{"text":"BOUCLIER BRISÉ !","color":"gold","bold":true}]
title @a subtitle [{"text":"L'Abomination est vulnérable !","color":"red"}]
execute as @a at @s run playsound minecraft:block.glass.break master @s ~ ~ ~ 1 0.5
