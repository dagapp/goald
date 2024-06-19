import { Link, Navigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { useDispatch, useSelector } from "react-redux";

import { InputForm } from "@shared/ui/inputForm";
import { Checkbox } from "@shared/ui/checkbox";
import { Button } from "@shared/ui/button";

import { fetchAuth } from "@entities/user";
import { selectIsAuth } from "@entities/user/model/authSlice";

import pinoeerPng from "@shared/assets/images/pioneer.png";
import "./loginPage.scss";

export function LoginPage() {
  const isAuth = useSelector(selectIsAuth);
  const dispatch = useDispatch();

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
    dispatch(fetchAuth(values));
  };

  if (isAuth) {
    return <Navigate to="/" />;
  }

  return (
    <div className="login__container">
      <div className="login__card">
        <form className="login-form" onSubmit={handleSubmit(onSubmit)}>
          <h2 className="login-form__title">Войдите в свой аккаунт Goald</h2>

          <InputForm
            id={"username"}
            placeholder="Имя пользователя"
            error={Boolean(errors.username?.message)}
            errorMessage={errors.username?.message}
            properties={{
              ...register("username", {
                required: "Enter user name",
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
                required: "Enter Password",
              }),
            }}
          />

          <div className="login-form__support">
            <Checkbox>Запомнить меня</Checkbox>
            {/* Not created yet */}
            <a href="/forgot" className="login-form__support_forgot">
              Забыли пароль?
            </a>
          </div>

          <Button className="login-form__button" type={"submit"}>
            Войти
          </Button>

          <div className="login-form__no-account">
            <span className="login-form__no-account_description">
              Нет аккаунта?{" "}
            </span>
            <Link to="/register" className="login-form__no-account_register">
              Зарегистрируйтесь
            </Link>
          </div>
        </form>

        <div className="login-form__image">
          <img src={pinoeerPng} alt="loginImage" />
        </div>
      </div>
    </div>
  );
}
