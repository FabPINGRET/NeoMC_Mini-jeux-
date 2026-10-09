# ------------------------------------------------------------------ Meccha Chameleon : outils des caméléons, visibles dans l'inventaire mais pas en main
# Exécuté par gen_rp.py (exec) : utilise wjson, A. Un caméléon est invisible : l'objet tenu ne doit pas trahir sa position.
for _nm, _mdl in (('cham_palette', 'minecraft:item/brush'), ('cham_pipette', 'minecraft:item/glass_bottle'), ('cham_pose', 'minecraft:item/armor_stand'),
                  ('cham_decoy', 'minecraft:item/totem_of_undying'), ('cham_taunt', 'minecraft:item/goat_horn')):
    wjson(os.path.join(A, 'items', _nm + '.json'),
          {"model": {"type": "minecraft:select", "property": "minecraft:display_context",
                     "cases": [{"when": ["gui", "fixed", "ground"], "model": {"type": "minecraft:model", "model": _mdl}}],
                     "fallback": {"type": "minecraft:empty"}}})
