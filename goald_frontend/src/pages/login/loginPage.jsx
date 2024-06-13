import { Link } from "react-router-dom";

import { InputForm } from "@shared/ui/inputForm";
import { Checkbox } from "@shared/ui/checkbox";
import { Button } from "@shared/ui/button";

import pinoeerPng from "@shared/assets/images/pioneer.png";
import "./loginPage.scss";

export function LoginPage() {
  return (
    <div className="login__container">
      <div className="login__card">
        <form className="login-form">
          <h2 className="login-form__title">Войдите в свой аккаунт Goald</h2>

          <InputForm placeholder={"Электронная почта"} />
          <InputForm placeholder={"Пароль"} type={"password"} />

          <div className="login-form__support">
            <Checkbox>Запомнить меня</Checkbox>
            {/* Not created yet */}
            <a href="/forgot" className="login-form__support_forgot">
              Забыли пароль?
            </a>
          </div>

          <Button className="login-form__button">Войти</Button>

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
