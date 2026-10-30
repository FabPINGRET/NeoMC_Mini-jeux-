execute positioned 214 43 122 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.witch.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute positioned 214 43 122 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zalvorn the Evil Puppet Guy","color":"gold"},{"text":"> Hush now, hush! Such nonsense does not become you. A puppet you are, and a puppet you shall remain. As for you, Hero, I do wish you hadn't seen this. I'm afraid I can't let you leave...","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/3 11s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
