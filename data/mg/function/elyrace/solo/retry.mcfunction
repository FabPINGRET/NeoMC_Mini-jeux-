# @s = joueur qui clique [⟲ Rejouer] (mg.xs 5) : nouvelle tentative sur le même parcours et la même place de départ, sans passer par stop
# (tag mg.xso, pause, mg.xsp0, mg.ri, mg.xcr, mg.xsl restent : seule solo/arm remet la course à zéro). Offert à l'arrivée seulement (phase 4)
execute unless entity @s[tag=mg.xso] run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Tu n'as pas de contre-la-montre en cours.","color":"red"}]
execute unless score @s mg.xph matches 4 run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Rejouer n'est proposé qu'à l'arrivée d'un contre-la-montre.","color":"red"}]
tellraw @s [{"text":"⟲ Nouvelle tentative !","color":"aqua"},{"text":" ","color":"gray"},{"text":"[✖ Abandonner]","color":"red","click_event":{"action":"run_command","command":"trigger mg.xs set 2"},"hover_event":{"action":"show_text","value":"Quitter le contre-la-montre"}}]
# le gel de la phase 4 est levé, puis re-posé par arm (sinon le modificateur serait ajouté deux fois)
function mg:core/unfreeze
function mg:elyrace/solo/arm
