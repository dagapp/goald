import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";

import { InputForm } from "@shared/ui/inputForm";
import { Button } from "@shared/ui/button";

import pinoeerPng from "@shared/assets/images/pioneer.png";
import "./registerPage.scss";

export function RegisterPage() {
  const {
    register,
    handleSubmit,
    setError,
    watch,
    formState: { errors, isValid },
  } = useForm({
    defaultValues: {
      username: "",
      password: "",
    },
    mode: "onChange",
  });

  const onSubmit = (values) => {
    console.log(values);
  };

  return (
    <div className="register__container">
      <div className="register__card">
        <form className="register-form" onSubmit={handleSubmit(onSubmit)}>
          <h2 className="register-form__title">Создайте аккаунт Goald</h2>
          <InputForm
            id={"username"}
            placeholder="Имя пользователя"
            error={Boolean(errors.username?.message)}
            errorMessage={errors.username?.message}
            properties={{
              ...register("username", {
                required: true,
              }),
            }}
          />

          <InputForm
            id={"password"}
            placeholder="Пароль"
            type={"password"}
            error={Boolean(errors.password?.message)}
            errorMessage={errors.password?.message}
            properties={{
              ...register("password", {
                required: true,
              }),
            }}
          />

          <InputForm
            id={"confirm-password"}
            placeholder="Повторите пароль"
            type={"password"}
            error={Boolean(errors.confirmPassword?.message)}
            errorMessage={errors.confirmPassword?.message}
            properties={{
              ...register("confirmPassword", {
                required: true,
                validate: (value) => {
                  if (watch("password") != value) {
                    return "Your passwords do no match";
                  }
                },
              }),
            }}
          />

          <Button className="register-form__button" type={"submit"}>
            Зарегистрироваться
          </Button>

          <div className="register-form__with-account">
            <span className="register-form__with-account_description">
              Уже есть аккаунт?{" "}
            </span>
            <Link to="/login" className="register-form__with-account_login">
              Войти в аккаунт
            </Link>
          </div>
        </form>

        <div className="register-form__image">
          <img src={pinoeerPng} alt="loginImage" />
        </div>
      </div>
    </div>
  );
}
