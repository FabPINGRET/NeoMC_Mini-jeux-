# Un secret trouvé (@s) : petite fête, et le grand final quand tout est trouvé
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.3
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.5 0.8 0.5 0.4 40
execute if entity @s[advancements={mg:secrets/terrier=true,mg:secrets/tuyau=true,mg:secrets/couronne=true,mg:secrets/etoiles=true,mg:secrets/ile=true,mg:secrets/plongeon=true,mg:secrets/vide=true,mg:secrets/arsenal=true,mg:secrets/mille=true,mg:secrets/lynx=true,mg:secrets/sommet=true,mg:secrets/ecureuil=true,mg:secrets/pilote=true,mg:secrets/volant=true,mg:secrets/danse=true,mg:secrets/bouton=true,mg:secrets/visite=true}] unless entity @s[advancements={mg:secrets/maitre=true}] run advancement grant @s only mg:secrets/maitre
