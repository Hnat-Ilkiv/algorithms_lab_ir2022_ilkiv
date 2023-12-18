#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <tuple>
#include <sstream>
#include <algorithm> // Включено необхідну бібліотеку


using namespace std;

void bfs(vector<vector<string>> &matrix, pair<int, int> start, string replace_color, int rows, int cols) {
    vector<vector<bool>> visited(rows, vector<bool>(cols, false));
    queue<pair<int, int>> queue; // Виправлено тип черги
    queue.push(start);
    string replace_node = matrix[start.first][start.second];

    while (!queue.empty()) {
        int x = queue.front().first;
        int y = queue.front().second;
        queue.pop(); // Виправлено метод видалення елемента з черги
        if (!visited[x][y]) {
            visited[x][y] = true;
            matrix[x][y] = replace_color;

            if (x > 0 && matrix[x - 1][y] == replace_node && !visited[x - 1][y]) {
                queue.push(make_pair(x - 1, y)); // Виправлено додавання елемента до черги
            }
            if (x < rows - 1 && matrix[x + 1][y] == replace_node && !visited[x + 1][y]) {
                queue.push(make_pair(x + 1, y)); // Виправлено додавання елемента до черги
            }
            if (y > 0 && matrix[x][y - 1] == replace_node && !visited[x][y - 1]) {
                queue.push(make_pair(x, y - 1)); // Виправлено додавання елемента до черги
            }
            if (y < cols - 1 && matrix[x][y + 1] == replace_node && !visited[x][y + 1]) {
                queue.push(make_pair(x, y + 1)); // Виправлено додавання елемента до черги
            }
        }
    }
}

void flood_fill(vector<vector<string>> &matrix, pair<int, int> start, string replace_color, int rows, int cols) {
    int x = start.first;
    int y = start.second;
    if (matrix[x][y] != replace_color) {
        bfs(matrix, start, replace_color, rows, cols);
    }
}

tuple<int, int, pair<int, int>, string, vector<vector<string>>> read_input(string file_path) {
    ifstream f(file_path);
    vector<string> lines;
    string line;
    while (getline(f, line)) {
        lines.push_back(line);
    }
    int height, width;
    sscanf(lines[0].c_str(), "%d,%d", &height, &width);
    pair<int, int> start;
    sscanf(lines[1].c_str(), "%d,%d", &start.first, &start.second);
    string replace_color = lines[2].substr(1, lines[2].size() - 2);
    vector<vector<string>> matrix;
    for (int i = 3; i < lines.size(); i++) {
        vector<string> row;
        stringstream ss(lines[i]);
        string item;
        while (getline(ss, item, ',')) {
            item.erase(remove(item.begin(), item.end(), ' '), item.end()); // Видаляємо пробіли
            item.erase(remove(item.begin(), item.end(), '\''), item.end()); // Видаляємо '
            item.erase(remove(item.begin(), item.end(), '['), item.end()); // Видаляємо [
            item.erase(remove(item.begin(), item.end(), ']'), item.end()); // Видаляємо ]
            row.push_back(item);
        }
        matrix.push_back(row);
    }
    return make_tuple(height, width, start, replace_color, matrix);
}


void write_output(string file_path, vector<vector<string>> &matrix) {
    ofstream f(file_path);
    for (auto &row : matrix) {
        f << "[";
        for (int i = 0; i < row.size(); i++) {
            f << "'" << row[i] << "'";
            if (i != row.size() - 1) {
                f << ", ";
            }
        }
        f << "]" << endl;
    }
}

void print_matrix(const vector<vector<string>> &matrix) {
    for (const auto &row : matrix) {
        for (const auto &element : row) {
            cout << element << " ";
        }
        cout << endl;
    }
}

int main() {
    string input_file = "big_input.txt";
    string output_file = "output.txt";

    cout << "Start reading ..." << endl;
    double start_time = clock();
    auto data = read_input(input_file);
    double end_time = clock();
    cout << "Time: " << (end_time - start_time) / CLOCKS_PER_SEC << "\nFinish reading ...\n" << endl;

    cout << "Start saving matrix and other data ..." << endl;
    start_time = clock();
    int height, width;
    pair<int, int> start;
    string replace_color;
    vector<vector<string>> matrix;
    tie(height, width, start, replace_color, matrix) = data; // Виправлено розпакування кортежу
    end_time = clock();
    cout << "Time: " << (end_time - start_time) / CLOCKS_PER_SEC << "\nFinish saving matrix and other data ...\n" << endl;

    // cout << "Matrix before flood fill:" << endl;
    // print_matrix(matrix);

    cout << "\nStart working ..." << endl;
    start_time = clock();
    flood_fill(matrix, start, replace_color, height, width);
    end_time = clock();
    cout << "Time: " << (end_time - start_time) / CLOCKS_PER_SEC << "\nFinish working ...\n" << endl;

    // cout << "Matrix after flood fill:" << endl;
    // print_matrix(matrix);

    cout << "Start writing ..." << endl;
    start_time = clock();
    write_output(output_file, matrix);
    end_time = clock();
    cout << "Time: " << (end_time - start_time) / CLOCKS_PER_SEC << "\nFinish writing ...\n" << endl;

    return 0;
}
