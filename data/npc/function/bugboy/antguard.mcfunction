execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Antguard","color":"green"},{"text":"> This tree is the Blade Willow, and it is a curious thing. It grows perfectly formed swords from its roots, like nature's own gift of protection. You should go","color":"white"},{"text":" underground beneath this tree","color":"green"},{"text":" and equip one quickly, the forest is a dangerous place during the night.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
