particle minecraft:dust{color:[0.4,0.1,0.6],scale:2} ~ ~1 ~ 0.3 1 0.3 0 40 force
particle minecraft:soul ~ ~1 ~ 0.4 1 0.4 0.05 20 force
execute unless score @s mg.olbless matches 1.. run damage @s 18 minecraft:magic
execute if score @s mg.olbless matches 1.. run damage @s 12 minecraft:magic
effect give @s minecraft:wither 3 1
playsound minecraft:entity.wither.shoot hostile @a ~ ~ ~ 1 0.8
