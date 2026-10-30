execute positioned 10020 94 -98 run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10020 94 -98 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> ","color":"white"},{"text":"Morbex","color":"dark_aqua"},{"text":", you big meanie, get ready to taste my slimy fist of justice! Your days of tyranny are over, scumlips!","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/10 9s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
