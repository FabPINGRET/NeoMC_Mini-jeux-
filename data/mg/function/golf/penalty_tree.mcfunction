# @s = balle : 🌳 Balle injouable dans un arbre → +1 coup, replacée au dernier point sec
execute at @s run playsound minecraft:block.azalea_leaves.break master @a ~ ~ ~ 1 1
execute at @s run particle minecraft:poof ~ ~0.3 ~ 0.2 0.2 0.2 0.02 10 force
scoreboard players operation $cur mg.st = @s mg.gfi
execute as @a[tag=mg.play] if score @s mg.gfi = $cur mg.st run tellraw @s [{"text":"🌳 Balle injouable dans un arbre","color":"aqua"},{"text":" : +1 coup, balle replacée.","color":"gray"}]
execute as @a[tag=mg.play] if score @s mg.gfi = $cur mg.st run scoreboard players add @s mg.gfc 1
scoreboard players operation @s mg.gfx = @s mg.gflx
scoreboard players operation @s mg.gfy = @s mg.gfly
scoreboard players operation @s mg.gfz = @s mg.gflz
execute store result entity @s Pos[0] double 0.001 run scoreboard players get @s mg.gfx
execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy
execute store result entity @s Pos[2] double 0.001 run scoreboard players get @s mg.gfz
tag @s add mg.gfg
tag @s remove mg.gfmv
scoreboard players set @s mg.gfu 0
scoreboard players set @s mg.gfv 0
scoreboard players set @s mg.gfw 0
execute as @a[tag=mg.play] if score @s mg.gfi = $cur mg.st run function mg:golf/next
