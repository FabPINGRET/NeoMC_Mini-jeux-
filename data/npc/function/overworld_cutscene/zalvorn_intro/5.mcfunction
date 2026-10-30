execute positioned -10192 68 131 run playsound minecraft:entity.witch.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute positioned -10195 66 131 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Evil Puppet Guy","color":"gold"},{"text":"> This performance, it’s a once-in-a-lifetime spectacle, a memory that will haunt your very soul!","color":"white"},{"text":" ⇒","color":"light_purple"}]

spawnpoint @a[tag=mg.flw] -10210 68 131 -90 0
scoreboard players set $flsp mg.st 41

#summon pumpkin illusions
setblock -10191 56 131 redstone_block
playsound minecraft:ambient.crimson_forest.mood master @a[tag=mg.flw] -10190 67 131 1 1

#start zalvorn's head twitch mario judah thing
setblock -10191 56 136 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/6 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
