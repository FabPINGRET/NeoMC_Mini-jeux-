execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Moko-Hapa","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"If you go left, you'll pass by the"},{"text":" Tangleweb","color":"dark_green"},{"text":" and end up at","color":"white"},{"text":" Pygmy Village","color":"green"},{"text":"! If you go right, you'll end up on","color":"white"},{"text":" Serpent's Treasure Island","color":"green"},{"text":"! No one knows why it's called that.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
