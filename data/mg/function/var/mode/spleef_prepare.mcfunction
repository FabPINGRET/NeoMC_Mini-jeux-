# Spleef sur un autre sol ($ar) — appelé par spleef/prepare. Généré.
execute if score $ar mg.st matches 21 run function mg:var/floor/l21/build_snow
execute if score $ar mg.st matches 22 run function mg:var/floor/l22/build_snow
execute if score $ar mg.st matches 23 run function mg:var/floor/l23/build_snow
execute if score $ar mg.st matches 24 run function mg:var/floor/l24/build_snow
execute if score $ar mg.st matches 25 run function mg:var/floor/l25/build_snow
execute if score $ar mg.st matches 26 run function mg:var/floor/l26/build_snow
kill @e[type=minecraft:item,x=-40,y=40,z=24260,dx=80,dy=70,dz=80]
scoreboard players set $vsk1 mg.st 800
scoreboard players set $vsk2 mg.st 240
execute if score $dif mg.st matches 1 run scoreboard players set $vsk1 mg.st 1000
execute if score $dif mg.st matches 1 run scoreboard players set $vsk2 mg.st 300
execute if score $dif mg.st matches 3 run scoreboard players set $vsk1 mg.st 600
execute if score $dif mg.st matches 3 run scoreboard players set $vsk2 mg.st 180
execute if score $dif mg.st matches 4 run scoreboard players set $vsk1 mg.st 400
execute if score $dif mg.st matches 4 run scoreboard players set $vsk2 mg.st 120
execute if score $ar mg.st matches 21 run function mg:var/floor/l21/place
execute if score $ar mg.st matches 22 run function mg:var/floor/l22/place
execute if score $ar mg.st matches 23 run function mg:var/floor/l23/place
execute if score $ar mg.st matches 24 run function mg:var/floor/l24/place
execute if score $ar mg.st matches 25 run function mg:var/floor/l25/place
execute if score $ar mg.st matches 26 run function mg:var/floor/l26/place
