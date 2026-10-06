# Panneau du plot $(n) : relit le pseudo enregistré puis met le texte à jour
data modify storage mg:plot cur.name set value ""
$data modify storage mg:plot cur.name set from storage mg:plot owner.p$(n)
function mg:plot/label_set with storage mg:plot cur
