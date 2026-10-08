# Élytra — préparation ($elm : 1 course d'anneaux, 2 course + combat, 3 survie en vol)
execute unless score $elm mg.st matches 1..3 run scoreboard players set $elm mg.st 1
execute unless data storage mg:sky {built:1b} run tellraw @a [{"text":"🪽 Le décor Élytra n'est pas encore construit : il apparaît pendant la partie (les anneaux comptent déjà).","color":"yellow"}]
execute unless data storage mg:sky {built:1b} run function mg:sky/build
scoreboard players set #-1 mg.st -1
scoreboard players set #2 mg.st 2
scoreboard players set #5 mg.st 5
scoreboard players set #10 mg.st 10
scoreboard players set #11 mg.st 11
scoreboard players set #20 mg.st 20
scoreboard players set #72 mg.st 72
scoreboard players set #160 mg.st 160
scoreboard players reset * mg.skr
scoreboard players reset * mg.sks
scoreboard players reset * mg.skst
scoreboard players reset * mg.skl
scoreboard players reset * mg.sko
tag @a remove mg.skf
tag @a remove mg.skstun
tag @a remove mg.skak
tag @a remove mg.skv
tag @a remove mg.skw
execute if score $elm mg.st matches 1..2 run scoreboard players set @a[tag=mg.play] mg.skr 0
execute if score $elm mg.st matches 3 run scoreboard players set @a[tag=mg.play] mg.sks 0
scoreboard players set @a[tag=mg.play] mg.skg -40
scoreboard players set @a[tag=mg.play] mg.skst 0
scoreboard players set @a[tag=mg.play] mg.skl 0
scoreboard players set @a[tag=mg.play] mg.sko 0
scoreboard players set $skt mg.st 0
scoreboard players set $skpd mg.st 0
scoreboard players set $skpw mg.st 0
scoreboard players set $skpo mg.st 1
advancement revoke @a only mg:sky/hurt
execute if score $elm mg.st matches 1..2 run scoreboard players set $px mg.st 0
execute if score $elm mg.st matches 1..2 run scoreboard players set $py mg.st 250
execute if score $elm mg.st matches 1..2 run scoreboard players set $pz mg.st 27700
execute if score $elm mg.st matches 3 run scoreboard players set $px mg.st 0
execute if score $elm mg.st matches 3 run scoreboard players set $py mg.st 222
execute if score $elm mg.st matches 3 run scoreboard players set $pz mg.st 28940
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
effect clear @a[tag=mg.play] minecraft:levitation
item replace entity @a[tag=mg.play] armor.chest with minecraft:elytra[minecraft:custom_data={mg_sky:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du ciel","color":"aqua","italic":false}]
execute if score $elm mg.st matches 1..2 run forceload add -16 27624 16 27656
execute if score $elm mg.st matches 3 run forceload add -16 28984 16 29016
schedule function mg:sky/pad_wait 2t
