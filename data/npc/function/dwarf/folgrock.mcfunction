execute positioned -301 65 -167 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -301 65 -167 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Folgrock","color":"dark_aqua"},{"text":"> When it gets extra busy, all you can hear is dwarves singing \"hi ho hi ho\" and it's very distracting.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
