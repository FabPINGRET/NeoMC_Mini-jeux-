# @s : couteau + pistolet
clear @s
function mg:gun/reset
item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},custom_name=[{"text":"🔪 Couteau","color":"gray","italic":false}]]
function mg:gun/put_1 {slot:"hotbar.1"}
item replace entity @s hotbar.8 with minecraft:cooked_beef 16
