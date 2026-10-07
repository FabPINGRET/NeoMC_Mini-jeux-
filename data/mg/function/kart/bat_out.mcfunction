# @s n'a plus de ballon : éliminé, son kart explose, il regarde la suite d'en haut
tag @s add mg.kout
tag @s add mg.kfin
scoreboard players add $kouto mg.st 1
scoreboard players operation @s mg.kfp = $kouto mg.st
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st at @s run particle minecraft:explosion_emitter ~ ~0.5 ~ 0 0 0 0 1
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st at @s run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 0.8
ride @s dismount
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st on passengers unless entity @s[type=minecraft:player] run kill @s
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st run kill @s
execute as @e[type=minecraft:item_display,tag=mg.kcam] if score @s mg.ri = $me mg.st run kill @s
execute as @e[type=minecraft:item_display,tag=mg.khead] if score @s mg.ri = $me mg.st run kill @s
gamemode spectator @s
function mg:kart/t3/spec_tp
title @s title [{"text":"ÉLIMINÉ","color":"red","bold":true}]
title @s subtitle [{"text":"Plus de ballon : regarde la fin de la bataille","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"🎈 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a perdu tous ses ballons !","color":"gray"}]
