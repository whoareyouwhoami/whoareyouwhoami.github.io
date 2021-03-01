Tesseract 설치법
================

이 문서에는 Tesseract 설치법에 대한 글이다.

### Windows

윈도우 운영체제에서는 Tesseract 버전 5.0.0 알파를 설치할 것이다. 비록 알파 버전이지만 이전 버전인 4.1.0 보다는
성능이 좋다고 한다.

먼저 시스템에 맞는 것을 골라 다운로드한 후 설치한다. 설치중에 원하는 언어 데이터도 골라 한번에 설치하는걸 권장한다.  
\- [32
비트](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20191030.exe)  
\- [64
비트](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20191030.exe)

### Mac

맥을 이용하면 Homebrew를 사용해서 설치하는게 쉽다. Homebrew를 설치하지 않았다면 아래 코드를 통해 설치하면 된다.
만약 Homebrew에 대해서 자세히 알고 싶으면 [여기](https://docs.brew.sh/)를 클릭하면 된다.

    #########################
    #### Homebrew 설치법 ####
    #########################
    # 터미널에 붙여넣기
    
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Homebrew가 있거나 설치 했으면 아래 코드를 통해 Tesseract을 설치하고 필요한 언어들도 설치한다.

    # Tesseract 설치
    $ brew install tesseract
    
    # Tesseract 모든 언어 설치
    $ brew install tesseract-lang
    $ brew install tesseract --all-languages

맥에서는 특정 언어를 설치하는 것 보다는 모든 언어를 설치하는게 편하다…

### Ubuntu

우분투에서는 설치가 쉽다. Tesseract 버전 4.x.x 와 개발도구를 아래와 같이 설치하면 된다.

    $ sudo apt install tesseract-ocr
    $ sudo apt install libtesseract-dev

설치가 완료되면 원하는 언어를 설치하면 된다.

    # Tesseract 언어 설치
    $ sudo apt-get install tesseract-ocr-[lang]
    
    예시:
    $ sudo apt-get install tesseract-ocr-kor
    
    # 만약 모든 언어를 원하면 [lang] 대신 all
