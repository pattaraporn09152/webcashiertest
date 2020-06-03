package com.ubu.andapp;

import android.os.Bundle;
import android.app.Activity;
import android.util.Log;

public class MainActivity extends Activity {

   private String name = "MainActivity";
   
   /** ฟังก์ชันที่จะทำงานเมื่อมีการเริ่มเรียกใช้งาน MainActivity */
   @Override
   public void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
      Log.d(msg, "The onCreate() event");
   }

   /** ฟังก์ชันที่จะทำงานเมื่อมีการแสดง MainActivity ให้ผู้ใช้เห็น */
   @Override
   protected void onStart() {
      super.onStart();
      Log.d(msg, "The onStart() event");
   }
}
