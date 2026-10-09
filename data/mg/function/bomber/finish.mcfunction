# Fin : résultat, puis 20 s en spectateur au-dessus de la ville pour admirer les dégâts
function mg:bomber/timeout
execute unless score $state mg.st matches 3 run return 0
scoreboard players set $timer mg.st 400
gamemode spectator @a[tag=mg.play]
gamemode spectator @a[tag=mg.out]
tp @a[tag=mg.play] 0 120 32292 facing 0 64 32400
tp @a[tag=mg.out] 0 120 32292 facing 0 64 32400
tellraw @a[tag=mg.play] {"text":"👁 20 s pour survoler la ville détruite (mode spectateur), puis retour au lobby.","color":"aqua"}
