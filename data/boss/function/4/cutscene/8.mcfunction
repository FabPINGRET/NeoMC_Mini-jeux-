playsound minecraft:entity.strider.death neutral @a[tag=mg.flw] -10072 116 -355 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Flame","color":"red"},{"color":"white","text":"> The lava underfoot obeys my voice..."},{"text":" ⇒","color":"light_purple"}]
data modify entity @e[tag=boss_ed_cutscene,limit=1,distance=0..] Pose set value {LeftArm:[200f,0f,15f],RightArm:[200f,0f,345f]}
setblock -10076 95 -371 minecraft:redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/9 5.2s
