def dequy(i):
    print(i)
    dequy(i+1)
    return
dequy(1)

#Ở đây đệ quy sẽ tiến hành bước vào vòng lặp vô hạn, gây quá tải bộ nhớ khiến chương trình bị đứng

def dequy(i):
    if i >=100:# Tạo một nút dừng để dừng mọi trạng thái
        return
    print(i)
    dequy(i+1)
    return
dequy(1)