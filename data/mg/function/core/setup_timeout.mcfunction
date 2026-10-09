# 15 min : la génération n'a pas tout terminé
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"⚠ Génération pas terminée après 15 min (souvent : une partie en cours bloque la course d'élytres). Reste :","color":"red"}]
function mg:core/setup_progress
