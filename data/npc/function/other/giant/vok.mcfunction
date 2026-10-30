execute positioned 10152 39 196 run playsound minecraft:entity.ravager.celebrate neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute positioned 10152 39 196 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Vok Stonebrow","color":"gray"},{"text":"> Ohoho, you are remarkably huge for a Pebbo, you must have quite the healthy diet! Have you come to visit or just use my ","color":"white"},{"text":"Mountain Forge","color":"gray"},{"text":"? Ah, I see the truth in your eyes. Well, my forge and I are at your disposal. May its warding fire protect you from harm.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
