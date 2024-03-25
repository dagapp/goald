import React from 'react'

import './login.scss'

export default function Login() {
  return (
    <div className="login__container">
        <h2 className="login__title">Войдите в свой аккаунт</h2>
        
        <div className="login__form">
            <div className="login__form_field">
                <span className="field__description">Электронная почта</span>
                <input type="text" className='field__placeholder' required />
            </div>
            
            <div className="login__form_field">
                <span className="field__description">Пароль</span>
                <input type="password" className='field__placeholder' required />
            </div>

            <div className="login__support">
                <div className="login__support_remember">
                    <input type="checkbox" className='login__support_checkbox'/>
                    <span className='field__description'>Запомнить меня</span>
                </div>
                <a href='#'>
                    <span className="login__support_forgot">Забыли пароль?</span>
                </a>
            </div>

            <button className="gradient__button rectangle__button">Войти</button>
        </div>
    </div>
  )
}
