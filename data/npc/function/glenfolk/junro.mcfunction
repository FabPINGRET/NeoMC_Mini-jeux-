execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if block 133 57 -12 tuff at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Junro","color":"aqua"},{"text":"> This stone structure appeared around the same time as the","color":"white"},{"text":" three scourges","color":"light_purple"},{"text":" did. Frustratingly, I feel like I'm the only one who thinks they're connected somehow... This will require a lot more study.","color":"white"}]
execute if block 133 57 -12 crying_obsidian at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Junro","color":"aqua"},{"text":"> Hah! I knew it! That structure was a dormant ","color":"white"},{"text":"Worldgate","color":"dark_purple"},{"text":" this whole time! Though I suppose I shouldn't be this excited about another hole punched through the fabric of our dimension.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
