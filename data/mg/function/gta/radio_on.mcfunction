# @s monte dans un véhicule : une station au hasard
tag @s add mg.gdrv
scoreboard players set @s mg.gal 60
execute store result score $gr mg.st run random value 0..7
execute if score $gr mg.st matches 0 run playsound minecraft:music_disc.pigstep record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 0 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Neo FM","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
execute if score $gr mg.st matches 1 run playsound minecraft:music_disc.chirp record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 1 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Radio Pixel","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
execute if score $gr mg.st matches 2 run playsound minecraft:music_disc.otherside record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 2 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Bass City","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
execute if score $gr mg.st matches 3 run playsound minecraft:music_disc.mall record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 3 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Lo-fi Avenue","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
execute if score $gr mg.st matches 4 run playsound minecraft:music_disc.blocks record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 4 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Retro 88","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
execute if score $gr mg.st matches 5 run playsound minecraft:music_disc.far record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 5 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Night Drive","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
execute if score $gr mg.st matches 6 run playsound minecraft:music_disc.creator record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 6 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Creator FM","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
execute if score $gr mg.st matches 7 run playsound minecraft:music_disc.precipice record @s ~ ~ ~ 0.8 1 0.5
execute if score $gr mg.st matches 7 run title @s actionbar [{"text":"📻 ","color":"white"},{"text":"Ocean Radio","color":"aqua","bold":true},{"text":"  ♪","color":"gray"}]
