# @s = joueur à replacer au dernier point de reprise de son parcours (mg.xcr)
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/respawn
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/respawn
