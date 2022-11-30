print("LATIHAN")
inputUser = float(input("masukan nilai lebih dari 0 dan kurang dari 5 atau \nlebih dari 8 dan kurang dari 11:"))
isKurangDari5 = inputUser < 5
print("isKurangDari5:",isKurangDari5)
isLebihDari0 = inputUser > 0
print("isLebihDari0:",isLebihDari0)
isKurangDari11 = inputUser < 11
print("isKurangDari11:",isKurangDari11)
isLebihDari8 = inputUser > 8
print("isLebihDari8:",isLebihDari8)

isCorrect = isLebihDari0 and isKurangDari5 or isLebihDari8 and isKurangDari11
print("correct:",isCorrect)



inputUser1 = float(input("masukan nilai kurang dari 0 dan lebih dari 5 atau \nkurang dari 8 dan lebih dari 11:"))
isKurangDari0 = inputUser1 < 0
print("isKurangDari0:",isKurangDari0)
isLebihDari5 = inputUser1 > 5
print("isLebihDari5:",isLebihDari5)
isKurangDari8 = inputUser1 < 8
print("isKurangDari8:",isKurangDari8)
isLebihDari11 = inputUser1 > 8
print("isLebihDari11:",isLebihDari11)

isCorrect = isKurangDari0 and isLebihDari5 or isKurangDari8 and isLebihDari11
print("correct:",isCorrect)