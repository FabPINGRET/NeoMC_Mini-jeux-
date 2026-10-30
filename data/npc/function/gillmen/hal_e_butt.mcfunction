execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if block -154 56 146 minecraft:redstone_torch run setblock -151 55 146 redstone_block

execute if block -154 56 146 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hal E. Butt","color":"yellow"},{"text":"> I got myself stuck in this mean ol' cage, don't ask me how. Ugh, if you could find a way to open the door and get me outta here, it would make me ","color":"white"},{"text":"really, really happy","color":"red"},{"text":".","color":"white"}]

execute unless block -154 56 146 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hal E. Butt","color":"yellow"},{"text":"> Honest to Glub, this cage has got me going stockholm syndrome mode BAD! I kinda love it here now, this cage is my whole world bro. It's made me","color":"white"},{"text":" really, really happy","color":"red"},{"text":"!","color":"white"}]
execute unless block -154 56 146 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
