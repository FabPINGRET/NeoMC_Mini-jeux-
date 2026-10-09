# 🎳 Nettoyage
kill @e[tag=mg.bowl]
clear @a minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_bowl:1b}]
tag @a remove mg.bwl
tag @a remove mg.bnr
data remove storage mg:bowl w
stopsound @a record minecraft:music_disc.cat
schedule clear mg:bowl/build_2
schedule clear mg:bowl/build_3
schedule clear mg:bowl/build_4
schedule clear mg:bowl/build_5
effect clear @a[tag=mg.play] minecraft:resistance
scoreboard players reset * mg.bsc
scoreboard players reset * mg.bph
scoreboard players reset * mg.bln
