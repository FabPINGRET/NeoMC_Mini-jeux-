execute at @n[tag=mlc_moon,distance=0..] run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

kill @e[tag=mlc_moon,type=armor_stand,limit=2,distance=0..]
tellraw @a[tag=mlc_tag,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> You stepped off the ","color":"white"},{"text":"Waxwane Brick","color":"aqua"},{"text":"! I told you I’m not following you over anything else. Oh well, I’ll just slither back to where no one wants me...","color":"white"}]

execute if score mlc_altar Value matches 0 run tp @a[tag=mlc_tag,tag=mg.flw] 9960 58 11 0 0
execute if score mlc_altar Value matches 1 run tp @a[tag=mlc_tag,tag=mg.flw] 9795 57 10 0 0
execute if score mlc_altar Value matches 2 run tp @a[tag=mlc_tag,tag=mg.flw] 9829 57 -36 90 0
execute if score mlc_altar Value matches 3 run tp @a[tag=mlc_tag,tag=mg.flw] 9903 46 57 90 0
execute if score mlc_altar Value matches 4 run tp @a[tag=mlc_tag,tag=mg.flw] 9847 57 159 0 0

tag @a[tag=mg.flw] remove mlc_tag

setblock -9766 273 431 minecraft:air
function main_quest:mlc/return_to_altar
