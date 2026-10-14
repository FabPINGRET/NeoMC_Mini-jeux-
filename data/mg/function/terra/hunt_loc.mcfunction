# Localisateurs des chasseurs de carnotaure : vers le carnotaure traqué
execute as @e[tag=mg.tvhunt,limit=1] run function mg:terra/mark_loc
execute if entity @e[tag=mg.tvhunt] as @a[tag=mg.tvw,scores={mg.tvm=4}] run function mg:terra/loc with storage mg:terra h
