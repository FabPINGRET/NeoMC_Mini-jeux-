# (OP) Devenir admin des mini-jeux : reçoit l'objet ≡ MENU
tag @s add mg.admin
function mg:core/give_menu
tellraw @s [{"text":"✔ Tu es maintenant admin des mini-jeux — objet ","color":"green"},{"text":"≡ MENU","color":"gold"},{"text":" ajouté à ta barre d'action.","color":"green"}]
tellraw @s [{"text":"Pour nommer un autre admin : ","color":"gray"},{"text":"/tag <joueur> add mg.admin","color":"yellow"}]
