# Retour au lobby : les participants peuvent noter (pas entre deux épreuves d'une Mini Party). Généré.
execute unless score $rgf mg.st matches 1.. run return 0
execute if score $mp mg.st matches 1 unless score $game mg.st matches 59 run return 0
tag @a[tag=mg.play] add mg.rate
tag @a[tag=mg.out] add mg.rate
scoreboard players enable @a[tag=mg.rate] mg.rt
function mg:rate/names
schedule function mg:rate/ask 50t
