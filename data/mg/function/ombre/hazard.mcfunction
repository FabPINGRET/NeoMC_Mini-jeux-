# Toutes les 2 s, @s : dangers des régions (froid, chaleur, ténèbres) sans protection
execute if score @s mg.olrg matches 3 unless score @s mg.olfur matches 1.. unless entity @s[x=-24,y=60,z=-140,dx=48,dy=40,dz=40] run function mg:ombre/hz/cold
execute if score @s mg.olrg matches 6 unless score @s mg.olfire matches 1.. unless entity @s[x=120,y=60,z=90,dx=40,dy=30,dz=40] run function mg:ombre/hz/heat
execute if score @s mg.olrg matches 8 unless score @s mg.olbless matches 1.. run function mg:ombre/hz/dark
