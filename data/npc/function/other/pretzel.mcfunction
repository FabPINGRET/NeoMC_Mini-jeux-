execute positioned 10520 43 -168 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10520 43 -168 if entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> How's it goin, buh'? I've come across a maximally splendid magic object and I would LOVE to share it with you when everyone is here...","color":"white"}]

execute positioned 10520 43 -168 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] run function npc:overworld_cutscene/pretzel/0

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
