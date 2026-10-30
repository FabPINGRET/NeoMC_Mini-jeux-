execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bwob","color":"aqua"},{"text":"> I feel bad for that ","color":"white"},{"text":"Gillman","color":"yellow"},{"text":" fella over there. As bad as the","color":"white"},{"text":" Dwarves","color":"dark_aqua"},{"text":" have had it, the ","color":"white"},{"text":"Gillmen","color":"yellow"},{"text":" have gone through even worse. Their entire lake is just teeming with deadly monsters and it doesn't look like they'll be able to return there anytime soon.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
