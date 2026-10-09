# @s : robot — coup imprécis : impact au hasard (parfois dehors), parfois un lob
execute store result score $tnlx mg.st run random value -6300..6300
execute store result score $tndepth mg.st run random value 5000..11800
execute store result score $tnT mg.st run random value 26..36
execute store result score $tnq mg.st run random value 1..8
execute if score $tnq mg.st matches 1 run scoreboard players set $tnT mg.st 50
scoreboard players operation $tnside mg.st = @s mg.tns
function mg:tennis/lz
