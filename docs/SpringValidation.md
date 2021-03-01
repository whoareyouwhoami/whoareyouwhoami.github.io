# 폼 검증방법

이 글에서는 Hibernate Validator를 사용해 어노테이션으로 폼 검증방법 대해서 알아보겠다.

## 시작하며

스프링으로 프로젝트를 해보았다면 모델을 만들 때 `@NotNull` 또는 `@Column` 어노테이션을 사용해보았을 것이다. 이러한 어노테이션은 데이터베이스에 있는 해당 테이블과 검증을 해준다. 그러나 상황에 따라 원하는 검증이 달라질 수 있다. 예를 들면 회원가입 때 사용되는 이메일 계정이 이미 존재하는지 확인하는 여부를 판단해주는 어노테이션은 없다. 그래서 직접 이메일 중복 여부를 확인하는 어노테이션을 직접 구현해 사용하면 된다.

## 커스텀 어노테이션

```
import javax.validation.Constraint;
import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.*;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Documented
@Constraint(validatedBy = EmailValidator.class)
@Target({TYPE, FIELD, ANNOTATION_TYPE})
@Retention(RUNTIME)
public @interface ValidcheckEmailExist {
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
    String message() default "검증 실패시 메시지";
    
    // 추가로 필요한 부분 작성
}

```

`@Constraint`: 검증 구현 클래스

`@Target`: 어노테이션 사용할 위치

`@Retention`: 언제 사용할지 지정

기본적으로 `message()`는 검증 실패시 나오는 메시지이다. 그 외에도 추가할 수 있다. 예를 들면 가입 페이지를 만들 때 비밀번호가 일치하는지 확인하려면 아래와 같이 `password1`, `password2` 를 추가해 비교하는 코드를 작성하면 된다.

```
...

public @interface ValidcheckEmailExist {
    ...

    String message();
    String password1();
    String password2();
}
```

## 커스텀 검증 클래스

검증할 클래스를 만들고 위에 검증 어노테이션을 `ConstraintValidator` 를 사용해 구현해 준다.  

```
public class EmailExistValidator implements ConstraintValidator<ValidcheckEmailExist, Object> {
    
    // String password1;

    @Override
    public void initialize(ValidCheckPasswordConfirm constraintAnnotation) {
        // message() 외 추가한 부분이 있으면 여기에 작성한다
        // this.password1 = constraintAnnotation.password1();
    }

    @Override
    public boolean isValid(Object value, ConstraintValidatorContext context) {
        // 검증절차 구현

        return true/false;
    }
}

```

## 커스텀 어노테이션 사용
이제 모델 부분을 구현한 클래스로 돌아가 어노테이션을 추가해주면 된다.

```
@Entity
public class User {

    @ValidcheckEmailExist
    private String email;

    ...
    ...

```

검증을 구현하는 방법은 어노테이션 외에도 `Validator`를 구현해 작성할 수 있다.