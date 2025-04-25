import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy.orm import sessionmaker
from database import SessionLocal, init_db
from models import (DiagramHeader, GraphType, Node, 
                    Figure, Message, Relationship)

class DiagramApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagram ER Manager")
        self.session = SessionLocal()
        
        # Inicializar la base de datos
        init_db()
        
        # Crear el notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        # Crear pestañas para cada entidad
        self.create_diagram_header_tab()
        self.create_graph_type_tab()
        self.create_node_tab()
        self.create_figure_tab()
        self.create_message_tab()
        self.create_relationship_tab()
        
        # Cargar datos iniciales
        self.load_data()
    
    def create_diagram_header_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Diagram Headers")
        
        # Treeview
        self.diagram_tree = ttk.Treeview(tab, columns=('ID', 'Name', 'GraphType'), show='headings')
        self.diagram_tree.heading('ID', text='ID')
        self.diagram_tree.heading('Name', text='Name')
        self.diagram_tree.heading('GraphType', text='Graph Type')
        self.diagram_tree.pack(fill='both', expand=True)
        
        # Formulario
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky='w')
        self.dh_name = ttk.Entry(form_frame)
        self.dh_name.grid(row=0, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Graph Type:").grid(row=1, column=0, sticky='w')
        self.dh_graph_type = ttk.Combobox(form_frame, state='readonly')
        self.dh_graph_type.grid(row=1, column=1, sticky='ew')
        
        # Botones
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Add", command=self.add_diagram_header).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_diagram_header).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_diagram_header).pack(side='left', padx=5)
    
    def create_graph_type_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Graph Types")
        
        # Treeview
        self.graph_type_tree = ttk.Treeview(tab, columns=('ID', 'Code', 'Description'), show='headings')
        self.graph_type_tree.heading('ID', text='ID')
        self.graph_type_tree.heading('Code', text='Code')
        self.graph_type_tree.heading('Description', text='Description')
        self.graph_type_tree.pack(fill='both', expand=True)
        
        # Formulario
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(form_frame, text="Code:").grid(row=0, column=0, sticky='w')
        self.gt_code = ttk.Entry(form_frame)
        self.gt_code.grid(row=0, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Description:").grid(row=1, column=0, sticky='w')
        self.gt_description = ttk.Entry(form_frame)
        self.gt_description.grid(row=1, column=1, sticky='ew')
        
        # Botones
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Add", command=self.add_graph_type).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_graph_type).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_graph_type).pack(side='left', padx=5)
    
    def create_node_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Nodes")
        
        # Treeview
        self.node_tree = ttk.Treeview(tab, columns=('ID', 'Content', 'Alias', 'Header', 'Figure'), show='headings')
        self.node_tree.heading('ID', text='ID')
        self.node_tree.heading('Content', text='Content')
        self.node_tree.heading('Alias', text='Alias')
        self.node_tree.heading('Header', text='Header')
        self.node_tree.heading('Figure', text='Figure')
        self.node_tree.pack(fill='both', expand=True)
        
        # Formulario
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(form_frame, text="Content:").grid(row=0, column=0, sticky='w')
        self.node_content = ttk.Entry(form_frame)
        self.node_content.grid(row=0, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Alias:").grid(row=1, column=0, sticky='w')
        self.node_alias = ttk.Entry(form_frame)
        self.node_alias.grid(row=1, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Header:").grid(row=2, column=0, sticky='w')
        self.node_header = ttk.Combobox(form_frame, state='readonly')
        self.node_header.grid(row=2, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Figure:").grid(row=3, column=0, sticky='w')
        self.node_figure = ttk.Combobox(form_frame, state='readonly')
        self.node_figure.grid(row=3, column=1, sticky='ew')
        
        # Botones
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Add", command=self.add_node).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_node).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_node).pack(side='left', padx=5)
    
    def create_figure_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Figures")
        
        # Treeview
        self.figure_tree = ttk.Treeview(tab, columns=('ID', 'Description', 'Initial', 'End'), show='headings')
        self.figure_tree.heading('ID', text='ID')
        self.figure_tree.heading('Description', text='Description')
        self.figure_tree.heading('Initial', text='Initial')
        self.figure_tree.heading('End', text='End')
        self.figure_tree.pack(fill='both', expand=True)
        
        # Formulario
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(form_frame, text="Description:").grid(row=0, column=0, sticky='w')
        self.figure_description = ttk.Entry(form_frame)
        self.figure_description.grid(row=0, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Initial:").grid(row=1, column=0, sticky='w')
        self.figure_initial = ttk.Entry(form_frame)
        self.figure_initial.grid(row=1, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="End:").grid(row=2, column=0, sticky='w')
        self.figure_end = ttk.Entry(form_frame)
        self.figure_end.grid(row=2, column=1, sticky='ew')
        
        # Botones
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Add", command=self.add_figure).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_figure).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_figure).pack(side='left', padx=5)
    
    def create_message_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Messages")
        
        # Treeview
        self.message_tree = ttk.Treeview(tab, columns=('ID', 'Description'), show='headings')
        self.message_tree.heading('ID', text='ID')
        self.message_tree.heading('Description', text='Description')
        self.message_tree.pack(fill='both', expand=True)
        
        # Formulario
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(form_frame, text="Description:").grid(row=0, column=0, sticky='w')
        self.message_description = ttk.Entry(form_frame)
        self.message_description.grid(row=0, column=1, sticky='ew')
        
        # Botones
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Add", command=self.add_message).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_message).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_message).pack(side='left', padx=5)
    
    def create_relationship_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Relationships")
        
        # Treeview
        self.relationship_tree = ttk.Treeview(tab, columns=('ID', 'Input', 'Output', 'Message'), show='headings')
        self.relationship_tree.heading('ID', text='ID')
        self.relationship_tree.heading('Input', text='Input Node')
        self.relationship_tree.heading('Output', text='Output Node')
        self.relationship_tree.heading('Message', text='Message')
        self.relationship_tree.pack(fill='both', expand=True)
        
        # Formulario
        form_frame = ttk.Frame(tab)
        form_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(form_frame, text="Input Node:").grid(row=0, column=0, sticky='w')
        self.rel_input = ttk.Combobox(form_frame, state='readonly')
        self.rel_input.grid(row=0, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Output Node:").grid(row=1, column=0, sticky='w')
        self.rel_output = ttk.Combobox(form_frame, state='readonly')
        self.rel_output.grid(row=1, column=1, sticky='ew')
        
        ttk.Label(form_frame, text="Message:").grid(row=2, column=0, sticky='w')
        self.rel_message = ttk.Combobox(form_frame, state='readonly')
        self.rel_message.grid(row=2, column=1, sticky='ew')
        
        # Botones
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Add", command=self.add_relationship).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_relationship).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_relationship).pack(side='left', padx=5)
    
    def load_data(self):
        # Cargar Diagram Headers
        self.diagram_tree.delete(*self.diagram_tree.get_children())
        diagram_headers = self.session.query(DiagramHeader).all()
        for dh in diagram_headers:
            self.diagram_tree.insert('', 'end', values=(dh.ID, dh.Name, dh.graph_type.Description if dh.graph_type else ''))
        
        # Cargar Graph Types
        self.graph_type_tree.delete(*self.graph_type_tree.get_children())
        graph_types = self.session.query(GraphType).all()
        for gt in graph_types:
            self.graph_type_tree.insert('', 'end', values=(gt.ID, gt.Code, gt.Description))
        
        # Actualizar combobox de graph types
        self.dh_graph_type['values'] = [(gt.ID, gt.Description) for gt in graph_types]
        
        # Cargar Nodes
        self.node_tree.delete(*self.node_tree.get_children())
        nodes = self.session.query(Node).all()
        for node in nodes:
            self.node_tree.insert('', 'end', values=(
                node.ID, 
                node.Content, 
                node.Alias, 
                node.header.Name if node.header else '',
                node.figure.Description if node.figure else ''
            ))
        
        # Actualizar combobox de headers y figures para nodes
        self.node_header['values'] = [(dh.ID, dh.Name) for dh in diagram_headers]
        figures = self.session.query(Figure).all()
        self.node_figure['values'] = [(f.ID, f.Description) for f in figures]
        
        # Cargar Figures
        self.figure_tree.delete(*self.figure_tree.get_children())
        for figure in figures:
            self.figure_tree.insert('', 'end', values=(figure.ID, figure.Description, figure.Initial, figure.End))
        
        # Cargar Messages
        self.message_tree.delete(*self.message_tree.get_children())
        messages = self.session.query(Message).all()
        for msg in messages:
            self.message_tree.insert('', 'end', values=(msg.ID, msg.Description))
        
        # Cargar Relationships
        self.relationship_tree.delete(*self.relationship_tree.get_children())
        relationships = self.session.query(Relationship).all()
        for rel in relationships:
            self.relationship_tree.insert('', 'end', values=(
                rel.ID,
                rel.input_node.Content if rel.input_node else '',
                rel.output_node.Content if rel.output_node else '',
                rel.message.Description if rel.message else ''
            ))
        
        # Actualizar combobox para relationships
        self.rel_input['values'] = [(n.ID, n.Content) for n in nodes]
        self.rel_output['values'] = [(n.ID, n.Content) for n in nodes]
        self.rel_message['values'] = [(m.ID, m.Description) for m in messages]
    
    # Métodos para agregar/actualizar/eliminar entidades
    def add_diagram_header(self):
        try:
            name = self.dh_name.get()
            graph_type_id = self.dh_graph_type.get().split(',')[0] if self.dh_graph_type.get() else None
            
            if not name:
                messagebox.showerror("Error", "Name is required")
                return
                
            new_dh = DiagramHeader(Name=name, GraphTypeID=graph_type_id)
            self.session.add(new_dh)
            self.session.commit()
            self.load_data()
            self.dh_name.delete(0, 'end')
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))
    
    def update_diagram_header(self):
        selected = self.diagram_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update")
            return
            
        try:
            item = self.diagram_tree.item(selected[0])
            dh_id = item['values'][0]
            
            dh = self.session.query(DiagramHeader).get(dh_id)
            if dh:
                dh.Name = self.dh_name.get()
                graph_type_id = self.dh_graph_type.get().split(',')[0] if self.dh_graph_type.get() else None
                dh.GraphTypeID = graph_type_id
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))
    
    def delete_diagram_header(self):
        selected = self.diagram_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete")
            return
            
        try:
            item = self.diagram_tree.item(selected[0])
            dh_id = item['values'][0]
            
            dh = self.session.query(DiagramHeader).get(dh_id)
            if dh:
                self.session.delete(dh)
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))
    
    # Métodos similares para las otras entidades (GraphType, Node, Figure, Message, Relationship)
    # Implementar add_graph_type, update_graph_type, delete_graph_type, etc.
    # Patrón similar para las demás entidades
    
    def __del__(self):
        self.session.close()

# ... (código anterior permanece igual hasta la línea 360)

    def add_graph_type(self):
        try:
            code = self.gt_code.get()
            description = self.gt_description.get()
            
            if not code or not description:
                messagebox.showerror("Error", "Code and Description are required")
                return
                
            new_gt = GraphType(Code=code, Description=description)
            self.session.add(new_gt)
            self.session.commit()
            self.load_data()
            self.gt_code.delete(0, 'end')
            self.gt_description.delete(0, 'end')
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def update_graph_type(self):
        selected = self.graph_type_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update")
            return
            
        try:
            item = self.graph_type_tree.item(selected[0])
            gt_id = item['values'][0]
            
            gt = self.session.query(GraphType).get(gt_id)
            if gt:
                gt.Code = self.gt_code.get()
                gt.Description = self.gt_description.get()
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def delete_graph_type(self):
        selected = self.graph_type_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete")
            return
            
        try:
            item = self.graph_type_tree.item(selected[0])
            gt_id = item['values'][0]
            
            gt = self.session.query(GraphType).get(gt_id)
            if gt:
                self.session.delete(gt)
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def add_node(self):
        try:
            content = self.node_content.get()
            alias = self.node_alias.get()
            header_id = self.node_header.get().split(',')[0] if self.node_header.get() else None
            figure_id = self.node_figure.get().split(',')[0] if self.node_figure.get() else None
            
            if not content:
                messagebox.showerror("Error", "Content is required")
                return
                
            new_node = Node(Content=content, Alias=alias, HeaderID=header_id, FigureID=figure_id)
            self.session.add(new_node)
            self.session.commit()
            self.load_data()
            self.node_content.delete(0, 'end')
            self.node_alias.delete(0, 'end')
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def update_node(self):
        selected = self.node_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update")
            return
            
        try:
            item = self.node_tree.item(selected[0])
            node_id = item['values'][0]
            
            node = self.session.query(Node).get(node_id)
            if node:
                node.Content = self.node_content.get()
                node.Alias = self.node_alias.get()
                header_id = self.node_header.get().split(',')[0] if self.node_header.get() else None
                node.HeaderID = header_id
                figure_id = self.node_figure.get().split(',')[0] if self.node_figure.get() else None
                node.FigureID = figure_id
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def delete_node(self):
        selected = self.node_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete")
            return
            
        try:
            item = self.node_tree.item(selected[0])
            node_id = item['values'][0]
            
            node = self.session.query(Node).get(node_id)
            if node:
                self.session.delete(node)
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def add_figure(self):
        try:
            description = self.figure_description.get()
            initial = self.figure_initial.get()
            end = self.figure_end.get()
            
            if not description:
                messagebox.showerror("Error", "Description is required")
                return
                
            new_figure = Figure(Description=description, Initial=initial, End=end)
            self.session.add(new_figure)
            self.session.commit()
            self.load_data()
            self.figure_description.delete(0, 'end')
            self.figure_initial.delete(0, 'end')
            self.figure_end.delete(0, 'end')
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def update_figure(self):
        selected = self.figure_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update")
            return
            
        try:
            item = self.figure_tree.item(selected[0])
            figure_id = item['values'][0]
            
            figure = self.session.query(Figure).get(figure_id)
            if figure:
                figure.Description = self.figure_description.get()
                figure.Initial = self.figure_initial.get()
                figure.End = self.figure_end.get()
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def delete_figure(self):
        selected = self.figure_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete")
            return
            
        try:
            item = self.figure_tree.item(selected[0])
            figure_id = item['values'][0]
            
            figure = self.session.query(Figure).get(figure_id)
            if figure:
                self.session.delete(figure)
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def add_message(self):
        try:
            description = self.message_description.get()
            
            if not description:
                messagebox.showerror("Error", "Description is required")
                return
                
            new_message = Message(Description=description)
            self.session.add(new_message)
            self.session.commit()
            self.load_data()
            self.message_description.delete(0, 'end')
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def update_message(self):
        selected = self.message_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update")
            return
            
        try:
            item = self.message_tree.item(selected[0])
            message_id = item['values'][0]
            
            message = self.session.query(Message).get(message_id)
            if message:
                message.Description = self.message_description.get()
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def delete_message(self):
        selected = self.message_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete")
            return
            
        try:
            item = self.message_tree.item(selected[0])
            message_id = item['values'][0]
            
            message = self.session.query(Message).get(message_id)
            if message:
                self.session.delete(message)
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def add_relationship(self):
        try:
            input_id = self.rel_input.get().split(',')[0] if self.rel_input.get() else None
            output_id = self.rel_output.get().split(',')[0] if self.rel_output.get() else None
            message_id = self.rel_message.get().split(',')[0] if self.rel_message.get() else None
            
            if not input_id or not output_id:
                messagebox.showerror("Error", "Input and Output nodes are required")
                return
                
            new_rel = Relationship(Input=input_id, Output=output_id, MessageID=message_id)
            self.session.add(new_rel)
            self.session.commit()
            self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def update_relationship(self):
        selected = self.relationship_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update")
            return
            
        try:
            item = self.relationship_tree.item(selected[0])
            rel_id = item['values'][0]
            
            rel = self.session.query(Relationship).get(rel_id)
            if rel:
                input_id = self.rel_input.get().split(',')[0] if self.rel_input.get() else None
                rel.Input = input_id
                output_id = self.rel_output.get().split(',')[0] if self.rel_output.get() else None
                rel.Output = output_id
                message_id = self.rel_message.get().split(',')[0] if self.rel_message.get() else None
                rel.MessageID = message_id
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def delete_relationship(self):
        selected = self.relationship_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to delete")
            return
            
        try:
            item = self.relationship_tree.item(selected[0])
            rel_id = item['values'][0]
            
            rel = self.session.query(Relationship).get(rel_id)
            if rel:
                self.session.delete(rel)
                self.session.commit()
                self.load_data()
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", str(e))

    def __del__(self):
        self.session.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagramApp(root)
    root.mainloop()