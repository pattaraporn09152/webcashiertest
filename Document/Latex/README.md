## ฟอนต์ที่ควรติดตั้งก่อน

* Tex-Gyre [https://ctan.org/pkg/tex-gyre?lang=en](https://ctan.org/pkg/tex-gyre?lang=en)

* th-sarabun-new [https://www.f0nt.com/release/th-sarabun-new/](https://www.f0nt.com/release/th-sarabun-new/)

## โปรแกรมที่ต้องติดตั้ง

หมายเหตุ: สำหรับผู้ใช้ Windows แนะนำให้ติดตั้ง `https://chocolatey.org`

1. ติดตั้ง texlive สำหรับ compile latex

  * Windows - http://mirror.ctan.org/systems/texlive/tlnet/install-tl.zip

  * Ubuntu - `sudo apt install texlive-full`

  * OSX - `brew cask install mactex`

2. ติดตั้ง pygments สำหรับ syntax hilighting

  * Windows - `pip install pygments`
  
  * Ubuntu - `sudo apt install python-pygments python3-pygments`


## วิธีการ compile

```sh
 xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex
```

* คำสั่ง compile บนระบบปฏิบัติการที่มี `latexmk`

```sh
latexmk -g -f CS58*.tex 
```

### คำสั่งสร้าง bibliography

```sh
bibtex CS58*.aux
```

### คำสั่งแปลง .eps เป็น .pdf

```sh
pdf2eps [no_page_in_pdf] [figure_file_name]
```

### วิธีการรัน

```
Compilation: *require XeTeX
  [When citations/references are changed.]
  1. xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex
  2. bibtex MathCS-tutorial.aux
  3. xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex
  4. xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex

  [When citations/references are not changed.]
  1. xelatex -interaction=nonstopmode -file-line-error -synctex=1 MathCS-tutorial.tex
```
