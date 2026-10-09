# @s : frappe ! (balle mg.gfmy, joueur mg.gfme, $gfclub = 1 bois/fer, 2 putter)
scoreboard players reset @s mg.qs
scoreboard players add @s mg.gfc 1
scoreboard players set @s mg.gfs 1
scoreboard players operation $gfpw mg.st = @s mg.gfp
execute if score $gfpw mg.st matches ..2 run scoreboard players set $gfpw mg.st 3
execute as @e[tag=mg.gfmy,limit=1] at @s rotated as @a[tag=mg.gfme,limit=1] rotated ~ 0 positioned ^ ^ ^10 summon minecraft:marker run function mg:golf/dir
execute if score $gfclub mg.st matches 1 run function mg:golf/v_wood
execute if score $gfclub mg.st matches 2 run function mg:golf/v_putt
execute as @e[tag=mg.gfmy,limit=1] run function mg:golf/launch
execute if score $gfclub mg.st matches 1 run playsound minecraft:entity.player.attack.strong master @a ~ ~ ~ 1 1.4
execute if score $gfclub mg.st matches 2 run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1 1.6
title @s actionbar ""
