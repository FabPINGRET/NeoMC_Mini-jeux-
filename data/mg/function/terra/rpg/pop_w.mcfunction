# Région Canyon des Renégats (un joueur y est) : complète la population près des joueurs
execute store result score $n mg.st if entity @e[tag=mg.tvs_raptor,tag=mg.trr_w]
execute if score $n mg.st matches ..5 run function mg:terra/rpg/sp/w_raptor
execute store result score $n mg.st if entity @e[tag=mg.tvs_ptera,tag=mg.trr_w]
execute if score $n mg.st matches ..3 run function mg:terra/rpg/sp/w_ptera
execute store result score $n mg.st if entity @e[tag=mg.tvs_dilo,tag=mg.trr_w]
execute if score $n mg.st matches ..1 run function mg:terra/rpg/sp/w_dilo
execute store result score $n mg.st if entity @e[tag=mg.trsix,tag=mg.trr_w]
execute if score $n mg.st matches ..7 run function mg:terra/rpg/sp/w_sixer
