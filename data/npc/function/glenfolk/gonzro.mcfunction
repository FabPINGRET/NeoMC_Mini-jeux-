execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gonzro","color":"aqua"},{"text":"> The power of the","color":"white"},{"text":" Bell of Life","color":"gold"},{"text":" allows us to wake up in our beds should we die before our time comes. I recommend sleeping in beds wherever you go, it's never fun to wake up in one half a world away!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
