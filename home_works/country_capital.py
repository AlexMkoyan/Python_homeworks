country = "Armenia"
capital = "yerevan"
answer =  "-" * len(capital)

while True:
    ms = input("What is the capital of %s?: \n\t%s\nEnter one letter: " %(country,answer))
    ms = ms.lower()
    if len(ms) > 1:
        print("Please enter one letter")
    else:
        if ms in capital:
            num_el = capital.index(ms)
            if num_el == 0:
                ms = ms.upper()

            answer = answer[:num_el] + ms + answer[num_el + 1:]
            if answer.lower() == capital:
                print("You win,congratulation! ",capital)
                break
        else:
            print("Entered wrong letter!")