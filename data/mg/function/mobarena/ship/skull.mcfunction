playsound minecraft:entity.wither.shoot hostile @a ~ ~ ~ 1 1.3
scoreboard players set $rs mg.st 50
execute positioned ^ ^ ^1.5 run function mg:mobarena/ship/skull_ray
