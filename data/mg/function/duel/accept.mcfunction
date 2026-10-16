# Accepter (@s = invité)
execute unless score @s mg.dlto matches 1.. run return run tellraw @s [{"text":"Tu n'as aucune invitation de duel en attente.","color":"gray"}]
scoreboard players operation $dlt mg.st = @s mg.dlto
execute as @a[tag=mg.dlrq] if score @s mg.dlid = $dlt mg.st run tag @s add mg.dlca
function mg:duel/accept_chk
tag @a remove mg.dlca
