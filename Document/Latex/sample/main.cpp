#include <set>
#include <string>
#include <iostream>

int main(int argc, char **argv)
{       
  // ประกาศตัวแปรพร้อมกำหนดค่าเริ่มต้น
  std::string word;
  std::set<std::string> wordcount;

  // อ่านคำที่ผู้กรอกเก็บไว้ใน set (rb-tree)
  while (std::cin >> word) wordcount.insert(word);

  // แสดงผลลัพธ์ ว่าแต่ละคำมีจำนวนเท่าไหร่
  std::cout << "คำ: " << wordcount.size() << std::endl;
  return 0;
}
