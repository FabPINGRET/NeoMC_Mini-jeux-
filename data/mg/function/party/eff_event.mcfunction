# Case « ? » : une surprise au hasard parmi 4
execute store result score $ev mg.st run random value 1..4
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run playsound minecraft:block.amethyst_block.chime master @a[tag=mg.mpp] ~ ~ ~ 1 1
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run particle minecraft:totem_of_undying ~ ~1 ~ 0.5 0.8 0.5 0.2 30

execute if score $ev mg.st matches 1 run scoreboard players add @s mg.mpm 8
execute if score $ev mg.st matches 1 run tellraw @a[tag=mg.mpp] [{"text":"? JACKPOT ! ","color":"green","bold":true},{"selector":"@s","color":"yellow"},{"text":" gagne 8 pièces.","color":"gold"}]

execute if score $ev mg.st matches 2 run scoreboard players operation @s mg.mpi = $mps mg.st
execute if score $ev mg.st matches 2 run function mg:party/prev
execute if score $ev mg.st matches 2 run function mg:party/place
execute if score $ev mg.st matches 2 run tellraw @a[tag=mg.mpp] [{"text":"? TÉLÉPORTEUR ! ","color":"green","bold":true},{"selector":"@s","color":"yellow"},{"text":" est envoyé juste devant l'étoile.","color":"gray"}]

execute if score $ev mg.st matches 3 run function mg:party/ev_swap

execute if score $ev mg.st matches 4 as @a[tag=mg.mpp,tag=!mg.mpcur,scores={mg.mpm=2..}] run function mg:party/ev_give
execute if score $ev mg.st matches 4 run tellraw @a[tag=mg.mpp] [{"text":"? CADEAUX ! ","color":"green","bold":true},{"text":"Chaque adversaire donne 2 pièces à ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":".","color":"gray"}]
