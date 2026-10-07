# Danse de la victoire (@s sur la place) : 10 accroupissements en 3 s
execute store result score $sn mg.t if predicate mg:sneak
execute if score $sn mg.t matches 1 unless score @s mg.esn matches 1 run scoreboard players add @s mg.esc 1
scoreboard players operation @s mg.esn = $sn mg.t
scoreboard players add @s mg.est 1
execute if score @s mg.est matches 60.. run scoreboard players set @s mg.esc 0
execute if score @s mg.est matches 60.. run scoreboard players set @s mg.est 0
execute if score @s mg.esc matches 10.. unless entity @s[advancements={mg:secrets/danse=true}] run advancement grant @s only mg:secrets/danse
