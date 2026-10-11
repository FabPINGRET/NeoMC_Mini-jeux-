# @s : joueur du lobby, prend l'arme $lgn (case 2)
function mg:gun/reset
execute if score $lgn mg.st matches 1 run function mg:gun/put_1 {slot:"hotbar.1"}
execute if score $lgn mg.st matches 2 run function mg:gun/put_2 {slot:"hotbar.1"}
execute if score $lgn mg.st matches 3 run function mg:gun/put_3 {slot:"hotbar.1"}
execute if score $lgn mg.st matches 4 run function mg:gun/put_4 {slot:"hotbar.1"}
execute if score $lgn mg.st matches 5 run function mg:gun/put_5 {slot:"hotbar.1"}
execute if score $lgn mg.st matches 6 run function mg:gun/put_6 {slot:"hotbar.1"}
execute if score $lgn mg.st matches 7 run function mg:lobby/rpg_give
title @s actionbar [{"text":"🔫 Arme prise (case 2) : ","color":"gold"},{"text":"clic gauche tirer, clic droit viser, accroupi recharger","color":"gray"}]
playsound minecraft:item.armor.equip_iron player @s ~ ~ ~ 1 1.2
