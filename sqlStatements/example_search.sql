SELECT * 
FROM device
INNER JOIN patient on patient.serial = device.serial
WHERE patient.serial = '654321';
