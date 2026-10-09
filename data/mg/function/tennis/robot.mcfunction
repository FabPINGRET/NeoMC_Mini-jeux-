# @s : robot (à sa position) — se déplace vers la balle attendue (ou le centre de sa ligne de fond) et renvoie
execute store result score $tnrx mg.st run data get entity @s Pos[0] 1000
scoreboard players operation $tnrx mg.st -= $tncx mg.st
execute store result score $tnrz mg.st run data get entity @s Pos[2] 1000
scoreboard players remove $tnrz mg.st 35400500
scoreboard players set $tntx mg.st 0
scoreboard players set $tntz mg.st -14000
execute if score @s mg.tns matches 2 run scoreboard players set $tntz mg.st 14000
execute if entity @s[tag=mg.tnchase] run scoreboard players operation $tntx mg.st = @s mg.tnx
execute if entity @s[tag=mg.tnchase] run scoreboard players operation $tntz mg.st = @s mg.tnz
scoreboard players operation $tntx mg.st -= $tnrx mg.st
scoreboard players operation $tntz mg.st -= $tnrz mg.st
execute if score $tntx mg.st matches 201.. run scoreboard players set $tntx mg.st 200
execute if score $tntx mg.st matches ..-201 run scoreboard players set $tntx mg.st -200
execute if score $tntz mg.st matches 201.. run scoreboard players set $tntz mg.st 200
execute if score $tntz mg.st matches ..-201 run scoreboard players set $tntz mg.st -200
scoreboard players operation $tnrx mg.st += $tntx mg.st
scoreboard players operation $tnrz mg.st += $tntz mg.st
execute if entity @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,limit=1] run tp @s ~ ~ ~ facing entity @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,limit=1]
scoreboard players operation $tnrx mg.st += $tncx mg.st
scoreboard players add $tnrz mg.st 35400500
execute store result entity @s Pos[0] double 0.001 run scoreboard players get $tnrx mg.st
execute store result entity @s Pos[2] double 0.001 run scoreboard players get $tnrz mg.st
scoreboard players operation $tnside mg.st = @s mg.tns
tag @e[tag=mg.tnhit] remove mg.tnhit
execute if score @s mg.tnt matches 0 unless entity @s[tag=mg.tnmiss] positioned ~ ~1 ~ as @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,tag=mg.tnlive,scores={mg.tnb=1},distance=..2.3,limit=1] unless score @s mg.tnl = $tnside mg.st run tag @s add mg.tnhit
execute if entity @e[tag=mg.tnhit] run function mg:tennis/robot_hit
