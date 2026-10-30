function music:end
#title @a actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"blue"}
tag @a[tag=mg.flw] remove bossroom

advancement grant @a[tag=mg.flw] only sidequest:undercroft_boss
scoreboard players set $fla12 mg.fla 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
bossbar set boss:secret players

scoreboard players set beat_sealed_citadel bool 1
execute as @a[tag=mg.flw] run function game:100_check

kill @e[tag=illock,distance=0..]
kill @e[tag=sc_keyring_pos,distance=0..]
kill @e[tag=sc_boss_model_keyring,distance=0..]

schedule function floaty:sched/boss/secret/cutscene/9 6s
function boss:secret/display/target/nearest
function boss:secret/display/pose/idle
function boss:secret/display/color/purple

#NACRE HEARTS
setblock -9761 236 420 minecraft:redstone_block
setblock -9761 236 422 minecraft:redstone_block
setblock -9761 236 424 minecraft:redstone_block
setblock -9761 236 426 minecraft:redstone_block
setblock -9761 236 428 minecraft:redstone_block
setblock -9761 236 430 minecraft:redstone_block
setblock -9765 236 416 minecraft:redstone_block
setblock -9765 236 418 minecraft:redstone_block
