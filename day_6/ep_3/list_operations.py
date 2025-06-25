egzersizler = ["squat", "deadlift", "plank", "barfiks"]

print(len(egzersizler))

print("plank" in egzersizler)

print("bench press" in egzersizler)

egzersizler.append("bench press")

egzersizler.insert(1, "curl")

del egzersizler[1]

egzersiz = egzersizler.pop(1)

print(egzersizler)

# egzersizler.remove("push up")

# egzersizler.clear()

print(egzersizler.count("barfiks"))

print(egzersizler.index("barfiks"))
