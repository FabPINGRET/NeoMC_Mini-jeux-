# Remet 10 quilles sur la piste #ln (les anciennes de la piste sont retirées)
execute as @e[type=minecraft:block_display,tag=mg.bpin] if score @s mg.bln = #ln mg.st run kill @s
execute if score #ln mg.st matches 0 run function mg:bowl/rack_0
execute if score #ln mg.st matches 1 run function mg:bowl/rack_1
execute if score #ln mg.st matches 2 run function mg:bowl/rack_2
execute if score #ln mg.st matches 3 run function mg:bowl/rack_3
execute if score #ln mg.st matches 4 run function mg:bowl/rack_4
execute if score #ln mg.st matches 5 run function mg:bowl/rack_5
execute if score #ln mg.st matches 6 run function mg:bowl/rack_6
execute if score #ln mg.st matches 7 run function mg:bowl/rack_7
