execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I will be the one Glooblin who you can't find at night. Once you deduce my identity, ","color":"white"},{"text":"talk to Mayor Plubby","color":"light_purple"},{"text":", he already knows my identity and can confirm it for you. If you figure it out, you can be my sidekick and help me rescue the ","color":"white"},{"text":"Lord of Spores","color":"light_purple"},{"text":"!","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/12 15s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
