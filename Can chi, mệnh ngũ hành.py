namSinh = int(input('Nhập năm sinh: '))

soThienCan = namSinh%10
thienCan = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]

soDiaChi = namSinh%12
diaChi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

soNguHanh = ((int(soThienCan/2)+3)%5+1 + (int(soDiaChi/2)+1)%3)%5
nguHanh = ["Mộc", "Kim", "Thủy", "Hỏa", "Thổ"]

mau1 = ["Đen, Xanh dương", "Vàng, Nâu đất", "Trắng, Xám", "Xanh lá", "Đỏ, Hồng, Cam, Tím",]
mau2 = ["Xanh lá", "Trắng, Xám", "Đen, Xanh dương", "Đỏ, Hồng, Cam, Tím", "Vàng, Nâu đất"]

print(f"Bạn sinh năm {thienCan[soThienCan]} {diaChi[soDiaChi]}, mệnh {nguHanh[soNguHanh]}.")
print(f"Màu tương sinh: {mau1[soNguHanh]}")
print(f"Màu tương hợp: {mau2[soNguHanh]}")
