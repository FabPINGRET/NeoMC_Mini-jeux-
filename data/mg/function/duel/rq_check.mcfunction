# Le défieur (@s, tag mg.dlrq) a-t-il encore un invité en ligne ? Sinon l'invitation est périmée
scoreboard players operation $dlt mg.st = @s mg.dlid
execute as @a[scores={mg.dlto=1..}] if score @s mg.dlto = $dlt mg.st run tag @s add mg.dlt2
execute unless entity @a[tag=mg.dlt2] run tellraw @s [{"text":"⚔ Invitation annulée : l'invité s'est déconnecté.","color":"gray"}]
execute unless entity @a[tag=mg.dlt2] run tag @s remove mg.dlrq
tag @a remove mg.dlt2
