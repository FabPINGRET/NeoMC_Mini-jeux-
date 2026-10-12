# Admin : arrête l'événement en cours ou annule celui qui est annoncé (le prochain revient dans 30 min)
execute unless score $evon mg.st matches 1.. unless score $evn mg.st matches 1..60 run return run tellraw @s {"text":"Aucun événement en cours ni annoncé.","color":"gray"}
scoreboard players set $evn mg.st 1800
function mg:lobby/ev/stop
tellraw @a {"text":"🎉 L'événement du lobby a été annulé par un admin.","color":"gray"}
