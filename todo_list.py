todo_list =[]

    def show_mwenu():
        print("\n=== TO-DO LIST APPLICATION ===")
        print("1. Tambah Tugas")
        print("2. Lihat Semua Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        print("=============================")

    def add_task():
        task = input("Masukan Tugas Terbaru :")
        todo_list.appent(task)
        print(f"Tugas {task}  Berhasil Di Tambahkan!")

    def view_task():
        if not todo_list:
            print("Tidak ad Tugas Tidak Ada dalam tugas.")
        else :
            print ("\nDaftarTugas:")
            for i task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    def delete_task():
        view_task()
        if todo_list:
            try:
            task_num = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
            
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Tugas '{removed_task}' berhasil dihapus!")

            else:
                print("Nomor tugas tidak valid.")

            except ValueError:
            print("Harap masukkan nomor yang valid.")

