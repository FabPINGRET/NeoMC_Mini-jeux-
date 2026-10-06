# Pion du joueur @s : porte-armure avec sa tête, son pseudo et une armure à sa couleur
summon minecraft:armor_stand 0.5 70 14948.5 {Tags:["mg.mppawn","mg.mpnew"],Invulnerable:1b,NoGravity:1b,ShowArms:1b,NoBasePlate:1b,DisabledSlots:4144959,CustomNameVisible:1b}
scoreboard players operation @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] mg.mpo = @s mg.mpo
loot replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.head loot mg:plot_head
data modify entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] CustomName set from entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] equipment.head.components."minecraft:profile".name
scoreboard players operation $pc mg.st = @s mg.mpo
scoreboard players operation $pc mg.st %= #8 mg.st
execute if score $pc mg.st matches 1 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=15022389]
execute if score $pc mg.st matches 1 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=15022389]
execute if score $pc mg.st matches 1 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=15022389]
execute if score $pc mg.st matches 2 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=1999077]
execute if score $pc mg.st matches 2 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=1999077]
execute if score $pc mg.st matches 2 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=1999077]
execute if score $pc mg.st matches 3 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=4431943]
execute if score $pc mg.st matches 3 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=4431943]
execute if score $pc mg.st matches 3 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=4431943]
execute if score $pc mg.st matches 4 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=16635957]
execute if score $pc mg.st matches 4 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=16635957]
execute if score $pc mg.st matches 4 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=16635957]
execute if score $pc mg.st matches 5 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=9315498]
execute if score $pc mg.st matches 5 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=9315498]
execute if score $pc mg.st matches 5 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=9315498]
execute if score $pc mg.st matches 6 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=16485376]
execute if score $pc mg.st matches 6 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=16485376]
execute if score $pc mg.st matches 6 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=16485376]
execute if score $pc mg.st matches 7 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=44225]
execute if score $pc mg.st matches 7 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=44225]
execute if score $pc mg.st matches 7 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=44225]
execute if score $pc mg.st matches 0 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.chest with minecraft:leather_chestplate[dyed_color=15753874]
execute if score $pc mg.st matches 0 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.legs with minecraft:leather_leggings[dyed_color=15753874]
execute if score $pc mg.st matches 0 run item replace entity @e[type=minecraft:armor_stand,tag=mg.mpnew,limit=1] armor.feet with minecraft:leather_boots[dyed_color=15753874]
tag @e[type=minecraft:armor_stand,tag=mg.mpnew] remove mg.mpnew
