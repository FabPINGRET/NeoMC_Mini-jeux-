scoreboard players set fs_fanswitch Value 1
tag @e[tag=fs_fan,tag=1,distance=0..] add on
execute as @e[tag=fs_fan,tag=3,distance=0..] at @s run function dungeon:8/stop_fan

tellraw @a[tag=mg.flw] [{"text":"Power has been redirected to the","italic":true,"color":"aqua"},{"text":" Red","color":"red"},{"text":" fan...","color":"aqua"}]
setblock -10765 70 333 minecraft:sea_lantern
setblock -10656 30 436 minecraft:netherite_block
setblock -10777 50 441 minecraft:netherite_block

#1
setblock -10694 10 393 minecraft:sea_lantern
#2
setblock -10729 12 391 minecraft:netherite_block
#3
setblock -10729 9 373 minecraft:netherite_block
