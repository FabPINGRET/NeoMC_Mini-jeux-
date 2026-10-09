# La roquette explose ici : destruction (rayon 3), 16 dégâts dans un rayon de 4, dollars pour les dégâts matériels
tag @e[tag=mg.grhit] remove mg.grhit
scoreboard players operation $bid mg.st = @s mg.bid
function mg:bomber/boom/r3
execute as @a[tag=mg.gtw] if score @s mg.bid = $bid mg.st run tag @s add mg.gro
execute as @e[tag=mg.gtg,distance=..4] run damage @s 16 minecraft:player_explosion by @a[tag=mg.gro,limit=1]
scoreboard players operation $gm mg.st = $bk mg.st
scoreboard players set #5 mg.st 5
scoreboard players operation $gm mg.st /= #5 mg.st
scoreboard players operation @a[tag=mg.gro] mg.gta += $gm mg.st
tag @a remove mg.gro
particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force
particle minecraft:flame ~ ~ ~ 1.5 1.2 1.5 0.12 40 force
particle minecraft:large_smoke ~ ~ ~ 1.6 1.2 1.6 0.06 30 force
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 5 0.8
kill @s
