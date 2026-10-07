# Joueur de survie dans le monde des mini-jeux (@s) : retour du Nether par un portail, ou réapparition sans lit
execute store result score $svx mg.st run data get entity @s Pos[0]
execute store result score $svz mg.st run data get entity @s Pos[2]
execute store result storage mg:survie id.id int 1 run scoreboard players get @s mg.svid
# Près du lobby ou des arènes : réapparition sans lit → retour au point de départ du joueur
execute if score $svx mg.st matches -20000..20000 if score $svz mg.st matches -20000..40000 run return run function mg:survie/home with storage mg:survie id
# Sinon : arrivée par un portail du Nether → même x / z dans le monde de survie, à la surface
execute store result storage mg:survie w.x int 1 run scoreboard players get $svx mg.st
execute store result storage mg:survie w.z int 1 run scoreboard players get $svz mg.st
function mg:survie/portal with storage mg:survie w
