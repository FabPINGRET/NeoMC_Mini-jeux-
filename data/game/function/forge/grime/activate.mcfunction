execute if block 10356 45 -216 anvil run particle lava 10350 41 -207 0.3 2 0.3 0 150
execute if block 10356 45 -216 anvil run playsound minecraft:entity.breeze.wind_burst master @a[tag=mg.flw] 10350 41 -207 2 0.5
execute if block 10356 45 -216 anvil run playsound minecraft:item.mace.smash_air master @a[tag=mg.flw] 10350 41 -207 2 0.1

execute if block 10356 45 -216 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:projectile_protection":1}
execute if block 10356 45 -216 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:projectile_protection":1}
execute if block 10356 45 -216 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:projectile_protection":1}
execute if block 10356 45 -216 anvil if score forge_level Value matches 1 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:projectile_protection":1}

execute if block 10356 45 -216 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:projectile_protection":2}
execute if block 10356 45 -216 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:projectile_protection":2}
execute if block 10356 45 -216 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:projectile_protection":2}
execute if block 10356 45 -216 anvil if score forge_level Value matches 2 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:projectile_protection":2}

execute if block 10356 45 -216 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.head.components."minecraft:enchantments" set value {"minecraft:projectile_protection":3}
execute if block 10356 45 -216 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.chest.components."minecraft:enchantments" set value {"minecraft:projectile_protection":3}
execute if block 10356 45 -216 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.legs.components."minecraft:enchantments" set value {"minecraft:projectile_protection":3}
execute if block 10356 45 -216 anvil if score forge_level Value matches 3 run data modify entity @n[tag=forge_stand,tag=grime,distance=0..] equipment.feet.components."minecraft:enchantments" set value {"minecraft:projectile_protection":3}

execute if block 10356 45 -216 anvil positioned 10352 40 -207 run advancement grant @p[gamemode=!spectator,tag=mg.flw] only sidequest_2:npc_mudtilda
execute if block 10356 45 -216 anvil positioned 10352 40 -207 run tag @p[gamemode=!spectator,tag=mg.flw] add upgrade_mudtilda

execute as @a[tag=mg.flw] run function game:100_check

execute unless block 10356 45 -216 anvil run particle lava 10350 38 -207 0.2 0.2 0.2 0 100
execute unless block 10356 45 -216 anvil run playsound minecraft:entity.breeze.idle_ground master @a[tag=mg.flw] 10350 41 -207 2 1

fill 10356 41 -216 10356 45 -216 minecraft:iron_chain strict
setblock 10356 40 -216 anvil[facing=west] strict
