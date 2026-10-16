# Chaque seconde : capacités des dinosaures (bond, crachat, charge, coup de queue, fuite)
execute as @e[tag=mg.tvraptor,tag=!mg.tvnetted,tag=!mg.trmount] at @s if entity @a[tag=mg.tvw,tag=mg.tvout,gamemode=adventure,distance=3..7] if predicate mg:tv_c33 run function mg:terra/rpg/ab/pounce
execute as @e[tag=mg.tvdilo,tag=!mg.tvnetted] at @s if entity @a[tag=mg.tvw,gamemode=adventure,distance=4..14] if predicate mg:tv_c50 run function mg:terra/rpg/ab/spit
execute as @e[tag=mg.tvcarno,tag=!mg.tvnetted] at @s if entity @a[tag=mg.tvw,gamemode=adventure,distance=6..18] if predicate mg:tv_c20 run function mg:terra/rpg/ab/charge
execute as @e[tag=mg.tvdef,tag=!mg.tvnetted] at @s if entity @a[tag=mg.tvw,gamemode=adventure,distance=..4.5] if predicate mg:tv_c50 run function mg:terra/rpg/ab/swipe
execute as @e[tag=mg.tvgalli] at @s if entity @a[tag=mg.tvw,distance=..7] run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw]
