# Caméra 3/4 (vue du ciel en diagonale) sur le pion actif, pour tous les joueurs du plateau
execute as @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] at @s run tp @a[tag=mg.mpp,tag=mg.play,tag=!mg.mpview,tag=!mg.mpfree,gamemode=spectator] ~6 ~8 ~6 facing entity @s eyes
