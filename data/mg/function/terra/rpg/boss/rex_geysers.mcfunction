# Geysers de lave : trois points autour des colons s'embrasent dans 2 s
scoreboard players set $trr3 mg.st 7
execute store result score $r mg.st run random value 0..15
execute if score $r mg.st matches 0 run summon minecraft:marker 5.5 99 186.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 1 run summon minecraft:marker 4.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 2 run summon minecraft:marker 0.5 99 191.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 3 run summon minecraft:marker -3.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 4 run summon minecraft:marker -4.5 99 186.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 5 run summon minecraft:marker -3.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 6 run summon minecraft:marker 0.5 99 181.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 7 run summon minecraft:marker 4.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 8 run summon minecraft:marker 9.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 9 run summon minecraft:marker 4.5 99 195.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 10 run summon minecraft:marker -3.5 99 195.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 11 run summon minecraft:marker -8.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 12 run summon minecraft:marker -8.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 13 run summon minecraft:marker -3.5 99 177.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 14 run summon minecraft:marker 4.5 99 177.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 15 run summon minecraft:marker 9.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute store result score $r mg.st run random value 0..15
execute if score $r mg.st matches 0 run summon minecraft:marker 5.5 99 186.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 1 run summon minecraft:marker 4.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 2 run summon minecraft:marker 0.5 99 191.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 3 run summon minecraft:marker -3.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 4 run summon minecraft:marker -4.5 99 186.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 5 run summon minecraft:marker -3.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 6 run summon minecraft:marker 0.5 99 181.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 7 run summon minecraft:marker 4.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 8 run summon minecraft:marker 9.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 9 run summon minecraft:marker 4.5 99 195.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 10 run summon minecraft:marker -3.5 99 195.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 11 run summon minecraft:marker -8.5 99 190.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 12 run summon minecraft:marker -8.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 13 run summon minecraft:marker -3.5 99 177.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 14 run summon minecraft:marker 4.5 99 177.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute if score $r mg.st matches 15 run summon minecraft:marker 9.5 99 182.5 {Tags:["mg.tv","mg.trgey","mg.trgn"]}
execute as @a[tag=mg.tvw,gamemode=adventure,x=-16,y=95,z=170,dx=32,dy=12,dz=32,sort=random,limit=1] at @s run summon minecraft:marker ~ 99 ~ {Tags:["mg.tv","mg.trgey","mg.trgn"]}
scoreboard players set @e[tag=mg.trgn] mg.tvst 2
tag @e[tag=mg.trgn] remove mg.trgn
