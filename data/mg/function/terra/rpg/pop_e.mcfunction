# Région Plaines d'Ambre (un joueur y est) : complète la population près des joueurs
execute store result score $n mg.st if entity @e[tag=mg.tvs_trike,tag=mg.trr_e]
execute if score $n mg.st matches ..4 run function mg:terra/rpg/sp/e_trike
execute store result score $n mg.st if entity @e[tag=mg.tvs_stego,tag=mg.trr_e]
execute if score $n mg.st matches ..3 run function mg:terra/rpg/sp/e_stego
execute store result score $n mg.st if entity @e[tag=mg.tvs_ankylo,tag=mg.trr_e]
execute if score $n mg.st matches ..2 run function mg:terra/rpg/sp/e_ankylo
execute store result score $n mg.st if entity @e[tag=mg.tvs_galli,tag=mg.trr_e]
execute if score $n mg.st matches ..8 run function mg:terra/rpg/sp/e_galli
execute store result score $n mg.st if entity @e[tag=mg.tvs_brachio,tag=mg.trr_e]
execute if score $n mg.st matches ..1 run function mg:terra/rpg/sp/e_brachio
execute store result score $n mg.st if entity @e[tag=mg.tvs_ptera,tag=mg.trr_e]
execute if score $n mg.st matches ..2 run function mg:terra/rpg/sp/e_ptera
execute store result score $n mg.st if entity @e[tag=mg.tvs_raptor,tag=mg.trr_e]
execute if score $n mg.st matches ..2 run function mg:terra/rpg/sp/e_raptor
