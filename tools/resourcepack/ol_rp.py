# ------------------------------------------------------------------ Ombrelune : dragons articulés (un modèle par os)
# Exécuté par gen_rp.py (exec) après dino_rp.py (réutilise _bone_assets) : données tools/arcade/ol_beasts.py.
# Os d'une espèce -> assets/mg/items/beast/<espèce>_<os>.json + modèle mg:item/beast/<espèce>_<os> (même convention que dino_rp.py).
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'arcade'))
import ol_beasts as _OB


_bone_assets(_OB.SPECIES, 'beast', _OB.bone_scale)
