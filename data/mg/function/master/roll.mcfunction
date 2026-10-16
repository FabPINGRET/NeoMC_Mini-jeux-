# @s : ordre personnel (tour « chacun sa consigne »)
execute store result score @s mg.mo run random value 1..10
scoreboard players set @s mg.mv 1
execute store result score $r mg.st run random value 1..100
execute if score @s mg.mo matches 1..3 if score $r mg.st matches ..35 run scoreboard players set @s mg.mv 0
