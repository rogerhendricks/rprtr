INSERT INTO device ( serial, type, model, mode, mfg, lowrate, name_given, name_family) 
VALUES (1234565,'ICD','lumax','DDDR','BIO',40,'Joe','Blow');
WHERE device.serial = patient.serial;

