grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# Задаём начальную и конечную ячейки
start = (0, 0)
end = (2, 2)

# Определяем размеры сетки
rows = len(grid)
cols = len(grid[0])

# Определяем вспомогательные списки для хранения пути и стоимости до каждой ячейки
path = [[None for j in range(cols)] for i in range(rows)]
cost = [[float('inf') for j in range(cols)] for i in range(rows)]
cost[start[0]][start[1]] = grid[start[0]][start[1]]

# Определяем список посещённых ячеек
visited = set()

# Определяем очередь с приоритетом для алгоритма Дейкстры
queue = []
grid.heappush(queue, (cost[start[0]][start[1]], start))


# Определяем функцию для проверки ячейки на корректность
def is_valid_cell(row, col):
    return row >= 0 and row < rows and col >= 0 and col < cols



while queue:
    current_cost, current_cell = grid.heappop(queue)
    if current_cell == end:
        break
    if current_cell in visited:
        continue
    visited.add(current_cell)
    row, col = current_cell
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for neighbor in neighbors:
        if is_valid_cell(*neighbor):
            neighbor_cost = grid[neighbor[0]][neighbor[1]]
            total_cost = current_cost + neighbor_cost
            if total_cost < cost[neighbor[0]][neighbor[1]]:
                cost[neighbor[0]][neighbor[1]] = total_cost
                path[neighbor[0]][neighbor[1]] = current_cell
                grid.heappush(queue, (total_cost, neighbor))


def find_path(start, end, path):
    if start == end:
        return [start]
    elif path[end[0]][end[1]] is None:
        return None
    else:
        p = find_path(start, path[end[0]][end[1]], path)
        p.append(end)
        return p


# Вычисляем путь минимальной стоимости и выводим его на экран
p = find_path(start, end, path)
if p is None:
    print("Путь не найден")
else:
    print("Путь минимальной стоимости:", p)