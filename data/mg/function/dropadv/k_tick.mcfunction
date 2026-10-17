# Passer un niveau : clic droit sur l'objet (mg.qs), puis décompte de la confirmation (mg.dkc) et de l'anti-maintien (mg.dku)
execute as @a[tag=mg.play,tag=!mg.ddone,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{mg_dskip:1b}] run function mg:dropadv/k_use
scoreboard players reset @a[tag=mg.play,scores={mg.qs=1..}] mg.qs
scoreboard players remove @a[tag=mg.play,scores={mg.dkc=1..}] mg.dkc 1
scoreboard players remove @a[tag=mg.play,scores={mg.dku=1..}] mg.dku 1
execute if score $dam mg.st matches 0 as @e[type=minecraft:item,x=-20,y=0,z=23980,dx=520,dy=308,dz=40] if items entity @s contents *[custom_data~{mg_dskip:1b}] run kill @s
