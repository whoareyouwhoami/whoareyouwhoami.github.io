# Dependency Injection

하나의 객체가 다른 객체에 참조되면 의존성을 가진다. 의존성 주입 (Dependency Injection)은 객체들의 의존성을 개발자가 아닌 설정을 통해 스프링 컨테이너가 대신 주입해주는 하나의 설계 패턴이다.

의존성 주입을 장점은 다음과 같다.

- 느슨 결합 (Loose Coupling)
- 코드 가독성/재사용의 편리함
- 테스트 코드 작성시 수월함


### Spring에서 사용하는 DI 유형

**1. Constructor Injection**

클래스의 생성자를 사용해서 의존성 주입을 한다.

```
class SomeClass {

    private SomeService someService;

    @Autowired
    public SomeClass(SomeService someService) {
        this.someService = someService;
    }
    ...
}
```

**2. Setter Injection**

setter() 메서드를 사용해서 의존성 주입을 한다.

```
class SomeClass {
    private SomeService someService;

    @Autowired
    public void setSomeService(SomeService someService) {
        this.someService = someService;
    } 
    ...
}
```

**3. Field Injection**

필드에 바로 의존성을 주입한다.

```
class Coffee {

    @Autowired
    private SomeService someService;
    ...
}
```

필드 의존성 주입보다는 생성자 또는 세터 메서드를 사용하는걸 권고한다.

**단일 책인의 원칙 위반**

필드에 바로 의존성을 주입하다 보면 수많은 객체에 대한 의존성을 주입할 수 있다. 그렇게 되면 하나의 클래스가 책임져야할 부분이 많아지므로 객체지향 프로그래밍의 원칙을 위반할 수 있다. 반대로 생성자를 사용하면 매개변수를 지정할 수 있으므로 매개변수가 많아지면 코드를 고쳐야 할 수 있는 신호를 줄 수 있다.

**불변성 (Immutability) 및 오류방지**

필드 주입은 final을 붙이지 못해 값이 변경될 수 있다. 그러나 생성자를 사용하면 final을 붙일 수 있어 혹시 모를 사태에 대비할 수 있다.

<br>

**Reference**

https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-dependencies

https://madplay.github.io/post/why-constructor-injection-is-better-than-field-injection

https://zorba91.tistory.com/238#recentEntries