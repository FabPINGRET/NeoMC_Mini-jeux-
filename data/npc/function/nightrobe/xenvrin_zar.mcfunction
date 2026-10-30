execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score Inventory FeatherBrush matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Xenvrin-Zar","color":"light_purple"},{"text":"> We hope this once great library will someday be able to be rebuilt. This contagion makes me furious, but we Nightrobes are not fighters.","color":"white"}]
execute if score Inventory FeatherBrush matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Xenvrin-Zar","color":"light_purple"},{"text":"> We hope this once great library will someday be able to be rebuilt. Thankfully, there are libraries in ","color":"white"},{"text":"other worlds","color":"dark_purple"},{"text":" yet unmarred by ruin.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
