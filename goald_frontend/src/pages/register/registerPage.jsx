import { Link } from "react-router-dom";

import { InputForm } from "@shared/ui/inputForm";
import { Button } from "@shared/ui/button";

import pinoeerPng from "@shared/assets/images/pioneer.png";
import "./registerPage.scss";

export function RegisterPage() {
  return (
    <div className="register__container">
      <div className="register__card">
        <form className="register-form">
          <h2 className="register-form__title">Создайте аккаунт Goald</h2>

          <InputForm placeholder="Имя пользователя" />
          <InputForm placeholder="Пароль" type={"password"} />
          <InputForm placeholder="Повторите пароль" type={"password"} />

          <Button className="register-form__button">Зарегистрироваться</Button>

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
