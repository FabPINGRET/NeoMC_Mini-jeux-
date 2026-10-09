# @s = joueur : GO, gravité de course de son parcours (mg.xcr), sans turbo (groupe : go ; solo : solo/go)
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/grav
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/grav
scoreboard players set @s mg.xu 0
