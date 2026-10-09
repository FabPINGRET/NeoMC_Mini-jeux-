# 🚫 « Exclure Zinedine » (menu ≡) : running gag, c'est celui qui clique qui part (@s)
tellraw @a [{"text":"🚫 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a voulu exclure Zinedine... ","color":"gray"},{"text":"mauvaise idée.","color":"red","bold":true}]
execute as @a at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 0.8
# kick : niveau 3 requis pour les fonctions (DockerMC : FUNCTION_PERMISSION_LEVEL=3). Passé par une macro, lue à l'exécution :
# sans la permission, seul cet appel échoue (une commande interdite écrite en dur empêcherait le chargement de la fonction)
scoreboard players set $zz mg.st 0
execute store success score $zz mg.st run function mg:troll/kick {m:"Zinedine ne se laisse pas exclure. C'est toi qui sors !"}
# sans la permission : fausse déconnexion (écran noir 4 s + message)
execute if score $zz mg.st matches 0 run function mg:troll/zinedine_fake
