execute if block 10136 44 196 anvil run particle lava 10145 40 201 0.3 2 0.3 0 150
execute if block 10136 44 196 anvil run playsound minecraft:entity.breeze.wind_burst master @a[tag=mg.flw] 10145 40 201 2 0.5
execute if block 10136 44 196 anvil run playsound minecraft:item.mace.smash_air master @a[tag=mg.flw] 10145 40 201 2 0.1

execute if block 10136 44 196 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:protection":1}
execute if block 10136 44 196 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:protection":1}
execute if block 10136 44 196 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:protection":1}
execute if block 10136 44 196 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:protection":1}

execute if block 10136 44 196 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:protection":2}
execute if block 10136 44 196 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:protection":2}
execute if block 10136 44 196 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:protection":2}
execute if block 10136 44 196 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:protection":2}

execute if block 10136 44 196 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:protection":3}
execute if block 10136 44 196 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:protection":3}
execute if block 10136 44 196 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:protection":3}
execute if block 10136 44 196 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=mountain,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:protection":3}

execute if block 10136 44 196 anvil positioned 10145 39 199 run advancement grant @p[gamemode=!spectator,tag=mg.flw] only sidequest_2:npc_vok
execute if block 10136 44 196 anvil positioned 10145 39 199 run tag @p[gamemode=!spectator,tag=mg.flw] add upgrade_vok

execute as @a[tag=mg.flw] run function game:100_check

execute unless block 10136 44 196 anvil run particle lava 10145 37 201 0.2 0.2 0.2 0 100
execute unless block 10136 44 196 anvil run playsound minecraft:entity.breeze.idle_ground master @a[tag=mg.flw] 10145 40 201 2 1

fill 10136 40 196 10136 44 196 minecraft:iron_chain strict
setblock 10136 39 196 anvil[facing=south] strict
