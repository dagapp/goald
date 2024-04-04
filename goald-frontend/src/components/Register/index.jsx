import React from 'react'

import Placeholder from '@components/Utils/Placeholder'

import pinoeerPng from '@assets/pioneer.png'
import './register.scss'

export default function Register() {
    return (
        <div className="register__container">
            <div className="register__card">
                <form className="register__form">
                    <h2 className="register__title">Создайте аккаунт</h2>
                    
                    <div className="register__name">
                        <Placeholder description="Имя" />
                        <Placeholder description="Фамилия" />
                    </div>
    
                    <Placeholder description="Электронная почта" />
                    <Placeholder description="Пароль" isPassword={true} />
                    <Placeholder description="Повторите пароль" isPassword={true} />
                    
                    <button className="register__button button_gradient button_rect">Зарегистрироваться</button>
                </form>

                <div className="register__image">
                    <img src={pinoeerPng} alt="pretty_girl" />
                </div>
            </div>
        </div>
    )
}
