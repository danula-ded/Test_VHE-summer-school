def main():
    import sys
    input = sys.stdin.read().strip()
    
    # Преобразуем ввод в строку и заполним нулями до 4 знаков
    number = input.zfill(4)
    
    # Проверяем симметричность
    result = int(number == number[::-1])
    
    # Выводим результат
    print(result)

if __name__ == "__main__":
    main()
