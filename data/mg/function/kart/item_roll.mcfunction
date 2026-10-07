# Tirage selon la position : les derniers ont de meilleurs objets (carapace bleue réservée aux derniers)
execute store result score $kr1 mg.st run random value 1..100
scoreboard players operation $kf1 mg.st = @s mg.krk
scoreboard players remove $kf1 mg.st 1
scoreboard players operation $kf1 mg.st *= #k100 mg.st
scoreboard players operation $kn1 mg.st = $kn mg.st
scoreboard players remove $kn1 mg.st 1
execute if score $kn1 mg.st matches ..0 run scoreboard players set $kf1 mg.st 50
execute if score $kn1 mg.st matches 1.. run scoreboard players operation $kf1 mg.st /= $kn1 mg.st
execute if score $kf1 mg.st matches ..33 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 41..75 run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 76..95 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 96.. run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 34..66 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 16..35 run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 36..65 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 66..95 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 96.. run scoreboard players set $kgv mg.st 5
execute if score $kf1 mg.st matches 67.. run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 11..30 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 31..55 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 56..78 run scoreboard players set $kgv mg.st 5
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 79..90 run scoreboard players set $kgv mg.st 6
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 91.. run scoreboard players set $kgv mg.st 7
scoreboard players operation @s mg.kit = $kgv mg.st
function mg:kart/item_give
