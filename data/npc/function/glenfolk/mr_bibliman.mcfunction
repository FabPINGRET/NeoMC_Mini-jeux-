execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mr. Bibliman","color":"aqua"},{"text":"> We rescued what little we could from the Great Library when it started to fall to the","color":"white"},{"text":" dust contagion","color":"gold"},{"text":". These are all the books that remain. We don't even know if the librarian was able to escape in time or where she went if she did...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
