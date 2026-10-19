# Os orphelins (créature morte) : retirés (chaque seconde)
execute as @e[type=minecraft:item_display,tag=mg.olbp] run function mg:ombre/bclean_one
execute as @e[type=minecraft:block_display,tag=mg.olbp] run function mg:ombre/bclean_one
