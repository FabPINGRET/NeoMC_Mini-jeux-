# @s est mort : son arc tombe, puis il est éliminé (seul : il continue)
execute unless score $n0 mg.st matches 2.. run return run scoreboard players set @s mg.deaths 0
execute if items entity @s container.* minecraft:bow run function mg:mm/drop_death
clear @s
effect clear @s minecraft:glowing
function mg:core/eliminate
