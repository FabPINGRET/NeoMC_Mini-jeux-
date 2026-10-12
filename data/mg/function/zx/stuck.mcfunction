# @s (mob) : immobile 12 s loin des joueurs et des fenêtres → retiré, il réapparaîtra (compté dans les restants)
execute store result score $sx mg.st run data get entity @s Pos[0]
execute store result score $sz mg.st run data get entity @s Pos[2]
scoreboard players operation $sx mg.st -= @s mg.zqx
scoreboard players operation $sz mg.st -= @s mg.zqz
execute store result score @s mg.zqx run data get entity @s Pos[0]
execute store result score @s mg.zqz run data get entity @s Pos[2]
scoreboard players add @s mg.zsk 1
execute unless score $sx mg.st matches 0 run scoreboard players set @s mg.zsk 0
execute unless score $sz mg.st matches 0 run scoreboard players set @s mg.zsk 0
execute if entity @a[tag=mg.play,tag=!mg.zdead,distance=..3] run scoreboard players set @s mg.zsk 0
execute if entity @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=1..},distance=..3.6] run scoreboard players set @s mg.zsk 0
execute if score @s mg.zsk matches 12.. run function mg:zx/unstick
