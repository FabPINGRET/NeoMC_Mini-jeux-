data modify entity @e[tag=mg.boss,limit=1] Invulnerable set value 0b
tag @e[tag=mg.boss] remove mg.shield
bossbar set mg:boss color red
title @a title [{"text":"TENTACULES DÉTRUITS !","color":"gold","bold":true}]
title @a subtitle [{"text":"Frappez l'Émissaire !","color":"red"}]
execute as @a at @s run playsound minecraft:entity.elder_guardian.death master @s ~ ~ ~ 1 1.2
