# @s : lit la 1re page de son livre → ch[mg.tc].s<étape>
data remove storage mg:tel tmp
execute store success score $tok mg.st run data modify storage mg:tel tmp set from entity @s Inventory[{id:"minecraft:writable_book"}].components."minecraft:writable_book_content".pages[0].raw
execute unless score $tok mg.st matches 1 store success score $tok mg.st run data modify storage mg:tel tmp set from entity @s Inventory[{id:"minecraft:writable_book"}].components."minecraft:writable_book_content".pages[0]
execute unless score $tok mg.st matches 1 run return run tellraw @s {"text":"⚠ Livre vide : écris sur la 1re page, clique « Terminé », puis valide.","color":"red"}
execute store result score $tl mg.st run data get storage mg:tel tmp
execute unless score $tl mg.st matches 1..40 run return run tellraw @s {"text":"⚠ De 1 à 40 caractères, s'il te plaît.","color":"red"}
execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc
execute if score $tp mg.st matches 0 run data modify storage mg:tel p.k set value "s0"
execute if score $tp mg.st matches 2 run data modify storage mg:tel p.k set value "s2"
execute if score $tp mg.st matches 4 run data modify storage mg:tel p.k set value "s4"
function mg:tel/store with storage mg:tel p
tag @s add mg.tdone
tellraw @s [{"text":"✔ Enregistré : ","color":"green"},{"nbt":"tmp","storage":"mg:tel","color":"white"},{"text":" — en attente des autres…","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2
