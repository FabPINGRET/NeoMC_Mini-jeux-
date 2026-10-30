execute positioned -23 136 99 run playsound minecraft:entity.silverfish.death master @a[tag=mg.flw] ~ ~ ~ 1 2

execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:leather_boots"}}] run advancement grant @s only sidequest_2:npc_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:chainmail_boots"}}] run advancement grant @s only sidequest_2:npc_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:iron_boots"}}] run advancement grant @s only sidequest_2:npc_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:diamond_boots"}}] run advancement grant @s only sidequest_2:npc_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:netherite_boots"}}] run advancement grant @s only sidequest_2:npc_scrimp

execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:leather_boots"}}] run tag @s add upgrade_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:chainmail_boots"}}] run tag @s add upgrade_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:iron_boots"}}] run tag @s add upgrade_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:diamond_boots"}}] run tag @s add upgrade_scrimp
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:netherite_boots"}}] run tag @s add upgrade_scrimp

execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:leather_boots"}}] as @a[tag=mg.flw] run function game:100_check
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:chainmail_boots"}}] as @a[tag=mg.flw] run function game:100_check
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:iron_boots"}}] as @a[tag=mg.flw] run function game:100_check
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:diamond_boots"}}] as @a[tag=mg.flw] run function game:100_check
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:netherite_boots"}}] as @a[tag=mg.flw] run function game:100_check

execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:leather_boots"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scrimp the Tailor","color":"blue"},{"text":"> We see boots, let us sew them, let us sew them! So clomping, so stomping, we will sew them proper! We will sew them right! Therrrrre there, we have fixed them, they are now swimming! They are now sleek! Try them, try them!","color":"white"}]
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:leather_boots"}}] run enchant @p[tag=mg.flw] depth_strider 3
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:chainmail_boots"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scrimp the Tailor","color":"blue"},{"text":"> We see boots, let us sew them, let us sew them! So clomping, so stomping, we will sew them proper! We will sew them right! Therrrrre there, we have fixed them, they are now swimming! They are now sleek! Try them, try them!","color":"white"}]
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:chainmail_boots"}}] run enchant @p[tag=mg.flw] depth_strider 3
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:iron_boots"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scrimp the Tailor","color":"blue"},{"text":"> We see boots, let us sew them, let us sew them! So clomping, so stomping, we will sew them proper! We will sew them right! Therrrrre there, we have fixed them, they are now swimming! They are now sleek! Try them, try them!","color":"white"}]
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:iron_boots"}}] run enchant @p[tag=mg.flw] depth_strider 3
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:diamond_boots"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scrimp the Tailor","color":"blue"},{"text":"> We see boots, let us sew them, let us sew them! So clomping, so stomping, we will sew them proper! We will sew them right! Therrrrre there, we have fixed them, they are now swimming! They are now sleek! Try them, try them!","color":"white"}]
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:diamond_boots"}}] run enchant @p[tag=mg.flw] depth_strider 3
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:netherite_boots"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scrimp the Tailor","color":"blue"},{"text":"> We see boots, let us sew them, let us sew them! So clomping, so stomping, we will sew them proper! We will sew them right! Therrrrre there, we have fixed them, they are now swimming! They are now sleek! Try them, try them!","color":"white"}]
execute positioned -23 136 99 as @p[tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:netherite_boots"}}] run enchant @p[tag=mg.flw] depth_strider 3

execute positioned -23 136 99 as @p[tag=mg.flw] unless entity @s[nbt={SelectedItem:{id:"minecraft:leather_boots"}}] unless entity @s[nbt={SelectedItem:{id:"minecraft:chainmail_boots"}}] unless entity @s[nbt={SelectedItem:{id:"minecraft:iron_boots"}}] unless entity @s[nbt={SelectedItem:{id:"minecraft:diamond_boots"}}] unless entity @s[nbt={SelectedItem:{id:"minecraft:netherite_boots"}}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scrimp the Tailor","color":"blue"},{"text":"> Scrimp hates boots, horrible boots, clumsy boots. We must fix them, we must sew them! We cannot help it if we are shown them...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
