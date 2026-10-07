# Garde les visiteurs de plots (spectateurs) dans la zone des plots
# Mauvaise dimension (téléport spectateur, survie...) ou trop loin du spawn → fin de visite
execute in mg:survie positioned 0.5 64 0.5 as @a[tag=mg.visit,distance=0..] run tellraw @s [{"text":"La visite des plots reste autour du spawn : retour.","color":"gray","italic":true}]
execute in mg:survie positioned 0.5 64 0.5 as @a[tag=mg.visit,distance=0..] run function mg:plot/leave
execute in minecraft:overworld positioned 0.5 70 0.5 as @a[tag=mg.visit,distance=250..] run tellraw @s [{"text":"La visite des plots reste autour du spawn : retour.","color":"gray","italic":true}]
execute in minecraft:overworld positioned 0.5 70 0.5 as @a[tag=mg.visit,distance=250..] run function mg:plot/leave
