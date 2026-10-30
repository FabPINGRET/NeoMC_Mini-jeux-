execute at @n[tag=mlc_moon,distance=0..] run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

tellraw @a[tag=mlc_tag,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> I can open this","color":"white"},{"text":" Worldgate","color":"dark_purple"},{"text":" for you!","color":"white"}]

execute positioned -415 51 -43 run function tool:worldgate_to_start

setblock -9761 248 426 minecraft:redstone_block

return 1
