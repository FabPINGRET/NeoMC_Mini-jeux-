# Admin : réinitialise les votes (@s = admin)
function mg:vote/clear
function mg:vote/refresh
tellraw @a [{"text":"☑ Les votes ont été réinitialisés.","color":"gray"}]
