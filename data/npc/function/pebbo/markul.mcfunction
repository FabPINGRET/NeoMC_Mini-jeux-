execute positioned 10049 187 1220 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10049 187 1220 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Markul the Breach","color":"blue"},{"text":"> Being tiny is super dangerous. We have to make our own luck. My best friend got inhaled by a mole rat.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
