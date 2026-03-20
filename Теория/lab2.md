<img width="394" height="558" alt="image" src="https://github.com/user-attachments/assets/7b2d153e-1245-4dda-8cea-f0d45b872592" /> <img width="276" height="400" alt="image" src="https://github.com/user-attachments/assets/cd2bcbb0-a28c-40fa-88b4-dc4b0d9e91eb" />

---
<img width="628" height="264" alt="image" src="https://github.com/user-attachments/assets/af5ca2f3-48cd-4dac-8df2-c984f4190a61" />

---

<img width="1937" height="849" alt="image" src="https://github.com/user-attachments/assets/62fd51f5-1525-4c18-8789-4e581ce79e0b" />

<img width="470" height="187" alt="image" src="https://github.com/user-attachments/assets/145d6940-4ab9-4feb-9e4d-3fb49f5e0f49" />

- server Có C1 | C2
- C2 = P2 XOR C1
- P2 = D(C2) XOR C1 -> server có P2
- Attacker gửi ciphertext mới: C1' | C2
- Server giải mã bình thường P2' = D(C2) XOR C1'
- Sau đó Server kiểm tra byte cuối của P2' nếu P2'_last = 01 → padding hợp lệ Server trả VALID

---
1.	Симметричные блочные и потоковые шифры.
- Mã khối đối xứng: chia thành các khối nhỏ có độ dài cố định, Mỗi khối sẽ được đưa vào thuật toán cùng với khóa bí mật để tạo ra bản mã. ví dụ DES: khối 64 bit, AES: khối 128 bit
- Mã dòng đối xứng: Là loại mã hóa đối xứng xử lý dữ liệu liên tục từng bit hoặc từng byte. Nó không chia thành khối lớn như block cipher, mà tạo ra một dòng khóa (keystream), rồi kết hợp dòng khóa này với bản rõ, thường bằng XOR. ci​=pi​⊕zi​
---
2.	Синхронные и асинхронные потоковые шифры.
- Mã dòng đồng bộ: Bên gửi và bên nhận đều tạo ra cùng một dòng khóa theo đúng thứ tự thời gian. Lỗi 1 bit truyền dẫn thường chỉ làm sai 1 bit giải mã
Nhưng nếu mất 1 bit hoặc thêm 1 bit, hai bên sẽ bị lệch nhịp và giải mã hỏng tiếp về sau, Dễ lệch nhịp hoàn toàn
- Mã dòng bất đồng bộ: lấy cipher text trước đó làm khóa cho cái sau, Có thể tự đồng bộ lại
---

