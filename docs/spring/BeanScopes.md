## Spring Bean Scopes

### Core Scopes

스프링 빈즈들을 어떻게 생성해서 관리할지는 5가지 scope을 통해 할 수 있다.

**1. Singleton**

스프링의 기본 scope이다. 컨테이너는 빈즈를 딱 한번 생성시킨 후 캐시에 담아 두어서 사용한다. 빈즈의 요청이 있을 때 이미 생선된 동일한 빈즈를 가져와 사용한다.

![](https://docs.spring.io/spring-framework/docs/3.0.0.M3/reference/html/images/singleton.png)

**2. Prototype**

스프링 컨테이너는 새로운 요청이 있을 때마다 새로운 빈즈를 생성한다.

![](https://docs.spring.io/spring-framework/docs/3.0.0.M3/reference/html/images/prototype.png)

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

<br>

**Reference**

https://docs.spring.io/spring-framework/docs/3.0.0.M3/reference/html/ch04s04.html