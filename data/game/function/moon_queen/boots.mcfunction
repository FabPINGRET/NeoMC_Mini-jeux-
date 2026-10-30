data modify entity @n[tag=moonqueen_5_display,distance=0..] item.components.minecraft:custom_model_data set value {strings:['11']}
clear @p[gamemode=!spectator,tag=mg.flw] flint[minecraft:custom_model_data={strings:['11']}]

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Moon Queen","color":"light_purple","bold":true},{"text":"> I grant you a new","color":"white"},{"text":" Oath","color":"light_purple"},{"text":", Hero..."}]
advancement grant @a[tag=mg.flw] only sidequest:netherite_start
scoreboard players set $fla25 mg.fla 1

playsound minecraft:entity.warden.sonic_boom master @a[tag=mg.flw] ~ ~ ~ 1 0.1
#playsound minecraft:entity.allay.death master @a ~ ~ ~ 1 1
particle minecraft:end_rod ~ ~2 ~ 0.1 0.1 0.1 0.1 100

item replace block 9878 58 -104 container.22 from block 9876 54 -101 container.22
item replace block 9875 54 -101 container.22 from block 9876 54 -101 container.22
data modify entity @n[tag=moonqueen_stand,distance=0..] equipment.feet.id set value "minecraft:netherite_boots"

execute if items block 9878 58 -104 container.4 minecraft:netherite_helmet if items block 9878 58 -104 container.12 minecraft:netherite_chestplate if items block 9878 58 -104 container.14 minecraft:netherite_leggings if items block 9878 58 -104 container.22 minecraft:netherite_boots if items block 9878 58 -104 container.13 minecraft:netherite_sword run advancement grant @a[tag=mg.flw] only sidequest:netherite_complete
execute if items block 9878 58 -104 container.4 minecraft:netherite_helmet if items block 9878 58 -104 container.12 minecraft:netherite_chestplate if items block 9878 58 -104 container.14 minecraft:netherite_leggings if items block 9878 58 -104 container.22 minecraft:netherite_boots if items block 9878 58 -104 container.13 minecraft:netherite_sword run scoreboard players set $fla26 mg.fla 1
execute if items block 9878 58 -104 container.4 minecraft:netherite_helmet if items block 9878 58 -104 container.12 minecraft:netherite_chestplate if items block 9878 58 -104 container.14 minecraft:netherite_leggings if items block 9878 58 -104 container.22 minecraft:netherite_boots if items block 9878 58 -104 container.13 minecraft:netherite_sword run scoreboard players set all_oaths bool 1
execute if items block 9878 58 -104 container.4 minecraft:netherite_helmet if items block 9878 58 -104 container.12 minecraft:netherite_chestplate if items block 9878 58 -104 container.14 minecraft:netherite_leggings if items block 9878 58 -104 container.22 minecraft:netherite_boots if items block 9878 58 -104 container.13 minecraft:netherite_sword as @a[tag=mg.flw] run function game:100_check


fill ~1 ~ ~1 ~-1 ~2 ~-1 air replace minecraft:polished_blackstone_button
