execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score slime_man Story matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Elderlop","color":"light_purple"},{"text":"> The Yucky Presence Up Above has blessed me with a long life. I'm going to live out the last of my days here, at the 'Neath, slurping down Boggy Marys.","color":"white"}]

execute if score slime_man Story matches 1..2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Elderlop","color":"light_purple"},{"text":"> All of us here at the 'Neath stick around night and day. If you're looking for anyone with a secret identity, they're not going to be here.","color":"white"}]

execute if score slime_man Story matches 3.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Elderlop","color":"light_purple"},{"text":"> The Yucky Presence Up Above has blessed me with a long life. I'm going to live out the last of my days here, at the 'Neath, slurping down Boggy Marys.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
