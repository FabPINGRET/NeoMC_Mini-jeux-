"""Scission du pack Floaty sur les VRAIS zips commités (releases/neomc_resourcepack.zip = pack serveur, releases/floaty_optional_resourcepack.zip = pack
optionnel), contrôlés avec le vrai manifeste tools/resourcepack/floaty_vanilla.json (sans la carte, sans jar, sans relancer gen_rp). Zip absent : tests ignorés.
Complète test_floaty_split_inv.py (mêmes invariants sur données synthétiques) et test_floaty_rp_real.py (structure du zip serveur).
violations() liste les écarts ; le test réel exige une liste vide, les tests « falsifiés » vérifient qu'elle détecte chaque écart (cas inverses) :
- le pack serveur n'a aucun fichier de la carte à un chemin vanilla remplacé, sauf les items/X.json enveloppés (select minecraft:context_dimension,
  UN cas mg:floaty, repli = définition vanilla du manifeste) ; les textures / modèles item remplacés sont sous assets/floaty/ ;
- chaque modèle lu par un item du pack serveur existe : floaty: et modèles de la carte dans le zip, vanilla jamais un modèle renommé ;
- le pack optionnel = exactement les remplacements globaux du manifeste (blocs, entités, particules, tableaux...) + son pack.mcmeta valide ;
- aucune entrée commune aux deux packs, hors pack.mcmeta (qui diffère).
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import copy
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SERVER = ROOT / 'releases' / 'neomc_resourcepack.zip'
OPT = ROOT / 'releases' / 'floaty_optional_resourcepack.zip'
MANIFEST = ROOT / 'tools' / 'resourcepack' / 'floaty_vanilla.json'
MC = 'assets/minecraft/'
ITEMS, TEX_ITEM, MODEL_ITEM = MC + 'items/', MC + 'textures/item/', MC + 'models/item/'
DIM, MCMETA = 'mg:floaty', 'pack.mcmeta'
ZOMBIE_PNG = MC + 'textures/entity/zombie/zombie.png'          # remplacement global : dans le pack optionnel, jamais dans le pack serveur


def load(path):
    with zipfile.ZipFile(path) as zf:
        return {n: zf.read(n) for n in zf.namelist() if not n.endswith('/')}


def refs_of(node, out):
    """Références de modèle d'une définition d'item (clés model / base, récursif)."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ('model', 'base') and isinstance(v, str):
                out.append(v)
            else:
                refs_of(v, out)
    elif isinstance(node, list):
        for v in node:
            refs_of(v, out)
    return out


def split_ref(ref):
    ns, _, path = ref.rpartition(':')
    return (ns or 'minecraft'), path


def jload(data):
    return json.loads(data.decode('utf-8'))


def server_items(server, man, bad):
    """Items du pack serveur : enveloppés (manifeste) bien formés ; renvoie [(chemin, modèle lu par la carte)] pour tous les items du zip."""
    cases = []
    for p in sorted(n for n in server if n.startswith(ITEMS)):
        doc = jload(server[p])
        model = doc['model']
        if p not in man['items']:                              # item neuf (la carte seule le lit) : pas enveloppé
            cases.append((p, model))
            continue
        extra_keys = {k: v for k, v in doc.items() if k != 'model'}        # hand_animation_on_swap, oversized_in_gui... : ceux de vanilla
        if extra_keys != {k: v for k, v in man['items'][p].items() if k != 'model'}:
            bad.append(f'serveur : {p} clés de premier niveau (hors model) différentes de vanilla')
        if model.get('type') != 'minecraft:select' or model.get('property') != 'minecraft:context_dimension':
            bad.append(f'serveur : {p} pas un select context_dimension')
        elif [c['when'] for c in model['cases']] != [DIM]:
            bad.append(f'serveur : {p} cas autre que {DIM}')
        elif model['fallback'] != man['items'][p]['model']:
            bad.append(f'serveur : {p} repli différent de la définition vanilla')
        elif 'floaty:' in json.dumps(model['fallback']):
            bad.append(f'serveur : {p} repli qui lit floaty:')
        else:
            cases.append((p, model['cases'][0]['model']))
    for p in sorted(man['items']):
        if p not in server:
            bad.append(f'serveur : item enveloppé absent {p}')
    return cases


def violations(server, opt, man):
    """Écarts aux invariants du pack serveur / optionnel (liste de messages, vide si tout est bon)."""
    bad = []
    rep = {p for paths in man['replaced'].values() for p in paths}
    kept = (ITEMS, TEX_ITEM, MODEL_ITEM)
    for p in sorted(server):
        if p in rep and p not in man['items']:
            bad.append(f'serveur : chemin vanilla remplacé {p}')
        if p.endswith('.png.mcmeta') and p[:-len('.mcmeta')] in rep:
            bad.append(f'serveur : mcmeta d\'une texture remplacée {p}')
    for p in sorted(r for r in rep if r.startswith((TEX_ITEM, MODEL_ITEM))):
        if 'assets/floaty/' + p[len(MC):] not in server:
            bad.append(f'serveur : copie floaty: absente pour {p}')
    renamed = {p[len(MC + 'models/'):-len('.json')] for p in list(man['models']) + man['replaced']['models'] if p.startswith(MODEL_ITEM)}
    for p, model in server_items(server, man, bad):
        for ref in refs_of(model, []):
            ns, path = split_ref(ref)
            if f'assets/{ns}/models/{path}.json' in server:
                continue
            if ns != 'minecraft' or path in renamed:
                bad.append(f'serveur : {p} lit un modèle introuvable {ref}')   # floaty: absent, ou modèle vanilla dont la texture est remplacée
    expected_opt = {p for p in rep if not p.startswith(kept)}
    if set(opt) - {MCMETA} != expected_opt:
        bad.append(f'optionnel : contenu != remplacements globaux (en trop {sorted(set(opt) - {MCMETA} - expected_opt)[:3]}, '
                   f'manquants {sorted(expected_opt - set(opt))[:3]})')
    bad.extend(f'optionnel : entrée interdite {p}' for p in sorted(opt) if p.startswith(('assets/mg/', 'assets/floaty/')) or '/lang/' in p)
    common = (set(server) & set(opt)) - {MCMETA}
    bad.extend(f'commun aux deux packs : {p}' for p in sorted(common))
    bad.extend(mcmeta_problems(server, opt, man))
    return bad


def mcmeta_problems(server, opt, man):
    bad = []
    if MCMETA not in opt or MCMETA not in server:
        return ['pack.mcmeta absent d\'un pack']
    try:
        meta = jload(opt[MCMETA])['pack']
        low, high, res = meta['min_format'], meta['max_format'], man['version']['resource']
        if not (isinstance(meta.get('description'), (str, list, dict)) and low <= res <= high):
            bad.append(f'optionnel : pack.mcmeta sans description ou qui ne couvre pas {res}')
        smeta = jload(server[MCMETA])['pack']
        if (smeta['min_format'], smeta['max_format']) != (low, high):
            bad.append('optionnel : formats différents du pack serveur')
        if opt[MCMETA] == server[MCMETA]:
            bad.append('optionnel : pack.mcmeta identique à celui du serveur')
    except (ValueError, KeyError, TypeError) as e:
        bad.append(f'optionnel : pack.mcmeta illisible ({e!r})')
    return bad


class RealZips(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert SERVER.is_file() and OPT.is_file(), f'{SERVER} / {OPT} absents : zips suivis par git, pas de skip (gen_rp.py avec NEOMC_FLOATY_RP les produit)'
        cls.server, cls.opt = load(SERVER), load(OPT)
        cls.man = json.loads(MANIFEST.read_text(encoding='utf-8'))

    def test_real_zips_respect_every_invariant(self):
        self.assertEqual(violations(self.server, self.opt, self.man), [])

    def test_counts_match_manifest(self):
        self.assertEqual(len([p for p in self.server if p in self.man['items']]), len(self.man['items']))
        self.assertEqual(len([p for p in self.server if p.startswith('assets/floaty/models/')]), len(self.man['models']) + 1)   # + modèle remplacé
        self.assertIn(ZOMBIE_PNG, self.opt)
        self.assertNotIn(ZOMBIE_PNG, self.server)
        self.assertIn(MC + 'sounds.json', self.server)                  # événements neufs : restent dans le pack forcé
        self.assertNotIn(MC + 'sounds.json', self.opt)

    def test_optional_pack_has_no_neomc_content(self):
        self.assertTrue(all(p == MCMETA or p.startswith(MC + 'textures/') for p in self.opt))
        self.assertFalse([p for p in self.opt if p.endswith('.json') and p != MCMETA], 'aucun JSON (items, modèles, sons) dans le pack optionnel')

    # ---- cas inverses : chaque écart falsifié est détecté (copies superficielles, les vrais zips ne sont pas touchés)
    def broken(self, server=None, opt=None, man=None):
        return violations(server if server is not None else self.server, opt if opt is not None else self.opt, man or self.man)

    def has(self, found, *needles):
        self.assertTrue(any(all(n in f for n in needles) for f in found), f'écart non détecté {needles} : {found[:4]}')

    def test_global_replacement_in_server_pack_is_caught(self):
        self.has(self.broken(server={**self.server, ZOMBIE_PNG: b'x'}), 'serveur', ZOMBIE_PNG)
        self.has(self.broken(server={**self.server, MC + 'textures/item/brush.png': b'x'}), 'chemin vanilla remplacé')
        coal = MC + 'textures/block/coal_ore.png'                       # png remplacé, mais son .mcmeta n'est pas dans le manifeste
        self.assertIn(coal, self.man['replaced']['textures_block'])
        self.assertNotIn(coal + '.mcmeta', self.man['replaced']['mcmeta'])
        self.has(self.broken(server={**self.server, coal + '.mcmeta': b'{}'}), 'mcmeta d\'une texture remplacée', coal)

    def test_unwrapped_or_altered_item_is_caught(self):
        bow = MC + 'items/bow.json'
        plain = {**self.server, bow: json.dumps({'model': {'type': 'minecraft:model', 'model': 'item/bow'}}).encode('utf-8')}
        self.has(self.broken(server=plain), bow, 'select')
        doc = jload(self.server[bow])
        doc['model']['cases'].append({'when': 'minecraft:overworld', 'model': {'type': 'minecraft:model', 'model': 'item/bow'}})
        self.has(self.broken(server={**self.server, bow: json.dumps(doc).encode('utf-8')}), bow, 'cas autre')
        doc = jload(self.server[bow])
        doc['model']['fallback'] = {'type': 'minecraft:model', 'model': 'item/arrow'}
        self.has(self.broken(server={**self.server, bow: json.dumps(doc).encode('utf-8')}), bow, 'repli')
        self.has(self.broken(server={p: d for p, d in self.server.items() if p != bow}), 'item enveloppé absent', bow)
        for key, value in (('oversized_in_gui', True), ('hand_animation_on_swap', False)):     # clé de premier niveau ajoutée ou changée
            doc = jload(self.server[bow])
            doc[key] = value
            self.has(self.broken(server={**self.server, bow: json.dumps(doc).encode('utf-8')}), bow, 'clés de premier niveau')
        doc = jload(self.server[bow])
        doc['model'] = {'type': 'minecraft:select', 'property': 'minecraft:context_dimension', 'cases': doc['model']['cases'], 'fallback': doc['model']['fallback']}
        self.assertEqual(self.broken(server={**self.server, bow: json.dumps(doc).encode('utf-8')}), [])    # même clés : pas de faux positif

    def test_missing_model_is_caught(self):
        floaty = sorted(p for p in self.server if p.startswith('assets/floaty/models/'))[0]
        self.has(self.broken(server={p: d for p, d in self.server.items() if p != floaty}), 'modèle introuvable')
        renamed = sorted(p for p in self.man['replaced']['textures_item'])[0]
        self.has(self.broken(server={p: d for p, d in self.server.items() if p != 'assets/floaty/' + renamed[len(MC):]}), 'copie floaty: absente')

    def test_vanilla_ref_to_a_renamed_model_is_caught(self):
        man = copy.deepcopy(self.man)
        man['replaced']['models'].append(MC + 'models/item/apple.json')       # apple lit item/apple : il serait vanilla et sa texture remplacée
        self.has(self.broken(man=man), 'modèle introuvable', 'item/apple')

    def test_optional_pack_drift_is_caught(self):
        self.has(self.broken(opt={**self.opt, MC + 'items/bow.json': b'{}'}), 'optionnel : contenu')
        self.has(self.broken(opt={p: d for p, d in self.opt.items() if p != ZOMBIE_PNG}), 'manquants')
        self.has(self.broken(opt={**self.opt, 'assets/mg/x.png': b'x'}), 'entrée interdite')

    def test_common_entry_is_caught_but_pack_mcmeta_is_fine(self):
        shared = MC + 'textures/block/emerald_ore.png'
        self.has(self.broken(server={**self.server, shared: b'x'}), 'commun aux deux packs', shared)
        self.assertEqual(set(self.server) & set(self.opt), {MCMETA})            # le seul nom commun est pack.mcmeta, qui diffère
        self.assertNotEqual(self.server[MCMETA], self.opt[MCMETA])

    def test_bad_optional_mcmeta_is_caught(self):
        def with_meta(meta):
            return {**self.opt, MCMETA: json.dumps(meta).encode('utf-8')}
        self.has(self.broken(opt={**self.opt, MCMETA: b'{pas du json'}), 'illisible')
        self.has(self.broken(opt=with_meta({'pack': {'description': 'x', 'min_format': [1, 0], 'max_format': [2, 0]}})), 'ne couvre pas')
        self.has(self.broken(opt=with_meta({'pack': {'min_format': [88, 0], 'max_format': [88, 99]}})), 'sans description')
        self.has(self.broken(opt=with_meta({'pack': {'description': 'x', 'min_format': [88, 0], 'max_format': [89, 0]}})), 'formats différents')
        self.has(self.broken(opt={**self.opt, MCMETA: self.server[MCMETA]}), 'identique')
        self.has(self.broken(opt={p: d for p, d in self.opt.items() if p != MCMETA}), 'absent')


if __name__ == '__main__':
    unittest.main()
