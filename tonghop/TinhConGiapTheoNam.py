def tinh_nam_ten_can_chi(nam):
    con_giap = ["Tí", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân","Dậu", "Tuất", "Hợi"]
    chi = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    
    
    nam_giap_chi = chi[(nam - 4)%10] + " " + con_giap[(nam - 4)%12]

    return nam_giap_chi

def main():
    nam = int(input("Nhập năm: "))
    print("Năm", nam, "là năm", tinh_nam_ten_can_chi(nam))

    

if __name__ == "__main__":
    main()