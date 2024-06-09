def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # количество отрезков
    m = int(data[1])  # количество точек
    
    segments = []
    points = []
    
    index = 2
    for i in range(n):
        l = int(data[index])
        r = int(data[index + 1])
        segments.append((l, r))
        index += 2
    
    points = list(map(int, data[index:index + m]))
    
    events = []
    
    # Добавляем события для начала и конца отрезков
    for l, r in segments:
        events.append((l, 'L'))  # событие начала отрезка
        events.append((r, 'R'))  # событие конца отрезка
    
    # Добавляем события для точек
    point_indices = {}
    for i, p in enumerate(points):
        if p not in point_indices:
            point_indices[p] = []
        point_indices[p].append(i)
        events.append((p, 'P'))  # событие точки
    
    # Сортируем события
    events.sort(key=lambda x: (x[0], x[1]))
    
    active_segments = 0  # количество активных отрезков
    point_counts = [0] * m  # результат для каждой точки
    
    # Обрабатываем события
    for event in events:
        if event[1] == 'L':
            active_segments += 1  # начался новый отрезок
        elif event[1] == 'R':
            active_segments -= 1  # закончился один из отрезков
        elif event[1] == 'P':
            # Обновляем количество активных отрезков для каждой точки
            for idx in point_indices[event[0]]:
                point_counts[idx] = active_segments
    
    # Выводим результаты
    for count in point_counts:
        print(count)

if __name__ == "__main__":
    main()
