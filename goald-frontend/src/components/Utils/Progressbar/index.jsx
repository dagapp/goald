import React from 'react'

import './progressbar.scss'

export default function Progressbar({daysLeft, amount, goal, percentage}) {
    return (
        //Possible XSS in this component
        <div className="progress-bar">
            <div className="progress-bar_content">
                <div className="progress-bar_statistic">
                    <div className="progress-bar_statistic_value">{ `${daysLeft}` }</div>
                    <div className="progress-bar_statistic_title">Дней осталось</div>
                </div>

                <div className="progress-bar_statistic">
                    <div className="progress-bar_statistic_value">{ `${amount}` } ₽</div>
                    <div className="progress-bar_statistic_title">Собрано</div>
                </div>

                <div className="progress-bar_statistic">
                    <div className="progress-bar_statistic_value">{ `${goal}` } ₽</div>
                    <div className="progress-bar_statistic_title">Цель</div>
                </div>
            </div>

            <div className="progress-bar_bar">
                <div className="progress-bar_bar_fill" style={{ width: `${percentage}%`}}></div>
            </div>
        </div>
    )
}
