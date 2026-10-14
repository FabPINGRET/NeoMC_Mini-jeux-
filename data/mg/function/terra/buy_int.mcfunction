# @s (présentoir) : le colon qui a cliqué achète
scoreboard players operation $tvk mg.st = @s mg.tvk
execute on target if entity @s[tag=mg.tvw] run function mg:terra/buy
data remove entity @s interaction
