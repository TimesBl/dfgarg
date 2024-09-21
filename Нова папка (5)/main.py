with open("quoltes.txt","r",encoding="utf-8") as file:
    data = file.read()
    print(data)

autor = input("хто написав рядки?")

with open("quoltes.txt","a",encoding="utf-8") as file:
    file.write(autor + "\n")





while True:
    answer = input("Бажаєте додати ще одну цитату? (так / ні)")
    answer = answer.lower()

    if answer == "так":
        quote = input("Введіть цитату:")
        autor = input("Введіть автора")


        file = open("quoltes.txt","a",encoding="utf-8")
        file.write(quote + "\n")
        file.write(+ autor +"\n")
        file.closed()


    else:
        break

print("Зчитуємо фінальний файл")
with open("quotes.txt","r",encoding="utf-8") as file:
    data = file.read()
    print(data)



    