from textblob import TextBlob

msg = TextBlob("Campk12 is a good compny and alays valule ttheir employeees.")
corrected = msg.correct()
print(corrected)

# msg1 = TextBlob("Bonjour")
# detected = msg1.detect_language()
# print(detected)

msg1 = TextBlob("Hello my name is arnav")
detected = msg1.translate(to="es")
print(detected)
