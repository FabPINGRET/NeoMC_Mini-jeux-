# Tirage selon la position (0 = premier, 100 = dernier) : la tête reçoit des objets de défense, la queue des objets puissants
execute store result score $kr1 mg.st run random value 1..100
scoreboard players operation $kf1 mg.st = @s mg.krk
scoreboard players remove $kf1 mg.st 1
scoreboard players operation $kf1 mg.st *= #k100 mg.st
scoreboard players operation $kn1 mg.st = $kn mg.st
scoreboard players remove $kn1 mg.st 1
execute if score $kn1 mg.st matches ..0 run scoreboard players set $kf1 mg.st 50
execute if score $kn1 mg.st matches 1.. run scoreboard players operation $kf1 mg.st /= $kn1 mg.st
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 1..28 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 29..36 run scoreboard players set $kgv mg.st 8
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 37..60 run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 61..70 run scoreboard players set $kgv mg.st 18
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 71..80 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 81..86 run scoreboard players set $kgv mg.st 16
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 87..92 run scoreboard players set $kgv mg.st 13
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 93..100 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 1..8 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 9..22 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 23..32 run scoreboard players set $kgv mg.st 9
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 33..42 run scoreboard players set $kgv mg.st 10
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 43..54 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 55..64 run scoreboard players set $kgv mg.st 11
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 65..72 run scoreboard players set $kgv mg.st 13
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 73..82 run scoreboard players set $kgv mg.st 15
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 83..89 run scoreboard players set $kgv mg.st 17
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 90..94 run scoreboard players set $kgv mg.st 16
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 95..100 run scoreboard players set $kgv mg.st 5
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 1..15 run scoreboard players set $kgv mg.st 11
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 16..30 run scoreboard players set $kgv mg.st 12
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 31..45 run scoreboard players set $kgv mg.st 5
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 46..60 run scoreboard players set $kgv mg.st 14
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 61..70 run scoreboard players set $kgv mg.st 10
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 71..80 run scoreboard players set $kgv mg.st 19
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 81..87 run scoreboard players set $kgv mg.st 6
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 88..92 run scoreboard players set $kgv mg.st 7
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 93..96 run scoreboard players set $kgv mg.st 17
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 97..100 run scoreboard players set $kgv mg.st 15
scoreboard players operation @s mg.kit = $kgv mg.st
function mg:kart/item_give
