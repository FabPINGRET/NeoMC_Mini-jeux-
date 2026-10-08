# @s = joueur à replacer au dernier point de reprise de son parcours
execute if score $xc mg.st matches 1 run function mg:elyrace/c1/respawn
execute if score $xc mg.st matches 2 run function mg:elyrace/c2/respawn
