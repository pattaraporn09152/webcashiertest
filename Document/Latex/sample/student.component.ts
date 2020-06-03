// import ฟังก์ชันสำคัญของ angular/core
import { Component, OnInit } from '@angular/core';

@Component({
   // ประกาศชื่อ selector เพื่อให้ component อื่นสามารถนำไปใช้ได้
   selector: 'student',
   // ระบุชื่ไฟล์ html ที่ใช้ฟังก์ชันใน component โดยตรง
   templateUrl: './student.component.html', 
   // ระบุ style ที่นำไปใช้กับ html
   styleUrls: ['./student.component.css']
})
export class StudentComponent implements OnInit {

   constructor() { }

   ngOnInit() {}

}
