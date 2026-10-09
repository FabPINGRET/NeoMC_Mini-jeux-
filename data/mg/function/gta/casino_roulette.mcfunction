# @s mise 100 $ à la roulette : 47 % de chances de doubler
execute store result score $gr mg.st run random value 0..99
scoreboard players set @s mg.gal 40
execute if score $gr mg.st matches ..46 run scoreboard players add @s mg.gta 200
execute if score $gr mg.st matches ..46 run title @s actionbar {"text":"🎡 Rouge ! +200 $","color":"red","bold":true}
execute if score $gr mg.st matches 47.. run title @s actionbar {"text":"🎡 Noir… la banque gagne","color":"gray"}
execute if score $gr mg.st matches ..46 at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.2
execute if score $gr mg.st matches 47.. at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6
