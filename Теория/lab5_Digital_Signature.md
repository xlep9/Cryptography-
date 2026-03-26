### 1. Mã hóa thông điệp và gửi kèm chữ ký số:
- Quá trình tạo chữ ký và mã hóa:
Người gửi băm (hash) thông điệp bằng một hàm băm (như SHA-256).
Sau đó, người gửi ký giá trị băm này bằng khóa bí mật của mình, tạo ra chữ ký số.
Người gửi mã hóa toàn bộ thông điệp (bao gồm thông điệp gốc) bằng khóa công khai của người nhận (ví dụ, sử dụng RSA) để bảo vệ tính bảo mật.
Người gửi gửi chữ ký số và thông điệp đã được mã hóa (bằng RSA) cho người nhận.
- Quá trình kiểm tra và giải mã:
Người nhận sử dụng khóa bí mật của mình để giải mã thông điệp (được mã hóa bằng khóa công khai của họ).
Sau khi giải mã được thông điệp, người nhận băm lại thông điệp để tạo ra giá trị hash.
Người nhận dùng khóa công khai của người gửi để giải mã chữ ký số và lấy giá trị hash đã được ký.
Nếu hash đã giải mã từ chữ ký số khớp với hash mà người nhận tính toán từ thông điệp, thì thông điệp là hợp lệ và không bị thay đổi.
### 2. Gửi thông điệp mà không mã hóa, chỉ gửi chữ ký số:
- Quá trình tạo chữ ký số:
Người gửi băm thông điệp (với SHA-256 chẳng hạn).
Người gửi ký giá trị băm này bằng khóa bí mật của mình, tạo ra chữ ký số.
Người gửi gửi chữ ký số và thông điệp gốc cho người nhận (không mã hóa thông điệp).
- Quá trình kiểm tra chữ ký số:
Người nhận nhận được thông điệp và chữ ký số.
Người nhận băm lại thông điệp để tạo giá trị hash mới.
Người nhận sử dụng khóa công khai của người gửi để kiểm tra chữ ký số và giải mã chữ ký để lấy giá trị hash mà người gửi đã ký.
Nếu hash đã giải mã từ chữ ký khớp với hash tính toán từ thông điệp, chữ ký là hợp lệ và thông điệp chưa bị thay đổi.

### Tóm tắt:
Phương thức 1: Mã hóa thông điệp + chữ ký số: Bảo mật thông điệp (người nhận cần giải mã trước khi kiểm tra chữ ký).
Phương thức 2: Thông điệp không mã hóa + chữ ký số: Thông điệp gửi trực tiếp, nhưng đảm bảo tính toàn vẹn và xác thực bằng chữ ký số.
