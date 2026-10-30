execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lyn","color":"aqua"},{"text":"> If I get good grades, my mom said she'd take me to Dryskull Desert to see the","color":"white"},{"text":" Sand Dragons","color":"gold"},{"text":"! I want to see one roar! But... the road to get to the desert got smashed and fell into the void, so no one can get there right now.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
