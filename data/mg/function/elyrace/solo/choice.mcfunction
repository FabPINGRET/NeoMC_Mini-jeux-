# @s = joueur dont la phase 3 (arrivée) se termine : PHASE 4, choix entre rejouer (solo/retry) et le lobby (solo/quit, ou solo/wait au bout de 30 s).
# Pas de stop : le tag, la pause et le parcours restent. Seule l'arrivée y passe (la limite de 3 minutes, elle, arrête le solo : pas de nouvelle tentative)
# gravité normale (plus de vol), retour sur sa place de départ, gel (le même que le décompte ; solo/retry le lève avant solo/arm)
function mg:core/attr_reset_g
function mg:elyrace/place_tp
function mg:core/freeze
scoreboard players set @s mg.xph 4
scoreboard players set @s mg.xst 0
tellraw @s [{"text":"🏁 Et maintenant ? ","color":"gold"},{"text":"[⟲ Rejouer]","color":"green","bold":true,"click_event":{"action":"run_command","command":"trigger mg.xs set 5"},"hover_event":{"action":"show_text","value":"Relancer le même parcours tout de suite"}},{"text":" ","color":"gray"},{"text":"[⌂ Retour au lobby]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.xs set 6"},"hover_event":{"action":"show_text","value":"Quitter le contre-la-montre"}},{"text":" (lobby automatique dans 30 s)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2
# compte à rebours affiché tout de suite (wait ne l'écrit qu'à chaque seconde pleine, et seen avance xst avant le prochain passage)
function mg:elyrace/solo/wait
