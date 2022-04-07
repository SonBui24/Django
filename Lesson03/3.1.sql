# 1. Đưa ra danh sách bao gồm: Tên khách hàng, Số điện thoại và Tên người liên hệ của các khách hàng có địa chỉ ở "Hà Nội"
SELECT name, phone, contact_name FROM customer WHERE address = 'Hà Nội';

# 2. Đưa ra danh sách các mặt hàng có lượng tồn kho lớn hơn 50 và giá lớn hơn 2 triệu
SELECT * FROM product WHERE quantity > 50 AND price > 2000000;

# 3. Đưa ra danh sách các mặt hàng chưa được mua bởi khách hàng nào
SELECT id, name, price FROM product WHERE NOT EXISTS (SELECT product_id FROM order_detail WHERE product_id = product.id);

# 4. Cho biết mặt hàng có giá lớn nhất
SELECT * FROM product ORDER BY price DESC;
SELECT * FROM product WHERE (SELECT MAX(price) FROM product);

# 5. Cho biết nhân viên nào có nhiều đơn nhất trong khoảng thời gian từ 01-01-2022 đến 31-03-2022
SELECT name, COUNT(employee_id) AS total_order FROM employee JOIN `order` ON employee.id = `order`.employee_id
WHERE '2022-01-01' < purchase_at < '2022-03-31' GROUP BY employee_id ORDER BY total_order DESC LIMIT 1;

# 6. Tính doanh số cho từng nhân viên phụ trách đơn trong khoảng thời gian từ 01-01-2022 đến 31-03-2022. Thông tin đưa ra cần có: Mã nhân viên, Họ tên và Doanh số
SELECT employee.id, employee.`name`, SUM(order_detail.quantity * price) AS sales FROM employee
JOIN `order` ON employee.id = `order`.employee_id
JOIN order_detail ON `order`.id = order_detail.order_id
JOIN product ON order_detail.product_id = product.id WHERE '2022-01-01' <= purchase_at <= '2022-03-31' GROUP BY employee.id;