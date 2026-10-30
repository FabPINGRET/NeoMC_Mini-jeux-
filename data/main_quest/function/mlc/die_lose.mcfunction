execute at @n[tag=mlc_moon,distance=0..] run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

kill @e[tag=mlc_moon,type=armor_stand,limit=2,distance=0..]
tellraw @a[tag=mlc_tag,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> Oh well, I’ll just slither back to where no one wants me...","color":"white"}]

tag @a[tag=mg.flw] remove mlc_tag

setblock -9766 273 431 minecraft:air
function main_quest:mlc/return_to_altar
