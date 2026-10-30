execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> How did I not see it before, you've been trying to copy my heroism across the","color":"white"},{"text":" Dark Isles","color":"dark_purple"},{"text":"! My righteous deeds have inspired you to want to be a hero yourself!","color":"white"},{"text":" ⇒","color":"light_purple"}]


schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/9 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
