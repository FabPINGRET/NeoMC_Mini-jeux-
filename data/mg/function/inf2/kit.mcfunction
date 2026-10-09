# @s : survivant (couteau, pistolet, une arme au hasard)
clear @s
function mg:gun/reset
item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},custom_name=[{"text":"🔪 Couteau","color":"gray","italic":false}]]
function mg:gun/put_1 {slot:"hotbar.1"}
execute store result score $zx mg.st run random value 2..4
execute if score $zx mg.st matches 2 run function mg:gun/put_2 {slot:"hotbar.2"}
execute if score $zx mg.st matches 3 run function mg:gun/put_3 {slot:"hotbar.2"}
execute if score $zx mg.st matches 4 run function mg:gun/put_4 {slot:"hotbar.2"}
item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=3361970,unbreakable={}]
effect give @s minecraft:saturation infinite 0 true
