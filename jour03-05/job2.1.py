import tkinter as tk  
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()
dbpassword = os.getenv("pass")

# Fonction pour se connecter à la base de données MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",    
        user="root",         
        password=dbpassword, 
        database="store"     
    )

# Fonction pour récupérer la liste des produits depuis la base de données
def fetch_products():
    connection = get_connection()  
    cursor = connection.cursor()  
    cursor.execute("SELECT product.id, product.name, product.description, product.price, product.quantity, category.name, product.id_category "
               "FROM product JOIN category ON product.id_category = category.id")
    rows = cursor.fetchall()  
    connection.close()       
    return rows              

# Fonction pour ajouter un nouveau produit dans la base de données
def add_product(name, desc, price, qty, category_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                   (name, desc, price, qty, category_id))  
    connection.commit()
    connection.close()   

# Fonction pour mettre à jour un produit existant dans la base de données
def update_product(id, name, desc, price, qty, category_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE product SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = %s",
                   (name, desc, price, qty, category_id, id))  # Mise à jour du produit
    connection.commit()  
    connection.close()  

# Fonction pour supprimer un produit de la base de données
def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))  
    connection.commit()  
    connection.close()  

# Fonction pour actualiser la table des produits affichée dans l'interface graphique
def refresh_table():
    products = fetch_products() 
    for row in tree.get_children(): 
        tree.delete(row)
    for product in products: 
        tree.insert('', tk.END, values=product)  

# Fonction appelée lors de l'ajout d'un produit via l'interface
def on_add_product():
    try:
        name = entry_name.get().strip()
        desc = entry_desc.get().strip()
        if not name or not desc:
            messagebox.showerror("Erreur", "Veuillez entrer un nom et une description valides.")
            return
        
        price = float(entry_price.get())  
        qty = int(entry_qty.get())  
        category_id = int(entry_category.get())  
        add_product(name, desc, price, qty, category_id) 
        refresh_table() 
    except ValueError:  
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

# Fonction appelée lors de la suppression d'un produit via l'interface
def on_delete_product():
    selected_item = tree.selection() 
    if selected_item: 
        product_id = tree.item(selected_item[0])['values'][0] 
        delete_product(product_id)  
        refresh_table() 
    else:
        messagebox.showerror("Erreur", "Veuillez sélectionner un produit à supprimer.")

# Fonction appelée lors de la mise à jour d'un produit via l'interface
def on_update_product():
    selected_item = tree.selection()
    if selected_item:
        product_id = tree.item(selected_item[0])['values'][0]  
        
        name = entry_name.get().strip()
        desc = entry_desc.get().strip()
        
        if not name or not desc:
            messagebox.showerror("Erreur", "Veuillez entrer un nom et une description valides.")
            return
        
        try:
            price = float(entry_price.get().strip()) 
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un prix valide.")
            return

        try:
            qty = int(entry_qty.get().strip())  
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une quantité valide.")
            return

        try:
            category_id = int(entry_category.get().strip())  
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un ID de catégorie valide.")
            return
        
       
        update_product(product_id, name, desc, price, qty, category_id)
        refresh_table()  
    else:
        messagebox.showerror("Erreur", "Veuillez sélectionner un produit à modifier.") 

# Création de l'interface graphique avec tkinter
root = tk.Tk()  
root.title("Gestion de Stock")  

frame = tk.Frame(root)  
frame.pack(pady=10)  

# Création de la table (Treeview) pour afficher les produits
columns = ('ID', 'Nom', 'Description', 'Prix', 'Quantité', 'Catégorie','id_category')  
tree = ttk.Treeview(frame, columns=columns, show='headings')  
tree.heading('ID', text='ID')  
tree.heading('Nom', text='Nom')  
tree.heading('Description', text='Description')  
tree.heading('Prix', text='Prix')  
tree.heading('Quantité', text='Quantité') 
tree.heading('Catégorie', text='Catégorie') 
tree.heading('id_category', text='id_category') 
tree.pack()

# Création des champs de saisie pour ajouter ou modifier un produit
entry_name = tk.Entry(frame, width=30)  
entry_name.pack()
entry_name.insert(0, "Nom du produit") 

entry_desc = tk.Entry(frame, width=30)  
entry_desc.pack()
entry_desc.insert(0, "Description du produit")  

entry_price = tk.Entry(frame, width=30) 
entry_price.pack()
entry_price.insert(0, "Prix") 

entry_qty = tk.Entry(frame, width=30) 
entry_qty.pack()
entry_qty.insert(0, "Quantité")  

entry_category = tk.Entry(frame, width=30)  
entry_category.pack()
entry_category.insert(0, "ID de la catégorie") 


# Création des boutons pour ajouter, modifier et supprimer des produits
add_button = tk.Button(frame, text="Ajouter", command=on_add_product)  
add_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(frame, text="Modifier", command=on_update_product) 
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Supprimer", command=on_delete_product) 
delete_button.pack(side=tk.LEFT, padx=5)

# Actualisation de la table au démarrage du programme
refresh_table()

# Boucle principale de l'application tkinter
root.mainloop()