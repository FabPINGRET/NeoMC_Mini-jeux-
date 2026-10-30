execute positioned -310 57 -69 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -310 57 -69 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thorheal","color":"dark_aqua"},{"text":"> Any chance you could spot me a big block of soap and some shoe polish? I wanna try somethin.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
