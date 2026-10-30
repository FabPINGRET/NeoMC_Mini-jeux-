execute at @n[tag=mlc_moon,distance=0..] run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

tellraw @a[tag=mlc_tag,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> I can open this","color":"white"},{"text":" Worldgate","color":"dark_purple"},{"text":" for you too!","color":"white"}]

execute positioned -337 46 91 run function tool:worldgate_to_start

setblock -9761 248 430 minecraft:redstone_block

return 1
