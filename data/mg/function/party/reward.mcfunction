# Fin d'un mini-jeu de la Mini Party (appelé par core/return_lobby avant la remise à zéro des joueurs)
scoreboard players add @a[tag=mg.mpp,tag=mg.win] mg.mpm 10
scoreboard players add @a[tag=mg.mpp,tag=!mg.win] mg.mpm 3
execute if entity @a[tag=mg.mpp,tag=mg.win] run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"text":"Mini-jeu terminé : ","color":"gray"},{"text":"+10 pièces","color":"gold"},{"text":" pour ","color":"gray"},{"selector":"@a[tag=mg.mpp,tag=mg.win]","color":"yellow","bold":true},{"text":", +3 pour les autres.","color":"gray"}]
execute unless entity @a[tag=mg.mpp,tag=mg.win] run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"text":"Mini-jeu terminé sans vainqueur : ","color":"gray"},{"text":"+3 pièces","color":"gold"},{"text":" pour tout le monde.","color":"gray"}]
