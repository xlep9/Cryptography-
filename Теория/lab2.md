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
