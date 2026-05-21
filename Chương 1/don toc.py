a = input("Ma dan toc: ")
ds = {
    "01": "Kinh",
    "02": "Tay",
    "03": "Nung",
    "04": "Thai",
    "05": "KhoMe"
}

print(a + " la dan toc " + ds.get(a, "Khong hop le"))