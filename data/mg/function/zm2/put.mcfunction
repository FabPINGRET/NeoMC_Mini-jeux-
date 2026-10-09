# Macro $(slot)
$execute if score $zgn mg.st matches 1 run function mg:gun/put_1 {slot:"$(slot)"}
$execute if score $zgn mg.st matches 2 run function mg:gun/put_2 {slot:"$(slot)"}
$execute if score $zgn mg.st matches 3 run function mg:gun/put_3 {slot:"$(slot)"}
$execute if score $zgn mg.st matches 4 run function mg:gun/put_4 {slot:"$(slot)"}
$execute if score $zgn mg.st matches 5 run function mg:gun/put_5 {slot:"$(slot)"}
$execute if score $zgn mg.st matches 6 run function mg:gun/put_6 {slot:"$(slot)"}
