# Fin du contre-la-montre (appelé par end, timeout et draw quand $xs vaut 1) : ni victoire ni match nul ; retour au lobby par core/ending
# (return_lobby appelle elyrace/cleanup, qui note $xse et remet $xs à 0). L'arrivée a déjà été annoncée par finish.
execute unless entity @a[tag=mg.play,scores={mg.xf=1..}] run tellraw @a [{"text":"⏱ Contre-la-montre terminé sans arrivée.","color":"gray"}]
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 30
