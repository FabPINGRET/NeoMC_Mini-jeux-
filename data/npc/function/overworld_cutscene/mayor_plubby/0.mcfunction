execute positioned 10383 59 -222 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Plubby","color":"light_purple"},{"text":"> Are you the one who saved the lords of ","color":"white"},{"text":"Flame","color":"red"},{"text":" and","color":"white"},{"text":" Forest","color":"green"},{"text":"? I've heard about you! Our","color":"white"},{"text":" Lord of Spores ","color":"light_purple"},{"text":"has been captured but don't worry, we've already got it covered.","color":"white"},{"text":" ⇒","color":"light_purple"}]

tag @a[tag=mg.flw] add cutscene

tag @a[tag=mg.flw] add no_warp

scoreboard players set slime_man Story 1

schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/1 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
