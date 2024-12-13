from datetime import datetime


todo_list = []


class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority 
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d") 

    def __str__(self):
        return f"{self.name} | Prioritas: {self.priority} | Tenggat: {self.due_date.strftime('%Y-%m-%d')}"


def show_menu():
    print("\n=== TO-DO LIST APPLICATION ===")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Hapus Tugas")
    print("4. Urutkan Tugas Berdasarkan Prioritas")
    print("5. Urutkan Tugas Berdasarkan Tenggat Waktu")
    print("6. Keluar")
    print("=============================")


def add_task():
    name = input("Masukkan nama tugas: ")
    while True:
        try:
            priority = int(input("Masukkan prioritas (1: Tinggi, 2: Sedang, 3: Rendah): "))
            if priority in [1, 2, 3]:
                break
            else:
                print("Masukkan angka 1, 2, atau 3.")
        except ValueError:
            print("Masukkan angka yang valid.")
    due_date = input("Masukkan tenggat waktu (YYYY-MM-DD): ")
    try:
        task = Task(name, priority, due_date)
        todo_list.append(task)
        print(f"Tugas '{name}' berhasil ditambahkan!")
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")


def view_tasks():
    if not todo_list:
        print("Tidak ada tugas dalam daftar.")
    else:
        print("\nDaftar Tugas:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")


def delete_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Tugas '{removed_task.name}' berhasil dihapus!")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Harap masukkan nomor yang valid.")


def sort_by_priority():
    if not todo_list:
        print("Tidak ada tugas untuk diurutkan.")
        return
    todo_list.sort(key=lambda task: task.priority)
    print("Daftar tugas berhasil diurutkan berdasarkan prioritas (1: Tinggi, 2: Sedang, 3: Rendah).")
    view_tasks()


def sort_by_due_date():
    if not todo_list:
        print("Tidak ada tugas untuk diurutkan.")
        return
    todo_list.sort(key=lambda task: task.due_date)
    print("Daftar tugas berhasil diurutkan berdasarkan tenggat waktu (paling dekat ke paling jauh).")
    view_tasks()


while True:
    try:
        show_menu()
        choice = input("Pilih menu (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            sort_by_priority()
        elif choice == "5":
            sort_by_due_date()
        elif choice == "6":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

