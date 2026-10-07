# Supprime les ANCIENNES parcelles + studio du Build Battle (ancien emplacement x -120..120, z 13700/13748, studio 0/13650)
# Les parcelles actuelles (x = 0, 640, 1280… ; studio -640) ne sont pas touchées : la parcelle 0 actuelle est préservée
tellraw @a[tag=mg.admin] [{"text":"Nettoyage des anciennes parcelles Build Battle en cours (chargement de la zone)…","color":"yellow"}]
forceload add -140 13630 140 13775
schedule function mg:bb/clear_old_run 3s
