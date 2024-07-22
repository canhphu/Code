#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    // Loại bỏ ký tự xuống dòng còn lại sau khi nhập số nguyên
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
    stack<int> s;
    for (int i = n - 1; i >= 0; i--) {
        s.push(a[i]);
    }  
    string str;
    char c;
    while (cin.get(c) && c != '\n') {
        str.push_back(c);
    }
    
    queue<int> q;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] == 'C') {
            if (!s.empty()) {
                int x = s.top();
                s.pop();
                q.push(x);
            }
        } else if (str[i] == 'H') {
            if (!q.empty()) {
                int x = q.front();
                q.pop();
                s.push(x);
            }
        }
    }
    
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }

    return 0;
}
