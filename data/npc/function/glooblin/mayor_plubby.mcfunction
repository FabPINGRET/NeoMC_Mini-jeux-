execute unless score slime_man Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute if score slime_man Story matches 0 positioned 10383 59 -217 if entity @a[gamemode=!spectator,distance=7..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Plubby","color":"light_purple"},{"text":"> Are you the one who saved the lords of ","color":"white"},{"text":"Flame","color":"red"},{"text":" and","color":"white"},{"text":" Forest","color":"green"},{"text":"? I've heard about you! Please, gather ","color":"white"},{"text":"everyone here ","color":"light_purple"},{"text":"so we can talk.","color":"white"}]

execute if score slime_man Story matches 0 positioned 10383 59 -217 if entity @a[gamemode=!spectator,distance=..7,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=7..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:overworld_cutscene/mayor_plubby/0


execute if score slime_man Story matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Plubby","color":"light_purple"},{"text":"> Have you accounted for the nighttime whereabouts of all the Glooblins who live in this village? There are","color":"white"},{"text":" 7","color":"light_purple"},{"text":" total who are not","color":"white"},{"text":" Slime Man","color":"green"},{"text":". Come talk to me when you are certain which Glooblin is really our slimy protector!","color":"white"}]

execute if score slime_man Story matches 3 if score Inventory Honeyboost matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Plubby","color":"light_purple"},{"text":"> And your guess is... Grlu? That's right, Grlu is","color":"white"},{"text":" Slime Man","color":"green"},{"text":"'s secret identity! He has a secret base on an island to the west of here, past the Sugar House. The secret passphrase to access the island is \"","color":"white"},{"text":"Valor","color":"gold"},{"text":".\" Good work!","color":"white"}]

execute if score Inventory Honeyboost matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mayor Plubby","color":"light_purple"},{"text":"> The","color":"white"},{"text":" Lord of Spores ","color":"light_purple"},{"text":"is safe. Thank the Yucky Presence Up Above!","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
