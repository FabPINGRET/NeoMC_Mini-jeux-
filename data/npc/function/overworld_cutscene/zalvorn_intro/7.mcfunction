execute positioned -10192 68 131 run playsound minecraft:entity.witch.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute positioned -10195 66 131 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Evil Puppet Guy","color":"gold"},{"text":"> You thought you could wander where you weren’t meant to be, snooping through what doesn't belong to you.","color":"white"},{"text":" Such... aggravating curiosity","color":"white","italic":true},{"text":".","color":"white","italic":false},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/8 11s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
