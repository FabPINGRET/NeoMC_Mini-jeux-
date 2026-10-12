# Menu texte des événements du lobby (@s = admin)
tellraw @s {"text":"🎉 Événements du lobby","color":"light_purple","bold":true}
tellraw @s ["",{"text":" [🎲 Au hasard]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.opt set 68"},"hover_event":{"action":"show_text","value":"Un des trois événements, annoncé 10 s avant"}}]
tellraw @s ["",{"text":" [👑 Roi Zombie]","color":"red","click_event":{"action":"run_command","command":"trigger mg.opt set 69"},"hover_event":{"action":"show_text","value":"Un zombie géant attaque le spawn ! Tape-le fort, le plus gros cogneur gagne."}}]
tellraw @s ["",{"text":" [💰 Pluie de pièces]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.opt set 70"},"hover_event":{"action":"show_text","value":"Des pièces tombent du ciel ! Pépite = 1, lingot = 5. Le plus riche gagne."}}]
tellraw @s ["",{"text":" [🗝 Chasse au trésor]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.opt set 71"},"hover_event":{"action":"show_text","value":"Un coffre est caché sur l'île. Suis les indices, le premier qui le trouve gagne."}}]
tellraw @s ["",{"text":" [⛔ Arrêter / annuler]","color":"dark_red","click_event":{"action":"run_command","command":"trigger mg.opt set 72"},"hover_event":{"action":"show_text","value":"Arrête l'événement en cours ou annule celui qui est annoncé"}}]
