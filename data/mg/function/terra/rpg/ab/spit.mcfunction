# @s (dilophosaure) : collerette déployée, crachat de venin
scoreboard players set @s mg.tvat 12
tag @s add mg.trsrc
scoreboard players set $tvr mg.st 0
playsound minecraft:entity.llama.spit hostile @a ~ ~ ~ 1.5 0.6
execute anchored eyes facing entity @p[tag=mg.tvw,gamemode=adventure,distance=..14] eyes positioned ^ ^ ^1 run function mg:terra/rpg/ab/spit_ray
tag @s remove mg.trsrc
