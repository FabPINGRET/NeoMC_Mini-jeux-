particle soul_fire_flame ~ ~1 ~ 0.3 0.3 0.3 0.1 100 normal
playsound minecraft:entity.allay.death master @a[tag=mg.flw] ~ ~ ~ 1 2
execute if entity @s[tag=s_walker] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["1"]},"minecraft:custom_name":{"bold":true,"color":"#DB9D2D","text":"Smiling Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Smilewalker"}]}}}
execute if entity @s[tag=s_walker] run scoreboard players set abnormazoid_1 bool 1
execute if entity @s[tag=m_wight] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["2"]},"minecraft:custom_name":{"bold":true,"color":"#B2B1AE","text":"Loamy Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Mulch White"}]}}}
execute if entity @s[tag=m_wight] run scoreboard players set abnormazoid_2 bool 1
execute if entity @s[tag=cryguy] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["3"]},"minecraft:custom_name":{"bold":true,"color":"#54617A","text":"Sniffling Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Dry Eye Guy"}]}}}
execute if entity @s[tag=cryguy] run scoreboard players set abnormazoid_3 bool 1
execute if entity @s[tag=grumblo] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["4"]},"minecraft:custom_name":{"bold":true,"color":"#404040","text":"Grumpy Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Grumbaby"}]}}}
execute if entity @s[tag=grumblo] run scoreboard players set abnormazoid_4 bool 1
execute if entity @s[tag=t_l_man] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["5"]},"minecraft:custom_name":{"bold":true,"color":"#D47FD1","text":"Regular Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Regular Little Man"}]}}}
execute if entity @s[tag=t_l_man] run scoreboard players set abnormazoid_5 bool 1
execute if entity @s[tag=scarygramps] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["6"]},"minecraft:custom_name":{"bold":true,"color":"#E23A26","text":"Elderly Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Kindlygramps"}]}}}
execute if entity @s[tag=scarygramps] run scoreboard players set abnormazoid_7 bool 1
execute if entity @s[tag=outlander] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["7"]},"minecraft:custom_name":{"bold":true,"color":"#84C775","text":"Feminine Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Mrs. Outlander"}]}}}
execute if entity @s[tag=outlander] run scoreboard players set abnormazoid_10 bool 1
execute if entity @s[tag=wildjaw] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["8"]},"minecraft:custom_name":{"bold":true,"color":"#3B7DB5","text":"Youthful Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Childjaw"}]}}}
execute if entity @s[tag=wildjaw] run scoreboard players set abnormazoid_13 bool 1
execute if entity @s[tag=diretroll] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["9"]},"minecraft:custom_name":{"bold":true,"color":"#05306E","text":"Misshapen Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Smallhead Diretroll"}]}}}
execute if entity @s[tag=diretroll] run scoreboard players set abnormazoid_14 bool 1
execute if entity @s[tag=metalshade] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["10"]},"minecraft:custom_name":{"bold":true,"color":"#404040","text":"Umbral Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Shadeshade"}]}}}
execute if entity @s[tag=metalshade] run scoreboard players set abnormazoid_8 bool 1
execute if entity @s[tag=squishly] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["11"]},"minecraft:custom_name":{"bold":true,"color":"#F3CA44","text":"Gourdlike Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Squashly"}]}}}
execute if entity @s[tag=squishly] run scoreboard players set abnormazoid_6 bool 1
execute if entity @s[tag=b_kobold] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["12"]},"minecraft:custom_name":{"bold":true,"color":"#75342F","text":"Bobo Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Bigbo Kobold"}]}}}
execute if entity @s[tag=b_kobold] run scoreboard players set abnormazoid_9 bool 1
execute if entity @s[tag=muncher] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["13"]},"minecraft:custom_name":{"bold":true,"color":"#93ED51","text":"Hard-Boiled Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Egg Muncher"}]}}}
execute if entity @s[tag=muncher] run scoreboard players set abnormazoid_11 bool 1
execute if entity @s[tag=s_shrimp] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["14"]},"minecraft:custom_name":{"bold":true,"color":"#EB5475","text":"Benthic Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Hovering Shrimp"}]}}}
execute if entity @s[tag=s_shrimp] run scoreboard players set abnormazoid_12 bool 1
execute if entity @s[tag=a_monk] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["15"]},"minecraft:custom_name":{"bold":true,"color":"#4C4C4C","text":"Negative Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Anti-Anti-Monk"}]}}}
execute if entity @s[tag=a_monk] run scoreboard players set abnormazoid_15 bool 1
execute if entity @s[tag=i_creep] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["16"]},"minecraft:custom_name":{"bold":true,"color":"#7AE8BD","text":"Minty Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Mint Ice Creep"}]}}}
execute if entity @s[tag=i_creep] run scoreboard players set abnormazoid_16 bool 1
execute if entity @s[tag=deepknight] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["17"]},"minecraft:custom_name":{"bold":true,"color":"#214C6E","text":"Lefty Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Southpaw Deepknight"}]}}}
execute if entity @s[tag=deepknight] run scoreboard players set abnormazoid_17 bool 1
execute if entity @s[tag=d_fairy] run summon item ~ ~1 ~ {NoGravity:1b,Glowing:1b,Item:{id:"minecraft:breeze_rod",count:1,components:{"minecraft:custom_model_data":{strings:["18"]},"minecraft:custom_name":{"bold":true,"color":"#FAD64A","text":"Flightless Zoidsoul"},"minecraft:lore":["Contains the","soul of a:",{"color":"aqua","text":"Wings-Ripped-Off Fairy"}]}}}
execute if entity @s[tag=d_fairy] run scoreboard players set abnormazoid_18 bool 1

execute as @n[type=item,distance=0..] run team join NoCollideZoid
tp @s ~ -100 ~
kill @s
