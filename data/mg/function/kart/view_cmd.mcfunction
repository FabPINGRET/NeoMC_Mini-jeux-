# /trigger mg.kv : 1 = 3e personne, 2 = 1re personne
execute if score @s mg.kv matches 1 run scoreboard players set @s mg.kvm 0
execute if score @s mg.kv matches 2 run scoreboard players set @s mg.kvm 1
execute if score @s mg.kv matches 1 run tellraw @s [{"text":"🎥 Caméra de poursuite (pas de clic en spectateur : Ctrl = objet).","color":"aqua"}]
execute if score @s mg.kv matches 2 run tellraw @s [{"text":"🎥 Vue assise (clic droit = objet, F5 = 3e personne).","color":"aqua"}]
scoreboard players reset @s mg.kv
scoreboard players enable @s mg.kv
