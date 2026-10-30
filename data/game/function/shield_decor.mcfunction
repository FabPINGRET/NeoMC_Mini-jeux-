execute if block ~ ~-2 ~ air run tellraw @p[tag=mg.flw] {"text":"This shield pattern has not been unlocked yet...","color":"gray","italic":true}
execute if block ~ ~-2 ~ redstone_block as @p[tag=mg.flw] if items entity @s weapon.mainhand minecraft:shield run item replace entity @s weapon.mainhand from block ~ ~-1 ~ container.0
execute if block ~ ~-2 ~ redstone_block as @p[tag=mg.flw] if items entity @s weapon.mainhand minecraft:shield run playsound minecraft:item.armor.equip_leather block @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block ~ ~-2 ~ redstone_block as @p[tag=mg.flw] if items entity @s weapon.offhand minecraft:shield run item replace entity @s weapon.offhand from block ~ ~-1 ~ container.0
execute if block ~ ~-2 ~ redstone_block as @p[tag=mg.flw] if items entity @s weapon.offhand minecraft:shield run playsound minecraft:item.armor.equip_leather block @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block ~ ~-2 ~ redstone_block as @p[tag=mg.flw] unless items entity @s weapon.* minecraft:shield run tellraw @p[tag=mg.flw] {"text":"You must equip a shield!","color":"gray","italic":true}
