## we can create dictionary using dict()

ds = dict()
ds.update({"ganesh":90})
print(ds)


## we can check key in dict like

if "ganesh" in ds:
    print("found ganesh ")

print(" all keys of ds :", list(ds.keys()))
print(" all values of ds:", list(ds.values()))
