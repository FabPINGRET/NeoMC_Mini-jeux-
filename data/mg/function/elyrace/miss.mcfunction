# @s = joueur qui a raté un anneau : retour au dernier point de reprise
tellraw @s [{"text":"✖ Anneau raté ! ","color":"red","bold":true},{"text":"Retour au dernier point de reprise.","color":"gray"}]
function mg:elyrace/respawn
