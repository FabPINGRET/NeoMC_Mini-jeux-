# @s : la bombe à fragmentation s'ouvre en 7 sous-munitions
execute store result score $mx mg.st run data get entity @s Motion[0] 1000
execute store result score $my mg.st run data get entity @s Motion[1] 1000
execute store result score $mz mg.st run data get entity @s Motion[2] 1000
scoreboard players operation $bid mg.st = @s mg.bid
execute summon minecraft:tnt run function mg:bomber/bomblet
execute summon minecraft:tnt run function mg:bomber/bomblet
execute summon minecraft:tnt run function mg:bomber/bomblet
execute summon minecraft:tnt run function mg:bomber/bomblet
execute summon minecraft:tnt run function mg:bomber/bomblet
execute summon minecraft:tnt run function mg:bomber/bomblet
execute summon minecraft:tnt run function mg:bomber/bomblet
particle minecraft:firework ~ ~0.5 ~ 0.3 0.3 0.3 0.15 25 force
playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 3 0.8
kill @s
