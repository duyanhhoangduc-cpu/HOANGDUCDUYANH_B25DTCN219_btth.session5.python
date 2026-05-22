employee_count = int(input("Nhập số lượng nhân viên: "))

for employee in range(1, employee_count + 1):

    print(f"\nNhân viên {employee}")

    employee_name = input("Nhập tên nhân viên: ")
    working_days = int(input("Nhập số ngày làm việc: "))

    if working_days < 0 or working_days > 22:
        print("Dữ liệu không hợp lệ")
        continue

    if working_days == 0:
        print(f"{employee_name} nghỉ toàn bộ tháng")

    print("Biểu đồ ngày làm việc:")

    for i in range(1):
        for j in range(working_days):
            print("*", end="")
        print()

    if working_days >= 18:
        print("Làm việc chăm chỉ")
    elif working_days < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")