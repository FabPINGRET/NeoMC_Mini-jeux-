execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if block 180 59 -265 bee_nest if block 158 61 -237 air if block 137 59 -233 air if block 138 60 -246 minecraft:bee_nest if block 139 60 -259 air if block 102 60 -232 minecraft:bee_nest run setblock 175 46 -220 minecraft:redstone_block

execute if block 175 46 -220 minecraft:air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Johnny","color":"yellow"},{"text":"> There are places on each giant tree stump to set up a beehive. We were really buzzzzzed about the trees Worm, Mayor Skeeter, and Phly live beneath, so we definitely want beehives on","color":"white"},{"text":" only those three","color":"yellow"},{"text":". If you could put beehives on those three, and those three only, we would be","color":"white"},{"text":" so, so happy","color":"red"},{"text":"!","color":"white"}]


execute if block 175 46 -220 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Johnny","color":"yellow"},{"text":"> What? You set up new beehives on those three trees?! This is amazzzzzzing news! I'm ","color":"white"},{"text":"so stingin' happy","color":"red"},{"text":" I could dance! Thank you, Hero!","color":"white"}]
execute if block 175 46 -220 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
