data merge entity @s {NoGravity:1b}
data modify entity @s Motion[1] set value 0
tag @s remove gravity

#Speed Up

execute store result score thren_arrow_xspeed Value run data get entity @s Motion[0] 1000
execute store result score thren_arrow_zspeed Value run data get entity @s Motion[2] 1000

scoreboard players operation thren_arrow_xspeed Value *= 15 Value
scoreboard players operation thren_arrow_zspeed Value *= 15 Value

execute store result entity @s Motion[0] float 0.001 run scoreboard players get thren_arrow_xspeed Value
execute store result entity @s Motion[2] float 0.001 run scoreboard players get thren_arrow_zspeed Value
