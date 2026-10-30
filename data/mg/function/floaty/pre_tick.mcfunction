# Avant survie/tick : un joueur de la carte hors de sa dimension quitte ; un joueur dans la dimension sans y être inscrit est renvoyé (admins exceptés)
execute as @a[tag=mg.flw] at @s unless dimension mg:floaty run function mg:floaty/strayed
execute as @a[tag=!mg.flw,tag=!mg.admin] at @s if dimension mg:floaty run function mg:floaty/intruder
