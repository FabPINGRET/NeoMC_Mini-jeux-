# @s (interaction d'un PNJ) : le colon qui a cliqué lui parle
scoreboard players operation $npc mg.st = @s mg.trnid
execute on target if entity @s[tag=mg.tvw] run function mg:terra/rpg/npc
data remove entity @s interaction
