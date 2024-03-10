cat = {}
info = {"status": "vaccinated", "breed": True}
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = ["лагідний", "кусається"]
cat.update(info)
print(cat)