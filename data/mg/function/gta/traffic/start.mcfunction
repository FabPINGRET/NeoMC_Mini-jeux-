# @s (nouvelle voiture PNJ) : carrefour le plus proche, cap au hasard
execute if entity @s[x=-76,y=65,z=32322,distance=..1.5] run scoreboard players set @s mg.gtn 0
execute if entity @s[x=-76,y=65,z=32346,distance=..1.5] run scoreboard players set @s mg.gtn 1
execute if entity @s[x=-76,y=65,z=32370,distance=..1.5] run scoreboard players set @s mg.gtn 2
execute if entity @s[x=-76,y=65,z=32394,distance=..1.5] run scoreboard players set @s mg.gtn 3
execute if entity @s[x=-76,y=65,z=32418,distance=..1.5] run scoreboard players set @s mg.gtn 4
execute if entity @s[x=-76,y=65,z=32442,distance=..1.5] run scoreboard players set @s mg.gtn 5
execute if entity @s[x=-76,y=65,z=32466,distance=..1.5] run scoreboard players set @s mg.gtn 6
execute if entity @s[x=-44,y=65,z=32322,distance=..1.5] run scoreboard players set @s mg.gtn 7
execute if entity @s[x=-44,y=65,z=32346,distance=..1.5] run scoreboard players set @s mg.gtn 8
execute if entity @s[x=-44,y=65,z=32370,distance=..1.5] run scoreboard players set @s mg.gtn 9
execute if entity @s[x=-44,y=65,z=32394,distance=..1.5] run scoreboard players set @s mg.gtn 10
execute if entity @s[x=-44,y=65,z=32418,distance=..1.5] run scoreboard players set @s mg.gtn 11
execute if entity @s[x=-44,y=65,z=32442,distance=..1.5] run scoreboard players set @s mg.gtn 12
execute if entity @s[x=-44,y=65,z=32466,distance=..1.5] run scoreboard players set @s mg.gtn 13
execute if entity @s[x=-12,y=65,z=32322,distance=..1.5] run scoreboard players set @s mg.gtn 14
execute if entity @s[x=-12,y=65,z=32346,distance=..1.5] run scoreboard players set @s mg.gtn 15
execute if entity @s[x=-12,y=65,z=32370,distance=..1.5] run scoreboard players set @s mg.gtn 16
execute if entity @s[x=-12,y=65,z=32394,distance=..1.5] run scoreboard players set @s mg.gtn 17
execute if entity @s[x=-12,y=65,z=32418,distance=..1.5] run scoreboard players set @s mg.gtn 18
execute if entity @s[x=-12,y=65,z=32466,distance=..1.5] run scoreboard players set @s mg.gtn 19
execute if entity @s[x=20,y=65,z=32322,distance=..1.5] run scoreboard players set @s mg.gtn 20
execute if entity @s[x=20,y=65,z=32346,distance=..1.5] run scoreboard players set @s mg.gtn 21
execute if entity @s[x=20,y=65,z=32370,distance=..1.5] run scoreboard players set @s mg.gtn 22
execute if entity @s[x=20,y=65,z=32394,distance=..1.5] run scoreboard players set @s mg.gtn 23
execute if entity @s[x=20,y=65,z=32418,distance=..1.5] run scoreboard players set @s mg.gtn 24
execute if entity @s[x=20,y=65,z=32442,distance=..1.5] run scoreboard players set @s mg.gtn 25
execute if entity @s[x=20,y=65,z=32466,distance=..1.5] run scoreboard players set @s mg.gtn 26
execute if entity @s[x=52,y=65,z=32322,distance=..1.5] run scoreboard players set @s mg.gtn 27
execute if entity @s[x=52,y=65,z=32346,distance=..1.5] run scoreboard players set @s mg.gtn 28
execute if entity @s[x=52,y=65,z=32370,distance=..1.5] run scoreboard players set @s mg.gtn 29
execute if entity @s[x=52,y=65,z=32394,distance=..1.5] run scoreboard players set @s mg.gtn 30
execute if entity @s[x=52,y=65,z=32418,distance=..1.5] run scoreboard players set @s mg.gtn 31
execute if entity @s[x=52,y=65,z=32442,distance=..1.5] run scoreboard players set @s mg.gtn 32
execute if entity @s[x=52,y=65,z=32466,distance=..1.5] run scoreboard players set @s mg.gtn 33
execute store result score @s mg.gth run random value 0..3
function mg:gta/traffic/arrive
