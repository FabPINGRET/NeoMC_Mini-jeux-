execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scoobert","color":"aqua"},{"text":"> Welcome to the Monstervatory! I’m the local monster conservationist, or as I like to say, ","color":"white"},{"text":"Monstervationist","color":"gold"},{"text":". With my custom-built Monstervator, you can ","color":"white"},{"text":"select a region of the world","color":"green"},{"text":", and I’ll tweak local ecological factors to ","color":"white"},{"text":"suppress nighttime monster spawns there","color":"green"},{"text":".","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
