execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wallai","color":"yellow"},{"text":"> Though we meant it to merely be a temporary refuge, Ishbowl has grown into a city in its own right. I'm honored ","color":"white"},{"text":"Papa Seamonster ","color":"yellow"},{"text":"trusted me with a leadership position here; I won't let him down.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
