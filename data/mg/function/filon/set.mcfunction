$setblock $(x) $(y) $(z) minecraft:$(f)
execute store result score #fr mg.st run random value 0..2
$execute if score #fr mg.st matches 1.. positioned $(x) $(y) $(z) run setblock ~1 ~ ~ minecraft:$(f)
$execute if score #fr mg.st matches 2.. positioned $(x) $(y) $(z) run setblock ~ ~1 ~ minecraft:$(f)
