import keyboard

keys = list(keyboard._canonical_names.canonical_names.items())[:63]
keys = map(lambda item: item[1], keys)
uniqueKeys = []

for key in keys:
  if key not in uniqueKeys:
    uniqueKeys.append(key)

for key in uniqueKeys:
  print(key)
