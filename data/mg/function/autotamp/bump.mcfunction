# @s = bateau sans délai : un autre bateau tout près ET plus rapide (≥ 15) → @s est tamponné
scoreboard players set $ms mg.st 0
execute as @e[type=#mg:at_boats,tag=mg.atb,distance=0.01..2] run scoreboard players operation $ms mg.st > @s mg.atv
execute if score $ms mg.st matches ..14 run return 0
execute unless score @s mg.atv < $ms mg.st run return 0
scoreboard players set @s mg.atc 20
execute as @e[type=#mg:at_boats,tag=mg.atb,distance=0.01..2] if score @s mg.atv = $ms mg.st run function mg:autotamp/pusher
execute on passengers if entity @s[type=minecraft:player,tag=mg.play] run function mg:autotamp/hit
execute at @s run particle minecraft:crit ~ ~0.8 ~ 0.6 0.4 0.6 0.4 25 force
execute at @s run playsound minecraft:entity.zombie.attack_wooden_door master @a ~ ~ ~ 0.9 1.4
