import csv
from tkinter import *
from tkinter import messagebox, simpledialog
from tabulate import tabulate
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from tkcalendar import Calendar

data_inventory = [
    ["CarID", "CarName", "Quantity"],
    [1, "Toyota Camry", 10],
    [2, "Honda Civic", 5],
    [3, "Hyundai Creta", 5],
    [4, "Tata Harrier", 10],
    [5, "Toyota Innova", 5],
    [6, "BMW X1", 5],
    [7, "BMW X5", 10],
    [8, "Audi Q7", 5],
    [9, "Audi R8", 10],
    [10, "Tata Safari", 5],
    [11, "Ford Mustang", 3],
    [12, "Maruti Suzuki Swift", 25],
    [13, "Kia Sorento", 6],
    [14, "Hyundai Creta", 8],
    [15, "Volkswagen Tiguan", 7],
    [16, "Subaru Forester", 5],
    [17, "Nissan Altima", 9],
    [18, "Mercedes-Benz C-Class", 4],
    [19, "Jaguar F-Pace", 3],
    [20, "Land Rover Discovery", 6],
    [21, "Jeep Wrangler", 10],
    [22, "Tesla Model 3", 15],
    [23, "Chevrolet Camaro", 5],
    [24, "Porsche Cayenne", 2],
    [25, "Dodge Challenger", 4],
    [26, "Honda Accord", 8],
    [27, "Hyundai Sonata", 7],
    [28, "Kia Sportage", 6],
    [29, "Ford Explorer", 9],
    [30, "Acura MDX", 4]
]

data_car_types = [
    ["TypeID", "TypeName"],
    [1, "SUV"],
    [2, "Sedan"],
    [3, "Sports Car"],
    [4, "MUV"],
    [5, "Convertible"],
    [6, "Luxury"],
    [7, "Electric"],
    [8, "Off-road"],
    [9, "Pickup Truck"],
    [10, "Hybrid"]
]

data_used_cars = [
    ["CarID", "CarName", "Year", "Mileage", "Quantity"],
    [1, "Ford Focus", 2015, 45000, 1],
    [2, "Skoda Rapid", 2014, 60000, 1],
    [3, "Toyota RAV4", 2019, 50000, 1],
    [4, "Honda CRV", 2018, 55000, 1],
    [5, "Honda Civic", 2020, 45000, 1],
    [6, "Toyota Prius", 2019, 40000, 1],
    [7, "Toyota Innova", 2017, 50000, 1],
    [8, "Hyundai Sonata", 2020, 35000, 1]
]

data_newly_arrived = [
    ["CarID", "CarName", "ArrivalDate", "Quantity"],
    [1, "BMW X5", "2024-10-01", 1],
    [2, "Audi Q7", "2024-10-05", 2],
    [3, "BMW X1", "2024-10-24", 3],
    [4, "Toyota Innova", "2024-10-20", 2],
    [5, "Toyota RAV4", "2024-10-10", 1],
    [6, "Xiaomi SU7", "2024-10-25", 5]
]

data_exported_cars = [
    ["CarID", "CarName", "ExportDate", "Quantity"],
    [1, "Audi Q7", "2024-09-12", 1],
    [2, "Audi R8", "2024-08-15", 3],
    [3, "Toyota LandCruiser", "2024-08-31", 2]
]

data_imported_cars = [
    ["CarID", "CarName", "ImportDate", "Quantity"],
    [1, "Toyota Corolla", "2024-07-20", 1],
    [2, "Mazda CX-5", "2024-06-20", 1],
    [3, "Tata Harrier", "2024-07-22", 2],
    [4, "Toyota Innova", "2024-08-24", 4]
]

data_employees = [
    ["EmployeeID", "Name", "Position"],
    [1, "Virat Kohli", "CEO"],
    [2, "Jane Smith", "Manager"],
    [3, "Joe Rogan", "Assistant Manager"],
    [6, "Roger Rocks", "Assistant Manager"],
    [5, "Steve Rogers", "Sales"],
    [6, "Jack Sparrow", "Sales"]
]

data_branches = [
    ["BranchID", "Location", "Manager"],
    [1, "New York", "John Doe"],
    [2, "Los Angeles", "Jane Smith"],
    [3, "Coimbatore", "Sabarish BA"]
]

data_worth_of_cars = [
    ["CarID", "CarName", "Worth", "Quantity"],
    [1, "Toyota Camry", 500000, 10],
    [2, "Honda Civic", 200000, 5],
    [3, "Hyundai Creta", 275000, 5],
    [4, "Tata Harrier", 500000, 5],
    [5, "Toyota Innova", 210000, 5],
    [6, "BMW X1", 300000, 5],
    [7, "BMW X5", 750000, 10],
    [8, "Audi Q7", 325000, 5],
    [9, "Audi R8", 750000, 10],
    [10, "Tata Safari", 315000, 5]
]

data_rental_cars = [
    ["RentalID", "CarName", "RentalPricePerDay"],
    [1, "Toyota Yaris", 2400],
    [2, "Honda Accord", 2500],
    [3, "Toyota RAV4", 3000],
    [4, "Honda CRV", 3500],
    [5, "Toyota LandCruiser", 5000]
]

tables = [
    ("inventory.csv", data_inventory),
    ("car_types.csv", data_car_types),
    ("used_cars.csv", data_used_cars),
    ("newly_arrived.csv", data_newly_arrived),
    ("exported_cars.csv", data_exported_cars),
    ("imported_cars.csv", data_imported_cars),
    ("employees.csv", data_employees),
    ("branches.csv", data_branches),
    ("worth_of_cars.csv", data_worth_of_cars),
    ("rental_cars.csv", data_rental_cars)
]

plot_tables = [
    ("inventory.csv", data_inventory),
    ("car_types.csv", data_car_types),
    ("used_cars.csv", data_used_cars),
    ("newly_arrived.csv", data_newly_arrived),
    ("worth_of_cars.csv", data_worth_of_cars),
    ("rental_cars.csv", data_rental_cars)
]

def initialize_files(overwrite=False):
    for filename, data in tables:
        if overwrite:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        else:
            try:
                with open(filename, mode='x', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
            except FileExistsError:
                continue

def plot_data(filename):
    try:
        if filename == "newly_arrived.csv":
            show_calendar()
            return
            
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = list(reader)

            plt.figure(figsize=(10, 6))
            
            if filename == "inventory.csv":
                car_names = [row[1] for row in data]
                quantities = [int(row[2]) for row in data]
                plt.bar(car_names, quantities)
                plt.title('Car Inventory')
                plt.xlabel('Car Names')
                plt.ylabel('Quantity')
                
            elif filename == "car_types.csv":
                types = [row[1] for row in data]
                plt.pie([1]*len(types), labels=types, autopct='%1.1f%%')
                plt.title('Distribution of Car Types')
                
            elif filename == "used_cars.csv":
                car_names = [row[1] for row in data]
                mileages = [int(row[3]) for row in data]
                plt.bar(car_names, mileages)
                plt.title('Used Cars Mileage')
                plt.xlabel('Car Names')
                plt.ylabel('Mileage')
                
            elif filename == "worth_of_cars.csv":
                car_names = [row[1] for row in data]
                worth = [int(row[2]) for row in data]
                plt.bar(car_names, worth)
                plt.title('Worth of Cars')
                plt.xlabel('Car Names')
                plt.ylabel('Worth (₹)')
                
            elif filename == "rental_cars.csv":
                car_names = [row[1] for row in data]
                prices = [int(row[2]) for row in data]
                plt.bar(car_names, prices)
                plt.title('Rental Prices per Day')
                plt.xlabel('Car Names')
                plt.ylabel('Price (₹)')
                
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
            
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def read_and_display_file(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = list(reader)

            if filename.split('.')[0].lower() not in ["car_types", "employees", "branches", "rental_cars"]:
                if "Quantity" not in headers:
                    messagebox.showerror("Error", f"The 'Quantity' column is missing in the {filename.split('.')[0]} table.")
                    return

            display_data = tabulate(data, headers=headers, tablefmt="grid")

            display_window = Toplevel()
            display_window.title(f"Displaying {filename.split('.')[0]}")

            text_area = Text(display_window, wrap=WORD, height=20, width=80, bg="black", fg="white", font=("Courier", 14))
            text_area.insert(INSERT, display_data)
            text_area.config(state=DISABLED)
            text_area.pack()

    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def insert_row(filename, headers):
    new_data = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            data = list(reader)
            new_id = len(data) + 1
    except FileNotFoundError:
        new_id = 1
        data = []

    unique_field_index = 1
    existing_names = {row[unique_field_index].lower() for row in data}

    while True:
        car_name = simpledialog.askstring("Input", f"Enter {headers[unique_field_index]}:")
        if not car_name:
            messagebox.showwarning("Invalid Input", f"{headers[unique_field_index]} cannot be empty!")
            continue
        if car_name.lower() in existing_names:
            messagebox.showwarning("Duplicate Entry", f"{car_name} already exists! Please enter a different value.")
            continue
        new_data.append(str(new_id))
        new_data.append(car_name)
        break

    for header in headers[2:]:
        while True:
            entry = simpledialog.askstring("Input", f"Enter {header}:")
            if not entry:
                messagebox.showwarning("Invalid Input", f"{header} cannot be empty!")
                continue
                
            if header == "Quantity":
                try:
                    quantity = int(entry)
                    if quantity <= 0:
                        messagebox.showwarning("Invalid Input", "This Format of Quantity is not Allowed")
                        continue
                    new_data.append(str(quantity))
                except ValueError:
                    messagebox.showwarning("Invalid Input", "This Format of Quantity is not Allowed")
                    continue
            else:
                new_data.append(entry)
            break

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)
    messagebox.showinfo("Success", "New row added successfully!")

def update_row(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = list(reader)

        row_id = simpledialog.askinteger("Input", "Enter the ID to update:")
        for row in data:
            if str(row[0]) == str(row_id):
                for idx, header in enumerate(headers[1:], start=1):
                    new_value = simpledialog.askstring("Input", f"Enter new {header} (current: {row[idx]}):")
                    if new_value:
                        row[idx] = new_value
                break

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
        messagebox.showinfo("Success", f"Row {row_id} updated successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' not found.")

def delete_row(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = list(reader)

        has_quantity = "Quantity" in headers

        id_index = 0

        row_id = simpledialog.askinteger("Input", f"Enter the ID to delete from {filename.split('.')[0]} table:")

        row_deleted = False
        for row in data:
            if str(row[id_index]) == str(row_id):
                if has_quantity:
                    quantity_index = headers.index("Quantity")
                    current_quantity = int(row[quantity_index])

                    remove_quantity = simpledialog.askinteger("Input", f"Enter quantity to remove (Available: {current_quantity}):")
                    if remove_quantity is None or remove_quantity <= 0:
                        messagebox.showwarning("Invalid Input", "Please enter a positive quantity.")
                        return
                    if remove_quantity > current_quantity:
                        messagebox.showwarning("Invalid Input", "Entered quantity exceeds available stock.")
                        return
                    elif remove_quantity == current_quantity:
                        data.remove(row)
                    else:
                        row[quantity_index] = str(current_quantity - remove_quantity)
                else:
                    data.remove(row)
                row_deleted = True
                break

        if not row_deleted:
            messagebox.showwarning("Error", f"ID {row_id} not found!")
            return

        for idx, row in enumerate(data, start=1):
            row[id_index] = str(idx)

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        messagebox.showinfo("Success", "Row deleted successfully!")

    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid data format encountered.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def show_members():
    members_window = Toplevel()
    members_window.title("Team Members")
    members_window.geometry("300x200")
    
    Label(members_window, text="Members:", font=("Helvetica", 16, "bold")).pack(pady=10)
    Label(members_window, text="SH Nihil Mukkesh", font=("Helvetica", 14)).pack(pady=5)
    Label(members_window, text="Nitharshan CK", font=("Helvetica", 14)).pack(pady=5)
    Label(members_window, text="Prasanna", font=("Helvetica", 14)).pack(pady=5)
    Label(members_window, text="Prawin Adithya", font=("Helvetica", 14)).pack(pady=5)

def show_used():
    used_window = Toplevel()
    used_window.title("Used Components")
    used_window.geometry("400x300")
    
    # Create a canvas with scrollbar
    canvas = Canvas(used_window)
    scrollbar = Scrollbar(used_window, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Add content to scrollable frame
    Label(scrollable_frame, text="Components Used:", font=("Helvetica", 16, "bold")).pack(pady=10)
    Label(scrollable_frame, text="Data Structures:", font=("Helvetica", 14, "bold")).pack(pady=5)
    Label(scrollable_frame, text="- Lists (for data storage)", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, text="- Tuples (for table configurations)", font=("Helvetica", 12)).pack()
    
    Label(scrollable_frame, text="\nLibraries:", font=("Helvetica", 14, "bold")).pack(pady=5)
    Label(scrollable_frame, text="- Tkinter (GUI framework)", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, text="- CSV (file handling)", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, text="- PIL/Pillow (image processing)", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, text="- Matplotlib (data visualization)", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, text="- Tabulate (table formatting)", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, text="- tkcalendar (calendar widget)", font=("Helvetica", 12)).pack()

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def show_calendar():
    def on_date_select():
        selected_date = cal.get_date()
        date_parts = selected_date.split('/')
        formatted_date = f"2024-{date_parts[0].zfill(2)}-{date_parts[1].zfill(2)}"
        
        with open('newly_arrived.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            cars_on_date = []
            for row in reader:
                if row[2] == formatted_date:
                    cars_on_date.append(f"Car: {row[1]}, Quantity: {row[3]}")
        
        if cars_on_date:
            result = "\n".join(cars_on_date)
            messagebox.showinfo("Cars on Selected Date", result)
        else:
            messagebox.showinfo("No Cars", "No cars arrived on this date")

    cal_window = Toplevel()
    cal_window.title("Select Date")
    cal = Calendar(cal_window, selectmode='day')
    cal.pack(pady=20)
    Button(cal_window, text="Show Cars", command=on_date_select).pack()

def setup_gui():
    root = Tk()
    root.title("Car Dealership Management System")

    bg_img = Image.open(r"C:\Users\Nihil\Downloads\car_images.jpg")
    bg_img = bg_img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(bg_img)

    bg_label = Label(root, image=bg_img)
    bg_label.place(relwidth=1, relheight=1)

    members_frame = Frame(root, bg="#333")
    members_frame.pack(anchor="ne", padx=10, pady=10)
    
    Button(members_frame, text="Members", font=("Helvetica", 12), command=show_members, bg="#FFD700", fg="#2E4053").pack(side=LEFT, padx=5)
    Button(members_frame, text="Used", font=("Helvetica", 12), command=show_used, bg="#FFD700", fg="#2E4053").pack(side=LEFT, padx=5)

    label_title = Label(root, text="Car Dealership Management", font=("Helvetica", 24, "bold"), bg="#333", fg="white")
    label_title.pack(pady=10)

    Button(root, text="Display", width=20, font=("Helvetica", 16), command=lambda: show_menu("Display", read_and_display_file), bg="#E74C3C", fg="white").pack(pady=10)
    Button(root, text="Insert", width=20, font=("Helvetica", 16), command=lambda: show_menu("Insert", insert_row), bg="#2ECC71", fg="white").pack(pady=10)
    Button(root, text="Update", width=20, font=("Helvetica", 16), command=lambda: show_menu("Update", update_row), bg="#3498DB", fg="white").pack(pady=10)
    Button(root, text="Delete", width=20, font=("Helvetica", 16), command=lambda: show_menu("Delete", delete_row), bg="#F1C40F", fg="white").pack(pady=10)
    Button(root, text="DATA", width=20, font=("Helvetica", 16), command=lambda: show_menu("Plot", plot_data), bg="#9B59B6", fg="white").pack(pady=10)

    bg_label.image = bg_img

    initialize_files(overwrite= True)

    root.mainloop()

def show_menu(action, func):
    menu = Toplevel()
    menu.title(f"{action} Menu")
    menu.configure(bg="#444")

    table_list = plot_tables if action == "Plot" else tables
    
    for filename, data in table_list:
        button_text = filename.split('.')[0].upper()
        Button(menu, text=button_text, font=("Helvetica", 16), command=lambda f=filename, h=data[0]: func(f, h) if action == "Insert" else func(f), bg="#FFCCCB", fg="#333").pack(pady=10)

if __name__ == "__main__":
    setup_gui()