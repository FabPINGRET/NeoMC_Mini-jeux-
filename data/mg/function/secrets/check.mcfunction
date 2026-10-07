# Secrets du spawn : vérifications (toutes les 0,5 s, @s = joueur du spawn, à sa position)
execute unless entity @s[advancements={mg:secrets/terrier=true}] if entity @s[x=-29,y=55,z=-32,dx=8,dy=4,dz=6] run advancement grant @s only mg:secrets/terrier
execute unless entity @s[advancements={mg:secrets/couronne=true}] if entity @s[x=-58,y=84,z=-0.3,dx=24,dy=2,dz=0.6] run advancement grant @s only mg:secrets/couronne
execute unless entity @s[advancements={mg:secrets/plongeon=true}] if entity @s[x=27,y=61.5,z=-33,dx=6,dy=1,dz=6] if block ~ ~ ~ minecraft:water run advancement grant @s only mg:secrets/plongeon
execute unless entity @s[advancements={mg:secrets/arsenal=true}] if items entity @s container.* minecraft:warped_fungus_on_a_stick if items entity @s container.* minecraft:blaze_rod if items entity @s container.* minecraft:wind_charge if items entity @s container.* minecraft:snowball run advancement grant @s only mg:secrets/arsenal
execute unless entity @s[advancements={mg:secrets/ile=true}] if entity @s[x=26,y=90.5,z=-36,dx=10,dy=3,dz=10] run advancement grant @s only mg:secrets/ile
execute unless entity @s[advancements={mg:secrets/ile=true}] if entity @s[x=-39,y=94.5,z=26,dx=10,dy=3,dz=10] run advancement grant @s only mg:secrets/ile
execute unless entity @s[advancements={mg:secrets/ile=true}] if entity @s[x=-35,y=98.5,z=-39,dx=8,dy=3,dz=8] run advancement grant @s only mg:secrets/ile
execute unless entity @s[advancements={mg:secrets/ile=true}] if entity @s[x=33,y=96.5,z=27,dx=8,dy=3,dz=8] run advancement grant @s only mg:secrets/ile
execute unless entity @s[advancements={mg:secrets/ile=true}] if entity @s[x=-9,y=104.5,z=27,dx=6,dy=3,dz=6] run advancement grant @s only mg:secrets/ile
execute if entity @s[x=-1,y=64,z=-1,dx=2,dy=1,dz=2,x_rotation=-90..-75] run scoreboard players add @s mg.eup 10
execute unless entity @s[x=-1,y=64,z=-1,dx=2,dy=1,dz=2,x_rotation=-90..-75] run scoreboard players set @s mg.eup 0
execute unless entity @s[advancements={mg:secrets/etoiles=true}] if score @s mg.eup matches 60.. run advancement grant @s only mg:secrets/etoiles
tag @s[x=-56,y=64,z=-10,dx=20,dy=6,dz=20] add mg.ev1
tag @s[x=64,y=63,z=-4,dx=6,dy=4,dz=8] add mg.ev2
tag @s[x=-6,y=63,z=-53,dx=12,dy=6,dz=12] add mg.ev3
tag @s[x=-5,y=63,z=43,dx=10,dy=4,dz=10] add mg.ev4
tag @s[x=-4,y=63,z=62,dx=8,dy=5,dz=8] add mg.ev5
execute unless entity @s[advancements={mg:secrets/visite=true}] if entity @s[tag=mg.ev1,tag=mg.ev2,tag=mg.ev3,tag=mg.ev4,tag=mg.ev5] run advancement grant @s only mg:secrets/visite
scoreboard players remove @s[scores={mg.ept=1..}] mg.ept 10
execute unless score @s mg.ept matches 1.. if predicate mg:sneak positioned -11.5 68 39.5 if entity @s[distance=..0.9] run function mg:secrets/pipe {x:12.5,z:57.5}
execute unless score @s mg.ept matches 1.. if predicate mg:sneak positioned 12.5 68 57.5 if entity @s[distance=..0.9] run function mg:secrets/pipe {x:-11.5,z:39.5}
execute unless score @s mg.ept matches 1.. if predicate mg:sneak positioned 12.5 68 39.5 if entity @s[distance=..0.9] run function mg:secrets/pipe {x:-11.5,z:57.5}
execute unless score @s mg.ept matches 1.. if predicate mg:sneak positioned -11.5 68 57.5 if entity @s[distance=..0.9] run function mg:secrets/pipe {x:12.5,z:39.5}
