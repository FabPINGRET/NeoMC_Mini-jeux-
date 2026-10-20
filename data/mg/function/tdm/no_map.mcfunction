# Annulation pendant la préparation (aucune arène utilisable) : pas de gel ni de partie (core/request s'arrête à $state 3)
execute unless data storage mg:duel {built:1b} run tellraw @a[tag=mg.play] [{"text":"🎯 TDM sniper : les arènes du duel ne sont pas encore construites (réessaie dans quelques minutes). Partie annulée.","color":"red"}]
execute if data storage mg:duel {built:1b} run tellraw @a[tag=mg.play] [{"text":"🎯 TDM sniper : toutes les arènes du duel sont occupées par un duel. Partie annulée.","color":"red"}]
scoreboard players set $tma mg.st 0
# pas de note : rate/begin (qui pose $rgf) n'a pas tourné, rate/collect noterait sinon la partie précédente
scoreboard players set $rgf mg.st 0
function mg:core/abort
