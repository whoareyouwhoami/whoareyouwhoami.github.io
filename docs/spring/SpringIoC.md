# Spring IoC Container

스프링 컨테이너는 스프링의 핵심이다. 먼저 IoC (Inversion Of Control)란 제어의 역전이라고 번역할 수 있다. 초기에는 어플리케이션을 개발할 때 개발자가 모든 제어권을 가지고 있었다. 자바 객체의 생성부터 객체간의 의존관계를 연결하는 등 모든 단계를 직접 관리했다. 그러나 서블릿, EJB가 등장한 후 개발자의 제어권들이 컨테이너로 넘어가서 이제는 컨테이너가 객체에 대한 관리를 하기 시작한 것을 IoC라고 한다. IoC는 하나의 프로그래밍 패턴으로 느슨 결합 (Loose Coupling)을 위해 사용된다.

스프링 컨테이너는 개발자가 명시한 설정파일을 읽은 후 조건에 알맞게 객체들을 생성한다. 이렇게 생성된 자바 객체들을 스프링 빈즈 (Spring Beans)이다. 좀 더 말하자면 빈즈는 자바 객체이다. (POJO - Plain Old Java Object)

스프링 IoC 컨터이네는 다음과 같은 역할을 한다.

1. Beans 생성
2. Beans 의존성 주입
3. Beans 설정/등록
4. Beans 생명주기 관리

![](https://docs.spring.io/spring-framework/docs/3.0.0.M3/reference/html/images/container-magic.png)

그러면 컨테이너에 있는 빈즈들을 어떻게 불러올까?

### BeanFactory

**BeanFactory**는 스프링 컨테이너에 접근할 수 있는 root 인터페이스다. 빈즈를 생성하고 의존성을 주입하는 역할을 한다.
보통은 BeanFactory는 lazy loading이라고 한다. 즉, 그때그때 빈즈를 호출해야지만 생성된다.


### ApplicationContext

**ApplicationContext**는 스프링 어플리케이션의 핵심 인터페이스이며 어플리케이션에 필요한 설정 정보들을 제공한다.
그리고 BeanFactory 인터페이스를 implement (상속) 한 것이여서 BeanFactory에서 제공하는 기능들 외에도 AOP, 메시지처리, 이번트처리 등 개발에 도움이 되는 기등들을 제공한다.
BeanFactory와 반대로 ApplicationContext는 eager loading이다. 즉, 어플리케이션이 시작되면 모든 빈즈들이 생성된다.

<br>

**Referenece**

https://docs.spring.io/spring-framework/docs/3.0.0.M3/reference/html/ch04s02.html