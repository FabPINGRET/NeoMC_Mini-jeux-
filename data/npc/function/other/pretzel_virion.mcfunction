execute positioned -12427 128 351 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -12427 128 351 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> ... What are you doing here?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
