Tesseract 학습
================

이 문서는 Tesseract 4.00을 학습시키는 과정을 알아보겠다. Tesseract을 설치해 한국어를 사용하면 결과가 생각보다
잘 안 나올 때가 많다. 인터넷에 찾아보면 주로 아랍어 학습이 많이 나오지만 CJK에 대한 학습은 찾아보기 힘들다. 그래서 한번
한국어 학습을 시켜 정확성을 올릴 수 있는지 실험을 해보기로 했다. 자세한 학습은
[tess4korean](https://github.com/whoareyouwhoami/tess4korean)에서 확인하면 된다.

**Tesseract 학습은 Ubuntu 18.04 운영 체제에서 했으며 [AI
Hub](http://www.aihub.or.kr/)에서 한국어 글자체 이미지 데이터를 받아서 학습했다.**

<br>

### 학습 옵션

Tesseract 학습은 3가지로 분류할 수 있다.

1.  **튜닝 (Fine tune)**
2.  **레이어 교체**
3.  **새로 학습 시키기**

### 학습 절차

학습을 시작하기 전에 Tesseract 학습에 대한 구조를 먼저 이해하면 편하다.

1.  학습을 위해서는 `<lang>.<font>.<exp>.tif`의 이미지 파일이 필요하다. 여기서 `<lang>`은 언어,
    `<font>`는 글꼴 그리고 `<exp>`는 순서를 지정해주면 된다. **(예시: `kor.font1.exp0.tif`,
    `kor.font1.exp1.tif`, `kor.font2.exp0.tif`)**

2.  `.box` 파일을 만들어 준다. 이 파일 안에는 단어/문장이 있는 위치가 있다. Tesseract 3에서는 각 단어의
    박스값들이 필요했지만 Tesseract 4 이후 부터는 각 문장의 박스값만 필요하다. 만약 다수의 문장들이 있으면
    박스 파일 안에 새줄이라고 표현해 주어야 한다.

3.  `unicharset` 파일을 만들어야 한다. 이 파일에는 이미지에 있는 중복된 단어들을 제외한 파일들이다.
    
      - **문장** : 안녕하세요. 안녕히 가세요.
      - **unicharset** : 안, 녕, 하, 히, 가, 세, 요

4.  위에 파일들을 다 만들면 학습에 필요한 `.lstmf` 파일을 만든다.

**위 4가지를 이해하면 나머지는
[Tesseract](https://github.com/tesseract-ocr/tesseract.git)에서 제공하는 스크립트
파일을 사용하여 학습시키면 된다.**

<br>

### 설치 가이드

자세한 학습 내용은
[tess4korean](https://github.com/whoareyouwhoami/tess4korean)을 확인하면
된다. 그러나 학습전에 아래 코드를 실행시켜 Tesseract와 학습에 필요한 패키지를 설치하면 된다.

**1. Ubuntu 18.04에는 `Leptonica` 패키지가 설치되어 있을 것이다. 안되어 있다면 아래 코드를 통해 설치하면
된다.**

    $ sudo apt-get install libleptonica-dev

**2. Tesseract을 설치하고 학습에 필요한 패키지들을 설치한다.**

    # Tesseract 설치 
    $ sudo apt install tesseract-ocr
    $ sudo apt install libtesseract-dev
    
    # v.4.1 설치
    $ sudo add-apt-repository ppa:alex-p/tesseract-ocr
    $ sudo apt-get update
    $ sudo apt install tesseract-ocr
    
    # 학습에 필요한 패키지 설치
    $ sudo apt-get install libicu-dev libpango1.0-dev libcairo2-dev
    $ sudo apt-get install g++ autoconf automake libtool pkg-config libpng-dev libjpeg8-dev libtiff5-dev zlib1g-dev
