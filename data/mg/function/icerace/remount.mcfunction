# @s = joueur sorti de son bateau : on ramène le bateau (ou on en crée un) et on remonte
scoreboard players operation $me mg.st = @s mg.ri
tag @e[tag=mg.ib] remove mg.mine
execute as @e[tag=mg.ib] if score @s mg.ri = $me mg.st run tag @s add mg.mine
execute unless entity @e[tag=mg.mine] at @s run summon minecraft:birch_boat ~ ~ ~ {Invulnerable:1b,Tags:["mg.ib","mg.mine"]}
scoreboard players operation @e[tag=mg.mine,limit=1] mg.ri = $me mg.st
tp @e[tag=mg.mine,limit=1] @s
ride @s mount @e[tag=mg.mine,limit=1]
tag @e[tag=mg.ib] remove mg.mine
