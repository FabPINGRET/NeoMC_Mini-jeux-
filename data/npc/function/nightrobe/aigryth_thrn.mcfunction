execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Aigryth-Thrn","color":"light_purple"},{"text":"> We came to the Floaty Isles for the protection of the ","color":"white"},{"text":"Bell of Life","color":"gold"},{"text":". Let us hope it's strong enough to protect from what's coming. These contagions are just the vanguard, the main force cannot be far behind.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
