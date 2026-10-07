scoreboard players add @s mg.kcp 1
execute if score @s mg.kcp >= $kK mg.st run scoreboard players set @s mg.kcp 0
execute if score @s mg.kcp matches 1 run function mg:kart/lap
