while input("For star write 1: ") == "1":
    try:
        num = [(input("Write number and type data (k - kilobytes, m - megabytes, g - gigabytes):    ")) for _ in range(int(input("List size; ")))]
        data = [х[-1] for х in num]
        number = [х[0:-1] for х in num]

        for i in range(len(data)):
            data1 = data[i]
            n = number[i]

            if data1 == "k":
                num1 = int(n) * 1024        #	BYTES (B) BINARY
                print(f"{n} kilobytes - {num1} bytes", end="\n\n")
            elif data1 == "m":
                num1 = int(n) * 1024**2     #    Megabyte in base 2 (binary)
                print(f"{n} megabytes - {num1} bytes", end="\n\n")
            elif data1 == "g":
                num1 = int(n) * 1024**3     #    Gigabytes in base 2 (binary)
                print(f"{n} gigabytes - {num1} bytes", end="\n\n")
            else:
                print("finish lol")
    except:
        print("EROR")
else:
    print("Googbye")


