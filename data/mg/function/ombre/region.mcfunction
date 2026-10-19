# Chaque seconde, @s : région (0 cité, 1..8), accès, titre
scoreboard players set $r mg.st 0
execute if entity @s[x=-240,y=-64,z=-80,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 1
execute if entity @s[x=-240,y=-64,z=-240,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 2
execute if entity @s[x=-80,y=-64,z=-240,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 3
execute if entity @s[x=80,y=-64,z=-240,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 4
execute if entity @s[x=80,y=-64,z=-80,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 5
execute if entity @s[x=80,y=-64,z=80,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 6
execute if entity @s[x=-80,y=-64,z=80,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 7
execute if entity @s[x=-240,y=-64,z=80,dx=159,dy=400,dz=159] run scoreboard players set $r mg.st 8
execute if score $r mg.st matches 1 unless score @s mg.olch matches 3.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
execute if score $r mg.st matches 2 unless score @s mg.olch matches 11.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
execute if score $r mg.st matches 3 unless score @s mg.olch matches 16.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
execute if score $r mg.st matches 4 unless score @s mg.olch matches 23.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
execute if score $r mg.st matches 5 unless score @s mg.olch matches 29.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
execute if score $r mg.st matches 6 unless score @s mg.olch matches 35.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
execute if score $r mg.st matches 7 unless score @s mg.olch matches 40.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
execute if score $r mg.st matches 8 unless score @s mg.olch matches 46.. unless entity @s[tag=mg.olfree] run return run function mg:ombre/deny
function mg:ombre/save_pos
execute unless score @s mg.olrg = $r mg.st run function mg:ombre/region_chg
