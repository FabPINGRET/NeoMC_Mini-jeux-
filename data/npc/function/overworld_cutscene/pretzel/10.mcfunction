execute positioned 10520 43 -168 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> See you soon, cutie! ","color":"white"},{"text":"*smooch*","color":"gray","italic":true}]

particle gust 10520 43 -168 0.3 0.3 0.3 0 3
playsound minecraft:block.dispenser.launch neutral @a[tag=mg.flw] 10520 43 -168 1 0.1

setblock 10520 43 -168 air
setblock 10520 42 -168 air
setblock 10520 41 -168 minecraft:warped_planks

#Pretzel to Buh' Tween
setblock -9769 240 426 minecraft:redstone_block

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
