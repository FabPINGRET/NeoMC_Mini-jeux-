tellraw @s [{"text":"⚔ Tu es occupé (partie ou activité en cours) : tu ne peux pas accepter maintenant.","color":"gray"}]
tellraw @a[tag=mg.dlca] [{"text":"⚔ Ton adversaire est occupé : invitation annulée.","color":"gray"}]
function mg:duel/inv_end
