# Spring

스프링이 어떻게 작동되는지 알아보겠다.


## Spring IoC Container

스프링 컨테이너는 스프링의 핵심이다. 먼저 IoC (Inversion Of Control)란 제어의 역전이라고 번역할 수 있다. 초기에는 어플리케이션을 개발할 때 개발자가 모든 제어권을 가지고 있었다.
자바 객체의 생성부터 객체간의 의존관계를 연결하는 등 모든 단계를 직접 관리했다. 그러나 서블릿, EJB가 등장한 후 개발자의 제어권들이 컨테이너로 넘어가서 이제는 컨테이너가 객체에 대한 관리를 하기 시작한 것을 IoC라고 한다. 
IoC는 하나의 프로그래밍 패턴으로 느슨 결합 (Loose Coupling)을 위해 사용된다.

스프링 컨테이너는 개발자가 명시한 설정파일을 읽은 후 조건에 알맞게 객체들을 생성한다. 이렇게 생성된 자바 객체들을 스프링 빈즈 (Spring Beans)이다.

스프링 IoC 컨터이네는 다음과 같은 역할을 한다.

1. Beans 생성
2. Beans 의존성 주입
3. Beans 설정/등록
4. Beans 생명주기 관리

그러면 컨테이너에 있는 빈즈들을 어떻게 불러올까?

### BeanFactory

**BeanFactory**는 스프링 컨테이너에 접근할 수 있는 root 인터페이스다. 빈즈를 생성하고 의존성을 주입하는 역할을 한다.
보통은 BeanFactory는 lazy loading이라고 한다. 즉, 그때그때 빈즈를 호출해야지만 생성된다.


### ApplicationContext

**ApplicationContext**는 스프링 어플리케이션의 핵심 인터페이스이며 어플리케이션에 필요한 설정 정보들을 제공한다.
그리고 BeanFactory 인터페이스를 implement (상속) 한 것이여서 BeanFactory에서 제공하는 기능들 외에도 AOP, 메시지처리, 이번트처리 등 개발에 도움이 되는 기등들을 제공한다.
BeanFactory와 반대로 ApplicationContext는 eager loading이다. 즉, 어플리케이션이 시작되면 모든 빈즈들이 생성된다.


## Spring Bean Scopes

### Core Scopes

스프링 빈즈들을 어떻게 생성해서 관리할지는 5가지 scope을 통해 할 수 있다.

**1. Singleton**

스프링의 기본 scope이다. 컨테이너는 빈즈를 딱 한번 생성시킨 후 캐시에 담아 두어서 사용한다. 빈즈의 요청이 있을 때 이미 생선된 동일한 빈즈를 가져와 사용한다.

**2. Prototype**

스프링 컨테이너는 새로운 요청이 있을 때마다 새로운 빈즈를 생성한다.

### Web Aware Scopes

이 부분은 HTTP 요청이 있을 때 객체들이 생성되는 scope들이다. DispatcherServlet은 요청을 받은 후 WebApplicationContext에 해당하는
빈즈를 찾는다. 이러한 빈즈들을 어떻게 생성할지는 web-aware scopes를 통해 할 수 있다.

*기본은 Singleton scope을 가진다.

**3. Request**

웹 컨테이너는 새로운 HTTP 요청이 있을 때마다 빈즈들을 생성시킨다. 응답을 한 후 빈즈는 소멸된다.

**4. Session**

컨테이너는 새로운 HTTP 세션마다 빈즈들을 생성한다. 예를 들면, 2개의 브라우저를 사용하면 각 브라우저 마다 새로운 객체가 생성될 것이다.

**5. Gloabl Session**

Session 스코프와 비슷하다 범위가 더 넓다고 보면 된다. 하나의 웹 어플리케이션에 모든 객체가 공유가 된다. 그러므로 2개의 브라우저에 
연결해도 같은 객체를 받을 것이다.