execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Olim","color":"aqua"},{"text":"> Howdy, I hope you were careful climbing up here! Monsters can't reach me on my little windmill island, so I can farm during the day in peace. The cave on the ground beneath us is overrun with those monstery varmints. Luckily, the way to open the entrance only appears when the ","color":"white"},{"text":"sun is set","color":"aqua"},{"text":"...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
