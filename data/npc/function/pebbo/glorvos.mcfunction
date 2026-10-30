execute positioned 10033 187 1226 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10033 187 1226 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glorvos the Pickshard","color":"blue"},{"text":"> Have you ever been to Valorforge? It's about a three month journey from here by Pebbo foot.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
