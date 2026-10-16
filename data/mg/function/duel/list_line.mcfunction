# Ligne de la liste (macro : $(v) = 1000 + id ; @s = joueur listé, destinataire = demandeur mg.dlq)
$tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"red"},{"selector":"@s","color":"white","click_event":{"action":"run_command","command":"trigger mg.duel set $(v)"},"hover_event":{"action":"show_text","value":"Défier ce joueur en duel sniper"}},{"text":"  ← clique pour défier","color":"gray"}]
