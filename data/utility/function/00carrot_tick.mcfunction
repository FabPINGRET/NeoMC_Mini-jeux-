# BONESTRIDE
execute as @a[scores={CarrotStick=1..},nbt={active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run tag @s add bone_cancel
execute if score FreeMagic bool matches 0 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect give @s minecraft:hunger 3 6 true
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run playsound minecraft:entity.bat.takeoff player @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run playsound minecraft:entity.skeleton_horse.gallop_water player @a[tag=mg.flw] ~ ~ ~ 1 1
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run particle minecraft:soul ~ ~ ~ 0.5 0.1 0.5 0.02 25 force
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect give @s minecraft:jump_boost 3 0 true
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect give @s minecraft:speed 3 6 true
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run tellraw @s {"text":"Bonestride successfully cancelled...","color":"gray","italic":true}
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run playsound minecraft:block.note_block.cow_bell player @s ~ ~ ~ 0.5 0.5
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect clear @s speed
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect clear @s jump_boost

# BONESTRIDE ✧
execute as @a[scores={CarrotStick=1..},nbt={active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run tag @s add bone_cancel
execute if score FreeMagic bool matches 0 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect give @s minecraft:hunger 3 6 true
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run playsound minecraft:entity.bat.takeoff player @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run playsound minecraft:entity.skeleton_horse.gallop_water player @a[tag=mg.flw] ~ ~ ~ 1 1
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run particle minecraft:soul ~ ~ ~ 0.5 0.1 0.5 0.02 25 force
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect give @s minecraft:jump_boost 5 0 true
execute as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect give @s minecraft:speed 5 8 true
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run tellraw @s {"text":"Bonestride ✧ successfully cancelled...","color":"gray","italic":true}
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run playsound minecraft:block.note_block.cow_bell player @s ~ ~ ~ 0.5 0.5
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect clear @s speed
execute as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect clear @s jump_boost

# BONESTRIDE OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},nbt={active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run tag @s add bone_cancel
execute if score FreeMagic bool matches 0 if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect give @s minecraft:hunger 3 6 true
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run playsound minecraft:entity.bat.takeoff player @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run playsound minecraft:entity.skeleton_horse.gallop_water player @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run particle minecraft:soul ~ ~ ~ 0.5 0.1 0.5 0.02 25 force
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect give @s minecraft:jump_boost 3 0 true
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect give @s minecraft:speed 3 6 true
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run tellraw @s {"text":"Bonestride successfully cancelled...","color":"gray","italic":true}
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] at @s run playsound minecraft:block.note_block.cow_bell player @s ~ ~ ~ 0.5 0.5
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect clear @s speed
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['1']}] run effect clear @s jump_boost

# BONESTRIDE ✧ OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},nbt={active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run tag @s add bone_cancel
execute if score FreeMagic bool matches 0 if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect give @s minecraft:hunger 3 6 true
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run playsound minecraft:entity.bat.takeoff player @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run playsound minecraft:entity.skeleton_horse.gallop_water player @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run particle minecraft:soul ~ ~ ~ 0.5 0.1 0.5 0.02 25 force
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect give @s minecraft:jump_boost 5 0 true
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=!bone_cancel,nbt=!{active_effects:[{id:"minecraft:speed"}]},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect give @s minecraft:speed 5 8 true
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run tellraw @s {"text":"Bonestride ✧ successfully cancelled...","color":"gray","italic":true}
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] at @s run playsound minecraft:block.note_block.cow_bell player @s ~ ~ ~ 0.5 0.5
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect clear @s speed
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=bone_cancel,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['11']}] run effect clear @s jump_boost

# AMULET SWAP

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['3']}] run tag @s add amulet_swap
execute as @a[scores={CarrotStick=1..},tag=amulet_swap,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['3']}] run item replace entity @s weapon.mainhand with carrot_on_a_stick[custom_name={"bold":true,"color":"blue","text":"Di-Aspect Amulet"},lore=["Gives the holder the","power to breathe water!",{"color":"aqua","text":"(Right click to swap"},{"color":"aqua","text":"active mode)"}],unbreakable={},tooltip_display={hidden_components:["unbreakable"]},damage=0,custom_model_data={strings:["4"]}] 1
execute as @a[tag=amulet_swap,tag=mg.flw] at @s run playsound minecraft:item.dye.use master @s ~ ~ ~ 1 1
execute as @a[tag=amulet_swap,tag=mg.flw] run scoreboard players set @s CarrotStick 0
execute as @a[tag=amulet_swap,tag=mg.flw] run tag @s remove amulet_swap

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['4']}] run tag @s add amulet_swap
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['4']}] run item replace entity @s weapon.mainhand with carrot_on_a_stick[custom_name={"bold":true,"color":"red","text":"Di-Aspect Amulet"},lore=["Gives the holder the","power to resist fire!",{"color":"aqua","text":"(Right click to swap"},{"color":"aqua","text":"active mode)"}],unbreakable={},tooltip_display={hidden_components:["unbreakable"]},damage=0,custom_model_data={strings:["3"]}] 1
execute as @a[tag=amulet_swap,tag=mg.flw] at @s run playsound minecraft:item.dye.use master @s ~ ~ ~ 1 1
execute as @a[tag=amulet_swap,tag=mg.flw] run scoreboard players set @s CarrotStick 0
execute as @a[tag=amulet_swap,tag=mg.flw] run tag @s remove amulet_swap

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['5']}] run tag @s add amulet_swap
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['5']}] run item replace entity @s weapon.mainhand with carrot_on_a_stick[custom_name={"bold":true,"color":"blue","text":"Tri-Aspect Amulet"},lore=["Gives the holder the","power to breathe water!",{"color":"aqua","text":"(Right click to swap"},{"color":"aqua","text":"active mode)"}],unbreakable={},tooltip_display={hidden_components:["unbreakable"]},damage=0,custom_model_data={strings:["6"]}] 1
execute as @a[tag=amulet_swap,tag=mg.flw] at @s run playsound minecraft:item.dye.use master @s ~ ~ ~ 1 1
execute as @a[tag=amulet_swap,tag=mg.flw] run scoreboard players set @s CarrotStick 0
execute as @a[tag=amulet_swap,tag=mg.flw] run tag @s remove amulet_swap

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['6']}] run tag @s add amulet_swap
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['6']}] run item replace entity @s weapon.mainhand with carrot_on_a_stick[custom_name={"bold":true,"color":"green","text":"Tri-Aspect Amulet"},lore=["Gives the holder the","power to resist toxins!",{"color":"aqua","text":"(Right click to swap"},{"color":"aqua","text":"active mode)"}],unbreakable={},tooltip_display={hidden_components:["unbreakable"]},damage=0,custom_model_data={strings:["7"]}] 1
execute as @a[tag=amulet_swap,tag=mg.flw] at @s run playsound minecraft:item.dye.use master @s ~ ~ ~ 1 1
execute as @a[tag=amulet_swap,tag=mg.flw] run scoreboard players set @s CarrotStick 0
execute as @a[tag=amulet_swap,tag=mg.flw] run tag @s remove amulet_swap

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['7']}] run tag @s add amulet_swap
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['7']}] run item replace entity @s weapon.mainhand with carrot_on_a_stick[custom_name={"bold":true,"color":"red","text":"Tri-Aspect Amulet"},lore=["Gives the holder the","power to resist fire!",{"color":"aqua","text":"(Right click to swap"},{"color":"aqua","text":"active mode)"}],unbreakable={},tooltip_display={hidden_components:["unbreakable"]},damage=0,custom_model_data={strings:["5"]}] 1
execute as @a[tag=amulet_swap,tag=mg.flw] at @s run playsound minecraft:item.dye.use master @s ~ ~ ~ 1 1
execute as @a[tag=amulet_swap,tag=mg.flw] run scoreboard players set @s CarrotStick 0
execute as @a[tag=amulet_swap,tag=mg.flw] run tag @s remove amulet_swap

# HONEYBOOST
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['8']}] at @s positioned ~ ~1 ~ run function utility:hb_check

# HONEYBOOST ✧
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['12']}] at @s positioned ~ ~1 ~ run function utility:hb_2_check

# HONEYBOOST OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['8']}] at @s positioned ~ ~1 ~ run function utility:hb_check

# HONEYBOOST ✧ OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['12']}] at @s positioned ~ ~1 ~ run function utility:hb_2_check

# DOMINION ROD
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['9']}] run function utility:dominion_start

# DOMINION ROD ✧
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['13']}] run function utility:dominion_2_start

# DOMINION ROD OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['9']}] run function utility:dominion_start

# DOMINION ROD ✧ OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['13']}] run function utility:dominion_2_start

# ICELIGHT SCEPTER
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['10']}] at @s run function utility:icelight_scepter_check

# ICELIGHT SCEPTER ✧
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s run function utility:icelight_scepter_2_check

# ICELIGHT SCEPTER OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['10']}] at @s run function utility:icelight_scepter_check

# ICELIGHT SCEPTER ✧ OFFHAND
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s run function utility:icelight_scepter_2_check

tag @a[tag=mg.flw] remove bone_cancel

# ZOIDBLASTER
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['17']}] run tag @s add zoiding
scoreboard players set @a[tag=zoiding,tag=mg.flw] shortray 0
execute as @a[tag=zoiding,tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['17']}] at @s anchored feet positioned ~ ~1.5 ~ positioned ^-0.5 ^ ^ facing ^0.5 ^ ^8 run function utility:zoidray
execute as @a[tag=zoiding,tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['17']}] at @s anchored feet positioned ~ ~1.5 ~ positioned ^0.5 ^ ^ facing ^-0.5 ^ ^8 run function utility:zoidray
execute as @a[tag=zoiding,tag=mg.flw] at @s run particle flash{color:[1.000,1.000,1.000,1.00]} ~ ~1 ~
execute as @a[tag=zoiding,tag=mg.flw] at @s run summon area_effect_cloud ~ ~ ~ {Tags:["zoid_death"],CustomName:"their own Zoid-Blasting self!"}
execute as @a[tag=zoiding,tag=mg.flw] at @s run damage @s 8 minecraft:mob_attack by @n[tag=zoid_death,distance=0..]
execute as @a[tag=zoiding,tag=mg.flw] at @s run kill @n[tag=zoid_death,distance=0..]
execute as @a[tag=zoiding,tag=mg.flw] at @s run playsound minecraft:entity.evoker.prepare_attack master @a[tag=mg.flw] ~ ~ ~ 1 2
tag @a[tag=mg.flw] remove zoiding

# ANCHORWAND

execute as @a[tag=mg.flw] if entity @s[scores={CarrotStick=1..}] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['16']}] run function utility:anchorwand_check

# PING

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['18']}] at @s run playsound minecraft:entity.allay.item_thrown master @s ~ ~ ~ 1 2
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['18']}] run effect give @a[gamemode=!spectator,tag=mg.flw] minecraft:glowing 10 0 true

# MAGIC SHOVEL

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['19']}] at @s run function utility:magic_shovel

# MIND ENTERER

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['20']}] at @s unless entity @n[tag=froggadew,distance=..2] run tellraw @s {"text":"Get close to a Froggadew to enter their mind...","color":"aqua","italic":true}
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['20']}] at @s unless entity @n[tag=froggadew,distance=..2] run playsound minecraft:block.note_block.cow_bell master @s ~ ~ ~ 1 0.6
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['20']}] at @s if entity @n[tag=froggadew,distance=..2] run function utility:mind_enterer

# SHOTGUN

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['21']}] unless entity @s[nbt={Inventory:[{id:"minecraft:arrow"}]}] run tellraw @s [{"text":"You don't have any arrows. Shotgun ammo hasn't been invented yet.","color":"gray","italic":true}]
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['21']}] unless entity @s[nbt={Inventory:[{id:"minecraft:arrow"}]}] at @s run playsound minecraft:block.note_block.cow_bell master @s ~ ~ ~ 1 0.5
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.* minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['21']}] if entity @s[nbt={Inventory:[{id:"minecraft:arrow"}]}] at @s facing ^ ^ ^1 run function utility:shotgun


# END CARROT CHECKS
scoreboard players set @a[tag=mg.flw] CarrotStick 0
