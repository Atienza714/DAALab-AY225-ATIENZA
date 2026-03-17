import tkinter as tk
from tkinter import messagebox, ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# DATA INITIALIZATION

def get_static_data():
    nodes = ["IMUS", "BACOOR", "DASMA", "KAWIT", "INDANG", "SILANG", "GENTRI", "NOVELETA"]
    
    base_edges = [
        ("IMUS", "BACOOR", 10, 15, 1.2),
        ("BACOOR", "DASMA", 12, 25, 1.5),
        ("DASMA", "KAWIT", 12, 25, 1.5),
        ("KAWIT", "INDANG", 12, 25, 1.2),
        ("INDANG", "SILANG", 14, 25, 1.5),
        ("SILANG", "GENTRI", 10, 25, 1.3),
        ("GENTRI", "NOVELETA", 10, 25, 1.5),
        ("NOVELETA", "IMUS", 10, 15, 1.2),
        ("BACOOR", "SILANG", 10, 25, 1.3),
        ("DASMA", "SILANG", 12, 25, 1.5),
        ("NOVELETA", "BACOOR", 10, 15, 1.2),
        ("SILANG", "KAWIT", 14, 25, 1.2),
        ("IMUS", "NOVELETA", 10, 15, 1.2)
    ]
    
    G = nx.DiGraph()
    for u, v, d, t, f in base_edges:

        G.add_edge(u, v, Distance=d, Time=t, Fuel=f)

        G.add_edge(v, u, Distance=d, Time=t, Fuel=f)
    return G, nodes


# GUI APPLICATION

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cavite Route Optimizer")
        self.root.geometry("1150x750")
        self.root.configure(bg="#1e1e2f")

        self.graph, self.locations = get_static_data()
        self.current_path = [] 

        # Header
        tk.Label(root, text="CAVITE TRANSPORT NETWORK", font=("Segoe UI", 20, "bold"), 
                 fg="white", bg="#1e1e2f").pack(pady=15)

        # Controls
        ctrl = tk.Frame(root, bg="#1e1e2f")
        ctrl.pack(pady=5)

        tk.Label(ctrl, text="From:", fg="white", bg="#1e1e2f").grid(row=0, column=0, padx=5)
        self.start_node = ttk.Combobox(ctrl, values=self.locations, width=12, state="readonly")
        self.start_node.grid(row=0, column=1, padx=5); self.start_node.set("DASMA")

        tk.Label(ctrl, text="To:", fg="white", bg="#1e1e2f").grid(row=0, column=2, padx=5)
        self.end_node = ttk.Combobox(ctrl, values=self.locations, width=12, state="readonly")
        self.end_node.grid(row=0, column=3, padx=5); self.end_node.set("BACOOR")

        tk.Label(ctrl, text="By:", fg="white", bg="#1e1e2f").grid(row=0, column=4, padx=5)
        self.metric = tk.StringVar(value="Time")
        ttk.Combobox(ctrl, textvariable=self.metric, values=["Distance", "Time", "Fuel"], 
                     width=10, state="readonly").grid(row=0, column=5, padx=5)

        tk.Button(ctrl, text="Analyze Route", command=self.solve, bg="#2196F3", 
                  fg="white", width=15, font=("Segoe UI", 9, "bold")).grid(row=0, column=6, padx=10)

        # Display
        main = tk.Frame(root, bg="#1e1e2f")
        main.pack(fill="both", expand=True, padx=20, pady=10)
        self.viz_frame = tk.Frame(main, bg="white")
        self.viz_frame.pack(side="left", fill="both", expand=True)
        
        res_side = tk.Frame(main, bg="#2b2b3c", width=300)
        res_side.pack(side="right", fill="both", padx=(10, 0))
        self.path_lbl = tk.Label(res_side, text="Select nodes to begin.", fg="yellow", 
                                   bg="#2b2b3c", font=("Segoe UI", 10), wraplength=250)
        self.path_lbl.pack(pady=20)

        self.table = ttk.Treeview(res_side, columns=("M", "V"), show="headings", height=5)
        self.table.heading("M", text="Criteria"); self.table.heading("V", text="Total")
        self.table.column("M", width=100, anchor="center"); self.table.column("V", width=100, anchor="center")
        self.table.pack(pady=10, padx=10)

        self.draw_graph()

    def draw_graph(self):
        for w in self.viz_frame.winfo_children(): w.destroy()
        fig, ax = plt.subplots(figsize=(7, 6))
        pos = nx.circular_layout(self.graph) 
        
        nx.draw_networkx_nodes(self.graph, pos, ax=ax, node_color='#4CAF50', node_size=1600)
        nx.draw_networkx_labels(self.graph, pos, ax=ax, font_size=8, font_weight='bold')
        
        drawn_labels = set()
        for u, v, d in self.graph.edges(data=True):
            # Check for same-value bidirectional routes (Clean Label Logic)
            if (v, u) in self.graph.edges() and d == self.graph[v][u]:
                nx.draw_networkx_edges(self.graph, pos, edgelist=[(u,v)], ax=ax, edge_color='#ccc', arrowstyle='<|-|>', connectionstyle='arc3,rad=0')
                if (v, u) not in drawn_labels:
                    lbl = { (u,v): f"{d['Distance']}k|{d['Time']}m\n{d['Fuel']}L" }
                    nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=lbl, font_size=7, ax=ax, rotate=False)
                    drawn_labels.add((u, v))
                continue

            # Standard line for any outliers
            nx.draw_networkx_edges(self.graph, pos, edgelist=[(u, v)], ax=ax, edge_color='#ccc', arrowstyle='-|>', connectionstyle='arc3, rad=0.1')

        if self.current_path:
            p_edges = list(zip(self.current_path, self.current_path[1:]))
            nx.draw_networkx_edges(self.graph, pos, edgelist=p_edges, edge_color='red', width=3)

        canvas = FigureCanvasTkAgg(fig, master=self.viz_frame)
        canvas.draw(); canvas.get_tk_widget().pack(fill="both", expand=True)

    def solve(self):
        u, v, m = self.start_node.get(), self.end_node.get(), self.metric.get()
        try:
            self.current_path = nx.shortest_path(self.graph, source=u, target=v, weight=m)
            sums = {"Distance": 0, "Time": 0, "Fuel": 0}
            for i in range(len(self.current_path)-1):
                data = self.graph[self.current_path[i]][self.current_path[i+1]]
                for k in sums: sums[k] += data[k]

            self.path_lbl.config(text=f"OPTIMAL PATH:\n{' → '.join(self.current_path)}")
            for r in self.table.get_children(): self.table.delete(r)
            self.table.insert("", "end", values=("Distance", f"{sums['Distance']} km"))
            self.table.insert("", "end", values=("Time", f"{sums['Time']} mins"))
            self.table.insert("", "end", values=("Fuel", f"{round(sums['Fuel'],2)} L"))
            self.draw_graph()
        except: messagebox.showerror("Error", "No path found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()