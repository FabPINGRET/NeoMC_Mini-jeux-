# Ouvre (ou rouvre) la fenêtre d'invitation (@s = invité) ; le pseudo du défieur vient de duel/inv_name (repli : « Un joueur »)
execute unless score @s mg.dlto matches 1.. run return 0
data modify storage mg:duel inv set value {p:"Un joueur"}
scoreboard players operation #dln mg.st = @s mg.dlto
execute as @a[tag=mg.dlrq] if score @s mg.dlid = #dln mg.st at @s run function mg:duel/inv_name
tag @s add mg.dlui
function mg:duel/inv_dlg with storage mg:duel inv
