# @s : le coffre, quelqu'un a cliqué
execute on target if entity @s[tag=mg.evl] run tag @s add mg.evwin
data remove entity @s interaction
execute unless entity @a[tag=mg.evwin] run return 0
tellraw @a [{"text":"🗝 ","color":"aqua"},{"selector":"@a[tag=mg.evwin,limit=1]","color":"yellow"},{"text":" a trouvé le trésor !","color":"aqua"}]
execute at @s run particle minecraft:totem_of_undying ~ ~0.5 ~ 0.4 0.4 0.4 0.4 60
execute as @a[tag=mg.evwin,limit=1] run function mg:lobby/ev/win
tag @a remove mg.evwin
function mg:lobby/ev/stop
