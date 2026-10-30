execute if block 10328 33 -54 anvil run particle lava 10333 29 -63 0.3 2 0.3 0 150
execute if block 10328 33 -54 anvil run playsound minecraft:entity.breeze.wind_burst master @a[tag=mg.flw] 10333 29 -63 2 0.5
execute if block 10328 33 -54 anvil run playsound minecraft:item.mace.smash_air master @a[tag=mg.flw] 10333 29 -63 2 0.1

execute if block 10328 33 -54 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:thorns":1}
execute if block 10328 33 -54 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:thorns":1}
execute if block 10328 33 -54 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:thorns":1}
execute if block 10328 33 -54 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:thorns":1}

execute if block 10328 33 -54 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:thorns":2}
execute if block 10328 33 -54 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:thorns":2}
execute if block 10328 33 -54 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:thorns":2}
execute if block 10328 33 -54 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:thorns":2}

execute if block 10328 33 -54 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:thorns":3}
execute if block 10328 33 -54 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:thorns":3}
execute if block 10328 33 -54 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:thorns":3}
execute if block 10328 33 -54 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=thorn,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:thorns":3}

execute if block 10328 33 -54 anvil positioned 10331 28 -63 run advancement grant @p[gamemode=!spectator,tag=mg.flw] only sidequest_2:npc_scleemotius
execute if block 10328 33 -54 anvil positioned 10331 28 -63 run tag @p[gamemode=!spectator,tag=mg.flw] add upgrade_scleemotius

execute as @a[tag=mg.flw] run function game:100_check


execute unless block 10328 33 -54 anvil run particle lava 10333 26 -63 0.2 0.2 0.2 0 100
execute unless block 10328 33 -54 anvil run playsound minecraft:entity.breeze.idle_ground master @a[tag=mg.flw] 10333 29 -63 2 1

fill 10328 29 -54 10328 33 -54 minecraft:iron_chain strict
setblock 10328 28 -54 anvil[facing=east] strict
