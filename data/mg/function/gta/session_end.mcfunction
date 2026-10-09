# Plus personne à Neo City : entités retirées, ville réparée en tâche de fond, puis plus de chargement forcé
scoreboard players set $gtw mg.st 0
scoreboard players set $gsu mg.st 0
schedule clear mg:gta/session_setup
function mg:gta/clear
function mg:gta/bars_remove
team remove mg_gciv
scoreboard players set $gwb mg.st 40
scoreboard players set $gwfull mg.st 0
schedule function mg:gta/wb_step 20t
