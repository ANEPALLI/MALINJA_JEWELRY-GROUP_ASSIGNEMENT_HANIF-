import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MALINJA_JEWELRY"
    )

mycursor = mydb.cursor()


def open_customer_info():
    customer_info_window = tk.Toplevel(root)
    customer_info_window.title("Customer Information")
    customer_info_window.geometry("650x350")
    customer_info_window.configure(bg="#030303")

    # Customer Information Form
    tk.Label(customer_info_window, text=" Name: ", font=("Times New Roman", 12), bg="#D4AF37").grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    customer_name_entry = tk.Entry(customer_info_window)
    customer_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    tk.Label(customer_info_window, text=" Title: ", font=("Times New Roman", 12), bg="#D4AF37").grid(row=0, column=2, padx=5, pady=5, sticky='ew')
    title_entry = ttk.Combobox(customer_info_window, values=["Dr.", "Mr.", "Mrs.","Dato", "Datin","Tan Sri"])
    title_entry.grid(row=0, column=3, padx=10, pady=10, sticky="ew")
    
    tk.Label(customer_info_window, text="  Age: ", font=("Times New Roman", 12), bg="#D4AF37").grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    age_entry = tk.Entry(customer_info_window)
    age_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    tk.Label(customer_info_window, text="E-Mail:", font=("Times New Roman", 12), bg="#D4AF37").grid(row=1, column=2, sticky="ew", padx=5, pady=5)
    email_entry = tk.Entry(customer_info_window)
    email_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
    
    tk.Label(customer_info_window, text="Phone Number:", font=("Times New Roman", 12), bg="#D4AF37").grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    phone_entry = tk.Entry(customer_info_window)
    phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    
    tk.Label(customer_info_window, text="Addess:", font=("Times New Roman", 12), bg="#D4AF37").grid(row=2, column=2, sticky="ew", padx=5, pady=5)
    address_entry = tk.Entry(customer_info_window)
    address_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

    tk.Label(customer_info_window, text="Gender:", font=("Times New Roman", 12), bg="#D4AF37").grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    gender_combobox = ttk.Combobox(customer_info_window, values=["Male", "Female"])
    gender_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    tk.Label(customer_info_window, text="Nationality:", font=("Times New Roman", 12), bg="#D4AF37").grid(row=4, column=0, sticky="ew", padx=5, pady=5)
    nationality_entry = ttk.Combobox(customer_info_window, values=["Malay", "Indian", "Chinese", "Iban", "Kadazan"])
    nationality_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    def submit_customer_info():
        customer_name = customer_name_entry.get()
        customer_age = age_entry.get()
        title = title_entry.get()
        customer_address = address_entry.get()
        customer_phone = phone_entry.get()
        customer_email = email_entry.get()
        customer_gender = gender_combobox.get()
        customer_nationality = nationality_entry.get()

        messagebox.showinfo("Customer Information",
                            f"Name: {customer_name}\nAge: {customer_age}\nPhone: {customer_phone}\nGender: {customer_gender}\nNationality: {customer_nationality}\nTitle: {title}\nAddress: {customer_address}\nEmail: {customer_email}")

        customer_info_window.destroy()

        # Update the customer information in the database
        update_sql = "UPDATE customer_information SET customer_name = %s, customer_age = %s, title = %s, customer_address = %s, customer_phone = %s, customer_email = %s, customer_gender = %s, customer_nationality = %s WHERE customer_name = %s"
        update_val = (customer_name, customer_age, title, customer_address, customer_phone, customer_email, customer_gender,customer_nationality, customer_name)
        mycursor.execute(update_sql, update_val)
        mydb.commit()

        messagebox.showinfo("Customer Information", f"Customer information updated for {customer_name}")
        customer_info_window.destroy()
        
        sql = "INSERT INTO customer_information (customer_name, customer_age, title, customer_address, customer_phone, customer_email, customer_gender, customer_nationality) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (customer_name, customer_age, title, customer_address, customer_phone, customer_email, customer_gender, customer_nationality)
        mycursor.execute(sql, val)
        mydb.commit()

        update_button = tk.Button(customer_info_window, text="Update", bg="#FAF49E", command=update_customer_info)
        update_button.grid(row=8, column=1, columnspan=5, sticky="ew", pady=10)

    def update_customer_info():
        selected_item = customer_listbox.get(tk.ACTIVE)
        if not selected_item:
            messagebox.showinfo("Update", "Please select a customer to update.")
            return

        customer_name = selected_item.split(" - ")[0]

        mycursor.execute("SELECT * FROM customer_information WHERE customer_name = %s", (customer_name,))
        customer_data = mycursor.fetchone()

        customer_name_entry.delete(0, tk.END)
        customer_name_entry.insert(tk.END, customer_data[0])

        title_entry.set(customer_data[2])
        age_entry.delete(0, tk.END)
        age_entry.insert(tk.END, customer_data[1])

        email_entry.delete(0, tk.END)
        email_entry.insert(tk.END, customer_data[5])

        phone_entry.delete(0, tk.END)
        phone_entry.insert(tk.END, customer_data[4])

        address_entry.delete(0, tk.END)
        address_entry.insert(tk.END, customer_data[3])

        gender_combobox.set(customer_data[6])
        nationality_entry.set(customer_data[7])

    def delete_customer_info():
        selected_item = customer_listbox.get(tk.ACTIVE)
        if not selected_item:
            messagebox.showinfo("Delete", "Please select a customer to delete.")
            return

        customer_name = selected_item.split(" - ")[0]

        customer_listbox.delete(tk.ACTIVE)

        delete_sql = "DELETE FROM customer_information WHERE customer_name = %s"
        delete_val = (customer_name,)
        mycursor.execute(delete_sql, delete_val)
        mydb.commit()

        messagebox.showinfo("Customer Information", f"Record for {customer_name} deleted successfully.")

        update_customer_list()

    def update_customer_list():
    # Function to update the customer listbox
        mycursor.execute("SELECT customer_name FROM customer_information")
        customers = mycursor.fetchall()
        customer_listbox.delete(0, tk.END)
        for customer in customers:
            customer_listbox.insert(tk.END, f"{customer[0]}")


    def clear_entries():
        customer_name_entry.delete(0, tk.END)
        title_entry.set("")
        age_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        gender_combobox.set("")
        nationality_entry.set("")

    submit_button = tk.Button(customer_info_window, text="Submit", bg="#FAF49E", command=submit_customer_info)
    submit_button.grid(row=8, column=0, columnspan=5, sticky="ew", pady=10)

    delete_button = tk.Button(customer_info_window, text="Delete", bg="#FAF49E", command=delete_customer_info)
    delete_button.grid(row=9, column=0, columnspan=5, sticky="ew", pady=10)

    # Listbox to display customer names
    customer_listbox = tk.Listbox(customer_info_window, selectmode=tk.SINGLE)
    customer_listbox.grid(row=0, column=4, rowspan=8, padx=10, pady=10, sticky='news')
    customer_listbox.bind("<ButtonRelease-1>", lambda event: update_customer_info())

    # Fetch and display existing customers in the listbox
    update_customer_list()

    clear_button = tk.Button(customer_info_window, text="Clear Entries", bg="#FAF49E", command=clear_entries)
    clear_button.grid(row=10, column=0, columnspan=5, sticky="ew", pady=10)

        
    submit_button = tk.Button(customer_info_window, text="Submit",bg="#FAF49E", command=submit_customer_info)
    submit_button.grid(row=8, column=0, columnspan=5,sticky="ew",  pady=10)
    
    
def open_order_jewelry():
    def delete_order_jewelry():
        selected_item = item_listbox.get(tk.ACTIVE)
        if not selected_item:
            messagebox.showinfo("Delete", "Please select an item to delete.")
            return

        item_value = selected_item.split(" - ")[0]

        item_listbox.delete(tk.ACTIVE)

        delete_sql = "DELETE FROM order_jewelry WHERE item_value = %s"
        delete_val = (item_value,)
        mycursor.execute(delete_sql, delete_val)
        mydb.commit()

        messagebox.showinfo("Order Jewelry", f"Record for {item_value} deleted successfully.")
        update_item_list()

    def update_item_list():
        mycursor.execute("SELECT item_value, product_value, quantity_value FROM order_jewelry")
        items = mycursor.fetchall()
        item_listbox.delete(0, tk.END)
        for item in items:
            item_listbox.insert(tk.END, f"{item[0]} - RM{item[1]} - Quantity: {item[2]}")

    def calculate():
        item_value = item_combobox.get()
        product_value = product_combobox.get()
        quantity_value = quantity_entry.get()

        try:
            quantity_value = int(quantity_value)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity (numeric value).")
            return

        try:
            product_value = float(product_value)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid product price (numeric value).")
            return

        total_price = product_value * quantity_value

        # Insert a new record for each entry
        sql = "INSERT INTO order_jewelry (item_value, product_value, quantity_value, total_price) VALUES (%s, %s, %s, %s)"
        val = (item_value, product_value, quantity_value, total_price)
        mycursor.execute(sql, val)
        mydb.commit()

        # Add the new item to the listbox
        item_listbox.insert(tk.END, f"{item_value} - RM{product_value} - Quantity: {quantity_value} - Total Price: RM{total_price}")

        messagebox.showinfo("Jewelry Info", f"Record for {item_value} inserted successfully.")


        update_item_list()

    def update_order_jewelry():
        # This function was missing, adding it back
        selected_item = item_listbox.get(tk.ACTIVE)
        if not selected_item:
            messagebox.showinfo("Update", "Please select an item to update.")
            return

        new_product_value = product_combobox.get()
        new_quantity_value = quantity_entry.get()

        try:
            new_quantity_value = int(new_quantity_value)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity (numeric value).")
            return

        try:
            new_product_value = float(new_product_value)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid product price (numeric value).")
            return

        item_value = selected_item.split(" - ")[0]

        update_sql = "UPDATE order_jewelry SET product_value = %s, quantity_value = %s WHERE item_value = %s"
        update_val = (new_product_value, new_quantity_value, item_value)
        mycursor.execute(update_sql, update_val)
        mydb.commit()

        messagebox.showinfo("Order Jewelry", f"Record for {item_value} updated successfully.")
        update_item_list()

    order_jewelry_window = tk.Toplevel(root)
    order_jewelry_window.title("Order Jewelry")
    order_jewelry_window.geometry("750x780")
    order_jewelry_window.configure(bg="#030303")
    
    price_text=tk.Text(order_jewelry_window, bg="#ffc953", fg="#030303", height=20 , width=50)
    price_text.grid(row=0, column=0, padx=20, pady=20)

    price_text.insert(tk.END, "JEWELRY ITEM:\n\n")
    price_text.insert(tk.END, "fish Bracelets : Bracelets: Price:RM350\n\n")
    price_text.insert(tk.END, "meteor bracelets : Bracelets: Price:RM600\n\n")
    price_text.insert(tk.END, "flower bracelets : Bracelets: Price:RM1190\n\n")
    price_text.insert(tk.END, "shark necklace : necklace : Price:RM6086\n\n")
    price_text.insert(tk.END, "dino necklace : necklace : Price:RM4093\n\n")
    price_text.insert(tk.END, "cat necklace : necklace : Price:RM7183\n\n")
    price_text.insert(tk.END, "diamond Ring : Ring : Price:RM10023\n\n")
    price_text.insert(tk.END, "gold ring : Ring : Price:RM6028\n\n")
    price_text.insert(tk.END, "silver ring : Ring : Price:RM1297\n\n")
    price_text.configure(state='disabled')

    item = tk.Label(order_jewelry_window, text="ITEM", font=("Felix Titling",), bg="#D5A970", fg="#030303" )
    item.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
    item_combobox = ttk.Combobox(order_jewelry_window, values=[" fish bracelets", "meteor bracelets", "flower bracelets", "shark necklace", "dino necklace", "cat necklace", "diamond ring", "gold ring", "silver ring"])
    item_combobox.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    product = tk.Label(order_jewelry_window, text="JEWELRY PRICE",font=("Felix Titling",), bg="#D5A970", fg="#030303")
    product.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
    product_combobox = tk.Entry(order_jewelry_window)
    product_combobox.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    quantity = tk.Label(order_jewelry_window, text="QUANTITY", font=("Felix Titling",), bg="#D5A970", fg="#030303")
    quantity.grid(row=5, column=0, padx=10, pady=10, sticky='ew')
    quantity_entry = ttk.Combobox(order_jewelry_window, values=["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    quantity_entry.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

    output_label = tk.Label(order_jewelry_window)

    submit_button = tk.Button(order_jewelry_window, text="Submit", bg="#FAF49E", fg="#030303", command=calculate)
    submit_button.grid(row=11, column=0, columnspan=2, pady=10, sticky="ew")

    delete_button = tk.Button(order_jewelry_window, text="Delete", bg="#FAF49E", fg="#030303", command=delete_order_jewelry)
    delete_button.grid(row=12, column=0, columnspan=2, pady=10, sticky="ew")

    update_button = tk.Button(order_jewelry_window, text="Update", bg="#FAF49E", fg="#030303", command=update_order_jewelry)
    update_button.grid(row=13, column=0, columnspan=2, pady=10, sticky="ew")

    item_listbox = tk.Listbox(order_jewelry_window, selectmode=tk.SINGLE)
    item_listbox.grid(row=0, column=1, rowspan=3, padx=10, pady=100, sticky='new')
    item_listbox.bind("<ButtonRelease-1>", lambda event: select_item(event))

    update_item_list()

    def select_item(event):
        selected_item = item_listbox.get(tk.ACTIVE)
        item_combobox.set(selected_item.split(" - ")[0])

def open_order_taking():
    order_taking_window = tk.Toplevel(root)
    order_taking_window.title("Order Taking")
    order_taking_window.geometry("480x400")
    order_taking_window.configure(bg="#D4AF37")

    # Order Taking Form
    note1 = tk.Label(order_taking_window, font=("Black Burger Rough",20),  text="THANK YOU FOR PURCHASING \n please select free gift ", bg="#D4AF37", fg="#fefefe")
    note1.grid(row=0, columnspan=2, padx=30, pady=30)
    
    free_gift = tk.Label(order_taking_window, text="Free Gift:", font=("Elephant",), bg="#282622", fg="#ffbf34" )
    free_gift.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    free_gift_combobox = ttk.Combobox(order_taking_window, values=["Perfume", "Umbrella", "Beg"])
    free_gift_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    
    tk.Label(order_taking_window, text="Place to Claim (Branch):", font=("Elephant",), bg="#282622", fg="#ffbf34").grid(row=2, column=0, sticky="Ew", padx=5, pady=5)
    place_combobox = ttk.Combobox(order_taking_window, values=["Hulu Teregganu,Terengganu (014-9307134)", "Batu Pahat,Johor(014-7726817)", "Petaling Jaya,Selangor (014-8726615)", "Alor Gajah, Melaka (014-3528817)) "])
    place_combobox.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

    tk.Label(order_taking_window, text="Date Claim:", font=("Elephant",), bg="#282622", fg="#ffbf34").grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    date_calender = DateEntry(order_taking_window, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_calender.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

    tk.Label(order_taking_window, text="Additional Notes:", font=("Elephant",), bg="#282622", fg="#ffbf34").grid(row=4, column=0, sticky="ew", padx=5, pady=5)
    notes_entry = tk.Entry(order_taking_window)
    notes_entry.grid(row=4, column=1, padx=5, pady=5, sticky='ew')

    def submit_order_taking():
        free_gift = free_gift_combobox.get()
        claim_place = place_combobox.get()
        claim_date = date_calender.get_date()
        additional_notes = notes_entry.get()

        messagebox.showinfo("Order Taking", f"Free Gift: {free_gift}\nPlace to Claim: {claim_place}\nDate Claim: {claim_date}\nAdditional Notes: {additional_notes}")

        order_taking_window.destroy()
        
        sql = "INSERT INTO order_tracking (free_gift, claim_place, claim_date, additional_notes) VALUES (%s, %s, %s, %s)"
        val = (free_gift, claim_place, claim_date, additional_notes)
        mycursor.execute(sql, val)
        mydb.commit()
        
    submit_button = tk.Button(order_taking_window, text="Submit", command=submit_order_taking)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='e')

root = tk.Tk()
root.title("Jewelry Online Store")
root.geometry("800x600")

bg_image = Image.open("gambar jewels.jpg")  
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Buttons to navigate to different interfaces
malinja_jewel = tk.Label(root, text="MALINJA JEWEL", font=("times new roman", 20, "bold", "italic"), bg="#DEB706", fg="#FFFFFF")
malinja_jewel.place(relx=0.5, rely=0.1, anchor="center")

note = tk.Label(root, text="   Let the jewels blink blink you ~   ", font=("times new roman", 20, "bold", "italic"), bg="#D4AF37", fg="#3A3536")
note.place(relx=0.5, rely=0.2, anchor="center")

customer_info_button = tk.Button(root, text="Customer Information", font=("times new roman", 20), bg="#5D5A4A", fg="#FFFFFF", command=open_customer_info)
customer_info_button.place(relx=0.5, rely=0.4, anchor="center")

order_jewelry_button = tk.Button(root, text="Order Jewelry", font=("times new roman", 20),bg="#5D5A4A", fg="#FFFFFF", command=open_order_jewelry)
order_jewelry_button.place(relx=0.5, rely=0.6, anchor="center")

order_taking_button = tk.Button(root, text="Order Taking", font=("times new roman", 20),bg="#5D5A4A", fg="#FFFFFF", command=open_order_taking)
order_taking_button.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()

# for 2nd submit assignment, we added the update and delete functions
# in customer informations, double click to the chosen data and click delete button to delete (there is only delete functions)
# in open order jewelry, to update click the chosen item that has been inserted to database in white listbox, insert the price and quantity and click update (we can't change the item, so considered as change quantity option only)