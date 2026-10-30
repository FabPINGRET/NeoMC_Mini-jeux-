execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Jellysqwudd","color":"light_purple"},{"text":"> I'm technically part of the ","color":"white"},{"text":"Gill Guild","color":"blue"},{"text":", but I don't really roll with them. I try to find ","color":"white"},{"text":"yet un-found secrets","color":"yellow"},{"text":" in the world they don't care about. For example:","color":"white"}]

execute if score Inventory ThornBow matches 1 if score beat_eye_in_the_grove bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","1","exclude"]}
execute if score Inventory Amulet matches 1 if score beat_custodian bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","2","exclude"]}
execute if score Inventory Amulet matches 1 if score beat_pretzel bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","3","exclude"]}
execute if score Inventory TomeOfTongues matches 1 if score beat_attestor_golem bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","4","exclude"]}
execute if score Inventory Honeyboost matches 1 if score beat_icelorn_choir bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","5","exclude"]}
execute if score Inventory DominionRod matches 1 if score beat_knotfire bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","6","exclude"]}
execute if score Inventory IcelightScepter matches 1 if score beat_wahrog bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","7","exclude"]}
execute if score Inventory IcelightScepter matches 1 if score beat_threnodist bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","8","exclude"]}
execute if score Inventory ThornBow matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_scrimp] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","9","exclude"]}
execute if score Inventory Bonestride matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_darknyss] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","10","exclude"]}
execute if score Inventory Amulet matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_scleemotius] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","11","exclude"]}
execute if score Inventory Amulet matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=vyrn] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","12","exclude"]}
execute if score Inventory TomeOfTongues matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_mudtilda] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","13","exclude"]}
execute if score Inventory Honeyboost matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_willy] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","14","exclude"]}
execute if score Inventory Honeyboost matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_vok] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","15","exclude"]}
execute if score Inventory DominionRod matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_etch] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","16","exclude"]}
execute if score Inventory DominionRod matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=upgrade_s18-6] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","17","exclude"]}
execute if score Inventory Amulet matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=bottle1] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","18","exclude"]}
execute if score Inventory Honeyboost matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=bottle2] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","19","exclude"]}
execute if score Inventory IcelightScepter matches 1 as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=bottle3] run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","20","exclude"]}
execute if score Inventory IcelightScepter matches 1 as @p[gamemode=!spectator,tag=mg.flw] if score forgemuzzle_1 bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","21","exclude"]}
execute if score Inventory SoaringTrident matches 1 as @p[gamemode=!spectator,tag=mg.flw] if score forgemuzzle_2 bool matches 0 run summon area_effect_cloud ~ ~ ~ {Tags:["gyl_temp","22","exclude"]}



tag @e[type=minecraft:area_effect_cloud,tag=gyl_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=gyl_temp,tag=exclude,distance=0..]

execute if entity @e[tag=gyl_temp,tag=1,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a Marauder having some apple-related trouble...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=2,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a little alien who's ready to retire from guarding his cave...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=3,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a peddler of magical wares who has acquired a remarkable object...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=4,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a golem that waits to reward any who can pass its trial...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=5,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a frigid singer who wants you in its audience...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=6,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a tiny spirit which awaits your supplication...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=7,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a prophet whose mind has been ruined by a crackling ailment...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=8,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a lamenter who sings through the vaults of spacetime for your nearing funeral...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=9,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a shellfish who hates clompy boots...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=10,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a surgeon who doesn't quite know what they're doing...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=11,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a giant in a prickly cave...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=12,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's an artificer who fled from Valorforge and went into hiding...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=13,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a giant who stirs her yucky pool with a staff...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=14,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a smuggler who has invented a new type of armament...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=15,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a giant who waits patiently for someone to converse with...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=16,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a pair of tiny fellows who run an ornamenting shop...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=17,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a robot who can upgrade a blaster you might have...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=18,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a bottle in a cauldron house...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=19,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a bottle on a floating vessel...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=20,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a bottle in a well-expanded mind...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=21,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a mage in a tunnel by submerged marble pillars...","color":"white"}]
execute if entity @e[tag=gyl_temp,tag=22,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":" There's a mage in a black and gold cave...","color":"white"}]


execute unless entity @e[tag=gyl_temp,distance=0..] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"Actually, there's nothing interesting out there I've found that you haven't already seen...","color":"white"}]

kill @e[type=minecraft:area_effect_cloud,tag=gyl_temp,distance=0..]
