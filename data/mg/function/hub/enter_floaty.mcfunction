# @s entre au portail de Scourge of the Floaty Isles (hub) : verrouillé tant que le terrain n'est pas installé
execute unless data storage mg:hub {floaty:1b} run return run title @s actionbar {"text":"🔒 Scourge of the Floaty Isles : bientôt disponible","color":"aqua"}
function mg:floaty/menu_go
