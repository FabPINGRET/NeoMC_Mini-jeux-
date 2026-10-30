execute positioned 10015 94 -95 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.silverfish.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10015 94 -95 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.puffer_fish.blow_up neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute positioned 10015 94 -95 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> I remember you,","color":"white"},{"text":" Slime Man","color":"green"},{"text":". You were planning a rescue for me long before your sidekick joined you.","color":"white"},{"text":" ⇒","color":"light_purple"}]

setblock 10031 91 -101 air
schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/face_spores 2t replace

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/5 9s replace
