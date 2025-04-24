import json
import tkinter as tk
from tkinter import messagebox
import heapq
import clipboard

with open("./match_results.json", "r", encoding="utf-8") as f:
    match_dict = json.load(f)

def build_win_graph(win_data):
    graph = {}
    for winner, losers in win_data.items():
        if winner not in graph:
            graph[winner] = set()
        for loser in losers:
            if loser not in graph:
                graph[loser] = set()  # 패배한 선수도 그래프에 추가
            graph[winner].add(loser)
    return graph

def find_win_path(graph, start, end):
    if start not in graph or end not in graph:
        return None

    # 우선순위 큐와 거리 초기화
    priority_queue = [(0, start, [start])]  # (거리, 현재 노드, 경로)
    visited = set()

    while priority_queue:
        current_distance, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        # 도착 노드에 도달하면 경로 반환
        if current_node == end:
            return path

        # 인접 노드 탐색
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_distance + 1, neighbor, path + [neighbor]))

    return None

def is_subsequence(query, name):
    query = query.lower()
    name = name.lower()
    i = 0
    for char in name:
        if i < len(query) and char == query[i]:
            i += 1
    return i == len(query)


# ========================= GUI ============================
class UFCApp:
    def __init__(self, root, win_data):
        self.root = root
        self.root.title("UFC 경로 탐색기")
        self.win_data = win_data
        self.graph = build_win_graph(win_data)
        self.fighters = sorted(win_data.keys())

        self.tmp_left = ""
        self.tmp_right = ""

        self.search_var1 = tk.StringVar()
        self.search_var1.trace("w", self.update_listbox1)
        self.search_var2 = tk.StringVar()
        self.search_var2.trace("w", self.update_listbox2)

        self.setup_widgets()
        self.update_listbox1()
        self.update_listbox2()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_widgets(self):
        tk.Label(self.root, text="시작 선수 검색용", font=("Georgia", 12)).grid(row=0, column=0, padx=5, pady=5)
        entry1 = tk.Entry(self.root, textvariable=self.search_var1, width=25, font=("Georgia", 14))
        entry1.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        tk.Label(self.root, text="도착 선수 검색용", font=("Georgia", 12)).grid(row=0, column=1, padx=5, pady=5)
        entry2 = tk.Entry(self.root, textvariable=self.search_var2, width=25, font=("Georgia", 14))
        entry2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        list_frame = tk.Frame(self.root)
        list_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.listbox1 = tk.Listbox(list_frame, selectmode=tk.SINGLE, height=8, width=30, font=("Georgia", 12))
        self.listbox2 = tk.Listbox(list_frame, selectmode=tk.SINGLE, height=8, width=30, font=("Georgia", 12))
        self.listbox1.grid(row=0, column=0, padx=10)
        self.listbox2.grid(row=0, column=1, padx=10)

        self.listbox1.bind("<<ListboxSelect>>", self.on_left_select)
        self.listbox2.bind("<<ListboxSelect>>", self.on_right_select)

        self.selection_label = tk.Label(self.root, text="시작: -\t\t\t도착: -", font=("Georgia", 12), fg="gray")
        self.selection_label.grid(row=3, column=0, columnspan=2, pady=5)

        self.check_button = tk.Button(self.root, text="경로 확인", font=("Georgia", 12), command=self.check_win_path)
        self.check_button.grid(row=4, column=0, columnspan=1, pady=10)

        self.copy_button = tk.Button(self.root, text="결과 복사", font=("Georgia", 12), command=self.paste_result)
        self.copy_button.grid(row=4, column=1, columnspan=1, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Georgia", 14), fg="blue")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def update_listbox1(self, *args):
        query = self.search_var1.get()
        self.listbox1.delete(0, tk.END)
        for name in self.fighters:
            if is_subsequence(query, name):
                self.listbox1.insert(tk.END, name)

    def update_listbox2(self, *args):
        query = self.search_var2.get()
        self.listbox2.delete(0, tk.END)
        for name in self.fighters:
            if is_subsequence(query, name):
                self.listbox2.insert(tk.END, name)

    def on_left_select(self, event):
        try:
            self.tmp_left = self.listbox1.get(self.listbox1.curselection())
            self.update_selection_label()
        except tk.TclError:
            pass

    def on_right_select(self, event):
        try:
            self.tmp_right = self.listbox2.get(self.listbox2.curselection())
            self.update_selection_label()
        except tk.TclError:
            pass

    def update_selection_label(self):
        left = self.tmp_left if self.tmp_left else "없음"
        right = self.tmp_right if self.tmp_right else "없음"
        self.selection_label.config(text=f"왼쪽: {left}     오른쪽: {right}")

    def check_win_path(self):
        if not self.tmp_left or not self.tmp_right:
            messagebox.showerror("선택 오류", "양쪽에서 선수를 선택해주세요.")
            return
        if self.tmp_left == self.tmp_right:
            self.result_label.config(text="같은 선수를 선택했습니다.")
            return

        path = find_win_path(self.graph, self.tmp_left, self.tmp_right)
        if path:
            print(" > ".join(path))
        else:
            self.result_label.config(text=f"{self.tmp_left}는 {self.tmp_right}를 이긴 적이 없습니다.")

    def paste_result(self):
        if self.tmp_left and self.tmp_right:
            path = find_win_path(self.graph, self.tmp_left, self.tmp_right)
            if path:
                result = " > ".join(path)
                clipboard.copy(result)
                messagebox.showinfo("결과 복사", f"결과가 클립보드에 복사되었습니다:\n{result}")
            else:
                messagebox.showinfo("결과 없음", f"{self.tmp_left}는 {self.tmp_right}를 이긴 적이 없습니다.")
        else:
            messagebox.showerror("선택 오류", "양쪽에서 선수를 선택해주세요.")


# =================== 실행 ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = UFCApp(root, match_dict)
    root.mainloop()