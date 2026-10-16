# Région Mont Cendre (un joueur y est) : complète la population près des joueurs
execute store result score $n mg.st if entity @e[tag=mg.tvs_carno,tag=mg.trr_s]
execute if score $n mg.st matches ..1 run function mg:terra/rpg/sp/s_carno
execute store result score $n mg.st if entity @e[tag=mg.tvs_ankylo,tag=mg.trr_s]
execute if score $n mg.st matches ..2 run function mg:terra/rpg/sp/s_ankylo
execute store result score $n mg.st if entity @e[tag=mg.tvs_raptor,tag=mg.trr_s]
execute if score $n mg.st matches ..5 run function mg:terra/rpg/sp/s_raptor
execute store result score $n mg.st if entity @e[tag=mg.tvs_compy,tag=mg.trr_s]
execute if score $n mg.st matches ..7 run function mg:terra/rpg/sp/s_compy
