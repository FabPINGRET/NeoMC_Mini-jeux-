execute positioned -10192 68 131 run playsound minecraft:entity.witch.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute positioned -10195 66 131 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Evil Puppet Guy","color":"gold"},{"text":"> Watch as I, the magnificent Zalvorn, twist the very fabric of reality to my will!","color":"white"},{"text":" ⇒","color":"light_purple"}]

#start pumpkin illusions
setblock -10191 56 133 redstone_block

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/7 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
