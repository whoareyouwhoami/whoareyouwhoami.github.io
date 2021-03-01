---
layout: post
title: Docker
---

이 글에서는 도커에 대해서 알아보겠다. 도커는 새로운 기술이 아니다. 이전에도 컨테이너 활용은 사용되어 왔다. [ [설치하기](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) ]

집에서 컴퓨터로 프로젝트를 하다가 친구집에 놀러간 적이 있었다. 친구 집에서도 코딩을 해볼까 해서 하던 프로젝트를 깃헙에서 풀 받아서 실행시켜보니... 그렇다. 왜 내 컴퓨터에서는 잘 돌아가는데 다른곳에서는 안 돌아가지? 라고 한번쯤 말해본 적이 있을 것이다. 이 문제를 해결하는 방법 중 하나가 컨테이너를 활용하는 것이다. 쉽게 말해 컨테이너에 환경, 설정 등 개발에 필요한 스택을 쌓아놓고 언제 어디서든 컴퓨터 환경에 방해받지 않고 필요할때 열어서 사용한다고 보면 된다.

## Virtual Machine vs Docker

![사진](https://img.scoop.it/tImVj_1Pbqv0HJDyMWTmBbnTzqrqzN7Y9aBZTaXoQ8Q=)


그럼 왜 컨테이너를 사용하는 걸까? 컴퓨터 환경이 다르면 가상머신을 사용하면 되는거 아닌가 라고 생각 할 수 있다. 위에 그림처럼 가상머신은 호스트 OS 위에 특정 자원을 할당받아 게스트 OS를 설치하는 방식이다. 그러나 할당 받은 자원이 부족할 수도 있고, 반대로 자원이 많이 남아있을 수도 있다. 비효율적이다.

그러나 도커를 사용하면 호스트 OS의 자원을 공유하므로 별도의 OS 설치가 필요가 없다. 단순히 이미지를 불러와 여러개의 컨테이너를 생성하면 된다. 그리고 여러개의 컨테이너는 독립적으로 실행되어 가볍기도 하고 각 컨테이너가 필요한 자원만 할당을 받아 효율적이다.

<br>

# Docker 용어

### **이미지 (Image)**

이미지는 단순히 컨테이너를 만들기 위해 필요한 파일과 설정값들이 있는 템플릿이다. 이미지를 실행하면 컨테이너가 생성되고 원하는 만큼 만들 수 있다. 우분투 20.04 버전 이미지는 `reposiroty:tag` 형태로 내려받을 수 있다. 만약 태크가 없다면 최신 버전으로 내려받는다.

```
docker pull ubuntu:20.04
```

### **컨테이너 (Container)**

컨테이너는 이미지를 실행한 인스턴스라고 보면 된다. 컨테이너를 실행시키면 원하는 파일을 추가, 제거, 수정할 수 있다. 실행을 멈추면 안에 있던 데이터들은 삭제된다. 그리고 컨테이너는 고립된 환경에서 작동하므로 네트위크, 저장소 등 사용자가 원하는 환경으로 설정할 수 있다. 그리고 이러한 컨테이너를 빌드해 이미지로 만들 수 있다.

```
docker run --name ContainerName -i -t ubuntu:20.04
```

만약 우분투 이미지가 없으면 내려받은 후 컨테이너가 실행된다.

<br>

# Docker 빌드

### **Dockerfile**

컨테이너를 실행한 후 원하는 작업을 할 수 있다. 예를 들어 우분투 컨테이너를 사용해 웹 서버와 앱을 설치해 실행할 수 있다. 그리고 새로운 환경을 하나의 이미지로 빌드해 배포할 수 있다. 이 부분을 `Dockerfile` 을 통해 편하게 실행시킬 수 있다. 


Dockerfile [ [문서](https://docs.docker.com/engine/reference/builder/#format) ]

```
FROM repository:tag
COPY file
RUN ["some", "command"]                                      
```

위에 도커파일을 만든 후 아래 명령어를 통해 새로운 이미지를 만들 수 있다.

```
docker build -t ImageName:Tag DockerfilePath
```

### **Docker Compose**

여러개의 컨테이너들을 편하게 만들기 위해서는 `docker-compose`를 사용한다. 도커 컴포즈는 YAML 파일을 통해 서비스에 필요한 설정을 한다. 아래 파일은 Spring Boot로 개발한 앱을 도커 컴포즈로 실행시켜본 예시이다.

docker-compose.yaml [ [문서](https://docs.docker.com/compose/) ]
```
version: '3.9'

services:
  db:
    image: mysql:8.0.22
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: db
      MYSQL_USER: user
      MYSQL_PASSWORD: password
      TZ: Asia/Seoul

  web:
    build: DockerfilePath
    ports:
      - "8080:8080"
    depends_on:
    - db
```

# Docker 배포

새로운 이미지를 도커 계정을 개인 계정으로 배포해 다른 장소에서 환경에 구애받지 않고 사용할 수 있다.

```
# 도커 계정 로그인
docker login

# 이미지 배포
docker push DockerUserName/ImageName:Tag
```