# @s : un bateau neuf (bois au hasard) à sa position, lié par mg.atid
execute unless score @s mg.atid matches 1.. run scoreboard players add $atn mg.st 1
execute unless score @s mg.atid matches 1.. run scoreboard players operation @s mg.atid = $atn mg.st
scoreboard players operation $p mg.st = @s mg.atid
execute as @e[type=#mg:at_boats,tag=mg.atb] if score @s mg.atid = $p mg.st run kill @s
execute store result score $r mg.st run random value 0..8
execute if score $r mg.st matches 0 run summon minecraft:oak_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 1 run summon minecraft:spruce_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 2 run summon minecraft:birch_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 3 run summon minecraft:jungle_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 4 run summon minecraft:acacia_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 5 run summon minecraft:dark_oak_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 6 run summon minecraft:mangrove_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 7 run summon minecraft:cherry_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute if score $r mg.st matches 8 run summon minecraft:pale_oak_boat ~ ~0.2 ~ {Tags:["mg.atb","mg.atn"],Invulnerable:1b}
execute as @e[tag=mg.atn] at @s run rotate @s facing 0 65 37400
scoreboard players operation @e[tag=mg.atn] mg.atid = $p mg.st
ride @s mount @e[tag=mg.atn,limit=1]
tag @e[tag=mg.atn] remove mg.atn
