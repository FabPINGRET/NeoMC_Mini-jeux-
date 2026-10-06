# Fin d'un mini-jeu de la Mini Party (appelé par core/return_lobby avant la remise à zéro des joueurs)
scoreboard players add @a[tag=mg.mpp,tag=mg.win] mg.mpm 10
scoreboard players add @a[tag=mg.mpp,tag=!mg.win] mg.mpm 3
execute if entity @a[tag=mg.mpp,tag=mg.win] run tellraw @a[tag=mg.mpp] [{"text":"● +10 pièces pour ","color":"gold"},{"selector":"@a[tag=mg.mpp,tag=mg.win]","color":"yellow","bold":true},{"text":", +3 pour les autres.","color":"gold"}]
execute unless entity @a[tag=mg.mpp,tag=mg.win] run tellraw @a[tag=mg.mpp] [{"text":"● Pas de vainqueur : +3 pièces pour tout le monde.","color":"gold"}]
