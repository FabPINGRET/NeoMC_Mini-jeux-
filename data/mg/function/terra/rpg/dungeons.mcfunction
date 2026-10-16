# Chaque seconde : donjons (déclenchement de l'alpha à l'approche, suivi, victoire)
scoreboard players remove $trdc0 mg.st 1
execute if score $trda0 mg.st matches 1 unless entity @e[tag=mg.trdg_arbre] run function mg:terra/rpg/dg/arbre_win
execute unless score $trda0 mg.st matches 1 if score $trdc0 mg.st matches ..0 positioned 55.5 102 -177.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/arbre_start
execute if score $trda0 mg.st matches 1 run function mg:terra/rpg/dg/arbre
scoreboard players remove $trdc1 mg.st 1
execute if score $trda1 mg.st matches 1 unless entity @e[tag=mg.trdg_pic] run function mg:terra/rpg/dg/pic_win
execute unless score $trda1 mg.st matches 1 if score $trdc1 mg.st matches ..0 positioned 228.5 114 24.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/pic_start
execute if score $trda1 mg.st matches 1 run function mg:terra/rpg/dg/pic
scoreboard players remove $trdc2 mg.st 1
execute if score $trda2 mg.st matches 1 unless entity @e[tag=mg.trdg_mine] run function mg:terra/rpg/dg/mine_win
execute unless score $trda2 mg.st matches 1 if score $trdc2 mg.st matches ..0 positioned -224.5 65 -54.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/mine_start
execute if score $trda2 mg.st matches 1 run function mg:terra/rpg/dg/mine
scoreboard players remove $trdc3 mg.st 1
execute if score $trda3 mg.st matches 1 unless entity @e[tag=mg.trdg_tube] run function mg:terra/rpg/dg/tube_win
execute unless score $trda3 mg.st matches 1 if score $trdc3 mg.st matches ..0 positioned -23.5 90 186.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/tube_start
execute if score $trda3 mg.st matches 1 run function mg:terra/rpg/dg/tube
