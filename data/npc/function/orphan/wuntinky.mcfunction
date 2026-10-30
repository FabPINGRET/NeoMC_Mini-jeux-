execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wuntinky","color":"aqua"},{"text":"> Ah, hero, it's yew! Welcome to the","color":"white"},{"text":" Noparentunnels","color":"gold"},{"text":"! It's gettin' right dangerous out there so we decided to move our lit'le town down 'ere where it's safe. Yew'd do the same if yew was mayor, yew would!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
