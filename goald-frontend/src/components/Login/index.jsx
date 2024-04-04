import React from 'react'

import Placeholder from '@components/Utils/Placeholder' 
import Checkbox from '@components/Utils/Checkbox'

import pinoeerPng from '@assets/pioneer.png'
import './login.scss'

export default function Login() {
    return (
        <div className="login__container">
            <div className="login__card">
                <form className="login__form">
                    <h2 className="login__title">Войдите в свой аккаунт</h2>
                    
                    <Placeholder description="Электронная почта" />
                    <Placeholder description="Пароль" isPassword={true} />
                    
                    <div className="login__support">
                        <Checkbox description="Запомнить меня" />
                        <a href='#' className="login__support_forgot">Забыли пароль?</a>
                    </div>
                    
                    <button className="button_gradient button_rect">Войти</button>
                    <div className="login__no-account">
                        <span className="login__no-account_description">Нет аккаунта? </span>
                        <a href='#' className="login__no-account_register">Зарегистрируйтесь</a>
                    </div>
                </form>
                
                <div className="login__image">
                    <img src={pinoeerPng} alt="loginImage" />
                </div>
            </div>
        </div>
    )
}
