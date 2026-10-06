# Caméra des joueurs du plateau : chacun tourne autour du pion actif avec sa souris (vue derrière lui, à 10 blocs)
execute if entity @e[type=minecraft:armor_stand,tag=mg.mpfocus] as @a[tag=mg.mpp,tag=mg.play,tag=!mg.mpview,tag=!mg.mpfree,gamemode=spectator] run function mg:party/cam_one
