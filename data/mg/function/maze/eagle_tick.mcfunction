scoreboard players remove @s mg.je 1
execute if score @s mg.je matches 1.. run return 0
scoreboard players operation $jx mg.st = @s mg.jid
execute as @e[type=minecraft:marker,tag=mg.jeg] if score @s mg.jid = $jx mg.st run tag @s add mg.jsel
tp @s @e[type=minecraft:marker,tag=mg.jsel,limit=1]
kill @e[type=minecraft:marker,tag=mg.jsel]
gamemode adventure @s
title @s actionbar {"text":"🦅 Retour au sol","color":"green"}
