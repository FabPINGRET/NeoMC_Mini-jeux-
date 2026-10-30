execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Thank you so much for rescuing me! I was near the","color":"white"},{"text":" Worldgate","color":"yellow"},{"text":" when it opened and couldn't resist checking out the Floaty Isles. I was admiring the desert when that nasty Zalvorn kidnapped me! I was starting to lose hope anyone would find me...","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
stopsound @a[tag=mg.flw] record
tag @a[tag=mg.flw] add cutscene
tag @a[tag=mg.flw] add no_warp

setblock 10467 57 121 air
setblock 10466 53 120 minecraft:blue_wool

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/1 13s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
