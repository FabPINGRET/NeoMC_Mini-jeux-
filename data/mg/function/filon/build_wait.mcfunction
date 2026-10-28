execute in minecraft:overworld run forceload add -30 45970 46 46046
execute unless loaded -22 99 45978 run return run schedule function mg:filon/build_wait 20t
execute unless loaded 38 99 46038 run return run schedule function mg:filon/build_wait 20t
scoreboard players set $fnb mg.st 0
function mg:filon/build
function mg:filon/regen
scoreboard players set $fnrp mg.st 0
execute unless score $fnw mg.st matches 1 run forceload remove -30 45970 46 46046
