# Клас для представлення автомобіля
class CAR:
    # Конструктор класу для ініціалізації атрибутів автомобіля
    def __init__(self):
        # Запитуємо модель автомобіля у користувача
        self.model = input("Enter car model: ")
        # Запитуємо колір автомобіля у користувача
        self.color = input("Enter car color: ")
        # Цикл для перевірки правильності введення року
        while True:
            try:
                # Запитуємо рік випуску автомобіля та конвертуємо в число
                self.year = int(input("Enter car year: "))
                break
            except ValueError:
                # Виводимо повідомлення про помилку при неправильному форматі року
                print("Please enter a valid year (numbers only)")
    
    # Метод для відображення інформації про автомобіль
    def display_info(self):
        # Виводимо заголовок інформації
        print(f"\nCar Information:")
        # Виводимо модель автомобіля
        print(f"Model: {self.model}")
        # Виводимо колір автомобіля
        print(f"Color: {self.color}")
        # Виводимо рік випуску автомобіля
        print(f"Year: {self.year}")

# Приклад використання класу
if __name__ == "__main__":
    # Створюємо екземпляр класу CAR
    my_car = CAR()
    # Викликаємо метод для відображення інформації про автомобіль
    my_car.display_info()
