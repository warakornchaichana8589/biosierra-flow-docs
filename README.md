# BioSierra ERP — Flow

แผนภาพขั้นตอนงานของระบบ ERP BioSierra รวมไว้ในหน้าเดียว แยกเมนูตามเรื่อง

| เมนู | ไฟล์ต้นฉบับ | เนื้อหา |
|---|---|---|
| ใบตวงสาร | `pages/weighing.html` | ก่อนถึงใบตวงสาร → QC ทวนสอบ → หลังผ่าน |
| Disposition (Lot ไม่ผ่าน) | `pages/disposition.html` | เส้นทาง Lot ไม่ผ่าน ก่อนและหลัง Disposition |
| เคลมผู้ขาย | `pages/supplier-claim.html` | Flow เคลมผู้ขาย (Supplier Claim) |

## เปิดดู

เปิด `index.html` ในเบราว์เซอร์ได้เลย (ไฟล์เดียว ไม่ต้องรันเซิร์ฟเวอร์)

## แก้ไข

1. แก้ไฟล์ใน `pages/`
2. รัน `python build.py` เพื่อสร้าง `index.html` ใหม่
3. commit ทั้งไฟล์ใน `pages/` และ `index.html`

เพิ่มหน้าใหม่: วางไฟล์ใน `pages/` แล้วเพิ่มบรรทัดในรายการ `PAGES` ของ `build.py`
