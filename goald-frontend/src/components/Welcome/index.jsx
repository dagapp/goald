import React from 'react'

import './welcome.scss'

import pinoeerPng from '../../assets/pioneer.png'

export default function Login() {
  return (
    <div className="welcome__container">
        <div className="welcome__content_text">
            <h1 className="welcome__title">
                Онлайн-сервис для сбора финансовых средств
            </h1>
            <span className="welcome__description">
                Платформа предоставляет возможность организовывать кампании по сбору средств на различные нужды и проекты
            </span>
            <button className="welcome__button gradient__button">Создать проект</button>
        </div>

        <img src={pinoeerPng} alt="pretty_girl" />

    </div>
  )
}
