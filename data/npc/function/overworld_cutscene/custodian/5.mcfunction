playsound minecraft:entity.allay.ambient_with_item neutral @a[tag=mg.flw] -10441 84 439 2 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Kovács János","color":"dark_purple"},{"text":"> You are a worthy successor...","color":"white"}]

schedule function floaty:sched/npc/overworld_cutscene/custodian/6 5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
