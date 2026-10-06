# @s = maître : lit la 1re page de son livre
data remove storage mg:bb tmp
execute store success score $bbok mg.st run data modify storage mg:bb tmp set from entity @s Inventory[{id:"minecraft:writable_book"}].components."minecraft:writable_book_content".pages[0].raw
execute unless score $bbok mg.st matches 1 store success score $bbok mg.st run data modify storage mg:bb tmp set from entity @s Inventory[{id:"minecraft:writable_book"}].components."minecraft:writable_book_content".pages[0]
execute unless score $bbok mg.st matches 1 run return run tellraw @s [{"text":"⚠ Livre vide ou introuvable : écris le thème sur la 1re page, clique sur « Terminé », puis valide à nouveau.","color":"red"}]
execute store result score $bbl mg.st run data get storage mg:bb tmp
execute unless score $bbl mg.st matches 1..40 run return run tellraw @s [{"text":"⚠ Le thème doit faire de 1 à 40 caractères.","color":"red"}]
data modify storage mg:bb word set from storage mg:bb tmp
function mg:bb/word_apply
