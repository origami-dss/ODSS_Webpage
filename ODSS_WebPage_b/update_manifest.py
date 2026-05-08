import json, hashlib, os

def file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

os.chdir('/Users/annette/Desktop/myR/ODSS_WebPage_b')

with open('manifest.json') as f:
    manifest = json.load(f)

to_add = ['blog.qmd']
for root, dirs, files in os.walk('posts'):
    for fname in files:
        if fname == '.DS_Store':
            continue
        fpath = os.path.join(root, fname).replace('\\', '/')
        to_add.append(fpath)

added = []
for fpath in to_add:
    if fpath not in manifest['files']:
        manifest['files'][fpath] = {'checksum': file_hash(fpath)}
        added.append(fpath)

print(f"Added {len(added)} files:")
for f in added:
    print(f"  + {f}")

with open('manifest.json', 'w') as out:
    json.dump(manifest, out, indent=2)

print("manifest.json updated successfully.")
