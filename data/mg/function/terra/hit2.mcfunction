# @s (dinosaure) touché par une impulsion
# précision du tireur : +1 dégât tous les 2 points (chiffre affiché au-dessus de la cible)
execute if entity @a[tag=mg.tvsh,scores={mg.trs4=8..}] run function mg:terra/hitd {d:9}
execute if entity @a[tag=mg.tvsh,scores={mg.trs4=6..7}] run function mg:terra/hitd {d:8}
execute if entity @a[tag=mg.tvsh,scores={mg.trs4=4..5}] run function mg:terra/hitd {d:7}
execute if entity @a[tag=mg.tvsh,scores={mg.trs4=2..3}] run function mg:terra/hitd {d:6}
execute unless entity @a[tag=mg.tvsh,scores={mg.trs4=2..}] run function mg:terra/hitd {d:5}
tag @s add mg.tvhitn
particle minecraft:crit ~ ~ ~ 0 0 0 0 1
particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0.3 10
execute as @a[tag=mg.tvsh] at @s run playsound minecraft:entity.arrow.hit_player player @s ~ ~ ~ 0.4 1.5
