execute positioned 10387 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> Uh oh, hero. If he was telling the truth, the ","color":"white"},{"text":"Floaty Isles","color":"yellow"},{"text":" might be in trouble. With the","color":"white"},{"text":" Bell","color":"gold"},{"text":" in enemy hands, there’d be no hope for any other world either.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/16 11s replace

execute as @e[tag=lord_machine,distance=0..] at @s run data modify entity @s Pose set value {}

#","color":"white"},{"text":"
