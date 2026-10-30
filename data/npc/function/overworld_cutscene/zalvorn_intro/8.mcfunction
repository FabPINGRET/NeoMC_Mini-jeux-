execute positioned -10192 68 131 run playsound minecraft:entity.witch.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute positioned -10195 66 131 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Evil Puppet Guy","color":"gold"},{"text":"> You’ve crossed the line. You see, you can't be just an observer anymore. You’re part of the show! Like a puppet, you have a role to play.","color":"white","italic":false},{"text":" ⇒","color":"light_purple"}]

#transform into pumpkin guy
item replace entity @n[tag=zalvorn_show_intro,distance=0..] armor.head from block -10191 56 129 container.1
particle dust{color:[1.000,0.467,0.000],scale:2} -10190 69 131 0.5 1 0.5 1 50 normal
particle minecraft:trial_spawner_detection -10190 69 131 0.5 1 0.5 0 50 normal
playsound minecraft:entity.creaking.spawn master @a[tag=mg.flw] -10190 67 131 1 2
playsound minecraft:ambient.crimson_forest.mood neutral @a[tag=mg.flw] -10190 67 131 1 1
#summon puppets
setblock -10191 56 138 redstone_block

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/9 13s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
