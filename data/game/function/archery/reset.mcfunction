scoreboard players set archery_going bool 0
fill 126 50 168 100 42 180 minecraft:chiseled_sandstone replace minecraft:target
setblock 113 40 166 minecraft:stone_button[face=floor,facing=south,powered=false]
kill @e[tag=archery_scoreboard,distance=0..]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8

execute if score archery_points Value matches ..39 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] ["<",{"color":"gold","text":"Javrazai"},{"color":"white","text":"> You got "},{"color":"red","score":{"name":"archery_points","objective":"Value"}},{"text":" points! Better luck next time.","color":"white"}]

execute if score archery_points Value matches 40.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] ["<",{"color":"gold","text":"Javrazai"},{"color":"white","text":"> You got "},{"color":"red","score":{"name":"archery_points","objective":"Value"}},{"text":" points! That's incredible! I'm ","color":"white"},{"text":"so, so happy","color":"red"},{"text":" we get to be best friends now!","color":"white"}]
execute if score archery_points Value matches 40.. run setblock 116 35 159 redstone_block

playsound minecraft:block.note_block.banjo master @a[tag=mg.flw] 113 39 166

schedule clear floaty:sched/game/archery/next_frame
