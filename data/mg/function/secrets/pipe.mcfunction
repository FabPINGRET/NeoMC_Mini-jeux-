# Tuyau de distorsion : @s file vers l'autre tuyau (macro x, z)
execute at @s run particle minecraft:portal ~ ~0.5 ~ 0.3 0.6 0.3 0.6 40
$tp @s $(x) 68.2 $(z)
scoreboard players set @s mg.ept 40
execute at @s run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 0.8 1.6
execute at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 0.6
execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.4 0.6 0.4 0 20
advancement grant @s only mg:secrets/tuyau
