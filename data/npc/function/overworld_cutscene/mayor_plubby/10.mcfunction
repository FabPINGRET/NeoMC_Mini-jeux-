execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> By day, I am one of the normal Glooblins who live in this village. By night, I'm ","color":"white"},{"text":"Slime Man","color":"green"},{"text":"! To discover my secret identity, you will need to account for the ","color":"white"},{"text":"nighttime activities of all 7 other Glooblins ","color":"light_purple"},{"text":"who live here.","color":"white"},{"text":" ⇒","color":"light_purple"}]


schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/11 13s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
