# Vol d'un mouton (@s = mouton, à sa position) : 4 sous-pas de vitesse/4 avec test de collision, puis gravité et frottement
# (mêmes valeurs qu'un bloc tombant). Le serveur déplace le mouton : les joueurs le voient exactement où il est.
execute store result storage mg:sw d.x double 0.00025 run scoreboard players get @s mg.svx
execute store result storage mg:sw d.y double 0.00025 run scoreboard players get @s mg.svy
execute store result storage mg:sw d.z double 0.00025 run scoreboard players get @s mg.svz
execute at @s run function mg:sheepwar/fly_step with storage mg:sw d
execute if entity @s[tag=mg.fly] at @s run function mg:sheepwar/fly_step with storage mg:sw d
execute if entity @s[tag=mg.fly] at @s run function mg:sheepwar/fly_step with storage mg:sw d
execute if entity @s[tag=mg.fly] at @s run function mg:sheepwar/fly_step with storage mg:sw d
scoreboard players set #98 mg.st 98
scoreboard players set #100 mg.st 100
scoreboard players remove @s mg.svy 40
scoreboard players operation @s mg.svx *= #98 mg.st
scoreboard players operation @s mg.svx /= #100 mg.st
scoreboard players operation @s mg.svy *= #98 mg.st
scoreboard players operation @s mg.svy /= #100 mg.st
scoreboard players operation @s mg.svz *= #98 mg.st
scoreboard players operation @s mg.svz /= #100 mg.st
