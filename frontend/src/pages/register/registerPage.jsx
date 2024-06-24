import { Link, Navigate } from "react-router-dom";
import { useForm } from "react-hook-form";

import { InputForm } from "@shared/ui/inputForm";
import { Button } from "@shared/ui/button";
import { authRegister } from "@shared/api/auth";

import pinoeerPng from "@shared/assets/images/pioneer.png";
import "./registerPage.scss";
import { useState } from "react";

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

  const [redirect, setRedirect] = useState(false)

  async function onSubmit(values) {
    if (isValid) {
      var response = await authRegister(values);
      
      if (response?.detail == "OK") {
        setRedirect(true);
      }
    }
  }

  return (
    <div className="register__container">
      {redirect && <Navigate to="/login" />}
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
                required: "Enter username",
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
                required: "Enter password",
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
                required: "Enter password again",
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
