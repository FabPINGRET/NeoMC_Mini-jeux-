# @s : jauge de braquage (Braquage du passant), mg.grob sur 40
scoreboard players set @s mg.gal 10
scoreboard players operation $gbp mg.st = @s mg.grob
scoreboard players set #10 mg.st 10
scoreboard players operation $gbp mg.st *= #10 mg.st
scoreboard players set $gbn mg.st 40
scoreboard players operation $gbp mg.st /= $gbn mg.st
execute if score $gbp mg.st matches 0 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"","color":"green"},{"text":"▯▯▯▯▯▯▯▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 1 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮","color":"green"},{"text":"▯▯▯▯▯▯▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 2 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮","color":"green"},{"text":"▯▯▯▯▯▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 3 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮","color":"green"},{"text":"▯▯▯▯▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 4 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮▮","color":"green"},{"text":"▯▯▯▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 5 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮▮▮","color":"green"},{"text":"▯▯▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 6 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮▮▮▮","color":"green"},{"text":"▯▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 7 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮▮▮▮▮","color":"green"},{"text":"▯▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 8 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮▮▮▮▮▮","color":"green"},{"text":"▯▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 9 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮▮▮▮▮▮▮","color":"green"},{"text":"▯","color":"dark_gray"}]
execute if score $gbp mg.st matches 10 run title @s actionbar [{"text":"💰 Braquage du passant  ","color":"yellow","bold":true},{"text":"▮▮▮▮▮▮▮▮▮▮","color":"green"},{"text":"","color":"dark_gray"}]
