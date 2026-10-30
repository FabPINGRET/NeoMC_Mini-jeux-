execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Fruddly","color":"aqua"},{"text":"> Yew can ","color":"white"},{"text":"check your quest progress ","color":"green"},{"text":"as you surely know. Either from the menu or","color":"white"},{"text":" by pressing [ ","color":"green"},{"keybind":"key.advancements","color":"green"},{"text":" ]","color":"green"},{"text":"! Oi use it to see 'ow much Oi've accomplished, Oi do!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value
