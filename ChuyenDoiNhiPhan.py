def convert_to_base(b, binary_string):
    # Định nghĩa độ dài nhóm bit dựa theo hệ cơ số b
    if b == 2:
        group_size = 1
    elif b == 4:
        group_size = 2
    elif b == 8:
        group_size = 3
    elif b == 16:
        group_size = 4
    
    # Đệm thêm các bit 0 vào đầu xâu nhị phân nếu cần để chia nhóm đều
    while len(binary_string) % group_size != 0:
        binary_string = '0' + binary_string
    
    # Chuyển từng nhóm bit thành số hệ cơ số b
    result = ''
    for i in range(0, len(binary_string), group_size):
        group = binary_string[i:i+group_size]
        result += str(int(group, 2))  # Chuyển nhóm bit thành số hệ 10, rồi ghép lại
    
    return result

# Đọc dữ liệu từ file DATA.in
with open('DATA.in', 'r') as file:
    T = int(file.readline().strip())  # Đọc số lượng test cases
    for _ in range(T):
        b = int(file.readline().strip())  # Đọc hệ cơ số b
        binary_string = file.readline().strip()  # Đọc xâu nhị phân
        print(convert_to_base(b, binary_string))
