execute positioned -10192 68 131 run playsound minecraft:entity.witch.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute positioned -10195 66 131 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Evil Puppet Guy","color":"gold"},{"text":"> Let’s see how well you dance on my strings.","color":"white","italic":false}]

bossbar set boss:zalvorn players @a[tag=mg.flw]



schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/10 5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
