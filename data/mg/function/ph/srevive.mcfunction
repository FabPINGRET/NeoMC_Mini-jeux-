# @s (entraînement, seul) : cacheur réapparu après sa mort → retrouve son déguisement
scoreboard players set @s mg.deaths 0
effect give @s minecraft:invisibility infinite 0 true
effect give @s minecraft:saturation infinite 0 true
attribute @s minecraft:scale base set 0.5
function mg:ph/apply
