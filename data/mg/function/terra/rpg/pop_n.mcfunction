# Région Marais des Brumes (un joueur y est) : complète la population près des joueurs
execute store result score $n mg.st if entity @e[tag=mg.tvs_dilo,tag=mg.trr_n]
execute if score $n mg.st matches ..5 run function mg:terra/rpg/sp/n_dilo
execute store result score $n mg.st if entity @e[tag=mg.tvs_compy,tag=mg.trr_n]
execute if score $n mg.st matches ..11 run function mg:terra/rpg/sp/n_compy
execute store result score $n mg.st if entity @e[tag=mg.tvs_raptor,tag=mg.trr_n]
execute if score $n mg.st matches ..2 run function mg:terra/rpg/sp/n_raptor
