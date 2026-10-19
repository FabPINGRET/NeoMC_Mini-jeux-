# @s (interaction d'un PNJ) : le joueur qui a cliqué lui parle
scoreboard players operation $npc mg.st = @s mg.olnid
execute on target if entity @s[tag=mg.olw] run function mg:ombre/npc/any
data remove entity @s interaction
