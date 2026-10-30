execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score chubcheek bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Stumpthumb","color":"green"},{"text":"> Grib grabnah gruhhhhh. Grudge go gooooorah g'brug grum grund!","color":"white"}]

execute if score chubcheek bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Stumpthumb","color":"green"},{"text":"> My childhood friend, Chubcheek, passed away and was buried in ","color":"white"},{"text":"Orcbarrow","color":"green"},{"text":". I am old, and too weak to make the journey there. Could you go ","color":"white"},{"text":"touch his remains","color":"gold"},{"text":" on my behalf? It would make me ","color":"white"},{"text":"very, very happy","color":"red"},{"text":". Let me ","color":"white"},{"text":"lay my hand upon you ","color":"gold"},{"text":"first, so you carry my blessing... Very good. And remember, you must touch the bones, it's an Orc tradition!","color":"white"}]
execute if score chubcheek bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run setblock -9773 240 420 minecraft:redstone_block

execute if score chubcheek bool matches 1 run setblock 10278 54 75 redstone_block

execute if score chubcheek bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Stumpthumb","color":"green"},{"text":"> Grub grudno? GAHAHAHAH! Grum guhhhhhh grobe gorgruhhhh. Grah grummmm grahhhhhhhh! ","color":"white"},{"text":"Grug","color":"red"},{"text":".","color":"white"}]

execute if score chubcheek bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Stumpthumb","color":"green"},{"text":"> You did it? You touched Chubcheek's skull? HAHAHAH! That's hilarious, haha you just gave him the ","color":"white"},{"text":"cheese touch","color":"gold"},{"text":"! I gave it to you when I touched you earlier, remember? That's great haha after all these years I get the last laugh! Thanks haha, that made me ","color":"white"},{"text":"deliriously happy","color":"red"},{"text":".","color":"white"}]

execute if block 10278 54 75 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
