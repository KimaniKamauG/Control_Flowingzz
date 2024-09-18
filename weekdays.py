day = input("Enter any day of the week (Monday to Sunday): ").lower()

match day:
    case "monday":
        print("Wuuuiiii, kuamka na kuingia Kazi!")
    case "tuesday":
        print("Two days into the week, keep flowing!")
    case "wednesday":
        print("Wednesday ni kama tu Monday.")
    case 'thursday':
        print("Thursday nangoja Friday!")
    case 'friday':
        print("Friday ni kudunda kama nanzennzzzzz!")
    case "saturday" | 'sunday':
        print("Kubleki kama nonsense!")
    case _:
        print("Kwani haujui days of the week?")
