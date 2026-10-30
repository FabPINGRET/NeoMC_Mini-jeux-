setblock 100 44 51 air
setblock 96 46 53 minecraft:chiseled_stone_bricks

scoreboard players set Inventory DungeonFlag 11
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"???","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#8536C2","text":"S"},{"color":"#8A3AC7","text":"e"},{"color":"#903FCB","text":"a"},{"color":"#9543D0","text":"l"},{"color":"#9A47D5","text":"e"},{"color":"#A04CD9","text":"d "},{"color":"#A550DE","text":"C"},{"color":"#AA54E3","text":"i"},{"color":"#AF58E8","text":"t"},{"color":"#B55DEC","text":"a"},{"color":"#BA61F1","text":"d"},{"color":"#BF65F6","text":"e"},{"color":"#CA6EFF","text":"l"}]
tp @a[tag=mg.flw] -12231 209 -171 90 0
function music:sc
spawnpoint @a[tag=mg.flw] -12239 184 -171 90 0
scoreboard players set $flsp mg.st 14
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
